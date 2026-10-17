---
title: "Invent Transformers From Memory: The Associative Memory Trick"
description: "Learn how to derive the transformer architecture from associative memory first principles. A step-by-step mental model guide for ML engineers and students."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Actually Derive Transformers From Memory (Not Just Memorize the Diagram)

Alex Wang's essay "You could have invented transformers from memory" (currently trending on Hacker News with 390+ points and 91 comments) makes a deceptively simple claim: if you understand **associative memory** — the idea that a system stores key–value pairs and retrieves a value by matching a query against keys — then the transformer block is not a magic architecture you memorize. It is the *only* reasonable thing you could build.

This guide turns that insight into a **reproducible mental derivation**. Instead of memorizing `Q @ K.T / sqrt(d) @ V`, you will rebuild the entire attention mechanism step by step, so you can whiteboard it in an interview, explain it in a paper review, or debug a model without a reference sheet. By the end you will be able to answer "why the square root of d?" and "why residual connections?" from first principles, not recall.

## Step-by-Step: Deriving Attention From Associative Memory

The core premise: a neural network needs a way to **look things up**. Classic feedforward layers cannot route information based on content — they apply the same weights everywhere. Associative memory fixes that. Here is the derivation chain.

1. **Start with a lookup table.** You have stored memories as key–value pairs `(k_i, v_i)`. Given a query `q`, you want to return the value whose key is most similar to `q`. The cleanest similarity measure is a dot product: `score_i = q · k_i`.

2. **Turn scores into a soft selection.** A hard `argmax` is non-differentiable. Instead, exponentiate and normalize: `weight_i = exp(q · k_i) / Σ_j exp(q · k_j)`. That is exactly **softmax attention**. You did not need to know the word "attention" — you needed a differentiable lookup.

3. **Batch it as matrices.** Stack keys into rows of `K` and values into rows of `V`. The lookup becomes `softmax(q Kᵀ) V`. Add multiple queries as rows of `Q` and you get the canonical `softmax(QKᵀ) V`. **This is the whole mechanism.** Everything else is engineering.

4. **Fix the exploding scores.** Dot products of `d`-dimensional random vectors have variance scaling with `d`, which saturates the softmax and kills gradients. Dividing by `sqrt(d_k)` rescales variance back to ~1. This is why the scale factor exists — it is a numerical stability fix, not a design flourish.

5. **Add multiple "memory banks" (heads).** One lookup table forces every query to compete over the same keys. Split `d_model` into `h` heads of size `d_k = d_model / h`, run attention in parallel, and concatenate. Different heads learn different associative structures (syntax, coreference, positional patterns).

6. **Make it order-aware.** Pure dot-product lookup is permutation-invariant — "dog bites man" and "man bites dog" look identical. Inject position via sinusoidal encodings or RoPE so keys carry location information.

7. **Wrap it for depth.** Attention alone is a linear mixer. Add a position-wise feedforward MLP for per-token nonlinearity, plus **residual connections** (so gradients flow and the block can learn an identity) and **LayerNorm** (so activations stay in a stable range across layers). Stack `N` of these blocks.

If you can recite those seven steps, you have reconstructed the transformer from memory — no diagram required.

## Common Pitfalls and What You Should Know

Even engineers who "know" attention get these wrong when deriving from scratch:

| Pitfall | Why it happens | The fix |
|---|---|---|
| Forgetting `sqrt(d_k)` | Looks cosmetic | It controls softmax temperature; without it, gradients vanish for large `d` |
| Confusing Q/K/V roles | All three are learned projections | Q = what you're looking for; K = how memories are indexed; V = the content returned |
| Assuming attention is nonlinear | Softmax is nonlinear, but the mixing is a weighted average | The nonlinearity that does the heavy lifting lives in the FFN |
| Skipping residuals | Blocks "work" without them on toy data | Deep stacks fail to train; residuals are load-bearing |
| Ignoring causal masking | Training on full sequences leaks the future | Mask `i > j` scores to `-inf` before softmax for autoregressive models |

**Information gain worth internalizing:** the "associative memory" framing is not just pedagogy — it is how modern retrieval-augmented and memory-augmented models (and even KV-cache mechanics) actually behave. When you understand attention as a differentiable dictionary lookup, KV-caching becomes obvious: you store the `K` and `V` of past tokens so you don't recompute them. That single insight explains a huge chunk of inference-time optimization.

**Alternatives to the mental model:** some people prefer deriving attention from **kernel smoothing** (Nadaraya–Watson regression) or from **graph message passing**. Both are valid and converge on the same equation — pick whichever clicks, but the associative-memory route is the shortest path from "lookup table" to "transformer block."

## Frequently Asked Questions (FAQ)

### Can you really derive transformers from memory without a reference?
Yes — if you anchor on associative memory. The chain is: lookup table → softmax → matrix form → scale → multi-head → positional encoding → residual/FFN/LayerNorm wrapper. Each step is forced by a concrete problem (differentiability, numerical stability, permutation invariance, trainability), so you reconstruct rather than recall.

### Why divide attention scores by the square root of d_k?
Because the dot product of two `d_k`-dimensional vectors has variance proportional to `d_k`. Without scaling, large `d_k` pushes softmax inputs into saturation, producing near-one-hot weights and vanishing gradients. Dividing by `sqrt(d_k)` normalizes the variance to roughly 1.

### Is the associative memory explanation of attention officially correct?
It is a faithful and widely used interpretation. Attention computes a soft, content-based weighted average of values keyed by query–key similarity — precisely a differentiable associative memory read. It does not replace the math, but it explains *why* the math takes that form.

### Do I need to know linear algebra to follow this derivation?
You need dot products, matrix multiplication, and a working sense of softmax. You do **not** need advanced proofs. If you can multiply a `3×4` by a `4×2` matrix and explain what a weighted average is, you can follow every step above.

## Final Verdict

Stop memorizing the transformer diagram. Start from a lookup table, force differentiability with softmax, batch it into matrices, stabilize it with `sqrt(d_k)`, parallelize with heads, inject position, and wrap it for depth — and you will have *invented* the architecture on a whiteboard. Read Alex Wang's original post for the full narrative, then test yourself: can you derive the block in under ten minutes with no notes? If yes, you genuinely understand transformers. If not, redo steps 1–7 until the derivation is muscle memory — it is the single highest-leverage mental model in modern ML.