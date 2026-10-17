---
title: "LFM2.5-24B-A2B: Run Fast On-Device AI Agents (Setup Guide)"
description: "Learn how to run LFM2.5-24B-A2B locally for fast on-device AI agents. Step-by-step setup, VRAM requirements, benchmarks, and alternatives compared."
pubDate: 2026-10-15
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## LFM2.5-24B-A2B Explained: How to Run Fast On-Device AI Agents Locally

Liquid AI's **LFM2.5-24B-A2B** is a Mixture-of-Experts (MoE) model built specifically for **fast on-device agents** — think autonomous tool-calling, browser control, and multi-step reasoning running on your own laptop or workstation instead of a cloud API. The "A2B" in the name signals **~2B active parameters** per token out of a 24B total, which is the key to its speed. This guide skips the press-release fluff and shows you how to actually download, configure, and benchmark it — plus whether your hardware can handle it.

If you searched for "how to run LFM2.5-24B-A2B locally" or "LFM2.5 VRAM requirements," you're in the right place. Below is a practical, copy-paste setup path.

## LFM2.5-24B-A2B Specs and Hardware Requirements

Before you download anything, confirm your machine can run it. Because it's an MoE model, memory needs are driven by **total** parameters (24B), not active ones.

| Component | Minimum | Recommended | Ideal (Agent Workloads) |
|---|---|---|---|
| GPU VRAM (Q4 quant) | 14 GB | 16–24 GB | 32 GB+ |
| GPU VRAM (FP16) | 48 GB | 48 GB | 80 GB (A100/H100) |
| System RAM | 32 GB | 64 GB | 128 GB |
| CPU | 8-core modern | 12-core+ | Apple M-series / Ryzen 9 |
| Storage | 15 GB free | 30 GB SSD | NVMe SSD |
| OS | Linux, macOS, Windows (WSL2) | Ubuntu 22.04+ | Ubuntu 24.04 |

**Key takeaway:** A single RTX 4090 (24 GB) or an Apple M3/M4 Max with 36–64 GB unified memory is the sweet spot for quantized local inference.

## Step-by-Step: Running LFM2.5-24B-A2B Locally

### 1. Install the runtime (llama.cpp or vLLM)

For on-device agents, **llama.cpp** is the fastest path on consumer hardware:

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON   # use -DGGML_METAL=ON for Apple Silicon
cmake --build build --config Release -j
```

For server-style throughput with batching, use **vLLM** instead:

```bash
pip install vllm
```

### 2. Download the GGUF quant

Grab a **Q4_K_M** quant for the best speed/quality tradeoff on 16–24 GB GPUs. Q5_K_M if you have 24 GB+ and want higher fidelity.

### 3. Launch the model

```bash
./build/bin/llama-server \
  -m lfm2.5-24b-a2b-Q4_K_M.gguf \
  -c 32768 \
  -ngl 99 \
  --host 0.0.0.0 --port 8080
```

- `-c 32768` sets a 32K context (agents need long context for tool traces).
- `-ngl 99` offloads all layers to GPU.
- The server exposes an **OpenAI-compatible API** at `http://localhost:8080/v1`.

### 4. Wire up your agent framework

Point any OpenAI-compatible agent (LangChain, LlamaIndex, OpenHands, or a custom tool-caller) at the local endpoint:

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8080/v1", api_key="local")
resp = client.chat.completions.create(
    model="lfm2.5-24b-a2b",
    messages=[{"role": "user", "content": "Book the cheapest flight to Tokyo next Friday."}],
    tools=[...]  # your tool schema
)
```

### 5. Tune for agent latency

- Set `--flash-attn` to cut KV-cache memory and speed up long contexts.
- Use **Q4_K_M + flash attention** to fit 32K context on a 24 GB card.
- Keep `--parallel 1` unless you're serving multiple agents.

## Common Issues and What You Should Know

**Issue 1: Out-of-memory on a 16 GB GPU.** Drop to Q3_K_M or reduce context to 16K. MoE models still load all experts into VRAM.

**Issue 2: Slow first token.** This is normal — MoE routing adds overhead. Warm the model with a dummy prompt before real agent calls.

**Issue 3: Tool-calling format errors.** LFM2.5 uses a specific chat template. Verify the GGUF's embedded template matches your framework, or pass `--chat-template` explicitly.

### LFM2.5-24B-A2B vs Alternatives

| Model | Active Params | Local Agent Speed | Best For |
|---|---|---|---|
| **LFM2.5-24B-A2B** | ~2B | Very fast | On-device tool-calling |
| Qwen2.5-32B | 32B | Slow locally | Max quality, cloud |
| Llama 3.1 8B | 8B | Fast | Lightweight agents |
| Mistral Small 24B | 24B | Medium | Balanced general use |

The A2B's edge is **latency per agent step** — critical when your agent makes 10+ tool calls per task.

## Frequently Asked Questions (FAQ)

### Can I run LFM2.5-24B-A2B on a MacBook?
Yes. An M3/M4 Max with 36 GB+ unified memory runs the Q4 quant comfortably via llama.cpp with Metal. Expect usable agent speeds, though slower than a dedicated 4090.

### How much VRAM does LFM2.5-24B-A2B need?
About **14–16 GB** for Q4_K_M at 32K context, and **~48 GB** for full FP16. Quantization is essential for consumer GPUs.

### Is LFM2.5-24B-A2B free to use?
The weights are openly downloadable, but check Liquid AI's license for commercial agent deployment terms before shipping a product.

### What makes it "built for on-device agents"?
Its ~2B active parameters keep per-token latency low, and it's tuned for reliable tool-calling and multi-step reasoning — the two things agents do most.

## Final Verdict

If you're building **local AI agents** and your bottleneck is latency, LFM2.5-24B-A2B is worth installing today — especially on a 24 GB GPU or Apple Silicon Mac. Start with the **Q4_K_M GGUF + llama.cpp**, get tool-calling working, then benchmark against Qwen2.5-32B if you need more raw reasoning. For cloud-scale throughput, skip it and use vLLM on an A100. For everyone else: this is one of the best on-device agent models you can run right now.