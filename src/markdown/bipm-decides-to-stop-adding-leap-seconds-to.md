---
title: "BIPM Ends Leap Seconds: What It Means for Your Servers"
description: "The BIPM just voted to stop adding leap seconds to UTC by 2035. Here's how to audit your NTP, GPS, and database clocks before the change hits."
pubDate: 2026-10-16
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## The BIPM Just Killed the Leap Second: What Sysadmins Need to Do Now

If you run servers, write time-sensitive code, or manage anything that touches NTP, GPS, or timestamps, you already know the pain of a leap second. The BIPM's 2026 General Conference on Weights and Measures (CGPM) passed Resolution 5, which sets a hard deadline: **no more leap seconds will be added to UTC after 2035**. Instead, the gap between atomic time (TAI) and Earth's rotation will be allowed to grow — and eventually reconciled with a much larger correction (potentially a "leap minute") sometime in the 22nd century or later.

The immediate takeaway: **you have roughly nine years to audit and harden your time infrastructure**. This isn't a "wait and see" situation. The last leap second was inserted on December 31, 2016, and the erratic, unpredictable nature of these insertions has caused real outages at Reddit, Cloudflare, and countless Linux fleets. Here's exactly what to check and change.

## Step-by-Step: How to Prepare Your Infrastructure for a Leap-Second-Free UTC

### Step 1: Inventory Every Clock Source You Rely On

You cannot fix what you haven't mapped. Build a table like this for your environment:

| Source | Protocol | Leap-Second Aware? | Action Needed |
|---|---|---|---|
| Public NTP (pool.ntp.org) | NTPv4 | Yes (via leap indicator bit) | Monitor, no change until 2035 |
| GPS receivers | NMEA / PPS | Yes (broadcasts leap offset) | Firmware may need update post-2035 |
| Cloud provider (AWS Time Sync) | NTP / PTP | Yes | Check provider roadmap |
| Internal PTP grandmaster | IEEE 1588 | Yes | Verify vendor support statement |
| Application-level `time()` calls | POSIX | Yes (via kernel) | No change needed |

### Step 2: Check Your `ntpd` or `chrony` Configuration

On Linux, run:

```bash
chronyc tracking
```

Look at the `Leap status` line. If it says `Normal`, you're fine for now. If it says `Insert second` or `Delete second`, a leap event is pending. After 2035, this field should remain `Normal` permanently — but only if your daemon is patched to handle the new UTC definition. **Chrony 4.5+ and NTPsec 1.2.3+ are the versions to target.**

### Step 3: Audit Application Code for Leap-Second Assumptions

Search your codebase for these patterns:

- `60` appearing in second-field validation (leap seconds make `:60` legal)
- Hardcoded assumptions that `TAI - UTC = 37` (the current offset as of 2026)
- Libraries like older versions of Java's `java.time` or Python's `datetime` that don't handle smearing

Google's "leap smear" approach — spreading the extra second over 24 hours — is now the de facto standard. If you're not smearing, you're at risk of the same thundering-herd bugs that hit Reddit in 2012.

### Step 4: Update Your Monitoring and Alerting Thresholds

Leap-second bugs often manifest as:

- Sudden CPU spikes at 23:59:60 UTC
- Database replication lag
- TLS certificate validation failures (due to time skew)
- Cron jobs firing twice or not at all

Add a synthetic check that compares your system clock against a trusted TAI source and alerts if the delta exceeds 1.5 seconds. After 2035, that delta will grow by roughly 1 second per 1–2 years, so your alerting logic must account for a **monotonically increasing TAI-UTC offset**.

### Step 5: Plan for the 2035 Cutover Date

Mark these dates on your calendar:

- **2026–2030**: Vendor firmware updates for GPS and PTP hardware
- **2031–2034**: Application testing with simulated post-2035 UTC
- **2035**: BIPM stops inserting leap seconds; TAI-UTC freezes at whatever value exists then
- **~2135**: First potential "leap minute" (speculative, per BIPM discussions)

## Common Issues, Alternatives, and What You Should Know

**The "smear vs. step" debate is over.** With no more leap seconds, the step approach disappears entirely. But legacy systems that hardcoded step logic may now break in unexpected ways — particularly embedded devices with firmware that hasn't been updated since 2016.

**GPS is the hidden risk.** GPS time is already offset from UTC by 18 seconds (as of 2026). After 2035, that offset will grow continuously. Any system that converts GPS time to UTC using a hardcoded offset table will drift. You need a firmware or software update that reads the current offset dynamically.

**Database vendors are lagging.** As of October 2026, only PostgreSQL 18 and MySQL 9.x have published roadmaps for post-2035 UTC handling. If you're on older versions, plan an upgrade cycle now.

**Cloud providers are your best ally.** AWS, Google Cloud, and Azure all operate their own atomic clocks and will absorb most of the complexity — but only if you use their time services. If you run your own NTP hierarchy, you own the problem.

## Frequently Asked Questions (FAQ)

### Will my Linux server break when leap seconds stop in 2035?
No, not automatically. Your server will continue to track UTC, but the offset between UTC and TAI will grow. The risk is in applications that assume a fixed offset. Patch your NTP daemon to Chrony 4.5+ or NTPsec 1.2.3+ and audit code for hardcoded `TAI-UTC` values.

### Does this affect GPS time or only UTC?
It affects the *relationship* between GPS time and UTC. GPS time is already offset from UTC (18 seconds in 2026), and that offset will increase after 2035. GPS receivers with outdated firmware that hardcode the offset will report incorrect UTC. Update firmware or use a software layer that reads the offset dynamically.

### What is a "leap minute" and when will it happen?
A leap minute is a hypothetical future correction where the BIPM would add 60 seconds at once instead of one second. It won't be needed until the TAI-UTC offset grows large enough — likely sometime in the 22nd century. No implementation details exist yet.

### Should I stop using leap smear now?
No. Leap smearing is still the safest approach for distributed systems, and it will remain useful for any future corrections. Keep your smear configuration in place.

## Final Verdict

The BIPM's decision is good news for anyone who has ever been paged at 23:59:60 UTC — but it's not a reason to relax. **You have a nine-year window to audit, patch, and test.** Start with your NTP daemon versions, then move to GPS firmware, then application code. The systems that break in 2035 will be the ones that assumed the offset would never change. Don't be one of them.