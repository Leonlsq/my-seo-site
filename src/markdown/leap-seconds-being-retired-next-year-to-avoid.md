---
title: "Leap Second Retired? How to Future-Proof Your Systems for 2026"
description: "Leap seconds are being retired. Here's how to audit NTP, Linux, and Java configs now so the leap-hour transition never breaks your servers in 2026."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Leap Seconds Are Being Retired: What Admins Must Do Before the Switch

The ITU and global timekeeping bodies have agreed to retire the leap second, replacing it with a "leap hour" that won't be needed for several centuries. The headline sounds like good news — no more 23:59:60 timestamps, no more midnight crashes. But if you run servers, databases, or trading systems, the real work starts now. **Your job isn't to celebrate; it's to audit every system that currently assumes leap seconds exist, because the transition window (and the legacy code still expecting them) is where outages hide.**

This guide gives you a concrete, step-by-step audit and hardening checklist you can run on Linux, Windows, Java, and NTP infrastructure today. It takes about two hours for a small fleet and pays for itself the first time a timestamp mismatch doesn't page you at 2 a.m.

## Step-by-Step: Future-Proof Your Time Infrastructure

### Step 1 — Inventory every time source and consumer
Run this on each Linux host to see what's synchronizing your clock:

```bash
timedatectl status
chronyc sources -v      # if using chrony
ntpq -p                 # if using classic ntpd
```

Document every NTP/chrony/PTP server, every application that reads `CLOCK_REALTIME`, and every service that does timestamp arithmetic. Flag anything using **TAI vs UTC** conversions — those are the highest-risk components.

### Step 2 — Know which kernel handles leap smearing
Most modern Linux kernels (2.6.23+) insert leap seconds by "smearing" or slewing rather than stepping. Check your kernel's behavior:

```bash
cat /sys/kernel/debug/timekeeping/leap_seconds 2>/dev/null
dmesg | grep -i "leap"
```

If your kernel steps the clock instead of slewing, any application doing tight timing (Kafka, Cassandra, financial ledgers) can see a 1-second jump. **Configure `leap_smear` on your NTP servers** so downstream clients never see a discontinuity.

### Step 3 — Patch Java and database drivers
Java's `java.time` and older `java.util.Date` handle leap seconds inconsistently across versions. Audit:

- **Java 8+**: `java.time.Clock` ignores leap seconds by default — verify no custom `Clock` subclass assumes them.
- **MySQL**: `TIMESTAMP` columns don't store leap seconds; audit any `UNIX_TIMESTAMP()` math.
- **PostgreSQL**: `timestamptz` is UTC-based and safe, but check `EXTRACT(EPOCH ...)` usage.

### Step 4 — Test with a simulated leap event
Use `libfaketime` or a staging NTP server with a forced leap flag to replay a leap-second insertion. Watch for:

| Symptom | Likely Cause | Fix |
|---|---|---|
| Duplicate log timestamps | Clock stepped backward | Enable slewing |
| Cron jobs firing twice | `CLOCK_REALTIME` jump | Use monotonic clocks |
| TLS handshake failures | Cert validity window mismatch | Re-sync + retry logic |
| DB replication lag spike | Timestamp ordering broken | Use logical clocks |

### Step 5 — Document your leap-hour readiness
Since the leap hour won't arrive for centuries, your deliverable is a **runbook**: which systems smear, which step, which apps use monotonic time, and who owns each. Store it next to your DR plan.

## Common Issues, Alternatives, and What You Should Know

- **Don't disable NTP to "avoid" leap seconds.** You'll drift and cause worse problems. Smear instead.
- **Windows** handles leap seconds via a registry-driven `TimeProvider`; verify `HKLM\SYSTEM\CurrentControlSet\Services\W32Time\Config\LeapSecondEnabled` is set correctly for your fleet.
- **Cloud providers** (AWS, GCP, Azure) already smear on their internal time services — but your VMs may still step if they sync to an external pool. Point clients at the provider's smeared endpoint.
- **Embedded/IoT devices** with hardcoded leap tables are the sleeper risk. If firmware hasn't been updated since 2016, its leap table is stale — flag it for replacement, not patching.
- **Cost note:** a full audit is mostly labor. Budget 4–8 engineer-hours per 50 hosts; no new hardware required unless you're running PTP for sub-microsecond needs.

## Frequently Asked Questions (FAQ)

### Will retiring the leap second break my servers in 2026?
Not directly — the leap second is being phased out, not inserted. The risk is legacy code that *expects* leap seconds and mishandles the absence of them. Audit and patch now to avoid surprises.

### What is a leap hour and when will it happen?
A leap hour is the proposed replacement mechanism that would add a full hour to UTC only when accumulated drift requires it — likely several centuries from now. No action needed beyond keeping your time infrastructure documented and smeared.

### Do I need to change my NTP configuration?
You should verify your NTP servers use leap smearing and that clients point to smeared sources. No config change is strictly required for the retirement itself, but smearing prevents step-induced outages.

## Final Verdict

**Treat this as a free audit window, not a non-event.** Run Steps 1–5 on your highest-value systems this quarter, document your leap-hour runbook, and point every client at a smeared time source. The leap second's retirement won't crash you — but the stale assumptions in your code just might, and you have a rare, low-pressure moment to fix them before they do.