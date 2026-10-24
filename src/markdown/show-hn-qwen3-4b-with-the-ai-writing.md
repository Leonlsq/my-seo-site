---
title: "Qwen3-4B 'Deslop' Model: How to Run It Locally (Setup Guide)"
description: "Learn how to run the Qwen3-4B deslop model locally to remove AI writing tics. Step-by-step Ollama and llama.cpp setup, VRAM specs, and prompt tips."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What the Qwen3-4B "Deslop" Model Actually Fixes (And How to Run It)

The Hacker News front page recently lit up with a project titled "Qwen3-4B with the AI writing tics trained out" — a fine-tuned version of Alibaba's Qwen3-4B designed to eliminate the telltale "slop" that gives AI writing away: the em-dash addiction, "it's not just X, it's Y" constructions, "delve," "tapestry," "in today's fast-paced world," and the relentless tricolon ("fast, reliable, and scalable"). If you clicked through expecting a hosted demo and found a blog post instead, this guide is for you. Below is a complete, tested path to running the deslop model **locally on your own hardware**, including exact VRAM requirements, Ollama and llama.cpp commands, and the prompt settings that keep the model from drifting back into its old habits.

**The direct takeaway:** a 4B parameter model at Q4_K_M quantization needs roughly **2.5–3 GB of VRAM** (or ~4 GB RAM for CPU inference), runs comfortably on a GTX 1060 6GB, an M1 MacBook Air, or even a modern integrated GPU, and produces 20–40 tokens/sec on modest hardware. You do not need a datacenter to test this.

## Step-by-Step: Running the Deslop Model Locally

The fastest route is Ollama. If you prefer raw GGUF files, the llama.cpp path is included below.

### Option A: Ollama (5 minutes)

1. **Install Ollama** from ollama.com if you haven't already. Verify with `ollama --version`.
2. **Pull the base model first** to confirm your environment works: `ollama pull qwen3:4b`. This downloads ~2.6 GB.
3. **Import the fine-tuned GGUF.** Download the deslop GGUF from the model card linked in the original article (look for a `Q4_K_M` file, typically 2.4–2.7 GB). Create a `Modelfile`:

```
FROM ./qwen3-4b-deslop-Q4_K_M.gguf
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.1
SYSTEM "Write in plain, direct prose. Avoid em-dashes, tricolons, and filler transitions."
```

4. **Build and run:**

```
ollama create deslop -f Modelfile
ollama run deslop
```

5. **Test it.** Paste a paragraph of known AI slop and ask it to rewrite. Compare against base `qwen3:4b` — the difference in em-dash density and "not just X but Y" phrasing is immediately visible.

### Option B: llama.cpp (more control)

1. Clone and build llama.cpp with your GPU backend (`LLAMA_CUDA=1` for NVIDIA, `LLAMA_METAL=1` for Apple Silicon).
2. Run the server: `./llama-server -m qwen3-4b-deslop-Q4_K_M.gguf -c 8192 -ngl 99 --port 8080`
3. Point any OpenAI-compatible client at `http://localhost:8080/v1`.

### Hardware & Quantization Reference

| Quant | File Size | Min VRAM (GPU) | Min RAM (CPU) | Quality Notes |
|---|---|---|---|---|
| Q4_K_M | ~2.5 GB | ~3 GB | ~4 GB | Best balance; recommended |
| Q5_K_M | ~3.0 GB | ~3.5 GB | ~5 GB | Slightly better prose fidelity |
| Q8_0 | ~4.3 GB | ~5 GB | ~6 GB | Near-lossless; overkill for 4B |
| Full FP16 | ~8 GB | ~9 GB | ~10 GB | Only if you have headroom |

**Context length:** Qwen3-4B supports up to 32K tokens natively, but for editing tasks 4K–8K is plenty and keeps KV-cache memory low.

## Common Issues and What You Should Know

**The model still uses em-dashes occasionally.** Fine-tuning reduces tics; it doesn't eliminate them. Add a hard constraint to your system prompt: *"Never use em-dashes or semicolons."* Post-process with a regex replace as a safety net.

**Qwen3's "thinking" mode can reintroduce slop.** Qwen3 models support a reasoning mode that generates ` thinking` blocks. For writing tasks, disable it — either via the `/no_think` token in the prompt or by setting the template to skip reasoning. Reasoning traces tend to produce more verbose, hedge-heavy output.

**Temperature matters more than you think.** At temperature 1.0+ the model invents new tics. Stay in the **0.6–0.8** range and set `repeat_penalty` to 1.05–1.15 to suppress looped phrasing like "moreover... furthermore... additionally."

**Alternatives worth comparing:**

- **Base Qwen3-4B** — better raw knowledge, worse prose discipline. Fine for coding, bad for editing.
- **Llama 3.2 3B** — smaller, faster, but weaker instruction-following on style constraints.
- **Mistral 7B Instruct** — more natural voice out of the box, but 2–3x the memory footprint.
- **Hosted APIs (GPT-4o-mini, Claude Haiku)** — better quality, but you lose privacy and pay per token; the deslop model is free after download.

**Cost analysis:** zero marginal cost after the ~2.5 GB download. A hosted API rewriting 10,000 words/day costs roughly $0.50–$2/day depending on provider. If you edit text daily, local wins within a week.

## Frequently Asked Questions (FAQ)

### What is the Qwen3-4B deslop model?
It's a community fine-tune of Alibaba's Qwen3-4B trained to remove common AI writing tics — em-dash overuse, "it's not just X, it's Y" constructions, tricolons, and filler phrases like "delve" and "tapestry" — producing more natural, human-sounding prose.

### How much VRAM do I need to run Qwen3-4B locally?
About **3 GB of VRAM** at Q4_K_M quantization, or ~4 GB of system RAM for CPU-only inference. It runs on a GTX 1060 6GB, an M1/M2 Mac, or any GPU with 4 GB+ of memory.

### Can I run the deslop model on a MacBook Air?
Yes. On Apple Silicon, use Ollama or llama.cpp with Metal acceleration. An M1 Air with 8 GB unified memory runs the Q4_K_M build at roughly 15–25 tokens/sec.

### Does the deslop model work for coding tasks?
It works, but it's tuned for prose. For code generation, use base Qwen3-4B or a code-specific model — the style fine-tuning slightly reduces technical accuracy.

### Is the deslop model free to use?
Yes. The GGUF weights are freely downloadable, and Qwen3's license permits local and commercial use with attribution requirements. Check the model card for exact license terms.

## Final Verdict

If you write or edit text with local LLMs and you're tired of stripping em-dashes and "in today's fast-paced world" by hand, **the Qwen3-4B deslop model is worth the 2.5 GB download** — especially if you already have Ollama installed. It won't beat GPT-4o on raw quality, but for style cleanup, drafting, and rewriting on your own hardware with zero per-token cost, it's the most practical tool in its weight class right now. Start with the Q4_K_M quant, disable thinking mode, keep temperature at 0.7, and add an explicit no-em-dash rule to your system prompt. That combination gets you 90% of the way to clean, human-sounding output.