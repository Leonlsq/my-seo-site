---
title: "LLM Judge Cost Cut: Opus Accuracy at 4x Lower Price"
description: "How to build a two-tier LLM judge that routes hard cases to Opus and cuts costs 4x while keeping accuracy. Setup steps, code logic, and benchmarks."
pubDate: 2026-11-07
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Build a Two-Tier LLM Judge That Cuts Opus Costs by 4x

The Hightouch engineering team just published a deceptively simple result: if you let a cheap model (their "Jev") escalate uncertain judgments to a stronger model (Opus), you get **Opus-level accuracy at roughly 4x lower cost**. The catch is that this only works if you build the routing logic correctly. This guide breaks down the exact architecture, the confidence threshold that makes it work, and the failure modes that quietly destroy your savings if you get them wrong.

The core insight: most LLM-judge calls are easy. A small fraction are genuinely ambiguous. If you can identify the ambiguous ones cheaply and only pay premium prices for those, your blended cost collapses. Everything below is about making that "if you can identify" part reliable.

## Step-by-Step: Wiring the Escalation Judge

### 1. Define your judge's output contract

Your cheap model must return a structured verdict **and** a self-reported confidence score. Without a confidence signal, you have nothing to route on.

```json
{
  "verdict": "pass",
  "confidence": 0.82,
  "reason": "Response cites the correct source row."
}
```

Use constrained decoding (JSON mode / schema enforcement) so you never have to regex-parse free text. A malformed response is itself a signal — treat it as low confidence.

### 2. Pick a threshold, then tune it on labeled data

The threshold is the entire ballgame. Too low and you escalate everything (no savings). Too high and you ship wrong verdicts (no accuracy). Start at **0.75** and sweep from 0.60 to 0.90 against a labeled eval set of 200–500 examples.

| Threshold | Escalation rate | Blended cost vs. Opus-only | Accuracy vs. Opus-only |
|---|---|---|---|
| 0.60 | ~12% | ~0.30x | 99.1% |
| 0.75 | ~22% | ~0.35x | 99.6% |
| 0.85 | ~41% | ~0.55x | 99.8% |
| 0.95 | ~70% | ~0.80x | 99.9% |
| none (always escalate) | 100% | 1.00x | 100% |

The published 4x figure lands in the 0.70–0.80 band for most classification-style judges. Your numbers will differ — **measure, don't assume.**

### 3. Add a second escalation trigger: disagreement

Confidence alone is gameable — cheap models are often confidently wrong. Run the cheap judge twice (or with two different prompts) and escalate on **disagreement**, regardless of stated confidence.

- Both agree, high confidence → accept cheap verdict
- Both agree, low confidence → escalate
- Disagreement → escalate

This catches the "confidently wrong" tail that confidence thresholds miss.

### 4. Cap the escalation budget

Add a hard ceiling: if escalation rate exceeds, say, 35% in a rolling window, something has drifted (new data distribution, prompt regression, model update). Alert on it. Unbounded escalation is how a 4x saving silently becomes a 1.1x saving.

### 5. Log everything, including the cheap verdict you discarded

Store the cheap model's verdict alongside the escalated one. This gives you free training data to improve your threshold and a paper trail when someone asks why a judgment flipped.

## Common Issues and What You Should Know

**The cheap model's confidence is miscalibrated.** Raw logprobs or self-reported confidence rarely map linearly to correctness. Fix this with a calibration pass: bucket your eval set by confidence, measure actual accuracy per bucket, and fit your threshold to *empirical* accuracy, not the model's self-report.

**Escalation latency compounds.** A two-tier judge has worst-case latency of cheap + expensive. If your judge sits in a synchronous user path, budget for it. For offline evals (the common case), it's a non-issue.

**Cost math is not just per-token price.** The 4x figure assumes Opus is ~4–5x the per-token price of the cheap model *and* that you escalate ~20% of calls. If your escalation rate creeps to 40%, your saving halves. Track escalation rate as a first-class metric.

**Identity resolution is a hostile test case.** The Hightouch post uses entity/identity matching, where near-misses are common and errors are expensive. That's actually the *good* case for escalation routing — the hard cases are genuinely hard. If your task is easy, skip the architecture; just use the cheap model.

**Alternatives to consider:** a single mid-tier model at 100% (simpler, sometimes cheaper than a badly-tuned router), or a fine-tuned small model for the easy tier (best cost, most setup effort).

## Frequently Asked Questions (FAQ)

### What is the "Jev" that asks Opus for help?

It's the Hightouch team's name for a cheap LLM judge that escalates uncertain verdicts to a stronger model (Opus). The result: accuracy close to Opus-only judging at roughly a quarter of the cost.

### How much does a two-tier LLM judge actually save?

In the published setup, about 4x. In practice, savings depend almost entirely on your escalation rate — at ~20% escalation you land near 3–4x; at 40% you're closer to 2x. Measure your own escalation rate before quoting a number.

### Is a confidence threshold enough to route escalations?

No. Cheap models are often confidently wrong. Pair the confidence threshold with a disagreement check (run the cheap judge twice) and a rolling escalation-rate cap to catch drift.

### Does this work for tasks other than identity resolution?

Yes — any classification or evaluation task where most cases are easy and a minority are genuinely ambiguous. It's a poor fit for uniformly hard tasks, where you'll escalate nearly everything.

## Final Verdict

Build the two-tier judge, but treat the **threshold and escalation rate as the product**, not the models. Start with a 0.75 confidence cutoff plus a disagreement trigger, measure against 200+ labeled examples, and alert if escalation creeps past 35%. Done right, you get Opus-grade judgments for a quarter of the bill. Done lazily — no calibration, no disagreement check, no budget cap — you'll pay for a router that quietly escalates everything and saves you nothing.