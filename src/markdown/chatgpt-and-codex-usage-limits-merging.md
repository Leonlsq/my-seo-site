---
title: "ChatGPT and Codex Usage Limits Merged: How to Fix 'Limit Reached"
description: "OpenAI merged ChatGPT and Codex usage limits. Learn how the new shared quota works, how to check remaining usage, and fixes for 'limit reached' errors."
pubDate: 2026-11-01
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## ChatGPT and Codex Now Share One Quota — Here's How to Stop Hitting the Wall

OpenAI has merged ChatGPT and Codex usage limits into a single shared quota, and the first thing most users notice is a "usage limit reached" error that appears out of nowhere — often mid-task in Codex, or right when they need ChatGPT for a quick question. The core takeaway: your Plus, Pro, Business, or Enterprise plan now draws from **one pool of usage** across both products, so heavy Codex sessions directly reduce the ChatGPT messages you have left (and vice versa). This guide explains exactly how the merged limits work, how to check your remaining usage, and the practical workarounds to stretch your quota without upgrading.

## How the Merged ChatGPT + Codex Usage Limits Actually Work

The change is documented in OpenAI's official help article on [understanding ChatGPT and Codex usage limits](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits). The short version of what changed:

| Before (Separate Limits) | After (Merged Limits) |
|---|---|
| ChatGPT message caps tracked separately | One shared usage pool per account |
| Codex tasks had their own allowance | Codex tasks consume from the same pool |
| Hitting one limit didn't affect the other | Exhausting the pool blocks **both** products |
| Limits reset on independent schedules | Unified reset window (rolling period) |

**What counts against your shared quota:**

- **ChatGPT:** messages on GPT-5-class models, file uploads, image generation, and Deep Research runs (these are the heaviest consumers).
- **Codex:** agent tasks, code review runs, and long autonomous sessions — each task can consume far more than a single chat message because the agent loops through multiple model calls.
- **Not counted (or counted minimally):** basic settings changes, viewing history, and lightweight model usage where applicable.

**Practical rule of thumb:** one medium Codex agent task ≈ 10–30 ChatGPT messages worth of quota, depending on how many files and iterations it touches. If you run Codex all morning, expect your ChatGPT allowance to look "drained" by lunch.

## Step-by-Step: Check Your Remaining Usage and Fix "Limit Reached" Errors

### Step 1: Find your current usage status
1. Open **ChatGPT** and click your profile icon (bottom-left on desktop, top-right on mobile).
2. Go to **Settings → Usage** (or check the plan/usage panel in the sidebar).
3. Note the reset time — this is now the **single reset window** for both ChatGPT and Codex.
4. In **Codex**, the usage indicator appears in the task panel; it reflects the same shared pool.

### Step 2: Diagnose which product is draining the pool
- **Codex-heavy days:** check your task history — long-running agent tasks with many file edits are the #1 quota killer.
- **ChatGPT-heavy days:** Deep Research, image generation, and long file analyses burn quota fastest.
- **Shared accounts (Business/Enterprise):** confirm whether your workspace admin has set per-member caps, which stack on top of the shared pool.

### Step 3: Apply the fixes
1. **Wait for the rolling reset** — the most reliable fix. Note the exact reset timestamp from Step 1.
2. **Switch to a lighter model** for routine questions (e.g., a mini/fast tier) to conserve the shared pool.
3. **Batch Codex work** into fewer, more specific tasks instead of many small exploratory runs — fewer agent loops means less quota consumed.
4. **Avoid Deep Research and image generation** until after your critical Codex tasks are done.
5. **Use API access separately** if you have it — API billing is independent of the ChatGPT/Codex subscription quota and won't drain your shared pool.

## Common Issues, Workarounds, and What You Should Know

**"My limit reset but Codex still says blocked."** Log out and back in, then refresh the Codex task panel. Cached usage indicators occasionally lag behind the actual reset by a few minutes.

**"I barely used ChatGPT but I'm out of messages."** This is the merged-limit trap. A single overnight Codex agent run can consume the equivalent of a full day of chat. Audit your Codex task history first.

**Workarounds that actually help:**
- **Split workflows by time:** run Codex tasks early, save ChatGPT Q&A for later in the same window.
- **Use Projects/Custom instructions** to reduce back-and-forth messages (fewer clarifying turns = less quota).
- **Team plans:** admins can allocate usage across members, so heavy Codex users don't starve everyone else.
- **Keep a local LLM or API fallback** for low-stakes queries so your subscription pool stays reserved for high-value work.

**Cost angle:** if you consistently hit the merged cap, compare upgrading your plan against paying per-token via the API for Codex-style automation. For heavy agent users, API billing is often more predictable than repeatedly upgrading a subscription tier.

## Frequently Asked Questions (FAQ)

### Did OpenAI really merge ChatGPT and Codex usage limits?
Yes. Per OpenAI's official help documentation, ChatGPT and Codex now draw from a single shared usage pool per account, so activity in one product reduces available usage in the other.

### Why am I hitting "usage limit reached" so much faster after the merge?
Because Codex agent tasks consume quota far faster than chat messages — each task can involve dozens of model calls. A single long Codex session can use the equivalent of a full day of ChatGPT messages, making the shared pool deplete quickly.

### When do the merged ChatGPT and Codex limits reset?
Limits reset on a unified rolling window rather than separate schedules. Check **Settings → Usage** in ChatGPT for your exact reset timestamp — it now applies to both products.

### Does using the OpenAI API count against my ChatGPT or Codex limits?
No. API usage is billed separately per token and does not draw from your ChatGPT/Codex subscription quota, making it a viable overflow strategy when you hit the shared cap.

## Final Verdict

The merged ChatGPT and Codex limits are here to stay, so the winning strategy is **quota discipline, not panic-upgrading**. Audit your Codex task history first — that's almost always where the quota goes. Batch agent runs, downgrade routine chats to lighter models, and keep an API key as your overflow valve. If you're a solo power user who runs Codex daily *and* relies on ChatGPT for research, the Pro tier is now genuinely easier to justify than it was under separate limits. Everyone else: check your usage panel, time your heavy tasks around the reset window, and you'll rarely see that "limit reached" wall again.