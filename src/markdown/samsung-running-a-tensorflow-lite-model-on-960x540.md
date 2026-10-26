---
title: "Samsung TensorFlow Lite Tracking: How to Check & Disable It"
description: "Samsung runs a TensorFlow Lite model on 960x540 images to track you. Here is how to check the process, disable it, and cut Samsung telemetry."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Samsung's TensorFlow Lite Tracker: What It Actually Does and How to Stop It

A viral report from developer Mike (@mike64_t) on X, later discussed on Hacker News, revealed that Samsung devices appear to run a bundled TensorFlow Lite model against image frames captured at **960x540 resolution** — a resolution that matches the Samsung Camera's preview stream, not a full-resolution photo. The takeaway most users need: this is almost certainly **on-device inference on the camera preview buffer**, not a silent upload of your full photos. But "on-device" does not mean "harmless," and you can reduce or block it. This guide shows you how to verify the process on your own phone, what the model likely does, and the exact settings to cut Samsung's telemetry and background camera access.

## How to Check for the TensorFlow Lite Process on Your Samsung Phone

You do not need root for the first three checks. Work through them in order.

1. **Developer Options → Running Services.** Enable Developer Options (Settings → About phone → Software information → tap *Build number* 7 times). Then go to Settings → Developer options → **Running services**. Look for `com.samsung.android.*` services holding a `tflite` or `vision`-named process. Note the RAM footprint — a 960x540 inference pipeline typically sits between 40–120 MB.
2. **Battery usage by app.** Settings → Battery → Battery usage → *Since last full charge*. Samsung camera-adjacent services (e.g., `Camera`, `Scene Optimizer`, `Bixby Vision`) that consume battery while the screen is off are a red flag.
3. **ADB process inspection (no root).** With USB debugging on, run:
   ```
   adb shell dumpsys activity services | grep -i -E "tflite|tensorflow|vision"
   adb shell dumpsys media.camera | grep -i "client"
   ```
   The second command lists processes holding a camera client — if a non-camera app appears while the camera UI is closed, that is the behavior worth investigating.
4. **Network sanity check.** Install a local VPN/firewall (NetGuard, RethinkDNS) and watch outbound traffic from `com.samsung.android.*` packages. On-device inference should generate **near-zero** upload traffic. If you see large image-sized POSTs, that changes the severity of the issue.

> **Reality check:** 960x540 (roughly 0.5 MP) is the standard Samsung preview resolution. It is too low for OCR of documents or reliable face identification at distance. The plausible use cases are **scene classification, gesture detection, attention/screen-on detection, and ad-personalization signals** — not covert photo theft. Treat claims of "full photo exfiltration" skeptically until packet captures prove it.

## Step-by-Step: Reduce Samsung Telemetry and Background Camera Access

These steps are reversible and require no root. Do them in this order.

1. **Revoke camera from non-camera apps.** Settings → Apps → *[app]* → Permissions → Camera → **Don't allow**. Audit every app, especially preinstalled Samsung/Bixby/AR services you never open.
2. **Disable Bixby Vision and Scene Optimizer.** Camera app → Settings → turn off **Scene optimizer** and **Bixby Vision**. These are the most likely consumers of a preview-resolution TFLite model.
3. **Turn off Customization Service.** Settings → Privacy → **Customization Service** → off. This is Samsung's personalization/telemetry backbone.
4. **Limit ad tracking.** Settings → Privacy → Ads → **Delete advertising ID** (Android 12+) or opt out of *Customized ads*.
5. **Kill Samsung's diagnostic data.** Settings → Privacy → **Diagnostics** → off. Also disable *Send diagnostic data* under Samsung account → Security and privacy.
6. **Restrict background data.** Settings → Apps → *[Samsung service]* → Mobile data → **Allow background data usage: off**.
7. **Use Private DNS to block telemetry domains.** Settings → Connections → More connection settings → Private DNS → *Hostname*: `dns.adguard-dns.com` (or your own blocklist resolver). This blocks known Samsung analytics endpoints without a VPN.
8. **For maximum control, use a firewall.** RethinkDNS or NetGuard lets you block per-app network access while keeping Wi-Fi on — ideal for verifying whether a service phones home.

### What Each Fix Actually Buys You

| Fix | Effort | Blocks on-device inference? | Blocks upload? | Reversible |
|---|---|---|---|---|
| Revoke camera permission | Low | Yes (for that app) | Yes | Yes |
| Disable Scene Optimizer/Bixby Vision | Low | Yes (camera app) | Partial | Yes |
| Customization Service off | Low | No | Yes (personalization) | Yes |
| Private DNS blocklist | Medium | No | Yes (known domains) | Yes |
| Local firewall (NetGuard) | Medium | No | Yes (per-app) | Yes |
| Debloat via ADB | High | Yes | Yes | Mostly |

## Common Issues, Alternatives, and What You Should Know

- **"I can't find Running Services."** Some One UI 6.x builds hide it. Use `adb shell dumpsys activity services` instead.
- **Debloating is the nuclear option.** `pm uninstall --user 0 com.samsung.android.bixbyvision.framework` removes Bixby Vision for the current user without root. It can be restored with `cmd package install-existing`. Do **not** remove core camera or system UI packages.
- **Custom ROMs / GrapheneOS** eliminate Samsung telemetry entirely but are only viable on supported devices (mostly Pixels). On Samsung, a **de-Googled One UI + firewall** is the realistic middle ground.
- **Don't confuse this with Google's ML Kit.** Many apps ship TensorFlow Lite legitimately (translation, barcode scanning). The concern is *preinstalled system services* running inference you never opted into — not TFLite itself.
- **Check for updates.** Samsung has historically adjusted telemetry behavior after public scrutiny. Keep One UI patched and re-audit permissions after major updates.

## Frequently Asked Questions (FAQ)

### Is Samsung really uploading my photos using a TensorFlow Lite model?
No evidence in the public report shows image uploads. The 960x540 resolution matches the camera **preview buffer**, which strongly suggests on-device inference (scene detection, attention tracking) rather than exfiltration. Verify with a firewall before assuming the worst.

### How do I stop Samsung from tracking me on my phone?
Disable Customization Service, Diagnostics, and ad personalization; revoke camera permissions from unused apps; turn off Scene Optimizer and Bixby Vision; and add a Private DNS blocklist or local firewall. This cuts the majority of Samsung telemetry without root.

### Does disabling Scene Optimizer break my camera?
No. Scene Optimizer only adjusts color and exposure automatically. Photos still work normally — you just lose automatic scene-based tuning.

### Can I remove the TensorFlow Lite model without root?
Not directly, but uninstalling the host service (e.g., Bixby Vision) via `pm uninstall --user 0` removes the model with it. Core camera packages should not be touched.

## Final Verdict

The viral claim is more nuanced than the headline suggests: Samsung is running **on-device TensorFlow Lite inference on low-resolution camera preview frames**, not secretly uploading your photo library. That said, an always-on vision pipeline you never consented to is a legitimate privacy concern. **Do the low-effort fixes now** — revoke stray camera permissions, disable Scene Optimizer, Customization Service, and Diagnostics, and add a Private DNS blocklist. If you want proof, spend 10 minutes with NetGuard and watch the traffic yourself. Verify first, panic never.