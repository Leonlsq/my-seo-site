---
title: "Total War: SHOGUN 2 Won't Launch? 7 Fixes That Work in 2026"
description: "Total War: SHOGUN 2 crashing or stuck on a black screen? Here are 7 proven fixes for launch errors, DX11 crashes, and mod conflicts in 2026."
pubDate: 2026-10-14
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Total War: SHOGUN 2 Won't Launch? Here's the Direct Fix

You click Play, the screen flickers, and nothing happens. Or you get a black screen, a silent crash to desktop, or an endless "Preparing to launch" loop. Total War: SHOGUN 2 is a 2011 game running on a DirectX 9/11 hybrid engine, and on modern Windows 10/11 systems with 12th-gen Intel CPUs, high-refresh monitors, and updated GPU drivers, it breaks in predictable ways. The good news: nearly every launch failure traces back to one of seven root causes, and all of them are fixable in under 20 minutes. Below are the fixes ordered by success rate, starting with the ones that solve the most cases.

## Step-by-Step Fixes (Ordered by Success Rate)

### Fix 1: Force DirectX 9 Mode (Solves ~40% of Crashes)

SHOGUN 2's DX11 renderer is unstable on newer GPUs. Force the older, more compatible path:

1. Open Steam → right-click **Total War: SHOGUN 2** → **Properties**.
2. In **Launch Options**, paste: `-dx9`
3. Launch the game. If it boots, keep this flag permanently — visual difference is minor.

### Fix 2: Verify Game Files & Clear the Scripts Cache

Corrupted config files are the #1 cause of black-screen launches.

1. Steam → right-click the game → **Properties** → **Installed Files** → **Verify integrity of game files**.
2. Navigate to `%AppData%\The Creative Assembly\Shogun2\scripts\` and **delete the entire contents** of the `scripts` folder (not the folder itself).
3. Also delete `preferences.script.txt` in `%AppData%\The Creative Assembly\Shogun2\scripts\`.
4. Relaunch. The game regenerates clean defaults.

### Fix 3: Disable the Steam Overlay and Discord Overlay

Overlay hooks inject into the DX9/DX11 context and cause instant crashes on some driver versions.

- Steam: **Properties** → uncheck **Enable the Steam Overlay while in-game**.
- Discord: **User Settings** → **Game Overlay** → toggle off, or remove SHOGUN 2 from the detected games list.

### Fix 4: Set a 60Hz Refresh Rate and Windowed Mode

High-refresh (144Hz+) monitors cause the launcher to hang on some setups.

1. Right-click desktop → **Display settings** → set refresh rate to **60Hz** temporarily.
2. Add `-windowed` to launch options, then switch to borderless fullscreen in-game.

### Fix 5: Compatibility Mode for Windows 7

1. Locate `Shogun2.exe` in `steamapps\common\Total War SHOGUN 2\`.
2. Right-click → **Properties** → **Compatibility** tab.
3. Check **Run this program in compatibility mode for: Windows 7**.
4. Check **Disable fullscreen optimizations** and **Run as administrator**.

### Fix 6: Remove Conflicting Mods

Mods like DarthMod or Radious that edit the same tables cause load-order crashes. Disable all mods via the launcher's **Mod Manager**, test vanilla, then re-enable one at a time. Delete leftover `.pack` files in the `data` folder if a mod was uninstalled incorrectly.

### Fix 7: Update GPU Drivers & Reinstall DirectX Runtime

- Update to the latest NVIDIA/AMD driver, but **roll back one version** if the crash started after a driver update.
- Install the legacy **DirectX End-User Runtime (June 2010)** from Microsoft — modern Windows often lacks the DX9 redistributables SHOGUN 2 needs.

## Quick Diagnosis Table

| Symptom | Most Likely Cause | Fix |
|---|---|---|
| Black screen on launch | Corrupt scripts/config | Fix 2 |
| Crash to desktop instantly | DX11 renderer | Fix 1 |
| Stuck on "Preparing to launch" | Steam overlay | Fix 3 |
| Freezes after logo | High refresh rate | Fix 4 |
| Crash only with mods | Load order conflict | Fix 6 |
| "d3dx9_xx.dll missing" | Missing DX9 runtime | Fix 7 |

## What You Should Know Before You Tinker

- **Fall of the Samurai** and **Rise of the Samurai** DLC campaigns use the same executable, so all fixes apply to them equally.
- **Save game corruption** after a crash is common. Back up `%AppData%\The Creative Assembly\Shogun2\save_games\` before troubleshooting.
- If you're on a **12th/13th-gen Intel CPU**, disable E-cores via BIOS or use Process Lasso to pin the game to P-cores only — the engine's old threading model misreads hybrid cores.
- **Linux/Steam Deck users**: force Proton Experimental and add `PROTON_USE_WINED3D=1 %command%` to launch options for the DX9 path.

## Frequently Asked Questions (FAQ)

### Why does Total War: SHOGUN 2 crash on Windows 11?
Windows 11's fullscreen optimization and updated DX11 drivers conflict with the game's 2011 engine. Running it in Windows 7 compatibility mode with `-dx9` and disabled fullscreen optimizations resolves the vast majority of crashes.

### Does Total War: SHOGUN 2 work on Steam Deck?
Yes. It runs well via Proton, but you must force the DX9 launch flag and may need to cap the framerate at 60 FPS to prevent audio desync during battles.

### How do I fix the "Preparing to launch" infinite loop?
Disable the Steam Overlay, verify game files, and delete the `scripts` folder in `%AppData%\The Creative Assembly\Shogun2\`. This combination clears the launch handshake failure in nearly all cases.

## Final Verdict

Start with **Fix 1 (`-dx9`) and Fix 2 (clearing scripts)** — together they solve the majority of launch failures in under five minutes. Only move to compatibility mode and driver rollbacks if those fail. SHOGUN 2 remains one of the best Total War entries ever made, and none of these fixes degrade the experience meaningfully. If you're still crashing after all seven steps, your issue is almost certainly hardware-level (failing RAM or an unstable GPU overclock), not the game itself.