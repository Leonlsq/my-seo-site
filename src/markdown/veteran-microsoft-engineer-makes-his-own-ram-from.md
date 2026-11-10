---
title: "Build Your Own RAM Like Dave Plummer: PDP-11 Guide"
description: "How to build PDP-11 RAM from scratch like Dave Plummer's AI-assisted project. Step-by-step guide, parts list, costs, and whether it's worth it."
pubDate: 2026-11-02
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Build Your Own RAM? The Dave Plummer Story and What You Can Learn

When veteran Microsoft engineer Dave Plummer got priced out of buying period-correct memory for his PDP-11 restoration, he did what most of us only joke about: he built his own RAM from scratch — with AI as his research assistant. The takeaway for anyone watching the story is simple: **you don't need a warehouse of vintage parts to get a retro machine running.** You need a clear spec, a handful of cheap modern components, and a willingness to design a small interface board. This guide breaks down exactly how that kind of project works, what it costs, and how to replicate the approach for your own PDP-11 (or any vintage computer with a memory bus).

The core problem Plummer faced is universal in retro computing: original DEC memory boards (like the MS11 series) are scarce, fragile, and expensive on the secondary market. A single working board can run hundreds of dollars, and the capacitors and logic chips on them are often decades past their rated life. Building a replacement means you control the cost, the reliability, and the supply chain.

## Step-by-Step Guide: Replicating a DIY PDP-11 RAM Board

Here's the practical path from "my PDP-11 needs memory" to "my PDP-11 boots with modern RAM." This mirrors the approach Plummer used: define the bus, design the interface, source parts, then test.

### 1. Understand the PDP-11 Unibus/Q-Bus Memory Requirements
- **Address space:** The PDP-11 uses 16-bit addressing (64 KB total) on classic models; memory boards map into specific address ranges.
- **Bus type:** Confirm whether your machine uses **Unibus** (PDP-11/20, /45, /70) or **Q-Bus** (PDP-11/23, /73, MicroPDP-11). The signal timing and connector pinout differ significantly.
- **Cycle timing:** Unibus memory cycles are relatively slow (hundreds of nanoseconds). This is *good news* — modern SRAM is far faster than the bus, so timing is easy to satisfy.

### 2. Choose Your Memory Technology
| Option | Pros | Cons | Best For |
|---|---|---|---|
| Modern SRAM (e.g., AS6C series) | Cheap, fast, 5V-tolerant variants exist | Needs level shifting on some buses | Most DIY builds |
| FRAM | Non-volatile, no battery | Higher cost per bit | Small boot ROMs |
| Original DRAM + refresh logic | Authentic | Complex refresh circuitry, obsolete parts | Purists only |
| FPGA-based memory emulator | Flexible, reconfigurable | Steeper learning curve | Multi-machine builders |

For a first build, **5V SRAM is the pragmatic choice** — it matches the TTL logic levels of the PDP-11 bus and eliminates level-shifting headaches.

### 3. Design the Bus Interface
- **Buffer the data lines** with bidirectional transceivers (e.g., 74LS245) so the board doesn't load the bus.
- **Decode the address** with a comparator (74LS688) so the board only responds to its assigned address range.
- **Generate the control signals** (MSYN, SSYN on Unibus) with simple glue logic or a small CPLD.
- Use AI tools — as Plummer did — to sanity-check timing diagrams, generate Verilog for a CPLD, or double-check pinouts against scanned DEC manuals.

### 4. Source Parts and Build
- Order SRAM, transceivers, and a custom PCB (or protoboard) — total component cost is typically **$30–$80**.
- Fabricate the board with a service like JLCPCB; a small run of 5 boards often costs under $20.
- Socket your chips so you can swap failed parts without desoldering.

### 5. Test Incrementally
1. Power the board alone and verify no shorts.
2. Connect to the bus and check that address decoding responds only in-range.
3. Run a memory diagnostic (DEC's own XXDP diagnostics or a simple write/read loop) before trusting it with an OS.

## Common Issues, Cost Analysis, and Alternatives

**What can go wrong:**
- **Bus loading:** Too many boards without buffers can cause signal reflections and intermittent faults. Always buffer.
- **Wrong address decode:** Double-check your jumper settings — a board responding to the wrong range will crash the machine instantly.
- **Power draw:** Vintage backplanes have limited current. Modern SRAM is efficient, but tally your budget.

**Cost comparison — DIY vs. buying original:**

| Approach | Typical Cost | Reliability | Effort |
|---|---|---|---|
| Buy original DEC board | $150–$500+ | Low (aging parts) | None |
| DIY SRAM board | $30–$80 + PCB | High | Moderate |
| FPGA emulator | $100–$250 | High | High |

**Alternatives worth knowing:** If you don't want to design a board, open-source PDP-11 memory projects and FPGA-based Unibus/Q-Bus emulators already exist — you can build a proven design and skip the reverse-engineering phase entirely.

## Frequently Asked Questions (FAQ)

### Did Dave Plummer really build PDP-11 RAM from scratch using AI?
Yes. The former Microsoft engineer designed a replacement memory board for his PDP-11 restoration, using AI tools to assist with research, timing verification, and design details rather than buying expensive original DEC hardware.

### How much does it cost to build your own PDP-11 RAM board?
A DIY SRAM-based board typically runs **$30–$80 in components** plus PCB fabrication (often under $20 for a small batch), far less than the $150–$500+ original boards command on the secondary market.

### Can I use modern RAM in a vintage PDP-11?
Yes — modern 5V SRAM works well because the PDP-11 bus is slow by modern standards, so timing is easy to meet. You need proper bus buffering and address decoding, but the memory chips themselves are cheap and reliable.

## Final Verdict

If you own a PDP-11 and are staring down the cost of original memory boards, **building your own is absolutely worth it** — cheaper, more reliable, and genuinely educational. Start with a buffered 5V SRAM design, lean on AI and open-source schematics to shortcut the research, and test with XXDP diagnostics before trusting it. You'll spend a weekend and under $100 to get a machine that outlasts any 40-year-old original board.