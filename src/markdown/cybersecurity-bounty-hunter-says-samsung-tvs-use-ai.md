---
title: "Samsung TV Spying: How to Disable AI Audio Recording"
description: "Stop Samsung TV AI from recording audio and screenshots for ads. Step-by-step privacy settings, ACR opt-outs, and router-level blocks that actually work."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Samsung TV AI Spying: What the Bounty Hunter Found (and How to Lock It Down)

A cybersecurity bounty hunter reverse-engineered his own Samsung smart TV and published findings claiming the set runs code that can capture audio from connected devices and take screenshots — data allegedly tied to advertising and "AI" features. Whether you call it malicious spying or aggressive telemetry, the practical takeaway is the same: **your TV ships with data collection switched on by default, and you can turn most of it off in about 10 minutes.** This guide walks you through the exact menus, the settings Samsung buries, and the router-level firewall rules that stop the TV from phoning home even when the UI says "off."

## Step-by-Step: Disabling Samsung TV Audio Capture & Ad Tracking

Do these in order. Menu names vary slightly by model year (2019–2025 Tizen builds), but the paths below cover the vast majority of QLED, Neo QLED, The Frame, and Crystal UHD sets.

### 1. Kill Voice Recognition & "Always Listening" Mic
1. Press **Home → Settings (gear) → All Settings**.
2. Go to **General & Privacy → Voice**.
3. Set **Voice Wake-Up / Bixby Voice Wake-Up** to **Off**. This is the setting that keeps the far-field mic hot for wake-word detection.
4. Under **Privacy → Voice Recognition**, toggle **Off** and delete any stored voice recordings.
5. If you use the SolarCell remote, its mic only activates on button press — but the **TV's built-in mic array** stays armed if Voice Wake-Up is on. Confirm it's off.

### 2. Disable Viewing Information Services (ACR)
Automatic Content Recognition is the "screenshot" engine — it fingerprints what's on screen to serve targeted ads.
1. **Settings → All Settings → General & Privacy → Terms & Privacy**.
2. Open **Viewing Information Services** and toggle **Off**.
3. Reject **Interest-Based Advertising** in the same menu.
4. Go to **Support → Terms & Policy** and withdraw consent for **Marketing Communications** and **Personalized Ads**.

### 3. Turn Off AI Upscaling Telemetry (2024–2025 models)
Newer sets bundle "AI" picture processing with cloud analytics.
- **Settings → Picture → Expert Settings → AI Picture / AI Mode** → set to **Off** if you don't want frame data sent for processing.
- **Settings → General & Privacy → Intelligent Mode Settings** → disable **Adaptive Sound**, **Adaptive Picture**, and **Brightness Optimization**.

### 4. Block at the Router (the only bulletproof layer)
Even with every toggle off, Samsung TVs maintain connections to telemetry endpoints. Add these to your router's blocklist or Pi-hole:

| Domain | Purpose |
|---|---|
| `*.samsungads.com` | Ad delivery / ACR matching |
| `*.samsungcloudsolution.com` | Telemetry upload |
| `log.samsungadhub.com` | Ad impression logging |
| `*.samsungosp.com` | OS telemetry |
| `*.samsungacr.com` | Content recognition |

**Steps:** Log into your router → **Parental Controls / Firewall → Blocked Domains** → paste the list → apply. On Pi-hole, add them under **Domains → RegEx Deny**. This survives firmware updates that silently re-enable toggles.

### 5. Use the TV in "No-Network" Mode for Max Privacy
If you only stream via an external Apple TV, Roku, or Fire Stick, you can disconnect the TV from Wi-Fi entirely: **Settings → Connection → Network → Network Status → Disconnect**. The panel still works as a monitor; all smart features route through your streaming box (which has its own, often cleaner, privacy settings).

## Common Issues, Workarounds & What Samsung Won't Tell You

- **Toggles reset after firmware updates.** Samsung has re-enabled Viewing Information Services after OTA updates on some 2020–2022 sets. Re-check after every update, or rely on the router blocklist.
- **"Off" doesn't always mean off.** Independent teardowns (and the bounty hunter's findings) suggest some telemetry uses first-party domains that look legitimate. Router-level blocking is the only reliable kill switch.
- **The mic on connected devices is the real risk.** If your TV can control a soundbar or smart speaker via HDMI-CEC, that device's mic may be reachable. Disable **Anynet+ (HDMI-CEC)** under **Settings → Connection → External Device Manager** if you don't need it.
- **Alternative: buy a "dumb" display.** Commercial signage panels (Samsung BET-H series, LG UR640S) ship without ACR and cost roughly the same as consumer models in 55–65". For privacy purists, this is the cleanest fix.

## Frequently Asked Questions (FAQ)

### Does my Samsung TV actually record audio without permission?
Samsung's terms disclose voice and viewing data collection when you accept the setup prompts. The controversy is about *scope* and *retention*, not existence. If you never toggled Voice Wake-Up or Viewing Information Services off, assume audio snippets and screen fingerprints can be captured.

### How do I know if my Samsung TV is sending data?
Check your router's traffic log for connections to `samsungads.com` or `samsungacr.com`. A Pi-hole dashboard is the fastest way — you'll see queries fire within minutes of the TV waking.

### Will blocking Samsung domains break my TV?
No. You'll lose the Samsung TV Plus ad-supported channels, some app store recommendations, and firmware auto-updates (update manually via USB). Core streaming apps like Netflix and YouTube work fine.

### Is this a hack, or just aggressive advertising?
It's not a remote exploit — it's the TV doing what its privacy policy permits. The bounty hunter's contribution is showing *how much* is technically possible, including cross-device mic access via connected hardware.

## Final Verdict

Treat your Samsung TV as an ad-funded device first and a display second. **Do all three layers: disable Voice Wake-Up and Viewing Information Services in the menus, block the five telemetry domains at your router, and re-verify after every firmware update.** That combination takes 10 minutes and closes the gap between what Samsung says it collects and what the hardware can actually do. If privacy is non-negotiable, disconnect the TV from Wi-Fi entirely and feed it from a streaming stick — or buy a commercial signage panel. The menus alone are not enough.