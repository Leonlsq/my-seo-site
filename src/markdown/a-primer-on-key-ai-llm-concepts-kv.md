---
title: "KV Cache, Weights & Quantization: LLM Inference Explained Simply"
description: "Confused by LLM jargon? Learn how KV cache, weights, and quantization actually work in AI inference, plus how to cut VRAM use and boost tokens/sec."
pubDate: 2026-11-02
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## LLM Inference Explained: What Actually Happens When You Type a Prompt

Every time you hit "send" in ChatGPT, Claude, or a local Llama install, your GPU runs through a predictable pipeline: **tokenize → embed → run weights → build a KV cache → sample the next token → repeat.** The confusion most people hit is that the words "weights," "KV cache," and "quantization" get thrown around as if they're the same thing. They aren't. Weights are the model's learned knowledge (static). The KV cache is a runtime memory buffer (dynamic). Quantization is a compression technique applied to both. Get these three straight and you can actually diagnose why your local model is running out of VRAM, why tokens/sec drops on long chats, or why a 4-bit model sounds dumber than the 8-bit one.

This guide breaks down each concept with concrete numbers, then shows you how to tune them for real hardware.

## The Three Pillars: Weights vs. KV Cache vs. Quantization

| Concept | What It Is | Stored Where | Grows During Chat? | Typical Size (7B model) |
|---|---|---|---|---|
| **Weights** | Learned parameters (the "brain") | Disk → VRAM | No (fixed) | ~14 GB (FP16), ~4 GB (4-bit) |
| **KV Cache** | Cached attention keys/values per token | VRAM | **Yes** (per token) | ~0.5 MB/token (FP16, 32 layers) |
| **Quantization** | Reducing numeric precision (FP16→INT4) | Applied to weights/KV | N/A | 4x memory reduction at 4-bit |

### 1. Weights — the model's fixed knowledge
Weights are the billions of numbers learned during training. A 7B model has ~7 billion parameters. At FP16 (2 bytes each), that's **~14 GB just to load**. This is why a 7B model won't fit on an 8 GB GPU at full precision — the weights alone overflow it.

### 2. KV Cache — the memory that grows with your conversation
During inference, the model processes your prompt (the "prefill" phase), then generates tokens one at a time (the "decode" phase). To avoid recomputing attention over the entire conversation for every new token, it caches the Key and Value tensors for every token already seen. That cache **grows linearly with context length**.

Rough formula for KV cache size:
```
KV bytes = 2 (K and V) × layers × heads × head_dim × bytes_per_value × tokens
```
For a 7B model (32 layers, 4096 hidden dim) at FP16, that's roughly **0.5 MB per token**. A 4,000-token chat ≈ **2 GB of VRAM** consumed by cache alone. Push to 32K context and you're looking at ~16 GB — often more than the weights.

### 3. Quantization — the compression lever
Quantization stores weights (and sometimes the KV cache) at lower precision:
- **FP16** — baseline, 2 bytes/param
- **INT8** — 1 byte/param, ~2x smaller, near-lossless
- **INT4 (GPTQ/AWQ/GGUF Q4)** — 0.5 bytes/param, ~4x smaller, minor quality loss

A 7B model goes from **14 GB (FP16) → 7 GB (INT8) → ~4 GB (INT4)**. This is the single biggest lever for running models on consumer GPUs.

## How to Tune These for Your Hardware (Step-by-Step)

1. **Check your VRAM budget.** `nvidia-smi` (Linux) or Task Manager → Performance → GPU (Windows). Leave ~1 GB headroom for the OS/display.
2. **Pick a quantization that fits weights.** 8 GB GPU → use a 7B at Q4_K_M (~4.5 GB) or Q5 (~5.5 GB). 24 GB GPU → 13B at Q5 or 7B at FP16.
3. **Cap context length to control KV cache.** In llama.cpp set `-c 4096` instead of default 32K. In Ollama, edit `num_ctx` in the Modelfile. Every 1K tokens ≈ 0.5 GB at FP16.
4. **Enable KV cache quantization if supported.** llama.cpp flags `--cache-type-k q8_0 --cache-type-v q8_0` halve KV memory with negligible quality loss.
5. **Use Flash Attention.** Add `-fa` in llama.cpp or enable in vLLM — cuts KV memory overhead and speeds decode.
6. **Batch carefully.** Larger batch sizes multiply KV cache memory; on single-user local setups, keep batch = 1.

## Common Issues, Alternatives, and What You Should Know

- **"My model loads but crashes mid-chat."** Classic KV cache overflow. You fit the weights but not the growing cache. Lower `num_ctx` or quantize the KV cache.
- **"Q4 model gives worse answers."** Expected at aggressive quantization (Q2/Q3). Stick to **Q4_K_M or higher** for quality-sensitive work; Q5/Q6 are near-lossless.
- **"Tokens/sec tanks on long prompts."** Prefill is compute-bound and slow on long context; decode is memory-bandwidth-bound. KV cache quantization helps the latter.
- **Cost angle:** On cloud GPUs (A100 80GB ≈ $2–3/hr), shrinking weights via INT8 lets you run larger models or more concurrent users per dollar — quantization is a direct cost lever.
- **Alternatives to brute-force VRAM:** PagedAttention (vLLM) and grouped-query attention (GQA) in modern models dramatically shrink KV cache — prefer GQA models (Llama 3, Mistral) for long-context work.

## Frequently Asked Questions (FAQ)

### What is the difference between model weights and the KV cache?
Weights are the fixed trained parameters loaded once from disk. The KV cache is a temporary runtime buffer that stores attention keys/values for every token processed, and it grows with conversation length.

### Does quantization affect the KV cache or just the weights?
Most quantization tools (GPTQ, AWQ, GGUF) target **weights**. KV cache quantization is a separate option (e.g., `--cache-type-k q8_0` in llama.cpp) and must be enabled independently.

### How much VRAM do I need to run a 7B model?
At Q4 you need ~4.5 GB for weights plus 1–2 GB for KV cache and overhead — plan for **8 GB total** for comfortable 4K-context chats. FP16 needs ~14 GB plus cache.

### Why does my LLM slow down as the conversation gets longer?
Each new token attends over the full KV cache, so decode cost and memory scale with context length. Longer chats = bigger cache = slower generation and higher VRAM use.

## Final Verdict

If you're running local LLMs, **quantize the weights to Q4_K_M first, then cap your context length, then quantize the KV cache** — in that order. That sequence solves 90% of "out of memory" and "why is it so slow" complaints on consumer GPUs. Weights are your fixed cost, the KV cache is your variable cost, and quantization is the dial you turn to make both fit. Master those three and every other LLM term — attention, prefill, decode, tokens/sec — falls into place.