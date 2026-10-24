---
title: "AMD Zen 6 APU 24GB LPDDR5: Steam Deck 2 Specs & Upgrade Guide"
description: "Decode the leaked Zen 6 APU benchmark: 24GB LPDDR5 at 9600 MT/s, 6 cores, 2.4 GHz iGPU. Is this the Steam Deck 2 chip? Specs, analysis, and what to expect."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## AMD Zen 6 APU Leak: What the 24GB LPDDR5 Benchmark Actually Tells Us

A mysterious AMD engineering sample just surfaced in benchmark databases, and the spec sheet reads like a wishlist for handheld gaming: **six Zen 6 CPU cores, 24GB of LPDDR5 memory at 9,600 MT/s, and a 2.4 GHz integrated GPU**. The immediate question everyone is asking: is this the Steam Deck 2 chip? The honest answer is that **AMD has not confirmed any connection to Valve's next handheld**, and engineering samples frequently get repurposed, canceled, or shipped in entirely different product categories (mini-PCs, thin-and-light laptops, embedded boards). What we *can* do is break down what this leak means technically, how it compares to current hardware, and what you should actually do with this information — whether you're a handheld buyer, a mini-PC builder, or just deciding whether to wait before upgrading.

This guide cuts through the hype. Below you'll find a full spec breakdown, a comparison table against current-gen APUs, an analysis of why 9,600 MT/s LPDDR5 matters for gaming, and a practical "should you wait?" buying framework.

## Zen 6 APU Specs Breakdown: 6 Cores, 24GB LPDDR5, 2.4 GHz iGPU

Here's what the leak reportedly shows, and why each number matters:

| Spec | Leaked Value | Why It Matters |
|---|---|---|
| CPU Cores | 6 (Zen 6) | Balanced for handhelds/mini-PCs; fewer cores = better power efficiency |
| Memory | 24GB LPDDR5 @ 9,600 MT/s | Massive bandwidth jump; 24GB is a sweet spot for shared GPU/CPU memory |
| iGPU Clock | 2.4 GHz | High for an integrated GPU — suggests a large RDNA-based compute unit count |
| Process Node | Unconfirmed (likely TSMC N3-class) | Determines efficiency and whether 2.4 GHz is sustainable in a handheld TDP |
| Target TDP | Unconfirmed | The single most important unknown for handheld viability |

**Key technical takeaways:**

1. **9,600 MT/s LPDDR5 is the headline.** Current Steam Deck OLED uses LPDDR5-6400. A jump to 9,600 MT/s represents roughly **50% more memory bandwidth**, which directly feeds the integrated GPU. For iGPUs, bandwidth is usually the #1 bottleneck — this is the spec that could unlock meaningfully higher frame rates at 1080p.
2. **24GB shared memory is strategically smart.** With a unified memory architecture, the OS, CPU, and GPU all draw from the same pool. 24GB gives developers headroom to allocate 8–12GB to the GPU while leaving plenty for the system — far more comfortable than 16GB.
3. **6 cores is a deliberate efficiency choice.** Handhelds live and die by TDP. Six Zen 6 cores (likely a mix of performance and efficiency cores, or six full cores depending on the final design) balance multi-threaded performance against battery drain.
4. **2.4 GHz iGPU clock is aggressive.** Sustaining that in a 15–28W envelope will require excellent cooling and a modern node. In a docked mini-PC with a higher TDP, it's far more plausible.

### How It Compares to Current Hardware

| Device / Chip | CPU | Memory | Bandwidth (approx.) | iGPU |
|---|---|---|---|---|
| Steam Deck OLED | 4c/8t Zen 2 | 16GB LPDDR5-6400 | ~102 GB/s | 8 RDNA 2 CUs @ 1.6 GHz |
| ROG Ally X | 8c Zen 4 | 24GB LPDDR5-7500 | ~120 GB/s | 12 RDNA 3 CUs |
| **Leaked Zen 6 APU** | **6c Zen 6** | **24GB LPDDR5-9600** | **~154 GB/s** | **Unknown CUs @ 2.4 GHz** |

The bandwidth figure is the standout. If accurate, this APU would sit comfortably above every current handheld on memory throughput — the metric that most directly predicts iGPU gaming performance.

## Is This the Steam Deck 2? What You Should Know Before Waiting

Here's the practical part. People hear "Zen 6 APU" and immediately assume Steam Deck 2. Slow down.

**Reasons it *could* be Valve-adjacent:**
- 24GB unified memory mirrors Valve's philosophy of generous shared VRAM.
- Six cores fits a low-TDP handheld profile better than eight.
- Valve has publicly said it's waiting for a "generational leap" — Zen 6 + RDNA-next + LPDDR5-9600 would qualify.

**Reasons to stay skeptical:**
- Engineering samples routinely leak and never ship in consumer handhelds.
- No TDP data means we can't judge handheld viability at all.
- AMD ships APUs to laptop OEMs and mini-PC makers first; this could be a thin-and-light chip.
- Valve has given **no timeline** for Steam Deck 2, and has said it won't rush.

**Actionable advice — a "should you wait?" decision framework:**

- **Buying a handheld in the next 3 months?** Buy now. Steam Deck OLED and ROG Ally X are mature, discounted, and this leak changes nothing about their current value.
- **Can comfortably wait 12–18 months?** A Zen 6-based handheld in late 2027 is plausible but unconfirmed. Waiting is a bet, not a plan.
- **Building a mini-PC?** Watch for this APU class specifically — 24GB + 9,600 MT/s is genuinely exciting for compact gaming rigs, and mini-PC launches often precede handheld versions.

## Frequently Asked Questions (FAQ)

### Is the leaked AMD Zen 6 APU the Steam Deck 2 chip?
Unconfirmed. AMD and Valve have not stated any connection. The specs (6 cores, 24GB LPDDR5, 2.4 GHz iGPU) are *consistent* with a handheld-class chip, but engineering samples often ship in laptops or mini-PCs instead. Treat any "Steam Deck 2 confirmed" headline as speculation.

### What does 24GB LPDDR5 at 9,600 MT/s mean for gaming?
It means roughly 154 GB/s of memory bandwidth shared between CPU and GPU — about 50% more than the Steam Deck OLED. Since integrated GPUs are bandwidth-starved, this is the single spec most likely to translate into real frame-rate gains, especially at 1080p.

### Should I wait for a Zen 6 handheld before buying a Steam Deck or ROG Ally?
Only if you can comfortably wait 12–18 months and accept the risk that no such device launches. Current handhelds are mature and often discounted. If you want to play now, buy now — the leak doesn't change today's value proposition.

### Will this APU run in a low enough TDP for a handheld?
Unknown — TDP wasn't in the leak. A 2.4 GHz iGPU is aggressive for a 15–28W handheld envelope. It's more clearly viable in a docked mini-PC with higher power limits. Watch for TDP figures before assuming handheld readiness.

## Final Verdict

**Don't change your buying plans based on this leak — but do keep it on your radar.** The Zen 6 APU with 24GB LPDDR5-9600 and a 2.4 GHz iGPU is a genuinely exciting spec sheet, and the memory bandwidth figure is the most meaningful signal yet that next-gen handhelds will take a real generational leap. But "engineering sample in a benchmark database" is a long way from "Steam Deck 2 you can buy." If you need a handheld or mini-PC in the next few months, buy a proven current-gen device. If you're a patient buyer with an 18-month horizon, this is exactly the class of chip worth waiting to see materialize — just verify the TDP and official OEM announcements before you commit.