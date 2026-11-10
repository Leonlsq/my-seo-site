---
title: "PHP EOL Security Risk: How to Audit & Fix Old Versions"
description: "PHP's single full-time dev exposes a bigger risk: unsupported versions. Learn how to audit your servers, find EOL PHP installs, and migrate safely."
pubDate: 2026-10-29
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## The PHP Security Snafu Is a Symptom — Your Old PHP Version Is the Disease

The recent PHP security incident made headlines for an uncomfortable reason: the language powering roughly 75% of the web reportedly has just **one full-time employee** and thin funding, and that resource crunch likely contributed to the vulnerability slipping through. But here's the part that should worry you more than the news cycle: **the servers most exposed to this class of bug are the ones running PHP versions that reached end-of-life years ago and receive no patches at all.** If your stack is on PHP 7.4, 7.2, or (yes, it happens) 5.6, no amount of upstream funding fixes your problem — only migration does. This guide gives you a concrete audit-and-fix workflow you can run this week.

## Step-by-Step: Audit Your PHP Versions and Close the Gap

### Step 1 — Inventory every PHP runtime you actually run
You can't fix what you can't see. Check your web servers and containers:

```bash
# On Debian/Ubuntu hosts
php -v
dpkg -l | grep -i php | awk '{print $2, $3}'

# On RHEL/Alma/Rocky
rpm -qa | grep -i '^php'

# Inside Docker
docker ps --format '{{.Image}}' | grep -i php

# Across a fleet via SSH (quick loop)
for h in $(cat hosts.txt); do echo "== $h =="; ssh "$h" 'php -v | head -1'; done
```

Also grep your web server configs — you may be running multiple PHP-FPM pools side by side:

```bash
grep -rE "php[0-9]\.[0-9]-fpm|proxy_pass.*php" /etc/nginx /etc/apache2 2>/dev/null
```

### Step 2 — Match each version against its support status
Use this reference table (as of late 2026) to classify findings:

| PHP Branch | Status | Security Support | Action |
|---|---|---|---|
| 8.4 | Active | Dec 2026 | ✅ Current — keep patched |
| 8.3 | Active | Dec 2027 | ✅ Current — keep patched |
| 8.2 | Security only | Dec 2026 | ⚠️ Plan upgrade now |
| 8.1 | EOL | Ended Dec 2025 | 🔴 Migrate immediately |
| 8.0 | EOL | Ended Nov 2023 | 🔴 Migrate immediately |
| 7.4 | EOL | Ended Nov 2022 | 🔴 Migrate immediately |
| 7.2 / 7.3 | EOL | Ended 2021 | 🔴 Critical — migrate now |
| 5.6 | EOL | Ended Dec 2018 | 🔴 Critical — migrate now |

Anything in the red rows is receiving **zero security patches** — the exact scenario the funding story warns about, but self-inflicted.

### Step 3 — Prioritize by exposure, not by count
Don't try to migrate everything at once. Rank your findings:

1. **Internet-facing** apps on EOL PHP → fix first.
2. **Apps handling payments, auth, or PII** on EOL PHP → fix second.
3. **Internal-only** apps on EOL PHP → schedule within the quarter.
4. **Legacy apps nobody owns** → isolate behind a WAF and set a kill date.

### Step 4 — Run a compatibility check before you migrate
Before upgrading, scan your codebase for removed functions and deprecations:

```bash
# Install PHP_CodeSniffer with PHPCompatibility rules
composer require --dev phpcompatibility/php-compatibility
./vendor/bin/phpcs -p . --standard=PHPCompatibility --runtime-set testVersion 8.3-
```

Fix flagged issues, then upgrade in a staging environment first. Most breakage comes from: `each()`, `create_function()`, dynamic properties, and removed `mysql_*` extensions.

### Step 5 — Upgrade the runtime, then lock it down
- On Debian/Ubuntu: `sudo apt install php8.3-fpm php8.3-mysql` (or your extension set), then repoint your web server.
- In Docker: bump the base image tag (`php:8.3-fpm`) and rebuild.
- After upgrading, **remove the old PHP packages** so nothing silently falls back to an EOL binary.

## Common Issues, Alternatives, and What You Should Know

**"We can't upgrade — the CMS/framework requires old PHP."** This is the real iceberg. Options, in order of preference:
- **Upgrade the CMS/framework** (WordPress, Laravel, Drupal all support current PHP).
- **Containerize the legacy app** behind a reverse proxy with strict network isolation, then set a hard retirement date.
- **Pay for commercial extended support** (e.g., vendor LTS offerings) — but treat this as a bridge, not a destination.

**"We patched, so we're fine."** Patching only helps versions *still receiving patches*. If your branch is EOL, the vendor won't ship a fix for the next snafu — you're on your own.

**Hidden risk: shared hosting.** Many budget hosts pin users to old PHP by default. Check your control panel's PHP selector and switch to the newest available branch; if the host offers nothing current, that's a reason to move.

**Cost reality check.** The upstream project's funding shortfall is a warning, not an excuse. The cheapest insurance is running a supported version and keeping automated dependency updates on.

## Frequently Asked Questions (FAQ)

### What is the latest supported PHP version in 2026?
PHP 8.4 and 8.3 are in active support, with 8.2 in security-only mode. Anything 8.1 or older is end-of-life and receives no security fixes.

### How do I check which PHP version my website is running?
Create a temporary `info.php` file containing `<?php phpinfo(); ?>`, load it in your browser, note the version, then **delete the file immediately**. Or check your host's control panel or run `php -v` on the server.

### Is PHP 7.4 still safe to use?
No. PHP 7.4 reached end-of-life in November 2022 and has received no security patches since. Running it exposes you to known, unpatched vulnerabilities — migrate to 8.2+ as soon as possible.

### Why does PHP only have one full-time developer?
The PHP project relies heavily on volunteer contributors and minimal corporate funding, leaving a very small paid core team. This resource gap is why running unsupported versions is especially dangerous — fixes are slower to arrive, so you must stay on supported branches.

## Final Verdict

The headline about PHP's staffing is a wake-up call, but the actionable takeaway is simple: **audit your PHP versions today, and treat any EOL branch as a live security incident.** Run the inventory commands above, use the support table to classify findings, and migrate internet-facing apps off PHP 8.1 and older first. You can't fund the upstream project single-handedly — but you can absolutely stop running code that no one is patching for you.