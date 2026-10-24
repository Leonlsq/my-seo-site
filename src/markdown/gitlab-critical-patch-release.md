---
title: "GitLab 19.5.1 Patch: How to Upgrade Safely (Step-by-Step)"
description: "GitLab 19.5.1 critical patch is out. Here's how to check your version, upgrade safely, and roll back if the migration fails."
pubDate: 2026-10-22
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## GitLab 19.5.1 Critical Patch: What It Fixes and How to Upgrade Without Downtime

GitLab has shipped **19.5.1**, a critical patch release that fixes security and reliability issues in the 19.5 line. If you're running any 19.5.x instance, this is a **patch-now** release — not a "wait for the next maintenance window" release. The upgrade itself is fast (typically 5–15 minutes on a single-node Omnibus install), but the failure modes are predictable: broken database migrations, skipped background migrations, and version-skew errors in multi-node setups. This guide gives you the exact pre-flight checks, the upgrade commands for each install type, and the rollback path if the migration stalls.

**Direct takeaway:** Always read the release notes and the linked issue tracker *before* upgrading. Critical patches sometimes include migration changes that require a maintenance window even though the version bump looks minor.

## Pre-Upgrade Checklist (Do This First)

Skipping these steps is the #1 cause of failed GitLab upgrades. Run them in order.

1. **Confirm your current version.** Run `sudo gitlab-rake gitlab:env:info` (Omnibus) or check **Admin Area → Overview → Components** (Helm/Kubernetes). You must be on the latest 19.5.x patch before jumping to 19.5.1.
2. **Read the patch release notes.** Open the official patch page (`docs.gitlab.com/releases/patches/`) and check the "Upgrade path" section. GitLab enforces required upgrade stops — you cannot skip intermediate versions.
3. **Take a full backup.** Omnibus: `sudo gitlab-backup create`. Docker: `docker exec -t <container> gitlab-backup create`. Verify the backup file exists and is non-zero in size.
4. **Back up config and secrets separately.** Copy `/etc/gitlab/gitlab.rb`, `/etc/gitlab/gitlab-secrets.json`, and your SSL certs off-box. The backup command does **not** include these.
5. **Check disk space.** Migrations can temporarily double table sizes. Ensure at least **2× your current database size** free on the data volume.
6. **Pause CI/CD runners.** Set runners to paused in **Admin Area → Runners** so no jobs start mid-migration.

## Step-by-Step Upgrade Commands by Install Type

### Omnibus (Linux package)

```bash
# 1. Stop services that write to the DB
sudo gitlab-ctl stop puma
sudo gitlab-ctl stop sidekiq

# 2. Run the upgrade
sudo apt-get update && sudo apt-get install gitlab-ee=19.5.1-ee.0
# (use gitlab-ce for Community Edition)

# 3. Reconfigure and restart
sudo gitlab-ctl reconfigure
sudo gitlab-ctl restart

# 4. Verify background migrations finished
sudo gitlab-rails runner "puts Sidekiq::Queue.new('background_migration').size"
```

A return value of `0` means background migrations are complete. If it's non-zero, **do not** proceed to the next upgrade — wait and re-check every 10 minutes.

### Docker

```bash
docker pull gitlab/gitlab-ee:19.5.1-ee.0
docker stop gitlab && docker rm gitlab
# Re-run your standard docker run / compose command with the new tag
docker compose up -d
docker exec -it gitlab gitlab-ctl reconfigure
```

### Kubernetes / Helm

```bash
helm repo update
helm upgrade gitlab gitlab/gitlab --version <matching-chart-version> -f values.yaml
kubectl rollout status deploy/gitlab-sidekiq
```

Check the chart-to-GitLab version compatibility table before upgrading — a mismatched chart is the most common Helm failure.

## Common Issues and How to Fix Them

| Symptom | Likely Cause | Fix |
|---|---|---|
| `PG::UndefinedTable` during migration | Skipped required upgrade stop | Restore backup, upgrade through the intermediate version first |
| 502 Bad Gateway after restart | Puma not fully booted | Wait 2–3 min, then `sudo gitlab-ctl status` and check `/var/log/gitlab/puma/current` |
| Background migrations stuck at non-zero | Large table, slow disk | Increase `sidekiq` concurrency temporarily; check `/var/log/gitlab/sidekiq/current` |
| `Version mismatch` in HA cluster | Nodes upgraded out of order | Upgrade the **primary** first, then secondaries one at a time |
| Login loops / session errors | Secrets file not carried over | Restore `gitlab-secrets.json` from your config backup |

### Rollback path

If migrations fail irrecoverably: stop GitLab, restore the database backup taken in step 3, reinstall the previous package version, and run `gitlab-ctl reconfigure`. **Note:** rollbacks are only safe within the same major/minor line — you cannot downgrade across a required upgrade stop.

## Frequently Asked Questions (FAQ)

### Is GitLab 19.5.1 a security release or a bugfix release?
It's a **critical patch** that bundles security fixes and reliability corrections for the 19.5 line. Treat it as mandatory for internet-facing instances; check the release notes for the specific CVE references and affected components.

### Can I skip GitLab 19.5.1 and go straight to the next minor version?
No. GitLab enforces upgrade stops. You must install the latest patch of your current minor (19.5.1) before moving to 19.6.x. Skipping patches is the most common cause of failed database migrations.

### How long does the GitLab 19.5.1 upgrade take?
On a single-node Omnibus install with a database under ~50 GB, expect **5–15 minutes** of downtime. Large instances (500 GB+) or those with pending background migrations should budget a **maintenance window of 1–2 hours**.

### Do I need to restart runners after upgrading?
No restart is required, but **unpause** them only after background migrations reach zero. Running CI jobs against a half-migrated database can corrupt job artifacts.

## Final Verdict

**Upgrade to GitLab 19.5.1 now if you're on any 19.5.x release.** The process is low-risk *only* if you follow the pre-flight checklist: back up the database **and** the secrets file, confirm your upgrade path, and verify background migrations hit zero before declaring victory. For HA and Kubernetes deployments, upgrade the primary node first and stagger secondaries. If you're several minor versions behind, don't jump — walk the required upgrade stops one patch at a time.