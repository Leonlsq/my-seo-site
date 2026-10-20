---
title: "KB5124010 AC-3 Crash Fix: Restore Dolby Audio Now"
description: "Games crashing after KB5124010? Learn how to fix the AC-3 Dolby Digital audio bug on Windows 11 with our step-by-step guide and verified workarounds."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Fix the KB5124010 AC-3 Audio Crash on Windows 11

If your games or media apps started hard-crashing immediately after installing the September 2026 Windows 11 preview update (**KB5124010**), you are not alone—and your hardware is not broken. Microsoft has confirmed that this specific update introduced a bug in the audio stack that causes applications relying on **AC-3 (Dolby Digital) decoding** to freeze or crash to desktop. The good news: Microsoft has shipped a fix, and if you are still stuck, there are several verified workarounds you can apply in under five minutes. This guide walks you through the official patch, the manual fixes, and how to confirm your audio pipeline is healthy again.

## Step-by-Step Guide to Restoring AC-3 Audio

Before you start, note your current build number (**Win + R**, type `winver`). You will need it to confirm the fix applied correctly.

### Step 1: Install the Official Microsoft Fix

Microsoft resolved the regression through a servicing update. The fastest path is Windows Update:

1. Open **Settings → Windows Update**.
2. Click **Check for updates**.
3. Look for the cumulative fix (a build revision above **26100.xxxx** on 24H2). Install it and **restart**.
4. Relaunch the affected game or app to confirm the crash is gone.

If Windows Update does not surface the patch, grab it manually from the **Microsoft Update Catalog** by searching your exact build number.

### Step 2: Roll Back KB5124010 (Temporary Workaround)

If you cannot wait for the patch or it fails to install, uninstalling the preview update restores the previous audio behavior:

1. Go to **Settings → Windows Update → Update history → Uninstall updates**.
2. Select **KB5124010** and click **Uninstall**.
3. Restart when prompted.
4. **Pause updates** temporarily so Windows does not reinstall it before the fix lands.

### Step 3: Force the Correct Audio Format

Some users report the crash persists because Windows defaults to a broken AC-3 passthrough path. Reset it manually:

1. Right-click the speaker icon → **Sound settings → More sound settings**.
2. Select your output device → **Properties → Advanced**.
3. Under **Default Format**, choose **16 bit, 48000 Hz (DVD Quality)**.
4. Uncheck **Enable audio enhancements**, then click **Test** and **Apply**.

### Step 4: Reinstall the Dolby/Realtek Audio Driver

A corrupted driver stack amplifies the bug. Use this clean sequence:

- Download the latest **Realtek** or **Dolby Atmos** driver from your motherboard or laptop vendor.
- Open **Device Manager → Sound, video and game controllers**.
- Right-click your audio device → **Uninstall device** (check "Attempt to remove the driver").
- Restart and install the fresh driver.

### Quick Reference: Which Fix Should You Use?

| Situation | Recommended Fix | Time Needed | Permanence |
|---|---|---|---|
| Patch available in Windows Update | Install cumulative fix | 5–10 min | Permanent |
| Patch not yet offered | Uninstall KB5124010 | 3 min | Temporary |
| Crash persists after patch | Reset audio format + driver | 10 min | Usually permanent |
| On metered/managed PC | Manual Catalog install | 10 min | Permanent |

## Common Issues and What You Should Know

**Why did only some games crash?** The bug only triggered when an app requested AC-3 decoding through the Windows media foundation pipeline. Games using their own internal audio engine (e.g., many Unreal titles) were unaffected, which is why reports looked random.

**The patch installed but audio still stutters.** This is usually a leftover enhancement profile. Disable **Spatial sound** (Settings → Sound → Device properties) and retest. Spatial audio and AC-3 passthrough can conflict post-patch.

**Should you disable automatic updates?** No—pausing updates long-term leaves you exposed to real security flaws. Instead, defer **preview** updates only: Settings → Windows Update → **Pause updates** for up to 5 weeks, and avoid the "Get the latest updates as soon as they're available" toggle.

**Home theater users:** If you bitstream AC-3 to an AV receiver over HDMI, verify the receiver still shows "Dolby Digital" after the fix. If it shows PCM, re-select **Dolby Digital** in your sound device's **Supported Formats** tab.

## Frequently Asked Questions (FAQ)

### What exactly did KB5124010 break in Windows 11?
The September 2026 preview update introduced a regression in the audio decoding stack that crashed games and apps requesting **AC-3 (Dolby Digital)** streams. Microsoft confirmed the issue and released a servicing fix.

### Is there a permanent fix for the AC-3 crash, or only workarounds?
Yes—Microsoft's cumulative servicing update is the permanent fix. Uninstalling KB5124010 and resetting audio formats are temporary workarounds for users who cannot install the patch immediately.

### Will uninstalling KB5124010 delete my files or game saves?
No. Uninstalling a Windows cumulative/preview update only reverts system components. Your documents, installed games, and save files are unaffected.

### Does this bug affect Windows 10 or only Windows 11?
The reported crashes center on **Windows 11** devices that installed the KB5124010 preview. Windows 10 users on standard updates were not part of the confirmed rollout.

## Final Verdict

**Install the official Microsoft fix first**—it is the only permanent solution and takes minutes through Windows Update. Only fall back to uninstalling KB5124010 if the patch is unavailable on your device, and always re-enable updates once the fix is confirmed installed. If your audio still misbehaves afterward, the culprit is almost always a stale driver or an enabled spatial-audio enhancement, not the update itself. Fix the patch, reset your audio format to **16-bit/48 kHz**, and your Dolby Digital games will run crash-free again.