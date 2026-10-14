---
title: "Epic Games Launcher Preview: Should You Switch Now?"
description: "Hands-on with the new Epic Games Launcher Preview. Learn how to install it, what changed, known bugs, and whether you should switch from the old launcher."
pubDate: 2026-10-14
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Is the New Epic Games Launcher Preview Actually Worth Installing?

Epic Games has officially rolled out the **Preview build of its completely rebuilt Epic Games Launcher**, and if you have been tolerating the old launcher's sluggish library scrolling and random 30-second startup delays, this is the update you have been waiting for. The short answer: **yes, install it — but keep the stable launcher as a fallback for the first week.** The Preview is a ground-up rewrite (built on a new rendering stack) that dramatically improves startup time, memory usage, and store navigation. However, it is still labeled "Preview" for a reason: some third-party integrations, cloud save edge cases, and overlay hooks are not fully stable yet. This guide covers exactly how to install it, what actually changed under the hood, the bugs users are reporting, and how to roll back safely if something breaks.

## How to Install the Epic Games Launcher Preview (Step-by-Step)

You do **not** need to uninstall your current launcher. The Preview runs as a separate build, so both can coexist.

1. **Back up your local game configs first.** Navigate to `C:\Users\[YourName]\AppData\Local\EpicGamesLauncher\Saved\Config` and copy the folder to a safe location. This preserves login tokens and settings if you need to revert.
2. **Open the current Epic Games Launcher** and sign in as normal.
3. Click your **profile icon (top-right)** → **Settings**.
4. Scroll to the bottom and look for **"Epic Games Launcher Preview"** under the *Experimental* or *Beta* section.
5. Toggle it on and click **Restart & Update**. The launcher will download the Preview build (roughly 250–400 MB depending on platform).
6. After relaunch, verify the version number in **Settings → About**. Preview builds use a distinct version string (e.g., `17.x-preview`) versus the stable `16.x` branch.

**Manual install alternative:** If the toggle does not appear (it rolls out in waves), download the installer directly from Epic's official Preview landing page and install it to a **separate directory** — never overwrite your stable install path.

### What Actually Changed: Preview vs. Old Launcher

| Feature | Old Launcher | New Preview Build |
|---|---|---|
| Startup time (cold boot) | 15–40 seconds | 3–8 seconds |
| Idle RAM usage | ~450–600 MB | ~180–280 MB |
| Library scroll | Stuttery, image pop-in | Smooth, virtualized list |
| Store page load | Full reload each visit | Cached, instant back-nav |
| Download manager | Basic queue | Per-game bandwidth caps |
| Overlay (friends/chat) | Heavy, laggy | Lightweight, detachable |
| Platform | Win/Mac | Win/Mac (Linux via Proton unofficial) |

The biggest architectural change is the shift to **virtualized lists and lazy image loading** in the library. This is why a 500-game library no longer freezes when you scroll. The download manager also finally supports **per-game throttle limits**, which is a feature Steam has had for years.

## Common Issues, Known Bugs, and Workarounds

The Preview is stable enough for daily use, but early adopters are reporting a handful of recurring problems. Here is what to expect and how to fix each one.

- **Blank/black launcher window on launch.** This is usually a GPU acceleration conflict. Go to **Settings → Advanced → disable Hardware Acceleration**, restart, then re-enable it. If it persists, update your GPU driver — the new renderer requires a reasonably current driver (NVIDIA 550+, AMD Adrenalin 24.x+).
- **Games not detecting the overlay (Discord, MSI Afterburner).** The Preview uses a new overlay hook that some third-party tools do not yet recognize. Launch those tools *after* the launcher, or add the game's `.exe` manually to your overlay's injection list.
- **Cloud saves showing "Sync Conflict."** Do not blindly overwrite. Open the conflict dialog and compare timestamps. If unsure, back up the local save folder before choosing "Upload Local."
- **Friends list not loading.** Sign out and back in once. The Preview caches the social graph separately, and the first login after switching can time out.
- **Controller/input not registering in the launcher UI.** Disable Steam Input for non-Steam games if you have it globally forced on.

### Should You Keep Both Launchers Installed?

Yes — at least for the first two weeks. The Preview and stable builds share the same game install directory, so **you do not need to re-download your games**. If the Preview misbehaves, just launch the stable build and your library is intact. The only thing that does not transfer automatically is in-progress download queues.

## Frequently Asked Questions (FAQ)

### Is the new Epic Games Launcher Preview safe to use as my main launcher?
For most users, yes. It is stable for launching, downloading, and updating games. The main risks are third-party overlay incompatibility and occasional cloud save sync conflicts. Keep the stable build installed as a fallback for the first week.

### Does the Epic Games Launcher Preview require me to re-download my games?
No. The Preview shares the same installation directory as the stable launcher. Your existing game files, save data, and install paths are detected automatically — only the launcher itself is a new download.

### Can I roll back to the old Epic Games Launcher if I don't like it?
Yes. Open the Preview's Settings, toggle off the Preview option, and restart. If the toggle is missing, uninstall the Preview build and reinstall the stable launcher from Epic's official site. Your games remain untouched.

### Does the Preview fix the high CPU usage issue?
Largely, yes. Idle CPU usage drops noticeably because the new build no longer runs the old web-based UI renderer continuously. Users report idle CPU dropping from 8–15% to under 3% on typical hardware.

### Is the Preview available on Linux or Steam Deck?
Not officially. It is a Windows and macOS build. Linux users can run it through Proton/Wine, but Epic does not support this configuration and overlay features will not work.

## Final Verdict

**Install the Preview now if you have a large library or a slower PC** — the startup and memory improvements are genuinely transformative, and the risk is low because your games and saves stay put. **Wait one to two weeks if you rely heavily on overlays, capture tools, or cloud saves across multiple machines**, since those are the areas still being ironed out. Either way, do not delete your stable launcher yet. The new Epic Games Launcher Preview is the best thing to happen to the platform in years — it just needs a few more patch cycles before it fully replaces the old build.