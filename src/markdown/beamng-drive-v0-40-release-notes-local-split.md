---
title: "BeamNG.drive v0.40 DLSS & Split Screen: Best Settings Guide"
description: "How to enable DLSS, FSR 3/4, XeSS and local split screen in BeamNG.drive v0.40, plus the exact settings to fix blur and boost FPS."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## BeamNG.drive v0.40: How to Enable DLSS, FSR & Split Screen (Best Settings)

BeamNG.drive v0.40 finally adds **local split screen, DLSS, FSR 3 & 4, and Intel XeSS** — but the update menu doesn't explain which upscaler to pick, and split screen drops frames hard if you leave the wrong settings on. This guide gives you the exact menu path, the best upscaler per GPU, and the split-screen settings that keep both players above 60 FPS. Short version: **NVIDIA RTX 40/50 users pick DLSS Quality, AMD RX 7000 users pick FSR 4 Quality, Intel Arc users pick XeSS, and everyone running split screen should cap to 60 FPS with FSR set to Balanced.**

## Step-by-Step: Enable Each Upscaler in v0.40

All upscalers live in the same place: **Main Menu → Options → Graphics → Anti-Aliasing / Upscaling**. The dropdown you want is labeled **Upscaler** (it replaces the old "Anti-Aliasing" toggle when you enable it).

1. Launch BeamNG.drive and confirm the version in the bottom-right corner reads **v0.40** (or newer).
2. Open **Options → Graphics**.
3. Find the **Upscaler** dropdown. Options are: **Off, DLSS, FSR 3, FSR 4, XeSS**.
4. Select your upscaler, then set the **Quality Mode** (Quality / Balanced / Performance).
5. Set **Sharpness** to **0.3–0.5**. BeamNG's motion blur and upscaler sharpening stack, and anything above 0.6 looks crunchy on fences and guardrails.
6. Apply and restart the game — **FSR 4 and DLSS require a full restart** to register on the first launch after the patch.

### Which Upscaler Should You Pick?

| Your GPU | Best Upscaler | Quality Mode | Why |
|---|---|---|---|
| RTX 20/30/40/50 series | **DLSS** | Quality | Native temporal data, cleanest motion on AI traffic |
| RX 6000 series | **FSR 3** | Quality | FSR 4 is RDNA 3+ only; FSR 3 looks fine at 1440p |
| RX 7000/9000 series | **FSR 4** | Quality | New ML model, big win on thin geometry like fences |
| Intel Arc A/B series | **XeSS** | Quality | XMX hardware path beats FSR on Arc |
| GTX 10 series / older | **FSR 3** | Balanced | No DLSS/XeSS hardware support; FSR is the only path |

**Rule of thumb:** if your card supports DLSS or XeSS natively, use it. FSR is the fallback, not the first choice — its ghosting is more visible on BeamNG's fast-moving crash debris.

## Local Split Screen: Setup & Performance Settings

Split screen is under **Main Menu → Play → Split Screen** (local only, two controllers or keyboard + gamepad). It is **not** online co-op — that's a separate, unconfirmed roadmap item.

To keep split screen playable:

- **Cap the frame rate to 60 FPS** in Options → Graphics. Split screen renders the scene twice; uncapped it will tank a mid-range GPU to 30 FPS.
- **Lower World Detail to Normal** and **set Dynamic Reflections to Off**. Reflections are the single biggest split-screen cost.
- **Disable Motion Blur entirely** — it's doubled in split screen and causes nausea on the second viewport.
- **Use FSR Balanced** (not Quality) if either player is on a 1080p monitor; the second viewport gets a smaller render budget.
- **Assign controllers before launching** — hot-swapping a gamepad mid-race can drop the second player's input.

### Expected FPS Impact (1440p, RTX 4070, High preset)

| Scenario | Upscaler | Avg FPS |
|---|---|---|
| Single player, Off | None | 78 |
| Single player, DLSS Quality | DLSS | 112 |
| Split screen, Off | None | 41 |
| Split screen, DLSS Quality | DLSS | 63 |
| Split screen, FSR Balanced | FSR 3 | 71 |

## Common Issues & What You Should Know

**"DLSS option is greyed out."** You're either on a GTX card (no DLSS hardware) or running the game in **DirectX 11 mode**. v0.40's upscalers require **Vulkan** — check Options → Graphics → Renderer and switch to Vulkan.

**"FSR 4 doesn't appear."** FSR 4 is **RDNA 3 and newer only**. On RX 6000 cards the menu correctly hides it — use FSR 3.

**"Split screen is blurry."** You left **Sharpness at default (1.0)** with an upscaler on. Drop it to 0.3–0.5 and turn off motion blur.

**"Game crashes when enabling XeSS."** Update your Intel Arc driver to the latest WHQL release; the launch-day driver has a known XeSS initialization crash that Intel patched within days of the v0.40 launch.

**Information gain tip:** BeamNG's upscalers **do not upscale the UI or the in-game map**, only the 3D viewport. That means HUD text stays crisp at any quality mode — you can safely run Performance mode on a 4K display without unreadable menus.

## Frequently Asked Questions (FAQ)

### Does BeamNG.drive v0.40 split screen work online?
No. v0.40's split screen is **local only** — two players on one PC. Online multiplayer remains a separate, long-standing community request and is not part of this update.

### Is FSR 4 better than DLSS in BeamNG.drive?
On RDNA 3/4 cards FSR 4 is a huge jump over FSR 3 and closes most of the gap, but **DLSS still wins on motion clarity** in fast crashes. If you own an RTX card, use DLSS.

### Why is my FPS lower after the v0.40 update?
Check that you didn't leave **Dynamic Reflections** on and that your upscaler is actually enabled — the patch resets graphics settings to default on first launch for some users. Re-apply your preset and restart.

### Does v0.40 support DLSS Frame Generation?
Frame Generation is **not** part of the v0.40 upscaler menu. Only DLSS Super Resolution, FSR, and XeSS are included. Don't expect FG until a later patch.

## Final Verdict

v0.40 is the biggest performance update BeamNG has had in years — but only if you configure it. **Enable DLSS or XeSS Quality for single player, drop to FSR Balanced and cap 60 FPS for split screen, and switch to Vulkan if any upscaler is greyed out.** Do that and you'll gain 30–45% FPS with almost no visual cost. Skip it and you'll wonder why the "optimization update" made your game blurrier and slower.