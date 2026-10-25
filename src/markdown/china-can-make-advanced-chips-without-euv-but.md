---
title: "China's No-EUV Chips: Why 5nm Costs 2x More"
description: "How China makes 5nm-class chips without EUV using DUV multi-patterning, the real cost and yield trade-offs, and why the bill keeps growing."
pubDate: 2026-10-24
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## China's No-EUV Chips Explained: The Real Cost of Skipping EUV

You've seen the headlines: China is pushing DUV lithography into 5nm-class territory without ASML's EUV machines. The question most people actually search for is simpler — **how does that even work, and what does it cost?** The short answer: it works through aggressive multi-patterning, and the bill grows fast. Every layer you can't print in one EUV pass becomes 2–4 DUV passes, and each extra pass multiplies mask costs, cycle time, and defect risk. Below is a practical breakdown of the technique, the numbers, and where the economics break down.

## How DUV Multi-Patterning Reaches 5nm-Class: Step-by-Step

The core trick is **SADP/SAQP (self-aligned double/quadruple patterning)** combined with LELE (litho-etch-litho-etch). Here's the practical workflow engineers use to stretch a 193nm DUV scanner:

1. **Start with a single DUV exposure** at the finest achievable pitch (roughly 38–40nm for immersion DUV).
2. **Deposit a spacer film** and etch back to create two features from one — this is SADP, effectively halving the pitch.
3. **Repeat the spacer process** (SAQP) to quarter the pitch, approaching the feature density EUV delivers natively.
4. **Apply cut masks** to trim unwanted lines and define real circuit patterns.
5. **Overlay every layer precisely** — misalignment between passes directly kills yield.

The catch is cumulative: each additional pass adds a mask set, an etch step, and an alignment tolerance budget. A single EUV layer might replace 3–4 DUV layers, but the DUV route needs those layers to exist *and* to align within a few nanometers.

### Cost Comparison: EUV vs. DUV Multi-Patterning (5nm-class)

| Factor | EUV (single pass) | DUV Multi-Patterning |
|---|---|---|
| Mask count per critical layer | 1 | 3–4 |
| Mask cost per layer | ~$3–5M (EUV mask) | ~$1–2M each, ×3–4 |
| Wafer passes per layer | 1 | 3–4 |
| Cycle time | Baseline | 2–4× longer |
| Yield (mature node) | Higher | Lower, defect-sensitive |
| Die size penalty | None | Larger due to spacing rules |

The mask economics flip fast. A single EUV mask is expensive, but when you need four DUV masks plus four etch cycles to match one EUV layer, the per-wafer cost climbs steeply — and that's before yield losses.

## Common Issues, Alternatives, and What You Should Know

**1. Yield is the silent tax.** Multi-patterning introduces more defect opportunities per layer. Overlay errors between passes are the dominant killer, and they scale with the number of passes. A process that yields 80% on EUV might yield 50–60% on equivalent DUV multi-patterning — and every lost wafer carries the full multi-pass cost.

**2. Die size grows.** Tighter spacing rules mean circuits can't be packed as densely. A chip designed for EUV might be 10–20% smaller than the same design forced onto DUV multi-patterning. Larger die = fewer chips per wafer = higher cost per chip.

**3. The economic wall.** Experts consistently flag that beyond 5nm-class, the pass count, mask costs, and yield penalties compound until the cost per good die exceeds what the market will pay. 3nm-class via pure DUV is widely considered economically unviable.

**4. Alternatives being explored.** Advanced packaging (chiplet stacking), mature-node optimization, and domestic EUV development are the parallel bets. Chiplets let designers sidestep the lithography wall by combining smaller dies.

**5. What this means for you as a buyer.** If you're evaluating hardware built on these processes, expect competitive performance at 7nm/5nm-class but watch for thermal and yield-driven pricing. Don't assume "5nm-class" means parity with TSMC N5 — the die-size and yield trade-offs are real.

## Frequently Asked Questions (FAQ)

### Can China really make 5nm chips without EUV?
Yes, at a cost. Using DUV immersion scanners with SAQP and multiple patterning, fabs can approach 5nm-class feature density. The trade-off is more mask layers, longer cycle times, lower yield, and larger die sizes — making it economically painful but technically possible.

### Why is DUV multi-patterning so much more expensive than EUV?
Each critical layer requires 3–4 separate exposures, etches, and mask sets instead of one EUV pass. That multiplies mask costs, wafer processing time, and defect risk. When yield drops, the cost per *good* die rises even faster than the raw wafer cost.

### Is 3nm possible without EUV?
Widely considered economically unviable. The pass count and yield penalties compound to the point where cost per good die exceeds market tolerance. Most industry analysis puts the practical DUV ceiling around 5nm-class.

### Does multi-patterning affect chip performance?
Indirectly, yes. Larger die sizes and tighter spacing rules can increase parasitics and reduce packing density. Performance at the same node is often close, but power and area efficiency lag EUV-based equivalents.

## Final Verdict

China's DUV multi-patterning is a genuine engineering achievement — but it's a bridge, not a destination. If you're following this space, the takeaway is clear: **5nm-class without EUV is real, but the cost curve bends upward sharply past that point.** For buyers, treat "5nm-class" claims with healthy skepticism and check die size and yield data before assuming parity. For the industry, the real race isn't lithography tricks — it's domestic EUV and advanced packaging. Watch those two, not the pass count.