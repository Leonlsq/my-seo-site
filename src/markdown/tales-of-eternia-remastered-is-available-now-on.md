---
title: "Tales of Eternia Remastered PC: Best Settings & Fixes"
description: "Tales of Eternia Remastered on Steam: best PC settings, 60FPS fixes, controller setup, and how it compares to the PSP original."
pubDate: 2026-10-16
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Tales of Eternia Remastered on PC: What You Need to Know First

Tales of Eternia Remastered is available now on Steam, bringing the classic 2000 PlayStation-era action RPG (known as Tales of Destiny II in North America) to modern hardware for the first time with official English support. If you just bought it and the game is stuttering, running at a locked framerate, or refusing to recognize your DualSense, this guide covers the exact settings, config tweaks, and workarounds you need. The short version: the port runs well on mid-range hardware, but it ships with a 30FPS cap enabled by default and a few controller quirks that trip up most players in the first hour.

## Best PC Settings for Tales of Eternia Remastered

The remaster is a lightweight title — it's a 2D sprite-based engine with upscaled assets, not a full 3D remake. That means you should be prioritizing framerate and input latency over visual fidelity. Here's a recommended baseline for most systems:

| Setting | Recommended Value | Why |
|---|---|---|
| Frame Rate Cap | 60 FPS (or Uncapped) | Default 30FPS cap adds input lag in combat |
| Resolution | Native (1080p/1440p/4K) | Sprites scale cleanly, minimal GPU cost |
| Sprite Filtering | Bilinear (not Nearest) | Nearest causes shimmer during camera pans |
| Scanline Filter | Off | Adds blur on LCD/OLED panels |
| Battle Speed | Normal | Fast mode can desync audio in some builds |
| V-Sync | On (with G-Sync/FreeSync off in driver) | Prevents screen tearing in scrolling towns |
| Motion Blur | Off | Not present in original; purely cosmetic toggle |

### Step-by-step: unlocking 60FPS

1. Launch the game and open **Options → Display Settings**.
2. Set **Frame Rate** from `30` to `60`. If you have a 120Hz+ monitor, try `Uncapped` — the engine handles it without physics issues in most tested builds.
3. Disable in-game V-Sync and instead force it through your GPU control panel (NVIDIA Control Panel → Manage 3D Settings → Program Settings → Tales of Eternia Remastered → V-Sync: On).
4. If you get micro-stutter, cap the framerate to 60 in the same panel using **Max Frame Rate** rather than using the in-game cap.
5. Restart the game — the framerate setting only applies on a fresh boot in the current build.

## Controller Setup and Input Fixes

The most common complaint after launch is controller detection. The remaster supports XInput natively but treats DirectInput and PlayStation controllers inconsistently.

- **Xbox controllers:** Plug-and-play. No config needed.
- **DualSense / DualShock 4:** Enable **Steam Input** (Steam → right-click the game → Properties → Controller → Enable Steam Input). Without it, the game may show Xbox button prompts or ignore the controller entirely.
- **Switch Pro Controller:** Works via Steam Input only. Set the layout to "Gamepad" template.
- **Keyboard players:** Rebind the Arte shortcuts — the default mapping puts them on the number row, which is awkward during fast combos. Move them to Q/E/R/F.

If your controller disconnects mid-battle, it's usually a Bluetooth power-saving issue. Switch to a wired USB connection or disable "Allow the computer to turn off this device to save power" in Device Manager under your Bluetooth adapter.

## Common Issues and What You Should Know

**Black screen on launch:** This is almost always a fullscreen resolution mismatch. Delete the config file at `%AppData%\TalesOfEterniaRemastered\settings.ini` and relaunch — the game will regenerate it at your desktop resolution.

**Audio desync in skits:** Skits (the optional character conversations) can drift out of sync if Battle Speed is set to Fast. Set it back to Normal, or toggle the "Skip Skit Animation" option in Accessibility.

**Save file location:** Backups live in `Documents\My Games\Tales of Eternia Remastered\Saves`. The remaster uses cloud saves via Steam, but local backups are worth keeping before major patches.

**How it compares to the PSP version:** The 2005 PSP port added widescreen and a new dungeon but cut the two-player co-op mode. This remaster restores local co-op, keeps the widescreen presentation, and adds a re-recorded English dub alongside the original Japanese audio. It does **not** include the PSP-exclusive dungeon, which is a genuine point of contention for veterans.

**Performance expectations:** On a GTX 1650 / Ryzen 5 3600 combo, the game holds a locked 60FPS at 1440p with GPU usage under 30%. Integrated graphics like Intel Iris Xe can manage 1080p/60 with filtering reduced to Nearest.

## Frequently Asked Questions (FAQ)

### Is Tales of Eternia Remastered worth it on Steam?
Yes, if you want the definitive English-language version with restored co-op and modern resolution support. It's a faithful port rather than a full remake, so temper expectations on visual overhaul. At its price point it's a solid pickup for JRPG fans.

### Does Tales of Eternia Remastered have Japanese voice acting?
Yes. You can switch between English and Japanese audio in **Options → Sound → Voice Language**. The Japanese track uses the original 2000 recordings.

### Can I play Tales of Eternia Remastered with two players?
Yes. Local co-op for two players is supported in battle, restored from the original PS1 release. Player 2 joins by pressing Start on a second connected controller during combat.

### Why is my framerate locked at 30FPS?
The game defaults to a 30FPS cap. Change it in Display Settings and restart the application — the change does not apply until the next launch.

## Final Verdict

Tales of Eternia Remastered is a competent, lightweight port that rewards five minutes of settings tweaking. Set the framerate to 60, enable Steam Input for non-Xbox controllers, and you'll get a clean, low-latency experience that finally does this underrated entry justice on PC. Skip it only if you were hoping for a full 3D remake — this is a preservation-grade remaster, and judged on those terms, it delivers.