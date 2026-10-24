---
title: "How to Break an OC World Record on a $60 Haswell CPU"
description: "Learn how Luumi toppled a 12-year Cinebench record using a cheap Haswell chip. Step-by-step guide to budget overclocking, bclk tuning, and cooling."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Break a Cinebench World Record on Cheap Haswell Hardware

When overclocker Luumi toppled a Cinebench R15 world record that had stood for 12 years, the headline wasn't the score — it was the hardware. No Ryzen 9000, no Core Ultra, no exotic LN2-only platform. Just an ancient Intel Haswell chip, careful bclk tuning, and a lot of patience. The takeaway is simple: **you do not need current-gen silicon to set records or have fun overclocking.** This guide breaks down exactly how that kind of run is built, what settings matter, and how you can replicate the methodology on your own legacy system — whether you're chasing a global record or just a personal best.

The key insight from the Luumi run is that records are won on *efficiency and stability*, not raw clocks. Haswell (4th-gen Core, LGA1150) is famous for two things: excellent memory controller scaling and a stubborn 100 MHz bclk wall. Beating a 12-year-old record means exploiting every last multiplier and reference-clock trick the platform allows.

## Step-by-Step: Building a Record-Class Haswell Overclock

Here's the practical playbook, in the order you should tackle it.

### 1. Pick the Right Chip and Board
- **CPU:** A Haswell "K" SKU (e.g., Core i5-4690K, i7-4790K) for unlocked multipliers. Non-K chips cap you at bclk-only tuning.
- **Motherboard:** A Z97 board with a strong VRM and granular bclk control. ASUS ROG and Gigabyte SOC boards are the classics for record attempts.
- **Memory:** Dual-channel DDR3 rated for high frequency. Haswell's IMC loves tight timings and can push well past 2400 MT/s with voltage.

### 2. Lock Down Cooling and Power Delivery
- **Cooling:** For ambient records, a large AIO or custom loop is enough. Sub-ambient (chilled water, dry ice) is where records actually fall — Luumi-class runs typically use phase-change or dry ice on the CPU.
- **PSU:** A quality 650W+ unit with clean ripple. Overclocking records are lost to unstable rails, not clocks.
- **Disable power limits:** Set CPU power limits to maximum, disable C-states, and lock the CPU to a fixed voltage.

### 3. Tune bclk, Not Just Multiplier
This is the secret sauce. Haswell's bclk strap lets you push past the 100 MHz default in small increments.

| Setting | Safe Daily | Record Attempt |
|---|---|---|
| CPU multiplier | 42–45x | 48–52x (cooling-dependent) |
| bclk | 100 MHz | 102–105 MHz (board-dependent) |
| Vcore | 1.25–1.30V | 1.40–1.50V (sub-ambient) |
| VCCIN | 1.80V | 2.00–2.10V |
| DRAM voltage | 1.50V | 1.65V+ |

Small bclk bumps multiply across the whole system, so a 103 MHz bclk with a 50x multiplier nets 5,150 MHz — often more than a clean 100 MHz bclk can achieve.

### 4. Validate and Submit
- Run **Cinebench R15** (the legacy benchmark where the 12-year record lived) with all background apps closed.
- Confirm stability with a short **Prime95** or **OCCT** pass before submitting.
- Screenshot CPU-Z (CPU, Memory, Mainboard tabs) alongside the Cinebench result — this is mandatory for HWBOT validation.

## Common Issues and What You Should Know

- **bclk instability:** Above ~103 MHz, SATA and PCIe devices can drop out. Disable unused controllers and, if possible, boot from a USB or use a board with a separate clock generator.
- **Thermal throttling:** Haswell runs hot once you pass 1.35V. Delidding (removing the IHS and replacing the TIM) can drop load temps 10–20°C — often the difference between a stable and unstable record run.
- **Memory training loops:** Aggressive DRAM settings can cause boot loops. Clear CMOS and step timings back one notch at a time.
- **Don't chase current-gen scores:** Cinebench R15 is a legacy benchmark; modern CPUs crush it trivially. The record only matters within its historical hardware class — which is exactly why a Haswell run can still top it.

## Frequently Asked Questions (FAQ)

### Can I break an overclocking world record with a cheap old CPU?
Yes — records are class-specific. Legacy benchmarks like Cinebench R15 have hardware-tier records, so a well-tuned Haswell system can top a 12-year-old score without modern hardware. Cooling and bclk tuning matter more than the chip's age.

### What is bclk and why does it matter for Haswell overclocking?
bclk (base clock) is the reference clock the CPU multiplies against. On Haswell, pushing bclk from 100 MHz to 103–105 MHz raises the effective frequency of the CPU and memory simultaneously, letting you squeeze extra performance beyond multiplier-only overclocking.

### Is delidding a Haswell CPU worth it for overclocking?
For record attempts, yes. Replacing Intel's stock TIM with liquid metal typically drops load temperatures 10–20°C, enabling higher stable voltages and clocks. For daily use, it's optional but popular among enthusiasts.

### What benchmark did the 12-year record use?
The record in question was set on **Cinebench R15**, a legacy multi-threaded CPU benchmark still tracked by the overclocking community on HWBOT.

## Final Verdict

You don't need a $600 CPU to have fun overclocking — and Luumi's run proves it. If you want to chase a record, grab a cheap Haswell K-chip and a Z97 board, delid it, and spend your time on bclk tuning and cooling rather than shopping. If you just want to learn overclocking, this same methodology — multiplier, bclk, voltage, validation — transfers directly to any modern platform. Start with a safe 4.4 GHz daily tune, then push when you're ready to submit.