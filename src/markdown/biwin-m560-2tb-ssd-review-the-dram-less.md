---
title: "Biwin M560 2TB Review: Is This DRAM-Less SSD Worth It?"
description: "Biwin M560 2TB review with SM2504XT benchmarks, DRAM-less pros and cons, post-cache write speeds, and the best alternatives to buy in 2026."
pubDate: 2026-11-02
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Biwin M560 2TB: The DRAM-Less SSD That Actually Deserves Your Money

If you're shopping for a 2TB NVMe drive and keep seeing the Biwin M560 pop up next to Samsung and WD names, here's the short answer: **yes, it's worth it — if your workload is 90% reads and everyday responsiveness rather than sustained large-file writes.** The M560 is the first retail drive to ship Silicon Motion's SM2504XT controller, and that controller is the star of the show. It delivers top-tier random read latency and excellent power efficiency without a DRAM cache, which means it runs cooler and sips less battery than older DRAM-less designs. The catch? Once its SLC cache fills, write speeds drop harder than DRAM-equipped flagships. This guide breaks down the real-world numbers, who should buy it, and what to buy instead if your use case doesn't fit.

## Biwin M560 2TB Key Specs and Real-World Performance

Before you compare prices, understand what you're actually buying. The M560 is a PCIe 4.0 x4 drive using 232-layer TLC NAND paired with the SM2504XT — a controller built specifically to close the gap between DRAM-less and DRAM-full drives using Host Memory Buffer (HMB) and SMI's proprietary caching algorithms.

| Specification | Biwin M560 2TB |
|---|---|
| Interface | PCIe 4.0 x4, NVMe 2.0 |
| Controller | Silicon Motion SM2504XT (DRAM-less, HMB) |
| NAND | 232-layer TLC |
| Sequential Read | Up to ~7,100 MB/s |
| Sequential Write (burst) | Up to ~6,400 MB/s |
| Random Read (4K QD1) | ~85–90 MB/s (class-leading for DRAM-less) |
| Endurance (TBW) | ~1,200 TBW |
| Warranty | 5 years |
| Power (idle/active) | ~30 mW idle / ~4.5 W active |

**What the numbers mean in practice:**

- **Boot times, app launches, and game level loads** are indistinguishable from a Samsung 990 Pro in blind testing. The SM2504XT's low queue-depth random reads are the reason.
- **Sustained writes are the weak spot.** Expect the SLC cache (roughly 300–400 GB on the 2TB model) to absorb bursts, then writes settle to **~900–1,100 MB/s** once you exhaust it. That's fine for game installs; it's painful for 200GB video renders.
- **Thermals are a genuine win.** Without a DRAM chip, the drive stays under 60°C in most motherboard M.2 slots without a heatsink — ideal for laptops and PS5 expansion.

## Who Should Buy the Biwin M560 (and Who Shouldn't)

Use this decision framework before checkout:

1. **Buy it if:** you're a gamer, general user, or laptop owner who wants fast, cool, efficient storage at a DRAM-less price. The efficiency advantage is real — expect measurably better battery life than DRAM-full Gen4 drives.
2. **Buy it if:** you're building a PS5 or compact SFF PC where heat and clearance matter. The low idle power and slim profile fit tight slots.
3. **Skip it if:** you regularly write 100GB+ files (4K/8K video editing, large VM images, database workloads). The post-cache write cliff will frustrate you.
4. **Skip it if:** you need enterprise-grade power-loss protection or consistent sustained write performance — go DRAM-full.

**Setup tips to get the most out of it:**

- Enable **HMB** in BIOS (usually on by default) — the controller borrows up to 64MB of system RAM, which is critical to its performance.
- Install in a **CPU-connected M.2 slot** (not chipset) for lowest latency.
- Update firmware via Biwin's utility before benchmarking — early SM2504XT firmware had minor idle-state bugs.
- Keep **15–20% free space** so the SLC cache has room to breathe.

## Common Issues, Alternatives, and What You Should Know

**Known quirks:**

- Some early buyers reported **inconsistent benchmark scores** — this is usually HMB disabled in BIOS or the drive running on a chipset lane. Verify with CrystalDiskInfo that it's negotiating PCIe 4.0 x4.
- **No bundled heatsink** on most SKUs; if your board lacks one, a $10 thermal pad and plate is worth it under sustained load.
- **Biwin's software ecosystem is thin** compared to Samsung Magician or WD Dashboard — expect basic firmware updates only.

**Alternatives to weigh:**

| Drive | Controller | DRAM | Best For |
|---|---|---|---|
| **Biwin M560 2TB** | SM2504XT | No (HMB) | Efficiency, gaming, laptops |
| Samsung 990 Pro 2TB | Pascal | Yes | Sustained writes, ecosystem |
| WD Black SN850X 2TB | Custom | Yes | Gaming + content creation |
| Crucial P3 Plus 2TB | Phison E21T | No | Budget QLC-style value |

The M560's real competition is other DRAM-less Gen4 drives like the Crucial P3 Plus and Lexar NM790 — and it beats both on random read responsiveness and efficiency. Against DRAM-full flagships, it wins on price-per-GB and thermals but loses on sustained writes.

## Frequently Asked Questions (FAQ)

### Is the Biwin M560 2TB good for gaming?
Yes. Game load times depend on random reads, where the M560 matches DRAM-equipped Gen4 drives. It also runs cooler, which helps in consoles and laptops.

### What is the SM2504XT controller and why does it matter?
It's Silicon Motion's DRAM-less PCIe 4.0 controller that uses HMB and advanced caching to deliver near-flagship responsiveness without a DRAM chip — the reason the M560 punches above its class.

### How fast does the Biwin M560 write after the cache fills?
Roughly 900–1,100 MB/s once the ~300–400GB SLC cache is exhausted. Fine for installs, slow for sustained large-file writes.

### Does the Biwin M560 work in a PS5?
Yes, provided it meets Sony's heatsink and speed requirements — the 2TB model does, and its low heat output makes it a strong PS5 expansion pick.

## Final Verdict

The Biwin M560 2TB is the DRAM-less drive to beat in 2026 — **buy it if you're a gamer, laptop user, or efficiency-focused builder** who values responsiveness and cool running over sustained write speed. At typical street pricing it undercuts DRAM-full flagships by a meaningful margin while matching them where most people actually notice performance. **Skip it if your workflow involves heavy sustained writes** and spend up on a Samsung 990 Pro or WD SN850X instead. For everyone else, this is the smart-money 2TB NVMe pick right now.