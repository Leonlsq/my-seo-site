---
title: "Build a Single-Motor 3D-Printed Drone: Full Guide & Tips"
description: "How to build a tiny 3D-printed single-motor drone like Joshua Bird's, with parts, firmware, PID tuning steps, and fixes for spin-testing issues."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Build a Tiny 3D-Printed Single-Motor Drone (Joshua Bird-Style)

Joshua Bird's bedroom-built drone went viral for a reason: it flies with **one motor**, a single propeller, and a 3D-printed frame that spins at high RPM to generate control torque. If you searched for this after seeing the video, you don't want the news recap — you want to know **how to replicate it, what parts to buy, and how to fix the wobble/spin problems everyone hits**. This guide gives you the build path, the tuning numbers, and the troubleshooting fixes so you don't waste filament and motors on a dead-end prototype.

The core trick: the whole airframe (motor + battery + electronics) rotates with the prop, and control comes from **differential thrust and cyclic pitch modulation** — not from four independent motors. That means your build succeeds or fails on three things: **mass balance, bearing quality, and control-loop tuning**. Nail those and it hovers; miss them and it just spins on the bench.

## Step-by-Step Build Guide

### 1. Bill of Materials (what actually matters)

| Component | Spec to target | Why it matters |
|---|---|---|
| Motor | 1x brushless, 2205–2306, ~2400KV (3S) | Single motor must handle full thrust + cyclic load |
| Propeller | 5"–6" with adjustable/collective pitch | Pitch modulation is your control authority |
| Swashplate / cyclic mechanism | Small heli-style or 3D-printed linkage | Converts servo input to blade pitch |
| Servos | 2x micro (9g–12g), metal gear | Fast response for cyclic control |
| Flight controller | Any STM32 F4/F7 board running Betaflight | Needs custom mixer support |
| Battery | 3S 450–850mAh LiPo | Keep mass low; every gram fights you |
| Bearings | High-precision, low-friction thrust bearings | The #1 failure point in single-motor designs |
| Frame | PETG or PA-CF (not PLA) | PLA creeps and warps at high RPM |

### 2. Print settings that survive high RPM

- **Material:** PETG or PA-CF. PLA will deform under centrifugal load and motor heat.
- **Walls:** 4–5 perimeters, 40–50% gyroid infill on load-bearing arms.
- **Tolerance:** print a bearing-fit test coupon first — aim for 0.1–0.15mm clearance.
- **Balance:** print a balancing jig and check the rotor assembly on a static balancer before first spin-up.

### 3. Firmware and mixer setup

1. Flash Betaflight (or a custom firmware fork) to your FC.
2. Configure a **custom motor/servo mixer**: one motor output + two servo outputs for cyclic pitch.
3. Set servo update rate to at least 250Hz.
4. Start with **low PID values (P ≈ 30–40% of a normal quad)** — single-motor frames oscillate violently if you copy quad tunes.
5. Enable a **throttle-to-pitch feedforward** curve so cyclic authority scales with RPM.

### 4. First spin-up (safely)

- Clamp the frame in a **test stand** — do not hand-hold it.
- Spin at 20%, 40%, 60% throttle and log vibration via the FC's blackbox.
- Check for resonance spikes; add damping (TPU mounts) where the log shows peaks.

## Common Issues & Fixes

**"It spins but won't stabilize."**
Almost always a **PID/feedforward mismatch**. Reduce P by 20%, increase servo rate, and verify your mixer signs (a reversed servo = instant flip).

**"Vibration destroys the video / FC disarms."**
Balance the rotor and prop. Add a TPU soft-mount between FC and frame. Check bearing play — even 0.1mm of slop causes high-RPM wobble.

**"I can't see what's happening at high RPM."**
This is exactly why Bird **built a custom high-speed camera**. You can replicate cheaply: a phone at 240fps in slow-mo mode, or a $30 USB high-speed cam. Film the rotor head at 1000+ fps equivalent to spot blade flex and linkage slop.

**"Filament parts crack at the hub."**
Switch to PA-CF, increase hub wall count, and add a metal insert at the bearing seat.

### Alternatives if single-motor is too hard

- **Standard quad build:** far easier tuning, but loses the novelty.
- **Collective-pitch quad:** similar cyclic control concept, four motors — good stepping stone.
- **Buy a micro heli (e.g., Blade/Eachine):** learn swashplate mechanics before printing your own.

## Frequently Asked Questions (FAQ)

### Can you really build a drone with just one motor?
Yes — it works by rotating the entire airframe and using cyclic blade pitch (like a helicopter) for control. It's mechanically harder than a quad but proven to fly, as Joshua Bird demonstrated.

### What 3D printer material is best for a single-motor drone frame?
PETG or carbon-fiber nylon (PA-CF). Avoid PLA because it softens and creeps under heat and centrifugal load at high RPM.

### Do I need a high-speed camera to tune it?
Not strictly, but it helps enormously. A 240fps phone slow-mo or a cheap high-speed USB camera lets you see blade flex, linkage slop, and vibration that are invisible at normal speed.

### How much does a single-motor drone build cost?
Roughly $120–$250 depending on motor, servos, FC, and battery. The 3D-printed frame is cheap; precision bearings and servos are the main cost drivers.

## Final Verdict

Building a single-motor 3D-printed drone is a **genuinely hard but rewarding project** — not a weekend beginner build. If you want the challenge, start with a **test-stand spin rig, PETG frame, and conservative PID tuning**, and film every spin-up with a high-speed camera. If you just want to fly, buy a micro quad or heli first; come back to this once you understand swashplate and cyclic mechanics. The payoff — a drone that flies on one motor — is worth the tuning pain.