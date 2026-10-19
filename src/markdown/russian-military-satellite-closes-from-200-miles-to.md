---
title: "Cosmos 2612 vs ICEYE-X36: How to Track Satellite Close Approaches"
description: "Track Russia's Cosmos 2612 near-miss with ICEYE-X36 using free tools. Step-by-step guide to TLE data, conjunction alerts, and orbit analysis."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Track the Cosmos 2612 and ICEYE-X36 Close Approach Yourself

When Russia's Cosmos 2612 maneuvered from more than 200 miles down to roughly 3 miles from ICEYE-X36 — a U.S.-owned synthetic aperture radar (SAR) satellite operated for Ukrainian intelligence — the story broke in mainstream outlets but left a practical gap: **how do you actually verify or monitor an event like this?** This guide turns the headline into a repeatable workflow. You'll learn to pull public orbital data (TLEs), run conjunction checks, and interpret the numbers — the same methods amateur satellite trackers and analysts use. Expect about 20–30 minutes to set up and a few minutes per check afterward.

## Step-by-Step: Monitor Any Satellite Close Approach

The core skill is comparing Two-Line Element sets (TLEs) — the public orbital snapshots published by Space-Track and CelesTrak. Here's the practical workflow:

1. **Create a free Space-Track.org account.** Registration is free for non-commercial use. Once approved, download the latest TLE for both objects (search by NORAD ID for Cosmos 2612 and ICEYE-X36).
2. **Load the TLEs into a tracking tool.** Free options: **Heavens-Above**, **N2YO.com**, **Skyfield** (Python), or **GMAT** for serious analysis. Paste the two-line element sets and set your observer location or target orbit.
3. **Run a conjunction (close-approach) screen.** In Skyfield, propagate both orbits over a 24–72 hour window at 10-second steps and compute the distance between position vectors. Flag any pass where the separation drops below your threshold (e.g., 5 km).
4. **Check the relative velocity.** A 3-mile (≈5 km) miss at 7+ km/s closing speed is a high-risk conjunction. Record the time of closest approach (TCA) and the miss distance.
5. **Cross-reference official alerts.** Space-Track publishes Conjunction Data Messages (CDMs) and screening alerts. Compare your computed TCA against theirs — discrepancies usually mean a stale TLE.
6. **Watch for maneuvers.** A large jump between consecutive TLEs (especially in mean motion or argument of perigee) signals an active maneuver — exactly what happened when Cosmos 2612 dropped from ~200 miles to ~3 miles.

### Quick Reference: Tools & Data Sources

| Tool / Source | Cost | Best For | Data Freshness |
|---|---|---|---|
| Space-Track.org | Free | Official TLEs + CDMs | Hours |
| CelesTrak | Free | Backup TLEs, GP data | Hours |
| N2YO.com | Free | Quick visual passes | Hours |
| Skyfield (Python) | Free | Custom conjunction math | Real-time |
| Heavens-Above | Free/Paid | Observer passes | Hours |
| Commercial SSA (e.g., LeoLabs) | Paid | High-precision tracking | Minutes |

## Common Issues, Alternatives, and What You Should Know

**TLE staleness is the #1 trap.** A TLE is a snapshot; accuracy degrades by roughly 1–3 km per day of propagation error for LEO objects. If you're screening a maneuver-heavy object like Cosmos 2612, always pull the freshest element set — a day-old TLE can show a 3-mile miss that has already changed.

**You can't see classified objects.** Military satellites like Cosmos 2612 often have limited or delayed public data. If Space-Track shows no recent TLE, that's a signal, not a glitch — check CelesTrak's supplemental GP data or community trackers (e.g., satellite observer forums) for amateur-derived elements.

**Don't confuse SAR with optical.** ICEYE-X36 is a radar satellite — it images through clouds and at night, which is precisely why it's valuable for defense intelligence. That context matters: a close approach to a SAR platform is a different operational concern than to an optical satellite.

**Cost reality check.** Free tools are adequate for education and rough screening. For anything resembling professional space-domain awareness, commercial SSA services (LeoLabs, Slingshot, ExoAnalytic) provide sub-kilometer precision and maneuver detection — typically enterprise pricing, not consumer.

**Legal/ethical note.** Tracking satellites is legal and widely practiced. Do not attempt to access non-public tracking data or interfere with any system.

## Frequently Asked Questions (FAQ)

### How close was Cosmos 2612 to ICEYE-X36?
Reports indicate Russia's Cosmos 2612 closed from more than 200 miles (≈320 km) to approximately 3 miles (≈5 km) from the U.S.-owned ICEYE-X36 radar satellite — a very close conjunction at orbital velocities, where relative speeds exceed 7 km/s.

### Can I track Cosmos 2612 and ICEYE-X36 for free?
Yes. Use Space-Track.org or CelesTrak for TLEs, then N2YO.com or Skyfield for propagation and conjunction screening. Free tools give good rough estimates, though classified objects may have delayed or missing public data.

### What is a dangerous satellite conjunction distance?
There's no universal threshold, but many operators flag conjunctions under 1–5 km as high-risk, especially at LEO closing speeds above 10 km/s. A 3-mile (≈5 km) miss is well inside the range that triggers maneuver reviews.

### Why does a satellite suddenly change orbit?
Maneuvers for station-keeping, collision avoidance, or intentional repositioning. A sharp change in TLE mean motion or altitude between element sets — like Cosmos 2612's drop — indicates an active burn.

## Final Verdict

Don't just read the headline — verify it. Spend 20 minutes setting up Space-Track and Skyfield, and you'll have a reusable conjunction-screening workflow that works for any satellite pair, not just this one. Start with the free stack (Space-Track + N2YO + Skyfield); only upgrade to commercial SSA if you need sub-kilometer precision or real-time maneuver alerts. For hobbyists and analysts alike, public TLE data is the fastest way to separate verified orbital facts from viral speculation.