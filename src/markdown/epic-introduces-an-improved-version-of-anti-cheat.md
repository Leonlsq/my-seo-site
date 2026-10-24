---
title: "Epic Anti-Cheat on Linux: How to Enable It & Fix Errors"
description: "Epic's improved anti-cheat for Linux is here. Learn how to enable EAC on Steam Deck and Linux, fix common launch errors, and which games support it."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Epic Anti-Cheat on Linux: What Actually Changed and How to Turn It On

Epic Games has shipped an improved build of Easy Anti-Cheat (EAC) for Linux and the Steam Deck, and the headline is simple: developers can now enable Linux support without maintaining a separate anti-cheat branch. The practical takeaway for you as a player is that **EAC-protected games can now run natively on Linux through Proton** — but only if the developer flips the switch on their end. This guide walks you through enabling it, verifying compatibility, and fixing the most common `EAC_LAUNCH_ERROR` and "Untrusted System File" failures that appear after the update.

Before you start, understand the core limitation: **you cannot force-enable EAC Linux support client-side.** The toggle lives in the game's build configuration on the developer's side. What you *can* do is verify support, configure Proton correctly, and troubleshoot the launch layer.

## Step-by-Step: Enabling and Verifying EAC on Linux

### Step 1 — Check if your game actually supports it
Not every EAC title gained Linux support overnight. Verify before troubleshooting:

1. Open **ProtonDB** and search your game title.
2. Look for the **"Easy Anti-Cheat"** badge and filter by "Native/Proton EAC" reports.
3. Check the game's Steam store page — a **Steam Deck Verified** badge with the anti-cheat note is the strongest signal.

### Step 2 — Set the correct Proton version
Outdated Proton builds are the #1 cause of EAC handshake failures.

1. Right-click the game in Steam → **Properties** → **Compatibility**.
2. Check **"Force the use of a specific Steam Play compatibility tool."**
3. Select **Proton Experimental** (or Proton 9.0+ for stable builds).
4. Launch the game once, let the EAC runtime install, then restart.

### Step 3 — Install the EAC runtime dependency
On some distros the EAC runtime is a separate package:

```bash
# Steam Deck / Arch-based
sudo steamos-readonly disable
sudo pacman -S steam-native-runtime

# Ubuntu/Debian
sudo apt install steam-installer
```

### Step 4 — Verify the launch flags
Add these to the game's **Launch Options** if you hit a black screen after the EAC splash:

```
PROTON_EAC=1 %command%
```

### Compatibility Quick Reference

| Scenario | EAC Linux Support | Action Needed |
|---|---|---|
| Steam Deck Verified + EAC badge | ✅ Yes | Proton Experimental |
| ProtonDB "Gold" with EAC reports | ⚠️ Partial | Force Proton 9.0+ |
| No EAC badge, "Borked" status | ❌ No | Wait for dev toggle |
| Native Linux build | ✅ Yes | None |

## Common Issues and What You Should Know

### "Untrusted System File" error
This fires when a kernel module or overlay (often MangoHud, GameMode, or a custom kernel) is flagged. Disable overlays one at a time via launch options (`MANGOHUD=0 %command%`) to isolate the culprit.

### EAC splash then instant crash
Usually a missing `libc++` or outdated Mesa driver. Update your GPU drivers and confirm `vulkaninfo` runs without errors.

### The developer hasn't enabled it yet
This is the honest bottleneck. Epic built the tooling, but **adoption is per-developer**. If your game shows "Borked" on ProtonDB, the fix is a support ticket or community upvote — not a config tweak. Check the game's official Discord for a "Linux/EAC" channel; many studios track demand there.

### What about BattlEye and kernel-level anti-cheat?
EAC's Linux support is *user-mode* and does not require kernel access, which is why it works under Proton. Games using kernel-level anti-cheat (e.g., Vanguard, some BattlEye titles) remain incompatible regardless of this update. Do not expect Valorant or similar titles to work.

## Frequently Asked Questions (FAQ)

### Does Epic's new anti-cheat make all EAC games work on Linux now?
No. It makes it *possible* for developers to enable Linux support with minimal effort. Each game must still opt in via a build configuration change. Check ProtonDB per title.

### Is Easy Anti-Cheat safe to run on Linux?
Yes. The Linux EAC runtime operates in user space and does not install kernel-level drivers, which is a key reason it works under Proton and is generally considered lower-risk than kernel anti-cheat.

### Why does my EAC game crash right after the splash screen on Steam Deck?
Most often it's an outdated Proton version or a graphics overlay conflict. Force Proton Experimental, disable MangoHud/GameMode, and update your system via SteamOS settings.

### Can I bypass EAC to play online on Linux?
No — and attempting to do so violates the game's terms of service and typically results in a permanent ban. The only supported path is the developer-enabled Linux build.

## Final Verdict

Epic's improved EAC for Linux is genuinely good news, but treat it as **enabling infrastructure, not a universal fix**. Your action plan: verify your specific game on ProtonDB, force Proton Experimental, strip out overlays if you hit "Untrusted System File," and — crucially — **lobby the developer** if support isn't live yet. For Steam Deck owners, this update quietly expands the "Verified" library over the coming months, so keep your Proton version current and re-check titles you'd previously written off. Don't buy a game *expecting* EAC Linux support until you see the badge — verify first, then play.