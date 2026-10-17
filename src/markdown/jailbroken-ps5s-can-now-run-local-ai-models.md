---
title: "PS5LM Fork Setup: Run Local AI on Jailbroken PS5 (100+ tok/s)"
description: "Step-by-step guide to install the PS5LM GPU fork on a jailbroken PS5, tune VRAM for Qwen3-27B, and hit 100+ tokens per second safely."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Run Local AI Models on a Jailbroken PS5 (PS5LM Fork Guide)

The PS5LM fork just changed what a jailbroken PlayStation 5 can do: it now runs natively, taps the AMD RDNA 2 GPU and unified memory pool, and can load larger LLMs — including Qwen3-27B at roughly 20 tokens per second, with smaller models like 7B–8B classes clearing 100+ tokens per second. This guide is the practical setup walkthrough: firmware requirements, install order, the exact flags that unlock GPU offload, VRAM budgeting, and the fixes for the crashes and OOM errors people are already hitting. Read the whole thing before you touch a terminal — one wrong flag and you'll be staring at a black screen.

## What You Need Before You Start

| Requirement | Detail | Why It Matters |
|---|---|---|
| PS5 firmware | A jailbreak-compatible build (commonly 3.00–4.51/5.10 class, check current scene compatibility charts) | The exploit chain is firmware-locked; newer firmware won't run the loader |
| Jailbreak state | Active, with persistent payload loader if available | PS5LM needs kernel-level memory access |
| Storage | 50–100 GB free NVMe space | GGUF quantized models are large (Q4 27B ≈ 16–18 GB) |
| Network | LAN, no PSN login | Avoid telemetry/update risk while jailbroken |
| Model files | GGUF format (Q4_K_M recommended) | The fork's loader expects GGUF, not safetensors |
| Input | USB keyboard or SSH client | CLI-driven; no polished UI yet |

**Model size vs. speed reality check (approximate, community-reported):**

- **7B–8B (Q4_K_M):** 100+ tok/s — usable for chat, coding help, summarization
- **13B–14B (Q4_K_M):** 40–60 tok/s — the sweet spot for quality vs. speed
- **27B (Q4_K_M, Qwen3-27B):** ~20 tok/s — slow but genuinely capable reasoning
- **Context length:** keep at 4K–8K tokens initially; long contexts eat the shared memory pool fast

## Step-by-Step: Install and Run PS5LM With GPU Offload

1. **Confirm your firmware and exploit status.** Check the current jailbreak compatibility list for your exact firmware. If you're above the supported ceiling, stop — there is no workaround that doesn't involve waiting for a new chain.
2. **Prepare storage.** Create a dedicated directory (e.g., `/data/ps5lm/models`) on internal NVMe. External USB drives work for cold storage but load times balloon; keep the active model internal.
3. **Grab the fork, not the original.** The fork is the whole point: native execution plus GPU/RAM access. Verify the release hash against the repo's published checksums before transferring.
4. **Transfer the payload and binary** over LAN (FTP or the payload loader's file push). Do not use PSN-linked cloud services.
5. **Download a GGUF model.** Start with a 7B Q4_K_M to validate the pipeline before committing to the 27B download.
6. **Launch with GPU offload flags.** The critical flags are the GPU layer count (`-ngl` / equivalent) and thread count. Start conservative:
   - GPU layers: set to max the fork reports, then back off by 2 if you get artifacts or crashes
   - Context: `4096` for first boot
   - Batch size: `512` default; drop to `256` if memory pressure appears
7. **Benchmark.** Run a fixed 200-token generation and time it. You should see 100+ tok/s on 7B. If you're at 10–15 tok/s, the GPU isn't engaged — see troubleshooting below.
8. **Scale up.** Only after a clean 7B run, swap in the 13B, then the 27B. Expect ~20 tok/s on Qwen3-27B; that's the current ceiling, not a bug.

## Troubleshooting: Common PS5LM Issues and Fixes

- **"GPU not detected" / CPU-only speeds (~10 tok/s):** The fork didn't get GPU access. Re-verify you're on the fork build, not upstream. Check the launch log for the GPU init line — if it's missing, the payload didn't load with sufficient privileges.
- **Out-of-memory on 27B load:** Reduce context to 2048, drop to Q4_K_S, and close any background payloads. The unified memory pool is shared with the OS; you don't get all of it.
- **Crash on first token:** Usually a bad or partial model download. Re-verify the GGUF checksum.
- **Thermal throttling mid-generation:** The PS5's cooling is tuned for games, not sustained compute. Ensure 10+ cm clearance, and expect speed to sag after 10–15 minutes of continuous generation.
- **Black screen after payload load:** Hard power cycle (hold power 15s), then relaunch with default flags. Don't stack payloads.

## Is It Worth It? Honest Comparison

| Option | 27B Speed | Cost | Effort |
|---|---|---|---|
| Jailbroken PS5 + PS5LM fork | ~20 tok/s | $0 (hardware owned) | High, risky |
| Used RTX 3090 PC | 40–60 tok/s | $700–900 | Low |
| Mac Mini M4 (32GB) | 15–25 tok/s | ~$1,000 | Very low |
| Cloud API | N/A | Per-token | None |

The PS5 route wins on **cost** if you already own the console and accept the jailbreak tradeoffs: no PSN, no online play, update risk, and a CLI-only experience. If you need reliability, a used GPU box is the better buy.

## Frequently Asked Questions (FAQ)

### Can a jailbroken PS5 really run Qwen3-27B locally?
Yes — the PS5LM fork loads GGUF-quantized 27B models using the GPU and shared RAM, at roughly 20 tokens per second. That's slow for long documents but fine for interactive chat.

### What firmware do I need for PS5LM?
Only jailbreak-compatible firmware builds work. Check the current scene compatibility chart for your exact version before attempting anything; unsupported firmware cannot run the payload.

### Will running local AI models damage my PS5?
Not directly, but sustained generation runs hotter than gaming and can trigger thermal throttling. Keep ventilation clear and avoid marathon sessions.

### Why am I only getting 10 tokens per second?
The GPU isn't engaged. You're likely on the original build or launched without offload flags. Confirm the fork build and check the GPU init log line.

## Final Verdict

If you already have a jailbroken PS5 on supported firmware and you're comfortable with CLI tools, the PS5LM fork is a genuinely impressive free upgrade — 100+ tok/s on 7B models is real, and 20 tok/s on Qwen3-27B is usable. But treat it as a hobbyist project: verify checksums, start small, budget your VRAM, and don't expect a polished app. If you need dependable daily AI performance, a used RTX 3090 machine remains the smarter purchase.