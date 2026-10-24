---
title: "MOZA AY210 + MFY Yoke Setup Guide: Best Settings & Is It Worth It?"
description: "Complete MOZA AY210 force feedback base and MFY yoke setup guide: MSFS 2024 settings, autopilot follow fix, firmware tips, and whether the bundle is worth it."
pubDate: 2026-10-18
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## MOZA AY210 + MFY Yoke: The Setup Guide Nobody Hands You in the Box

You unboxed the MOZA AY210 Force Feedback Base and MFY Yoke, bolted it to your desk, plugged in the USB-C and power, and… the yoke feels either dead-stiff or like a wet noodle, and the autopilot-follow feature everyone raved about isn't doing anything. This guide fixes that. Below you get the exact MOZA Cockpit settings, Microsoft Flight Simulator 2024 force feedback tuning, a troubleshooting checklist for the three most common AY210 problems, and a straight answer on whether the ~$600–$700 bundle beats a Honeycomb Alpha + Brunner CLS-E setup. Short version: the AY210 is the best value force-feedback yoke base on the market right now — **if** you spend 20 minutes configuring it properly.

## Step-by-Step Setup: From Dead Yoke to Full FFB Immersion

### Step 1 — Firmware and Software Baseline (Do This First)
1. Download **MOZA Cockpit** (Windows 10/11 only) from the official MOZA Racing site. Do not use third-party mirrors.
2. Connect the AY210 base **directly to a rear motherboard USB port** — no unpowered hubs. The base draws meaningful current during FFB spikes.
3. Update base firmware and MFY yoke firmware inside MOZA Cockpit. Mismatched firmware is the #1 cause of "yoke detected but no force feedback."
4. Run the **motor calibration** wizard and let the yoke sweep fully to both stops without touching it. Skipping this causes a permanent dead zone at center.

### Step 2 — Recommended MOZA Cockpit Settings
| Setting | Recommended Value | Why |
|---|---|---|
| Force Feedback Strength | 70–85% | Above 90% clips on high-rate joystick updates and overheats the motor |
| Damper | 15–25% | Adds yoke weight without masking control-surface feedback |
| Friction | 10–15% | Simulates cable tension in light GA aircraft |
| Spring (center) | 20–30% | Keep low — MSFS injects its own centering via FFB |
| Autopilot Follow | ON | This is the headline feature: the yoke physically moves with the AP |
| FFB Smoothing | 3–5 | Reduces motor whine on the AY210's direct-drive motor |

### Step 3 — Microsoft Flight Simulator 2024 Configuration
1. In MSFS controls, bind the MFY axes to **Elevator Axis** and **Aileron Axis** — not the generic "Yoke X/Y."
2. Set in-sim **Force Feedback Strength to 100%** but keep MOZA Cockpit at 70–85%. Let the sim send full signal and the base attenuate it; this preserves trim and stall-buffet fidelity.
3. Enable **"Force Feedback"** under General Options → Controls. If the toggle is greyed out, MSFS hasn't detected the base — recheck Step 1.
4. For autopilot follow: engage AP in a stable climb, then verify the yoke physically tracks pitch changes. If it doesn't, the sim's FFB output is being blocked by a competing input device (see troubleshooting below).

## Common Issues and Fixes

- **Yoke is detected but has zero resistance:** Almost always a firmware mismatch or a missing motor calibration. Re-run calibration; if it fails, unplug for 30 seconds and retry.
- **Autopilot follow doesn't move the yoke:** MSFS only outputs AP-follow FFB when the aircraft's AP is actively trimming. Test in the default Cessna 172 first — some third-party add-ons don't forward FFB trim data.
- **Motor overheating / thermal throttling during long flights:** Drop FFB strength to 65% and enable smoothing at 5. The AY210's motor is rated for continuous desktop use, not 100% clipping for hours.
- **Yoke feels notchy near center:** Increase damper to 25% and confirm you're not running the base through a USB 2.0 port.

## AY210 + MFY vs. Alternatives: Is It Worth It?

| Option | Price (approx.) | FFB | Autopilot Follow | Best For |
|---|---|---|---|---|
| MOZA AY210 + MFY | $600–$700 | Yes | Yes | Best value FFB yoke |
| Honeycomb Alpha/Bravo | $500+ | No | No | Plug-and-play, no FFB |
| Brunner CLS-E NG | $1,500+ | Yes | Yes | Pro-grade, high budget |
| Logitech G Pro Yoke | ~$350 | No | No | Budget, no FFB |

The AY210 is the only sub-$800 bundle that delivers real force feedback **and** autopilot follow. If you fly airliners on autopilot for hours, the AP-follow feature alone justifies the upgrade over a static yoke — the physical movement keeps you situationally aware of what the aircraft is doing.

## Frequently Asked Questions (FAQ)

### Does the MOZA AY210 work with X-Plane 12?
Partially. X-Plane 12 supports force feedback via its native FFB API, but autopilot follow is currently MSFS-only. Basic FFB effects (stall buffet, control loading) work in X-Plane with manual axis binding.

### Is the MOZA MFY yoke included with the AY210 base?
No — they're sold as a bundle but also separately. The AY210 base requires a compatible grip; the MFY is the recommended pairing and the only one that unlocks full autopilot-follow behavior.

### Can I use the AY210 on a desk without a cockpit rig?
Yes, but use the included desk clamp and ensure your desk is rigid. FFB torque will flex a thin desk and cause phantom inputs. A wheel stand or sim rig is strongly recommended.

## Final Verdict

**Buy it — with caveats.** The MOZA AY210 + MFY bundle is the smartest force-feedback entry point for desktop flight simmers in 2026, and the autopilot-follow feature is genuinely transformative for airliner flying. But budget 30 minutes for firmware, calibration, and MSFS tuning, or you'll think the hardware is broken. If you only fly manual GA aircraft and never touch autopilot, save the money and get a static yoke. If you want immersion that moves with you, this is the bundle to beat.