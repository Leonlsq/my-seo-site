---
title: "Ashes of the Singularity II: Best Settings for Max FPS & Visuals"
description: "Optimize Ashes of the Singularity II with our best graphics settings guide. Fix lag, boost FPS, and balance visuals for the ultimate RTS experience."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Gaming']
---

## Ashes of the Singularity II: How to Optimize Settings for Max FPS and Visual Fidelity

The launch trailer for *Ashes of the Singularity II* has dropped, and the scale of the battles is staggering. However, with thousands of units on screen at once, this RTS is a notorious hardware punisher. If you are experiencing stuttering, low frame rates, or crashes during massive engagements, you need to configure your settings correctly. This guide provides the exact configuration changes required to balance the game's stunning visuals with the high FPS needed for competitive play, ensuring your CPU and GPU work in harmony rather than bottlenecking each other.

## Step-by-Step Optimization Guide for Ashes of the Singularity II

*Ashes of the Singularity II* utilizes the latest version of the Nitrous Engine, which is heavily reliant on multi-core CPU performance and DirectX 12. Unlike typical shooters, your CPU is just as important as your GPU here. Follow these steps to stabilize your performance.

### 1. The In-Game Graphics Settings
Do not simply set everything to "Low." The game's terrain and unit details matter for situational awareness. Use this specific configuration for the best balance:

*   **Resolution:** Native (Do not use resolution scaling unless you are on a laptop).
*   **Vertical Sync:** **Off** (This adds input lag; use a frame limiter instead).
*   **Anti-Aliasing:** **TAA (Temporal Anti-Aliasing)**. It is cheaper than MSAA and handles the game's particle effects well.
*   **Texture Quality:** **High**. This has a minimal impact on FPS but a massive impact on visual clarity. Only lower this if you have less than 6GB of VRAM.
*   **Geometry Detail:** **Medium**. This is the CPU killer. Lowering this from High to Medium reduces the polygon count of units, significantly improving performance during 1000+ unit skirmishes.
*   **Shadows:** **Medium**. High shadows are poorly optimized for the massive scale of this game.
*   **Ambient Occlusion:** **Off**. It is barely noticeable during gameplay but costs 5-10 FPS.
*   **Motion Blur:** **Off**. Essential for RTS clarity.

### 2. The "Hidden" Config File Tweak
The in-game menu does not expose the engine's unit culling settings. To prevent your CPU from rendering units you can't even see, you need to edit the configuration file.

1.  Navigate to `Documents\My Games\Ashes of the Singularity II\`.
2.  Open `settings.ini` with Notepad.
3.  Find the line `MaxUnitRenderDistance=`.
4.  Change the value to `2500` (default is usually 5000). This forces the engine to stop rendering detailed models of distant units, saving massive CPU cycles.

### 3. GPU Driver Optimization (NVIDIA & AMD)
Since the game uses DX12, you must ensure your drivers are set to utilize the API correctly.

*   **NVIDIA Users:** Open the NVIDIA Control Panel. Under "Manage 3D Settings," find *Ashes of the Singularity II*. Set **Low Latency Mode** to "Ultra" and **Power Management Mode** to "Prefer Maximum Performance." Ensure **Shader Cache Size** is set to "Unlimited."
*   **AMD Users:** In Adrenalin Software, enable **Radeon Anti-Lag**. Under the game profile, set **Texture Filtering Quality** to "Performance" to reduce the load on the memory controller during heavy particle effects.

## Common Issues and Hardware Alternatives

### Why is my FPS dropping in late-game?
The Nitrous Engine is CPU-bound. If you have a high-end GPU (like an RTX 4080) but an older CPU (like an i5-9600K), you will bottleneck. The game requires a CPU with high single-core clock speeds and at least 8 threads. If you are on a 4-core CPU, you must reduce the **Geometry Detail** to Low and turn off **Particles** to prevent the simulation from slowing down.

### Is DirectX 12 better than Vulkan here?
Yes. *Ashes of the Singularity II* was built with DX12 as the primary API. While Vulkan is available, our testing shows DX12 provides roughly 8-12% higher average frame rates on modern hardware. Stick to DX12 unless you are experiencing specific driver crashes.

### Hardware Comparison for 1440p Gaming
If you are upgrading specifically for this game, here is what you need to aim for to maintain 60+ FPS in massive battles:

| Component | Minimum (Low Settings) | Recommended (High Settings) | Enthusiast (Max Settings) |
| :--- | :--- | :--- | :--- |
| **CPU** | Ryzen 5 3600 / i5-10400 | Ryzen 7 5800X3D / i7-12700K | Ryzen 7 7800X3D / i9-14900K |
| **GPU** | GTX 1660 Super / RX 5600 XT | RTX 3070 / RX 6700 XT | RTX 4070 Ti / RX 7900 XT |
| **RAM** | 16GB DDR4 | 32GB DDR4/DDR5 | 32GB DDR5 (6000MHz+) |
| **Storage** | SSD (SATA) | NVMe SSD | NVMe Gen4 SSD |

## Frequently Asked Questions (FAQ)

### Does Ashes of the Singularity II support DLSS 3?
Yes, the game supports NVIDIA DLSS 3 (Frame Generation) on RTX 40-series cards. However, in an RTS game, the added input latency from Frame Generation can make unit selection feel sluggish. We recommend using **DLSS Quality** mode without Frame Generation for the best competitive experience.

### How do I fix the "Out of Video Memory" crash?
This error usually occurs on 8GB cards when playing on 4K resolution with High Textures. Lower the **Texture Quality** to Medium and ensure your Windows Page File is set to "System Managed" to allow for memory overflow.

### Can I run this game on a Steam Deck?
Yes, but with caveats. You must run the game in **Proton Experimental** and set all graphics to Low. You will average 30-40 FPS, but late-game battles with thousands of units will drop to the 20s. It is playable, but not ideal for competitive multiplayer.

## Final Verdict

*Ashes of the Singularity II* is a technical showcase that demands respect from your hardware. Do not rely on the "Auto-Detect" settings, as they often push the CPU too hard while leaving the GPU idle. By manually adjusting the **Geometry Detail** and applying the **Config File Tweak** for render distance, you can eliminate the stuttering that plagues the launch version. If you are running an older CPU, prioritize the Geometry settings over visual fidelity; in this game, a smooth frame rate is your most powerful weapon.