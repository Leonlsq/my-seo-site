---
title: "GPT-5.6 Sol Beats Factorio: How to Replicate the Run"
description: "Learn how GPT-5.6 Sol beat Factorio on peaceful mode, the exact prompts and settings used, and how to replicate the AI automation run yourself."
pubDate: 2026-11-01
tags: ['Tech', 'Guide', 'AI', 'Gaming']
---

## Can GPT-5.6 Sol Really Beat Factorio? The Setup Explained

Yes — according to Ryan Madden's write-up and the 187-comment Hacker News thread that followed, GPT-5.6 Sol completed a Factorio freeplay run on **peaceful mode**, meaning biters were disabled and the only win condition was launching a rocket. That distinction matters: peaceful mode removes combat, turret logistics, and pollution management, so the model only had to solve the production-chain puzzle. If you want to replicate the run or understand what it actually proves, this guide covers the exact configuration, the prompt scaffolding, and the failure points you'll hit.

The short takeaway: the model did not "play" Factorio in real time like a human. It operated through an agent loop that read game state via a bridge mod and issued commands as Lua or blueprint strings. Your results will depend almost entirely on how well you build that loop.

## Step-by-Step: Replicating the GPT-5.6 Sol Factorio Run

### 1. Set the correct map and difficulty parameters

Peaceful mode is not a single checkbox — it changes several generation values. Use these settings so your run is comparable:

| Setting | Value | Why it matters |
|---|---|---|
| Biters / bases | None (peaceful) | Removes all combat and repair logic |
| Pollution | Enabled (default) | Still affects evolution stats; keep it for parity |
| Starting area | Default | Larger areas trivialize early ore access |
| Map seed | Fixed (record yours) | Required for reproducible comparisons |
| Research queue | Enabled | Lets the agent plan multi-step tech trees |
| Cliff generation | Off (recommended) | Eliminates pathing edge cases the agent mishandles |

### 2. Install the state-bridge mod

The agent needs structured game state, not screenshots. Two approaches work:

1. **RCON + Lua bridge** — the agent sends `remote.call` commands and receives JSON dumps of inventories, crafting queues, and entity positions. Lowest latency, but you must serialize state yourself.
2. **Headless server with a REST shim** — run Factorio's headless binary and wrap the RCON socket in a small HTTP layer. Easier to debug, slightly slower.

Either way, expose at minimum: current inventory counts, available recipes, entity list with positions, and power network status.

### 3. Build the prompt scaffold

The run's success came from a **goal-decomposition loop**, not one giant prompt. Structure it as:

- **System prompt:** defines the win condition (launch one rocket), the tool schema, and the rule "never issue a command whose precondition you have not verified from state."
- **Planner step:** the model outputs a short ordered task list (e.g., "mine iron → smelt → automate red science").
- **Executor step:** one tool call per turn, with the resulting state diff fed back.
- **Verifier step:** a second model call that checks the diff against the expected outcome before the planner continues.

### 4. Cap the context and checkpoint aggressively

Long runs blow past context windows. Save a full state snapshot every N actions and summarize completed milestones into a compact "memory block" (e.g., "red science automated at tick 40k, 12 assemblers"). Feed the memory block, not the raw history, into new context windows.

### 5. Log every action for post-mortem

Record each tool call, the state before and after, and the verifier's verdict. Without this you cannot tell whether a failure was a bad plan or a bad tool schema — and the HN thread's most useful comments were people diagnosing exactly that.

## Common Failure Points and What the Run Actually Proves

- **Blueprint string parsing is the biggest trap.** Malformed strings fail silently; validate them against a schema before sending.
- **The agent over-builds early.** Models tend to over-provision miners and belts; add a hard cap per milestone.
- **Peaceful mode is doing a lot of the work.** Remove the combat constraint and the task becomes a deterministic logistics optimization — impressive, but not a general "beats the game" claim.
- **Cost and time.** A full run consumes a large number of tokens and hours of wall-clock time. Budget accordingly before attempting a replication.
- **No real-time reflex requirement.** Factorio is turn-friendly, which is why an agent loop works here at all.

## Frequently Asked Questions (FAQ)

### What does "peaceful mode" mean in Factorio?
Peaceful mode disables enemy expansion and combat pressure, so biters won't attack your factory. The win condition — launching a rocket — stays the same, but the difficulty drops sharply because you skip defense, ammo, and pollution management entirely.

### Did GPT-5.6 Sol play Factorio in real time?
No. It operated through an external agent loop that read game state via a mod or RCON bridge and issued commands turn by turn. The model planned and verified actions; it did not control a mouse or keyboard.

### Can I replicate the run with a different model?
Yes, in principle — the scaffolding matters more than the model. A weaker model will need more verifier steps and tighter milestone caps, but the bridge-mod and prompt-loop architecture is model-agnostic.

### Is beating Factorio on peaceful mode a fair benchmark?
It's a fair benchmark for **long-horizon planning and tool use**, but not for general game-playing ability. Peaceful mode removes the reactive, adversarial elements that make most games hard for AI agents.

## Final Verdict

If you want to test GPT-5.6 Sol yourself, start with the bridge mod and a fixed seed, then run a short red-science-only milestone before attempting a full rocket launch. The run is genuinely impressive as a planning benchmark — but treat "beats Factorio" as shorthand for "solves a deterministic logistics puzzle with good scaffolding," and you'll get far more useful signal out of your own replication attempts.