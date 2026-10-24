---
title: "PHP 8.2.35 Security Update: How to Patch & Verify Fast"
description: "A step-by-step guide to applying the PHP 8.2.35 security release, verifying your patch level, and hardening your stack after the latest PHP security fixes."
pubDate: 2026-10-22
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## PHP 8.2.35 Is Out: Here's How to Patch, Verify, and Harden Your Stack Today

A new PHP security release is live, and the Hacker News thread around **PHP 8.2.35** (and the linked follow-ups) is a reminder that most production outages after a patch aren't caused by the patch itself — they're caused by *how* teams apply it. The direct takeaway: if you run PHP 8.2.x in production, treat this as a **same-week patch window**, verify the exact build string afterward, and confirm your extensions (OPcache, APCu, ImageMagick bindings) are rebuilt against the new ABI. This guide gives you the commands, the verification checklist, and the rollback plan so you don't join the "my site broke after updating PHP" crowd.

## Step-by-Step: Apply and Verify the PHP 8.2.35 Security Release

The release is a **patch-level bump within the 8.2 branch**, so it should be a drop-in for most applications — but only if you follow the sequence below.

### 1. Snapshot before you touch anything
```bash
# Debian/Ubuntu example
sudo cp -a /etc/php/8.2 /root/php-8.2-backup-$(date +%F)
php -v > /root/php-version-before.txt
```
On containers, tag the current image (`docker tag myapp:php82 myapp:php82-pre-patch`) so rollback is a one-liner.

### 2. Update through your package manager (not manual tarballs)
| Distro / Stack | Command |
|---|---|
| Ubuntu/Debian (ondrej PPA) | `sudo apt update && sudo apt install --only-upgrade php8.2-cli php8.2-fpm php8.2-common` |
| Amazon Linux / RHEL (Remi) | `sudo dnf upgrade --refresh 'php82-php*'` |
| Alpine (Docker) | Rebuild image: `FROM php:8.2-fpm-alpine` then `docker build --no-cache` |
| macOS (Homebrew) | `brew upgrade php@8.2` |
| Windows | Replace the `php-8.2.x` zip in your PHP directory; keep `php.ini` |

### 3. Restart the right services
```bash
sudo systemctl restart php8.2-fpm
sudo systemctl reload nginx   # or apache2
```
FPM holds the old binary in memory until restarted — a `reload` alone is **not** enough.

### 4. Verify the exact build
```bash
php -v
# Expect: PHP 8.2.35 (cli) (built: ...)
php -r 'echo PHP_VERSION, PHP_EOL;'
```
Then confirm the FPM worker matches (CLI and FPM can diverge on some distros):
```bash
curl -s https://yoursite.test/phpinfo.php | grep -i "PHP Version"
```
Delete `phpinfo.php` immediately after.

### 5. Rebuild extensions and OPcache
```bash
php -m | sort > /root/extensions-after.txt
diff /root/extensions-before.txt /root/extensions-after.txt
sudo systemctl restart php8.2-fpm
```
If you compile extensions (Redis, Imagick, Swoole), reinstall them against the new headers: `pecl install redis && echo "extension=redis.so" >> php.ini`.

### 6. Run a smoke test
```bash
composer check-platform-reqs
php artisan about   # Laravel
bin/console about   # Symfony
```
Load your three highest-traffic pages and check `error_log` for `E_DEPRECATED` or `Class not found` noise.

## Common Issues, Alternatives, and What You Should Know

**"Fatal error: Cannot redeclare class" after update.** Almost always a stale OPcache. Flush it: `sudo systemctl restart php8.2-fpm` or `php -r 'opcache_reset();'` from a web-triggered script.

**CLI and FPM versions disagree.** On Debian, `php8.2-cli` and `php8.2-fpm` are separate packages. Upgrade both explicitly.

**Composer platform check fails.** If your `composer.json` pins `"php": "8.2.34"`, loosen it to `"^8.2"` — patch releases shouldn't require a constraint edit, but strict pins break silently.

**Can't upgrade yet?** If a critical dependency blocks you, mitigate by:
- Disabling `allow_url_include` and `allow_url_fopen` in `php.ini`.
- Tightening `open_basedir` to your app root.
- Fronting PHP-FPM with a WAF rule set for the affected CVE class.
This is a stopgap, not a substitute — schedule the patch within 14 days.

**Docker users:** don't `docker pull` a `:8.2` tag and assume you're current. Pin to `php:8.2.35-fpm-alpine` so your build is reproducible and your scanner can prove the version.

**Performance note:** patch releases occasionally tweak OPcache defaults. After updating, benchmark with `ab -n 1000 -c 50 https://yoursite.test/` and compare against your pre-patch numbers before declaring victory.

## Frequently Asked Questions (FAQ)

### Is PHP 8.2.35 a security release or a bug-fix release?
It's a **security release within the 8.2 maintenance branch**, meaning it bundles security fixes plus a small set of regression fixes. Treat it as mandatory for any internet-facing PHP 8.2 deployment.

### Do I need to update PHP 8.1 or 8.3 as well?
Check the corresponding release notes for your branch. Security fixes are typically backported to all supported branches, so **8.1.x and 8.3.x will have their own patch versions** — apply the equivalent update for whichever branch you run.

### Will PHP 8.2.35 break my WordPress, Laravel, or Symfony app?
For the vast majority of apps, no. The breaking-risk items are: **compiled extensions needing a rebuild**, **strict Composer platform pins**, and **deprecation warnings escalated to errors** in custom code. Run your test suite before pushing to production.

### How do I roll back if something breaks?
Restore the config backup and downgrade via your package manager (`sudo apt install php8.2-fpm=8.2.34-...`) or redeploy the pre-patch container tag. Keep the old `.deb`/`.rpm` cached with `apt-get download` or `dnf download` before upgrading.

### How do I check my PHP version from the command line quickly?
`php -v` for CLI, and a temporary `<?php echo PHP_VERSION; ?>` file (or `curl -I` against a header that exposes it) for FPM. Never leave a `phpinfo()` page publicly reachable.

## Final Verdict

**Patch now, verify the build string, and restart FPM — not just the web server.** PHP 8.2.35 is a routine-but-important security bump; the teams that get burned are the ones who update the CLI package and forget the FPM worker, or who pin Composer to an exact patch version and get stuck. Set a 7-day patch SLA for security releases, keep a cached copy of the previous package for rollback, and add a post-deploy `php -v` check to your CI pipeline. If you're still on an end-of-life branch, this release is your cue to plan the jump to 8.2 or 8.3 — running unsupported PHP is the real vulnerability.