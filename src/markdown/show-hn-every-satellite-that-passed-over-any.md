---
title: "How to See Every Satellite That Photographed Your Street"
description: "Step-by-step guide to using the Show HN satellite tracker: find every satellite pass over your location in 7 days and pull real Sentinel-2 and Landsat photos."
pubDate: 2026-11-09
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to See Every Satellite That Photographed Your Street (7-Day Pass Guide)

A developer just released a browser-based tool that answers a question most of us have never been able to ask: *which satellites actually photographed my street this week?* The Show HN project cross-references the CelesTrak catalog using SGP4 orbital propagation, finds every pass over any location in the last 7 days, and then pulls the real Sentinel-2, Landsat, and NASA imagery from those passes. The best part: it runs entirely in your browser in roughly half a second and never stores your location. This guide walks you through exactly how to use it, what the results actually mean, and how to verify the data yourself.

## Step-by-Step: Finding Satellites Over Your Location

Here's how to get from "I'm curious" to "here's the photo of my neighborhood from space."

1. **Open the tool** from the GitHub repo (`github.com/dev-Armaan/sa`) and let the CelesTrak catalog load. The full ~17,000-object catalog is rendered on the GPU, solving Kepler's equation every frame, so the globe stays smooth even at full density.
2. **Enter any place** — your street address, a landmark, or coordinates. The pass search runs SGP4 propagation locally in your browser, typically completing in about **0.5 seconds**.
3. **Review the 7-day pass list.** Each entry shows the satellite, the pass time, and whether imagery is available.
4. **Check the "watched" label.** This is the critical detail: the tool only marks a location as "watched" if a **real image actually exists** for that pass. No phantom passes, no fake coverage.
5. **Pull the imagery.** Click through to the Sentinel-2, Landsat, or NASA image associated with that pass.
6. **Cross-check the timestamp.** Expect Sentinel-2 timestamps to be **5–10 minutes off** from when the satellite actually crosses your exact spot — this is a known quirk the developer had to work around, not a bug in your search.

### What the Data Sources Actually Cover

| Source | Resolution | Revisit Cadence | Best For |
|---|---|---|---|
| Sentinel-2 | ~10 m | ~5 days (2-sat constellation) | Recent, color imagery of streets/fields |
| Landsat | ~30 m | ~16 days per satellite | Long-term change, archival comparison |
| NASA imagery | Varies | Varies | Context and supplementary views |

The 7-day window is deliberate: it matches the practical revisit cadence of the Sentinel-2 constellation, so you're seeing genuinely recent passes rather than stale archives.

## Why the Pass Search Is Trustworthy (And How to Verify It)

The most impressive claim in the project is that **the pass search cannot skip a pass**. The developer validated this against a brute-force search on the hardest edge cases in orbital mechanics:

- **The poles**, where ground tracks converge and passes overlap heavily.
- **The antimeridian** (the ±180° longitude line), where naive math breaks.
- **Tiny swaths**, where a narrow sensor footprint could easily be missed by a sloppy algorithm.

The result: **0 missed passes** against brute force. If you want to sanity-check this yourself, pick a location near the antimeridian (e.g., Fiji or the Aleutians) and compare the tool's output against a manual SGP4 calculation — the lists should match exactly.

### Common Issues and What You Should Know

- **"No passes found" for your location?** This usually means no *imaging* satellite covered your spot in the window — not that the tool failed. Polar-orbiting sensors have gaps, especially at low latitudes between swaths.
- **Timestamps look slightly off?** That 5–10 minute Sentinel-2 offset is expected. The tool reports the pass time; the image capture time can differ by minutes.
- **Privacy concern?** The location is processed client-side and not stored. You can confirm this by watching the network tab — no location payload leaves your browser.
- **Performance on older machines?** Rendering all ~17k objects on the GPU is demanding. If the globe stutters, close other GPU-heavy tabs; the pass search itself remains fast regardless.

## Frequently Asked Questions (FAQ)

### Can I find out if a satellite photographed my house in the last week?
Yes — enter your address and the tool lists every satellite pass over that point in the last 7 days, then flags which passes have real Sentinel-2, Landsat, or NASA imagery available. It only says "watched" when an actual image exists.

### How accurate is the satellite pass search?
The developer verified the SGP4-based search against brute-force calculations at the poles, the antimeridian, and tiny swaths, with **zero missed passes**. It uses the CelesTrak catalog and runs in your browser in about half a second.

### Why are Sentinel-2 timestamps 5–10 minutes off?
Sentinel-2's reported timestamps often differ by 5–10 minutes from the moment the satellite physically crosses your location. This is a known quirk of the data, and the tool accounts for it rather than hiding it.

### Does the tool store my location?
No. All computation happens client-side in your browser, and the location is not stored or transmitted.

## Final Verdict

If you've ever wondered what actually photographed your street from orbit, this is the most direct answer available — and it's free, open-source, and privacy-respecting. Start with your home address, then test the antimeridian claim yourself if you want to see the engineering rigor up close. For satellite-curious users, OSINT researchers, and anyone verifying imagery coverage, this tool is an instant bookmark.