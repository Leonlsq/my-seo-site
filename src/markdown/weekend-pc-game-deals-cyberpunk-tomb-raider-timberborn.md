---
title: "Cyberpunk & Tomb Raider PC Deals: Best Settings to Max FPS"
description: "Scored the weekend PC game deals? Here's how to optimize Cyberpunk 2077, Tomb Raider, and Timberborn settings for max FPS on mid-range hardware."
pubDate: 2026-10-24
tags: ['Tech', 'Guide', 'Gaming']
---

## Weekend PC Game Deals Are Live — Here's How to Actually Run Them

The weekend sale wave is here: **Cyberpunk 2077**, the **Tomb Raider** trilogy, and **Timberborn** are all discounted across major storefronts, and thousands of players are buying first and checking their specs second. If that's you, this guide is the fix. Below you'll find the exact graphics settings, upscaling configurations, and CPU tweaks that let mid-range rigs (think RTX 3060 / RX 6600 and Ryzen 5 / Core i5) hit a stable 60+ FPS in Cyberpunk 2077, squeeze 144 FPS out of Shadow of the Tomb Raider, and keep Timberborn from chugging once your beaver colony hits 200+ citizens. No fluff — just settings that work.

## Cyberpunk 2077: The Settings That Actually Matter

Cyberpunk is the heaviest title in this batch. On a 6GB–8GB GPU, the difference between default "High" and a tuned profile is roughly **35–45% more frames** with almost no visual loss.

**Step-by-step optimization:**

1. **Enable upscaling first.** Set DLSS (NVIDIA) to **Quality**, or FSR 2.2/3 (AMD) to **Quality**. On a 1080p display, DLSS Quality renders internally at 720p and reconstructs — this alone is worth 30+ FPS.
2. **Kill the frame-eaters.** Set these to Medium or Off: **Volumetric Fog Quality**, **Screen Space Reflections Quality**, **Cascaded Shadows Range**, and **Local Shadow Mesh Quality**. These four settings cost the most GPU time per frame.
3. **Ray tracing: skip it** unless you have an RTX 4070-class card. Path tracing is a 4090-only feature at playable framerates.
4. **Cap your framerate.** Use in-game V-Sync off + a driver-level cap (NVIDIA Control Panel → Max Frame Rate, or AMD Adrenalin → Frame Rate Target Control) at your monitor's refresh minus 2–3. This stabilizes frame pacing in Night City's crowded districts.
5. **CPU-bound in crowded areas?** Lower **Crowd Density** to Medium. This is the single biggest CPU-side win in the game.

**Quick reference table (1080p, RTX 3060 / RX 6600 class):**

| Setting | Recommended | FPS Impact |
|---|---|---|
| DLSS/FSR | Quality | +25–35 FPS |
| Volumetric Fog | Medium | +6–8 FPS |
| Screen Space Reflections | Medium | +5–7 FPS |
| Crowd Density | Medium | +4–6 FPS (CPU) |
| Ray Tracing | Off | +20–40 FPS |

## Tomb Raider Trilogy: Lock In 144 FPS

The Tomb Raider games (especially the 2013 reboot and Rise) are old enough that **any GPU from the last six years should max them out** — but Shadow of the Tomb Raider's built-in benchmark is notoriously CPU-sensitive in its village sections.

- **Run the built-in benchmark** (Options → Graphics → Benchmark) before playing. It gives you a real average and minimum FPS, not guesses.
- **Disable DirectX 12** if you get stutter on older drivers — DX11 is more stable in Rise and Shadow on many systems.
- **Set Shadows to High, not Ultra.** Ultra shadows in Shadow of the Tomb Raider cost ~10% performance for a difference you won't notice in motion.
- **Turn off Motion Blur and Film Grain** — free performance and a cleaner image.

## Timberborn: Stop the Late-Game Stutter

Timberborn isn't GPU-heavy — it's a **CPU and simulation** problem. Once your colony passes ~150 beavers, pathfinding and water simulation hammer a single core.

1. **Lower "Water Simulation Quality"** in settings — this is the biggest late-game FPS saver.
2. **Reduce map size** on new saves if you plan long playthroughs; larger maps scale simulation cost.
3. **Cap FPS to 60** in-game. Timberborn will happily render 300 FPS and cook your CPU for no benefit.
4. **Close browser tabs** — seriously. Timberborn is single-thread-bound, and background Chrome processes steal the exact core it needs.

## Common Issues, Alternatives, or What You Should Know

- **"My FPS is fine but it stutters."** That's frame pacing, not raw FPS. Cap your framerate and enable FreeSync/G-Sync. In Cyberpunk, also delete the shader cache (`%LOCALAPPDATA%\CD Projekt Red\Cyberpunk 2077\cache`) after driver updates — it rebuilds and eliminates first-encounter hitches.
- **Refund windows matter.** Steam gives 2 hours / 14 days. Benchmark *before* that window closes — the Cyberpunk built-in benchmark is under Settings → Graphics.
- **Don't buy the DLC blind.** Phantom Liberty is excellent but adds GPU load in Dogtown specifically. Test the base game first.
- **Storefront tip:** check IsThereAnyDeal before checkout — these sale prices rotate, and historical lows are often 20–30% below the current "deal."

## Frequently Asked Questions (FAQ)

### Can I run Cyberpunk 2077 on a GTX 1650?
Yes, at 1080p Low with FSR set to Performance, targeting ~40–50 FPS. It won't be pretty, but it's playable. Skip ray tracing entirely.

### Is Timberborn worth it on a laptop?
Yes — it's light on GPU and runs well on integrated graphics at 1080p. Just cap FPS to 60 and expect slowdowns on very large colonies with weaker CPUs.

### Do the Tomb Raider deals include all DLC?
Depends on the edition. The "Definitive Edition" of Shadow includes the season pass; the base version does not. Check the store page's "includes" list before buying.

## Final Verdict

Buy **Cyberpunk 2077** if you have an RTX 3060-class GPU or better and don't mind tuning settings — with DLSS Quality and the four settings above, it's a 60+ FPS experience at 1080p. Grab the **Tomb Raider** games guilt-free; they'll run maxed on almost anything. And **Timberborn** is the sleeper pick of the sale — just cap your FPS and lower water simulation quality before your colony gets huge. Benchmark within the refund window, and you can't lose.