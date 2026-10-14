---
title: "Valor Mortis Steam: Fix Crashing & Best Settings Guide"
description: "Valor Mortis is out on Steam. Fix crashes, stutters, and FPS drops with our best settings guide, plus controller and co-op setup tips."
pubDate: 2026-10-14
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Valor Mortis Is Out on Steam: Here's How to Actually Make It Run Well

Valor Mortis has officially launched on Steam, and if you're reading this, you've probably already noticed the launch-day jank. Within hours of release, the Steam forums and r/ValorMortis filled with the same three complaints: random crashes to desktop, shader compilation stutter, and FPS drops in the necropolis hub area. The good news is that most of these issues are fixable in under 15 minutes with the right settings and launch commands. This guide covers the exact fixes, the optimal graphics configuration for both mid-range and high-end GPUs, and the controller/co-op setup most players miss.

## Step-by-Step Fixes for Valor Mortis Crashes and Stutter

### Fix 1: Verify Game Files and Clear the Shader Cache

Corrupted shader caches are the #1 cause of the "Fatal Error: D3D12 Device Removed" crash on launch.

1. Open Steam → right-click **Valor Mortis** → **Properties** → **Installed Files** → **Verify integrity of game files**.
2. Navigate to `%LOCALAPPDATA%\ValorMortis\Saved\ShaderCache` and delete the entire folder.
3. Relaunch the game and let it recompile shaders on the title screen for 3–5 minutes. Do not skip this.

### Fix 2: Add Launch Commands

In Steam → Properties → **Launch Options**, paste:

```
-dx11 -USEALLAVAILABLECORES -high
```

The `-dx11` flag forces the DirectX 11 renderer, which eliminates the DX12 device-removed crashes on RTX 30-series and RX 6000-series cards. You lose roughly 8–12% peak FPS but gain total stability.

### Fix 3: Disable Overlays

Discord, GeForce Experience, and Steam Overlay all hook into the render pipeline and cause micro-stutters. Disable all three, then re-enable them one at a time to find the culprit.

### Recommended Settings by Hardware Tier

| Setting | Low-End (GTX 1660 / RX 580) | Mid-Range (RTX 3060 / RX 6700) | High-End (RTX 4070+) |
|---|---|---|---|
| Resolution | 1080p | 1440p | 1440p / 4K |
| Upscaler | FSR 2 Quality | DLSS Quality | DLSS Quality |
| Shadows | Low | Medium | High |
| Volumetric Fog | Off | Low | Medium |
| Ray Tracing | Off | Off | On (Reflections only) |
| Texture Quality | Medium | High | Ultra |
| Target FPS | 60 | 90 | 120+ |

**Key tip:** Turn Volumetric Fog to Off or Low regardless of your GPU. It costs 15–20% performance in the necropolis hub for almost no visual gain.

## Common Issues, Controller Setup, and Co-op Notes

**Controller not detected:** Valor Mortis uses Steam Input, but dual-sense haptics require the game to be launched *through* Big Picture mode at least once. After that, standard desktop launch works.

**Co-op desync:** The 2-player co-op mode uses peer-to-peer hosting. If you get rubber-banding, the host should forward UDP port 27015 on their router. There is no dedicated server option at launch.

**Save file corruption:** Back up `%LOCALAPPDATA%\ValorMortis\Saved\SaveGames` weekly. Cloud sync has been unreliable for some users, and there's no manual rollback in-game.

**Alternatives worth knowing:** If Valor Mortis won't stabilize on your rig, *No Rest for the Wicked* and *Morbid Metal* offer similar gothic action-roguelike gameplay with far lower system requirements.

## Frequently Asked Questions (FAQ)

### Is Valor Mortis worth buying on Steam right now?
Yes, if you have a GTX 1660 or better and can tolerate launch-window bugs. The core combat loop is excellent, but wait for the first patch if you're on older DX12-only hardware.

### Why does Valor Mortis keep crashing on startup?
The most common cause is a corrupted shader cache or a DX12 device-removed error. Delete the ShaderCache folder and add `-dx11` to your Steam launch options.

### Does Valor Mortis support co-op and crossplay?
It supports 2-player online co-op via peer-to-peer. There is no crossplay with consoles at launch, and no dedicated servers.

### What are the best settings for high FPS in Valor Mortis?
Set Volumetric Fog to Off, Shadows to Medium, enable DLSS/FSR Quality, and disable ray tracing unless you're on an RTX 4070 or better.

## Final Verdict

Valor Mortis is a genuinely good game buried under a rough PC port. Spend 15 minutes applying the fixes above—especially the `-dx11` launch command and shader cache wipe—and you'll go from constant crashes to a stable 90+ FPS experience on mid-range hardware. If you're on the fence, buy it, but keep your expectations calibrated for a patch or two before it's fully polished.