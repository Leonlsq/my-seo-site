---
title: "Shogun 2 Remaster PC Fixes: AI & Performance Guide"
description: "Fix Shogun 2 Remaster's bad AI and stuttering performance on PC with this step-by-step settings, mod, and config guide."
pubDate: 2026-10-15
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Shogun 2 Remaster Performance and AI: What Actually Broke

The *Shogun 2* remaster landed on Steam to an "Overwhelmingly Negative" review score, and the complaints cluster around two things: broken campaign/battle AI and frame times that collapse in large sieges. If you already bought it (or are holding off), this guide skips the outrage cycle and gives you the fixes that actually move the needle — config edits, driver settings, and the mods that patch what the developers shipped.

The short version: the remaster is a **re-render, not a re-code**. The underlying engine is still the 2011 Warscape build, so the AI logic and CPU threading behave like a 15-year-old game wearing a new 4K texture pack. That mismatch is why you get 90 FPS in the campaign map and 24 FPS the moment 40 units collide. Treat it as an old game with new paint and the fixes below make sense.

## Step-by-Step Fixes for Stutter, Low FPS, and Dumb AI

### 1. Fix the CPU bottleneck first (biggest FPS win)

Warscape is **CPU-bound in battles**, not GPU-bound. Before touching graphics, cap your frame rate so the CPU isn't fighting itself:

1. Open `%AppData%\The Creative Assembly\Shogun2\scripts\preferences.script.txt`.
2. Find `gfx_vsync` and set it to `1`, or use your GPU driver's frame limiter to cap at 60.
3. Set `number_of_threads` to your physical core count (not logical). A 6-core CPU should read `6`, not `12`.
4. Save, then right-click the file → Properties → check **Read-only** so the game can't overwrite it.

Uncapped frame rates on this engine cause the classic "high average FPS, terrible 1% lows" pattern. Capping is the single most effective change.

### 2. Graphics settings that matter (and the ones that don't)

| Setting | Recommended | Why |
|---|---|---|
| Unit size | Ultra only if 6+ cores | Direct CPU cost per soldier |
| Shadows | Medium | Huge GPU cost, minimal visual gain |
| Anti-aliasing | FXAA (not MSAA) | MSAA tanks siege FPS |
| Texture quality | Ultra | VRAM-bound, cheap on modern GPUs |
| Water/reflections | Low | Remastered shaders are unoptimized |
| Depth of field | Off | Post-process stutter source |

### 3. Driver and OS-level tweaks

- **Disable fullscreen optimizations**: right-click the `.exe` → Compatibility → check "Disable fullscreen optimizations."
- **Force exclusive fullscreen** via the in-game option; borderless windowed adds input lag and frame pacing issues.
- **NVIDIA users**: set Low Latency Mode to "Ultra" and Power Management to "Prefer Maximum Performance" in the Control Panel.
- **AMD users**: enable Anti-Lag and disable Radeon Chill for this title.
- **Windows 11**: add the game folder to Exploit Protection exclusions — the remaster's anti-tamper layer occasionally trips CFG.

### 4. Fixing the "dumb AI" complaints

The AI issues are largely **design regressions**, not bugs you can patch with settings. But you can mitigate:

- **Battle AI passivity**: the remaster's AI often holds position instead of flanking. There's no config fix — this is hardcoded behavior.
- **Campaign AI**: reduce difficulty to Normal; higher difficulties inflate AI bonuses rather than intelligence, which makes the map feel more broken, not smarter.
- **Mods**: search the Workshop for "AI overhaul" and "Better Campaign AI" packs. These restore much of the original 2011 aggression logic that the remaster appears to have regressed.

## What You Should Know Before Buying or Refunding

- **Refund window**: Steam's 2-hour/14-day policy still applies. If you're past 2 hours and unhappy, you can still submit a refund request citing performance — it's discretionary but frequently granted for broken launches.
- **The remaster vs. original**: the 2011 *Shogun 2* with the same mods often runs *better* on modern hardware than the remaster, because it lacks the new shader layer. If you own the original, test it before committing.
- **No official performance patch** had shipped at the time of writing. Community mods are your only real lever.
- **VRAM**: 8GB is the practical floor for Ultra textures at 1440p. 6GB cards will stutter in sieges regardless of settings.

## Frequently Asked Questions (FAQ)

### Why does Shogun 2 Remaster stutter in battles but run fine on the campaign map?
The campaign map is GPU-light and single-threaded, so it hits high FPS easily. Battles are CPU-bound: every soldier runs AI and pathfinding logic on the same 2011 engine threads. More units = more CPU load, which is why capping frame rate and matching `number_of_threads` to your physical core count helps most.

### Is the Shogun 2 Remaster AI actually broken or just different?
It's a regression, not a total failure. The AI functions but is more passive and less likely to flank than the original. Difficulty settings add stat bonuses rather than smarter behavior, so raising difficulty makes it feel worse. Community AI-overhaul mods are the only meaningful fix.

### Can I fix Shogun 2 Remaster performance without mods?
Yes. Cap your frame rate, set thread count to physical cores, drop shadows and water to Low/Medium, disable depth of field, and force exclusive fullscreen. These changes alone typically recover 20–40% of lost frame time in large battles on mid-range CPUs.

## Final Verdict

If you haven't bought it: **wait**. The remaster is a texture-and-lighting pass on a 2011 engine, and the AI regression isn't fixable through settings. If you already own it, apply the config and graphics fixes above immediately — they'll get you from unplayable to tolerable — then grab a Workshop AI overhaul to restore campaign behavior. If you still own the original *Shogun 2*, honestly, mod that instead and refund this. The remaster is only worth it once the developer ships a real performance and AI patch, and there's no confirmed date for that.