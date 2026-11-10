---
title: "Exanima November 2026 Patch: Best Physics & Shadow Settings"
description: "Exanima November 2026 dev diary brings parry, physics, stacking, and shadow upgrades. Here's how to configure settings for stable FPS and better combat."
pubDate: 2026-11-03
tags: ['Gaming', 'Guide', 'Optimization']
---

## Exanima November 2026 Dev Diary: What Actually Changed and How to Configure It

The November 2026 Exanima dev diary (posted by u/TilkinBass on r/Exanima) confirms four long-requested systems landing in the experimental branch: a reworked **parry window**, **physics-driven object stacking**, **improved contact shadows**, and **stability fixes for ragdoll collisions**. The direct takeaway: this is not a content patch — it's a simulation upgrade, and it will change how your PC performs and how melee combat feels. If you're returning to the game or tuning it for the first time, the settings you used in 2025 are now suboptimal. This guide gives you the exact configuration to keep 60 FPS while exploiting the new parry timing.

## Step-by-Step: Optimizing Exanima for the 2026 Physics & Shadow Update

The headline feature is that **parry is now physics-resolved** rather than animation-cancelled. That means your weapon's actual collision volume must intercept the incoming swing, so timing windows are tighter but more consistent. Here's how to adapt your setup.

### 1. Update to the Experimental Branch First
The dev diary features ship to `experimental` before `stable`. On Steam: right-click Exanima → **Properties** → **Betas** → select `experimental`. Back up your save from `%AppData%/Local/Exanima` before switching — physics changes can corrupt in-progress ragdoll states.

### 2. Recalibrate Shadow Settings
Improved contact shadows are the biggest performance cost. Recommended tiering:

| GPU Tier | Shadow Quality | Contact Shadows | Expected FPS (1080p) |
|---|---|---|---|
| GTX 1660 / RX 580 | Medium | Off | 55–70 |
| RTX 3060 / RX 6600 | High | On | 60–75 |
| RTX 4070+ | Ultra | On | 90+ (uncapped) |

Disable **Ambient Occlusion** if you drop below 50 FPS in the Arena — the new shadow pass already approximates contact darkening.

### 3. Tune Physics Stacking Load
Object stacking is now fully simulated, so rooms with many crates and debris cost CPU time. If you get stutter when entering the Market or Cellar:
- Cap **Physics Update Rate** at 60 Hz (default 120 Hz is overkill for most CPUs).
- Lower **Max Active Ragdolls** to 8.
- Avoid dragging more than ~15 loose items at once — the stacking solver recalculates contacts every frame.

### 4. Master the New Parry Timing
The parry window is now roughly **120–160 ms** depending on weapon mass and swing speed. Heavier weapons (longsword, poleaxe) have a slightly wider window but slower recovery. Practice in the training arena: block *into* the swing arc rather than tapping at the last frame. Light weapons like the short sword reward early parries; heavy weapons reward late ones.

## Common Issues, Workarounds & What You Should Know

- **"My parries stopped registering after the patch."** You're likely still on the `stable` branch. The old animation-based parry still exists there; the physics parry is experimental-only as of November 2026.
- **Frame drops in stacked-object rooms.** This is expected — the new solver is accurate but CPU-bound. A 6-core CPU (Ryzen 5 5600 or better) is now the practical floor.
- **Shadows look softer, not sharper.** That's intentional. The dev diary describes a denoised contact shadow pass; it trades crispness for realistic grounding. If you prefer the old look, set Shadow Quality to Medium.
- **Save compatibility.** Physics states from pre-patch saves may behave oddly (items floating or clipping). Load a fresh save if you see persistent glitches.

### Quick Comparison: Old vs. New Systems

| System | Pre-Nov 2026 | Post-Nov 2026 |
|---|---|---|
| Parry | Animation cancel, ~200 ms window | Physics collision, ~120–160 ms |
| Stacking | Approximated, capped objects | Full solver, CPU-limited |
| Shadows | Standard shadow map | Denoised contact shadows |
| Performance | GPU-bound | More CPU-bound |

## Frequently Asked Questions (FAQ)

### Is the Exanima November 2026 update on the stable branch yet?
No. As of the dev diary, all four features are on the `experimental` branch. Expect a stable merge in a later patch, historically 3–6 weeks after experimental.

### Does the new parry system make combat harder?
It raises the skill floor but lowers randomness. Timing is tighter, but successful parries are more reliable because they're resolved by actual weapon collision rather than animation state.

### Will the shadow improvements hurt performance on older GPUs?
Yes, noticeably. On a GTX 1050 Ti or RX 570, expect a 10–20% FPS drop with contact shadows enabled. Disable them and use Medium shadow quality to recover most of the loss.

### Can I revert to the old physics if I dislike the changes?
Yes — switch back to the `stable` branch in Steam Betas. Your experimental save may not load correctly on stable, so keep separate backups.

## Final Verdict

The November 2026 Exanima update is a genuine simulation upgrade, not a graphics reskin — and that means **you should treat it as a performance re-tuning task, not just a content drop**. Switch to experimental only if you have a 6-core CPU and a mid-range GPU or better; otherwise, wait for the stable merge and the inevitable optimization pass. For everyone else: cap physics at 60 Hz, keep contact shadows on if you're above an RTX 3060, and spend 20 minutes in the training arena relearning parry timing. The combat is better — but only if your rig and your muscle memory are configured for it.