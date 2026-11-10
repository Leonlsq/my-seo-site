---
title: "PHP-ocalypse: How to Patch CVE-2024-4577 & CVE-2024-8932 Now"
description: "Two critical PHP bugs almost broke the internet. Learn how to detect, patch, and harden CVE-2024-4577 and CVE-2024-8932 on Windows and Linux in minutes."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## PHP-ocalypse Explained: The Two Critical Bugs and How to Patch Them Today

The "PHP-ocalypse" refers to two severe vulnerabilities disclosed in 2024 that affected PHP, the language powering roughly **77% of all websites** with a known server-side language. The first, **CVE-2024-4577** (CVSS 9.8), is a critical argument-injection flaw in PHP's CGI mode on Windows that allows remote code execution with no authentication. The second, **CVE-2024-8932**, is an out-of-bounds read in PHP's `ldap_escape()` function that can leak memory or crash processes. The direct takeaway: **if you run PHP 8.1.x below 8.1.29, 8.2.x below 8.2.20, or 8.3.x below 8.3.8, you are exposed right now.** This guide gives you the exact commands to detect and patch both.

## Step-by-Step Guide: Detect and Patch Both Vulnerabilities

### Step 1: Check Your PHP Version

Run this on any affected server:

```bash
php -v
```

Compare against the patched versions in the table below. If you're on an older branch, you're vulnerable.

| PHP Branch | Vulnerable Versions | Patched Version | Fixes |
|---|---|---|---|
| 8.3.x | < 8.3.8 | **8.3.8** | CVE-2024-4577 |
| 8.2.x | < 8.2.20 | **8.2.20** | CVE-2024-4577 |
| 8.1.x | < 8.1.29 | **8.1.29** | CVE-2024-4577 |
| 8.3.x | < 8.3.11 | **8.3.11** | CVE-2024-8932 |
| 8.2.x | < 8.2.23 | **8.2.23** | CVE-2024-8932 |
| 8.1.x | < 8.1.31 | **8.1.31** | CVE-2024-8932 |

> **Note:** CVE-2024-4577 only affects **Windows** installations running PHP in CGI or php-cgi mode. CVE-2024-8932 affects all platforms using the LDAP extension.

### Step 2: Patch on Debian/Ubuntu

```bash
sudo apt update
sudo apt install --only-upgrade php8.3 php8.3-cgi php8.3-ldap
sudo systemctl restart php8.3-fpm apache2 nginx
```

### Step 3: Patch on RHEL/CentOS/Rocky/AlmaLinux

```bash
sudo dnf update php php-fpm php-ldap
sudo systemctl restart php-fpm httpd nginx
```

### Step 4: Patch on Windows (CVE-2024-4577 Hotspot)

Windows is the highest-risk target. Do **all three**:

1. **Update PHP** to 8.3.8+ / 8.2.20+ / 8.1.29+ from windows.php.net.
2. **Disable CGI mode** if you don't need it — edit `php.ini` and ensure you are not loading `php-cgi.exe` through your web server.
3. **Apply the workaround** if you cannot patch immediately: add a rewrite rule to block `%ADd` and `%add` injection patterns, or switch to FastCGI/PHP-FPM.

Example Apache workaround (temporary only):

```apache
RewriteEngine On
RewriteCond %{QUERY_STRING} ^%ad [NC]
RewriteRule .? - [F,L]
```

### Step 5: Verify the Patch

```bash
php -r "echo PHP_VERSION;"
```

Confirm the output matches or exceeds the patched version in the table. Then re-scan with a vulnerability scanner (e.g., `nuclei -tags php` or your host's built-in scanner).

## Common Issues, Workarounds, and What You Should Know

- **Shared hosting users:** You cannot patch the server yourself. Contact your host and confirm their PHP version. Most major hosts (cPanel, Plesk) pushed emergency updates within 48 hours — but verify via your control panel's "Select PHP Version" tool.
- **Docker containers:** Rebuild from the latest official `php:8.3-fpm` image. Pinned tags like `php:8.3.5-fpm` remain vulnerable forever.
- **The LDAP trap:** Many admins ignore CVE-2024-8932 because they "don't use LDAP." Check with `php -m | grep ldap` — if the module is loaded (common in default builds), you're exposed even if your app never calls it.
- **Why it's not the last scare:** PHP's long tail of legacy deployments (WordPress, Drupal, Laravel apps on old stacks) means patch lag is measured in months, not days. The 2024 bugs followed the same pattern as the 2019 `CVE-2019-11043` PHP-FPM flaw — a reminder to automate updates.
- **Automate it:** Enable `unattended-upgrades` (Debian) or `dnf-automatic` (RHEL) for security-only patches to close the gap.

## Frequently Asked Questions (FAQ)

### Is CVE-2024-4577 exploitable on Linux?
No — CVE-2024-4577 is a **Windows-only** flaw caused by how Windows handles character encoding in CGI argument passing. Linux and macOS PHP-CGI are not affected by this specific bug.

### How do I know if my WordPress site is affected by the PHP-ocalypse bugs?
Check your host's PHP version (many show it in the dashboard). If you're below 8.1.29/8.2.20/8.3.8 on Windows, or below 8.1.31/8.2.23/8.3.11 with LDAP enabled, you're exposed. Update PHP, then update WordPress core and plugins.

### Can I just disable PHP-CGI instead of patching?
Yes for CVE-2024-4577 — switching to PHP-FPM or mod_php removes the attack surface entirely. But you **still** need to patch for CVE-2024-8932, which is unrelated to CGI mode.

### What is the CVSS score of these bugs?
CVE-2024-4577 scores **9.8 (Critical)**. CVE-2024-8932 scores **7.5 (High)**. Both warrant immediate action.

## Final Verdict

Don't wait for a breach notification. **Check your PHP version now, patch to the versions in the table above, and disable CGI mode on Windows if you can.** If you're on shared hosting, screenshot your host's PHP version and open a support ticket demanding confirmation. The PHP-ocalypse wasn't a one-off — it's a pattern. Automate security updates today so the next critical bug patches itself before you even read the headline.