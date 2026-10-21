---
title: "Kosmos 2612 vs ICEYE-X36: Satellite Close-Approach Explained"
description: "What the Kosmos 2612 extreme proximity maneuver near ICEYE-X36 means for satellite operators and how to track close approaches yourself."
pubDate: 2026-10-21
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What the Kosmos 2612–ICEYE-X36 Close Approach Actually Means (And How to Track It)

On October 21, 2026, reports confirmed that Russia's **Kosmos 2612** spacecraft closed from hundreds of kilometers away to "extreme proximity" of **ICEYE-X36**, a synthetic aperture radar (SAR) satellite operated by Finland's ICEYE and used extensively by Ukraine for all-weather imaging. If you're a satellite operator, orbital analyst, or just someone trying to separate signal from hype, here's the direct takeaway: **this is a rendezvous-and-proximity-operations (RPO) event, not a collision**—but it is a textbook case of why conjunction assessment and space domain awareness (SDA) tooling matter. This guide breaks down the maneuver, the tracking tools, and the exact steps you can take to monitor similar events yourself.

## Step-by-Step: How to Track a Close Approach Like Kosmos 2612 vs ICEYE-X36

You don't need a government clearance to watch this. Here's a practical workflow using public TLE (Two-Line Element) data and free tools.

### 1. Pull current orbital data
- **Space-Track.org** (free account required) — authoritative source for TLEs and Conjunction Data Messages (CDMs).
- **CelesTrak** — public TLEs, updated multiple times daily.
- **n2yo.com / Heavens-Above** — consumer-friendly pass predictions.

### 2. Compute the miss distance
Use **GMAT** (free, NASA), **STK** (commercial), or the open-source **Skyfield** Python library. A minimal Skyfield check:

```python
from skyfield.api import load
ts = load.timescale()
sats = load.tle_file('https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle')
by_name = {s.name: s for s in sats}
t = ts.utc(2026, 10, 21, 12, 0)
a, b = by_name['KOSMOS 2612'], by_name['ICEYE-X36']
print(a.at(t).separation_from(b.at(t)).km)
```

### 3. Set a screening threshold
| Threshold | Action |
|-----------|--------|
| > 5 km | Monitor, no action |
| 1–5 km | Flag for daily re-screening |
| < 1 km | Escalate; request CDM from Space-Track |
| < 100 m | Treat as maneuver-worthy; notify operator |

### 4. Cross-check the maneuver signature
A genuine RPO maneuver shows up as a **sudden change in mean motion or argument of perigee** between consecutive TLE epochs. If Kosmos 2612's semi-major axis shifted by more than ~1 km within 24 hours, that's a deliberate burn—not drift.

### 5. Watch for the "shadowing" pattern
Kosmos 2612 is a Russian military satellite (likely a Luch/Olymp inspector-class asset). These craft are designed to loiter near targets. Track the **relative drift rate**—if it stabilizes near zero at close range, the spacecraft is station-keeping, which is the strongest indicator of intentional inspection.

## Common Issues, Alternatives, and What You Should Know

**Issue 1: TLEs are stale.** Public TLEs can lag 6–24 hours behind reality. For a fast-moving RPO event, that's a huge error bar. *Workaround:* use Space-Track's CDMs (updated hourly for flagged conjunctions) or commercial SDA feeds from LeoLabs or Slingshot Aerospace.

**Issue 2: "Extreme proximity" is undefined.** Media reports don't specify the actual miss distance. Historically, Russian inspector satellites have closed to **tens of kilometers** (e.g., Luch/Olymp maneuvers near Intelsat satellites in 2015 and 2018). Treat any figure under 50 km as operationally significant.

**Issue 3: ICEYE-X36 is a commercial SAR asset.** Unlike government satellites, ICEYE cannot maneuver freely without customer coordination. This makes it a soft target—which is precisely the strategic point of the maneuver.

**Alternatives to paid SDA tools:**
- **OrbitGuardian** (free tier) — automated conjunction alerts.
- **KeepTrack** — open-source, excellent for visualizing RPO geometry.
- **Space-Track's "Decay" and "Conjunction" APIs** — free but rate-limited.

**What this means for operators:** Add RPO screening to your standard conjunction workflow. Standard CDM screening catches accidental collisions; it does *not* flag deliberate shadowing. You need a separate "proximity anomaly" rule that triggers on any object closing to < 25 km and station-keeping.

## Frequently Asked Questions (FAQ)

### What is Kosmos 2612 and why does it matter?
Kosmos 2612 is a Russian military satellite believed to be part of Russia's inspector-satellite program. Its maneuver toward ICEYE-X36 demonstrates active RPO capability against Western commercial assets—a growing concern for both military and commercial operators.

### Did Kosmos 2612 collide with ICEYE-X36?
No. Reports describe "extreme proximity," not contact. No collision or debris-generating event has been confirmed. The maneuver is best characterized as a close-approach or inspection pass.

### How close can satellites safely operate?
There's no universal rule, but 1 km is a common operational red line for non-cooperative objects. Cooperative formation flying (like Planet's flocks) routinely operates at tens of meters with active control. The danger is when one party isn't coordinating.

### Can I track this event for free?
Yes. Space-Track.org, CelesTrak, and KeepTrack all offer free access. Expect a 6–24 hour lag on TLEs, which is why CDMs from Space-Track are more reliable for fast-moving events.

### Is ICEYE-X36 still operational?
As of reporting, no damage or loss of service has been announced. ICEYE has not publicly confirmed the encounter's details.

## Final Verdict

The Kosmos 2612–ICEYE-X36 encounter is a wake-up call, not a catastrophe. **If you operate or insure satellites, add RPO-specific screening to your conjunction workflow today**—standard CDMs won't catch a deliberate shadow. For hobbyist trackers, Space-Track plus Skyfield is enough to follow the geometry in near-real time. For commercial operators, budget for a paid SDA feed (LeoLabs or Slingshot) if you carry high-value assets in low Earth orbit. The era of assuming "close approach = accident" is over.