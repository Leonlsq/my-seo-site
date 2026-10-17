---
title: "Llama.cpp on PS5: How to Run GGUF Models Natively"
description: "Step-by-step guide to running Llama.cpp and GGUF models natively on a jailbroken PS5, plus VRAM limits, token speeds, and fixes for common errors."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Can You Actually Run Llama.cpp on a Jailbroken PS5? (Yes — Here's How)

The `cobanov/PS5LM` project proved something the console modding scene has speculated about for years: a jailbroken PS5 can execute native FreeBSD-based binaries, and that means you can compile and run **llama.cpp** directly on the hardware — no Linux VM, no remote server, no PC streaming. This guide walks you through the real setup path, the memory ceiling you'll hit, and the exact model sizes that actually run at usable speeds. Short version: 7B–8B Q4 models are the sweet spot, and anything above ~13B will fight the console's unified memory pool.

## What the PS5 Hardware Actually Gives You for LLM Inference

Before you touch a single command, understand the constraints. The PS5's APU is not a gaming GPU in the PC sense — it shares memory between CPU and GPU, which is both a blessing and a curse for llama.cpp.

| Component | PS5 Spec | Impact on llama.cpp |
|---|---|---|
| CPU | 8-core AMD Zen 2 @ 3.5 GHz (variable) | Solid for CPU-only inference on small models |
| GPU | RDNA 2, ~10.3 TFLOPS | Limited without a tuned backend; no CUDA |
| Memory | 16 GB GDDR6 (unified) | ~10–13 GB usable after OS reserve |
| Storage | NVMe SSD | Fast model loading from disk |
| OS | FreeBSD-derived (jailbroken) | Requires native compilation, no standard Linux packages |

The critical number is **usable memory**. After the system reserves its share, expect roughly **10–13 GB** for your model, KV cache, and context. A 7B Q4_K_M GGUF lands around 4.4 GB — comfortable. A 13B Q4 sits near 8 GB and leaves little headroom for long contexts.

## Step-by-Step: Compiling and Running llama.cpp on the PS5

This assumes you already have a working jailbreak with shell access (the PS5LM repo documents the specific payload chain — follow it exactly, as firmware version matters).

1. **Confirm shell access and toolchain.** You need a working `clang`/`gcc`, `make`, and `cmake` in your environment. Run `uname -a` to verify the kernel and `cc --version` to confirm the compiler.
2. **Clone the source.** `git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp`
3. **Build CPU-only first.** Start with `make` (or `cmake -B build && cmake --build build -j8`). Do **not** attempt GPU offload on the first build — get a known-good CPU binary before experimenting.
4. **Grab a quantized model.** Download a GGUF from Hugging Face. Start small: `Llama-3.2-3B-Instruct-Q4_K_M.gguf` (~2 GB) or `Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` (~4.4 GB).
5. **Run a baseline test.** `./llama-cli -m model.gguf -p "Hello" -n 128 -t 6` — the `-t 6` pins threads to 6 of 8 cores, leaving headroom for the OS.
6. **Tune context and batch.** Use `-c 2048` (not the default 4096) to conserve KV cache memory. Increase only if you have headroom.
7. **Measure tokens/sec.** Watch the reported eval speed. If you're under ~3 tok/s, drop to a smaller quant (Q4_0 or Q3_K_M) or a smaller model.

### Recommended Settings by Model Size

- **3B Q4_K_M:** `-t 6 -c 4096` — fast, ~10–20 tok/s range depending on build tuning.
- **7B–8B Q4_K_M:** `-t 6 -c 2048` — the realistic daily driver.
- **13B Q4:** `-t 8 -c 1024` — expect sluggish output; use only for batch/offline tasks.

## Common Issues and What You Should Know

**Out-of-memory crashes mid-generation.** The KV cache grows with context. If you crash at token 800 of a 2048 context, your model + cache exceeded the pool. Halve `-c` and retry.

**Build fails on missing headers.** The FreeBSD-derived environment lacks some Linux-only headers. The PS5LM repo includes patches — apply them before building rather than chasing individual errors.

**GPU offload doesn't help (yet).** RDNA 2 acceleration in llama.cpp relies on ROCm/HIP paths that don't map cleanly to this environment. Treat CPU inference as the supported path in 2026 and watch the repo for backend work.

**It's not a ChatGPT replacement.** At 7B Q4 on CPU, you're getting a competent local assistant for summarization, code snippets, and offline Q&A — not frontier reasoning. Compare it to running the same GGUF on a Steam Deck (similar unified-memory constraints) rather than to a desktop RTX rig.

**Alternatives worth knowing:** If you want more headroom, a jailbroken PS4 Pro running Linux, a Steam Deck, or a mini-PC with 32 GB RAM will all beat the PS5 on flexibility. The PS5's appeal is novelty and raw memory bandwidth — not ecosystem maturity.

## Frequently Asked Questions (FAQ)

### Can llama.cpp run on a PS5 without a jailbreak?
No. Native execution requires the jailbreak to gain shell access and run unsigned binaries. There is no official Sony-sanctioned path, and updating firmware can close the exploit.

### What's the largest GGUF model a PS5 can run?
Practically, a 13B Q4 model at short context. 7B–8B Q4_K_M is the largest size that runs at comfortable speeds with usable context lengths given the ~10–13 GB usable unified memory.

### How fast is llama.cpp on PS5 in tokens per second?
Expect roughly 3–15 tok/s depending on model size, quantization, and thread tuning — CPU-bound, with no mature GPU backend in 2026.

### Is running an LLM on a jailbroken PS5 safe?
It carries the same risks as any jailbreak: potential instability, warranty voiding, and ban risk if you connect to PSN. Run it offline and keep a recovery path.

## Final Verdict

**Try it if you already have a jailbroken PS5 and enjoy tinkering** — the PS5LM project is a genuinely impressive proof of concept, and a 7B Q4 model at 2048 context is a fun, functional offline assistant. **Skip it if you want a practical daily local LLM** — a 32 GB mini-PC or Steam Deck will give you more memory headroom, better tooling, and no ban risk. Treat the PS5 build as a weekend experiment, not a production setup.