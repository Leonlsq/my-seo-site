---
title: "wiz3D 0.4 Setup Guide: Restore 3D Vision in GTA V & NieR"
description: "Complete wiz3D 0.4 setup and troubleshooting guide to restore NVIDIA 3D Vision Stereo3D in GTA V Legacy, Max Payne 3, NieR: Automata and more."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## wiz3D 0.4: How to Restore 3D Vision Stereo3D in GTA V, NieR: Automata & More

NVIDIA killed 3D Vision drivers years ago, but wiz3D 0.4 just brought Stereo3D back from the dead for a huge list of DX11 titles. This community wrapper translates DirectX 11 calls into the legacy 3D Vision output path, meaning games like **GTA V Legacy**, **Max Payne 3**, **NieR: Automata**, **BioShock Infinite**, and **Far Cry 4** now render in true stereo 3D again — or for the first time. This guide walks you through a clean install, per-game configuration, and the exact fixes for the black screen, double-image, and crash issues most users hit on day one.

**The short version:** drop the wiz3D files into the game folder, set the game to fullscreen with V-Sync off, launch through the included injector, then press **Ctrl+T** to toggle stereo. If it doesn't work, 90% of the time it's a fullscreen-exclusive conflict or a missing `d3d11.dll` override — both covered below.

## Step-by-Step: Installing wiz3D 0.4 Correctly

The single biggest cause of failure is a messy install. Follow this order exactly.

1. **Verify your hardware path.** You need an NVIDIA GPU (GTX 900 series or newer works best) plus either a 3D Vision-ready monitor with emitter, a 120Hz+ display using the 3D Vision "DLP/LCD checkerboard" or "Anaglyph" fallback, or a VR headset via the legacy path. wiz3D does **not** create stereo from nothing — it needs a compatible output.
2. **Install a legacy 3D Vision driver.** Use the last official 3D Vision driver package (425.31 or the community-patched 3D Fix Manager driver). Reboot before continuing.
3. **Download wiz3D 0.4** from the official GitHub/community release page. Extract to a temp folder — never run it from inside a zip.
4. **Copy the core files into the game's root directory** (the folder containing the game's `.exe`):
   - `d3d11.dll` (the wrapper)
   - `wiz3D.ini` (config)
   - `wiz3D_Launcher.exe` (injector)
5. **Edit `wiz3D.ini` before first launch.** Set `StereoEnabled=1`, `OutputMode=0` (auto-detect), and `Separation=15.0` as a starting convergence value.
6. **Launch the game via `wiz3D_Launcher.exe`**, not Steam directly. This ensures the injector hooks before the DX11 device is created.
7. **In-game:** set **Fullscreen (exclusive)**, disable **V-Sync**, and disable any in-game anti-aliasing (MSAA/TAA) — these break the depth buffer wiz3D reads.
8. **Press `Ctrl+T`** to toggle stereo on. Use `Ctrl+F5`/`Ctrl+F6` to adjust separation and convergence live.

### Quick Reference: Keybinds

| Key Combo | Function |
|---|---|
| `Ctrl + T` | Toggle Stereo3D on/off |
| `Ctrl + F5` / `Ctrl + F6` | Decrease / increase separation (depth) |
| `Ctrl + F3` / `Ctrl + F4` | Decrease / increase convergence |
| `Ctrl + F7` | Cycle output mode |
| `Ctrl + F10` | Save current profile |

## Per-Game Configuration Notes

Not every title behaves the same. Here's what the community has confirmed for the headline games in the 0.4 release:

- **GTA V Legacy:** Works best at 1080p fullscreen. Disable MSAA and set "DirectX Version" to 11. The Legacy branch is required — the Enhanced edition uses a different renderer that 0.4 does not yet hook.
- **Max Payne 3:** Rock-solid out of the box. Set shadows to Medium; Ultra shadows cause depth flicker.
- **NieR: Automata:** Newly added in 0.4. Use the **FAR (Fix Automata Resolution)** mod alongside wiz3D and cap the frame rate to 60 — the game's engine ties physics to framerate and stereo separation drifts above 60 FPS.
- **BioShock Infinite:** Disable the in-game "Alternate Post Processing." It flattens the depth buffer and kills pop-out.
- **Far Cry 4:** Requires the `-dx11` launch flag. Water reflections render at wrong depth — a known 0.4 limitation with no fix yet.

## Common Issues and Fixes

**Black screen on launch.** Almost always a fullscreen-exclusive conflict or the wrapper loading after the game's own DXGI swap chain. Fix: run the launcher as Administrator, and add `-windowed -noborder` to the game's launch arguments, then force fullscreen via the in-game menu.

**Double image / cross-eyed look.** Your separation is too high for the convergence. Drop `Separation` to ~10 in `wiz3D.ini`, then fine-tune with `Ctrl+F5/F6` in-game.

**Game crashes with `d3d11.dll` error.** Another overlay (Discord, MSI Afterburner, Steam overlay) is injecting first. Disable all overlays, then relaunch through `wiz3D_Launcher.exe`.

**Stereo works but depth feels flat.** Anti-aliasing is still on. TAA and MSAA both destroy the depth buffer — turn them fully off and rely on resolution scaling instead.

## Frequently Asked Questions (FAQ)

### Does wiz3D 0.4 work with the GTA V Enhanced edition?
No. Version 0.4 hooks the DX11 renderer used by **GTA V Legacy** only. The Enhanced edition uses a newer pipeline that the wrapper does not yet support; use the Legacy branch via the Rockstar launcher.

### Do I need an actual 3D Vision monitor to use wiz3D?
Not strictly. wiz3D outputs through the legacy 3D Vision driver, which supports 3D Vision monitors, 120Hz displays with checkerboard/anaglyph fallback, and some VR headsets via the old path. You do need a compatible NVIDIA GPU and the legacy driver installed.

### Is wiz3D 0.4 safe, or will it get me banned?
It's a community wrapper, not a cheat. However, injecting any DLL into an online game can trigger anti-cheat. **Only use wiz3D in single-player modes** — never in GTA Online, and disable it before joining any multiplayer session.

## Final Verdict

If you've been sitting on a 3D Vision monitor or a 120Hz display and mourning the death of Stereo3D, **wiz3D 0.4 is the single best reason to dig that hardware out of the closet** — the DX11 support finally makes modern-ish titles viable, and the five headline games all run well after the config tweaks above. It's not plug-and-play: expect 20–30 minutes of per-game tuning, and accept that anti-aliasing is off the table. But for the niche it serves, there's no real alternative. Install the legacy driver first, follow the eight steps exactly, and start with Max Payne 3 — it's the most stable test case before you tackle NieR: Automata.