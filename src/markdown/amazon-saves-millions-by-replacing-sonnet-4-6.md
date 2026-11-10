---
title: "Strands Decider vs Sonnet 4.6: Cut AI Costs or Risk It?"
description: "Amazon saved millions swapping Sonnet 4.6 for Strands Decider. Learn how the routing model works, cost math, setup steps, and when it's worth it."
pubDate: 2026-11-10
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Strands Decider vs Sonnet 4.6: What Amazon Actually Changed (And Should You?)

Amazon reportedly saved millions of dollars by replacing direct calls to Sonnet 4.6 with a model-routing layer called **Strands Decider** — and if you run any production LLM workload, the headline alone should make you audit your own token bill. The direct takeaway: Strands Decider is not a better model than Sonnet 4.6. It's a **dispatcher** that decides *which* model (cheap, mid-tier, or frontier) handles each request, so you stop paying frontier prices for tasks a small model can nail. This guide breaks down how the routing pattern works, the cost math, a step-by-step setup, and the failure modes nobody mentions in the announcement thread.

## How Strands Decider Works: The Routing Architecture

The core idea is a **classifier-in-front-of-the-LLM** pattern. Instead of every prompt hitting Sonnet 4.6 at ~$3/$15 per million input/output tokens, a lightweight decider scores each request and routes it:

| Request Type | Routed To | Approx. Cost Tier | Example |
|---|---|---|---|
| Simple extraction, formatting, classification | Small model (e.g., Haiku-class) | ~$0.25/$1.25 per 1M tokens | "Extract the SKU from this email" |
| Multi-step reasoning, light code | Mid-tier model | ~$1/$5 per 1M tokens | "Summarize this support thread" |
| Complex agentic chains, long-context reasoning | Sonnet 4.6 (frontier) | ~$3/$15 per 1M tokens | "Debug this Terraform plan" |

**The savings math:** If 70% of your traffic is simple and you shift it from Sonnet-tier ($3/$15) to small-model tier ($0.25/$1.25), you cut blended cost by roughly **60–75%** — which is how "millions saved" at Amazon's scale becomes plausible. At 1 billion tokens/month of mixed traffic, that's the difference between ~$9,000 and ~$3,000 per month on input alone.

## Step-by-Step: Set Up Your Own Decider Layer

You don't need Amazon's internal tooling to replicate the pattern. Here's a working blueprint:

1. **Instrument first.** Log every prompt, response, token count, latency, and a quality score (human or LLM-as-judge). You cannot route what you haven't measured.
2. **Bucket your traffic.** Tag requests by task type: classification, extraction, summarization, code-gen, agentic multi-step. Most teams find 60–80% falls into the first three.
3. **Build the classifier.** Start with a cheap heuristic (prompt length, keyword match, presence of code blocks) before reaching for a model-based router. A 50-line rules engine often captures 80% of the savings.
4. **Add an escalation path.** Route low-confidence requests *up* to Sonnet 4.6. This is the critical safety valve — a decider that never escalates will silently degrade quality.
5. **A/B test quality.** Run shadow traffic: send 5–10% of requests to both the routed model and Sonnet 4.6, and diff outputs. Set a quality floor (e.g., 95% semantic match) before full rollout.
6. **Monitor drift.** Re-evaluate monthly. Prompt distributions shift, and a decider tuned in January can be misrouting by March.

## Common Issues, Cost Traps, and What You Should Know

- **The classifier isn't free.** Your decider adds latency (typically 20–100ms) and its own token cost. Budget for it — it's usually worth it, but not always.
- **Quality regressions are silent.** Unlike an outage, a bad route just produces slightly worse answers. You need evals in CI, not just uptime monitoring.
- **Agentic loops break routing.** Multi-turn agents that call tools repeatedly can ping-pong between models, inflating cost. Pin the model for the duration of an agent session.
- **Vendor lock-in risk.** If Strands Decider is tied to one provider's model catalog, you lose the ability to swap in a cheaper competitor. Keep the router provider-agnostic.
- **The HN thread's real concern:** commenters on the discussion (103 points, 24 comments) questioned whether "saved millions" accounts for the engineering cost of building and maintaining the routing layer. Valid — the pattern pays off above roughly **$50k/month in LLM spend**; below that, a simple two-tier heuristic is enough.

**Alternatives to consider:** LiteLLM proxy routing, OpenRouter's model fallback, or a custom semantic-router library. All achieve the same 50–70% cost reduction without a bespoke build.

## Frequently Asked Questions (FAQ)

### What is Strands Decider and how does it differ from Sonnet 4.6?
Strands Decider is a routing layer that classifies each request and sends it to the cheapest model capable of handling it, escalating to Sonnet 4.6 only for complex tasks. Sonnet 4.6 is a single frontier model used for everything.

### How much can model routing actually save on LLM costs?
Teams typically see **50–75% cost reduction** when 60–80% of traffic is simple. Savings scale with volume; below ~$50k/month in spend, the engineering overhead may outweigh the benefit.

### Is Strands Decider open source or available to the public?
The pattern is replicable with open tools like LiteLLM and OpenRouter. Check the Strands Agents blog for current availability of the official implementation.

## Final Verdict

**Replicate the pattern, don't chase the specific tool.** If you're spending more than $10k/month on a single frontier model, build a two-tier router this quarter — cheap model first, Sonnet 4.6 as escalation. Measure quality with shadow traffic before you flip the switch. Amazon's savings are real, but they came from disciplined instrumentation and evals, not from a magic drop-in replacement. Start with logging, not routing.