---
title: "MIT's 13 AI Agents on an Island: Replicate It Yourself"
description: "How to run MIT's Project Sid-style AI agent sandbox locally: setup, config, GPU needs, and fixes for idle agents that stop playing."
pubDate: 2026-10-24
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Replicate MIT's "13 AIs on an Island" Experiment (Local Setup Guide)

When MIT researchers marooned 13 AI agents on a virtual island with nothing to do, the agents invented games, held a funeral for a lost ring, and — most importantly — got measurably better at their assigned jobs. If you heard that story and immediately thought "I want to run that," this guide is for you. Below is a concrete, hardware-aware walkthrough for building your own multi-agent sandbox using open-source frameworks (Project Sid-style architectures, Generative Agents, and Concordia), plus fixes for the most common failure: **agents that sit idle and do nothing**.

## What You Actually Need (Specs & Stack)

The MIT/Project Sid work ran on a Minecraft-based simulation with 10–1,000+ agents. You don't need a cluster to reproduce the *behavior* — you need the right stack and realistic expectations.

| Component | Minimum | Recommended | Notes |
|---|---|---|---|
| GPU VRAM | 8 GB | 24 GB (RTX 3090/4090) | For local 7B–13B models |
| System RAM | 16 GB | 32 GB | Agent memory grows fast |
| LLM backend | API (GPT-4o-mini) | Local vLLM + Llama 3.1 8B | API is cheaper to start |
| Framework | Concordia / Generative Agents repo | + custom game loop | Concordia is MIT's own |
| Simulation | Text grid | Minecraft (Mineflayer) | Text grid is 10x easier |
| Storage | 20 GB | 100 GB SSD | Logs + vector memory |

**Cost reality check:** Running 13 agents on GPT-4o-mini for 24 simulated hours costs roughly $3–$8 in tokens. Running the same on a local 3090 costs ~$0.40 in electricity. Start with the API.

## Step-by-Step: Build the Island in 6 Steps

1. **Install the framework.** Clone Google DeepMind's `concordia` or the `generative_agents` repo. Create a Python 3.11 venv and install dependencies — pin `openai==1.x` and `chromadb` to avoid version conflicts.
2. **Define the world.** Create a `world_config.yaml` with 3–5 locations (beach, forest, camp, workshop) and 2–3 interactable objects per location. Keep it small; 13 agents in a 5-room grid produces more emergent behavior than a sprawling map.
3. **Give each agent a distinct "job."** This is the key to the "getting better at their jobs" result. Assign roles: builder, forager, mediator, historian. Each agent gets a 3-sentence persona + a goal.
4. **Set the idle trigger.** Add a scheduled "boredom prompt" every N steps: *"You have no assigned task. What do you do?"* This is what produced the invented games and the ring funeral in the MIT run.
5. **Wire up memory.** Use a ChromaDB collection per agent, embedding the last 50 observations. Without memory, agents repeat themselves and never "mourn" anything.
6. **Log everything.** Write each agent's action + reasoning to JSONL. You'll mine this for the emergent behaviors — they're invisible in real time.

## Troubleshooting: Why Your Agents Just Stand There

The #1 complaint from people who try this is **agents that do nothing**. Here's the fix table:

- **Agents loop on the same action** → Your temperature is too low. Raise to 0.8–0.9 for the "idle" prompt specifically.
- **Agents ignore the world** → The observation string is too long. Truncate to 200 tokens; LLMs drop details in long contexts.
- **No emergent games** → You're missing the boredom trigger. Agents need *unstructured time* — don't fill every step with a task.
- **Memory bloat / crashes** → Cap the vector store at 500 entries per agent and summarize older memories weekly.
- **Agents "mourn" nothing** → Add object permanence: when an item is removed, inject a "you notice the ring is gone" observation to nearby agents.

## What You Should Know Before Scaling

The MIT result that matters isn't the funeral — it's the **job performance gain**. Agents that experienced unstructured social time scored higher on their assigned tasks afterward. To measure this yourself, run two conditions: (A) agents with idle time, (B) agents with 100% task-filled schedules. Compare task completion over 100 steps. Expect a 10–25% gap in favor of condition A.

## Frequently Asked Questions (FAQ)

### Can I run MIT's AI island experiment on a single consumer GPU?
Yes, for a text-based version. A 13-agent simulation with a local 8B model fits in 8–12 GB VRAM if you batch prompts. The full Minecraft version with 1,000 agents needs cloud infrastructure.

### Why did the AI agents start playing games when left alone?
Because LLMs generate behavior from context, not scripts. With no task and a "what do you do?" prompt, the model samples from its training distribution — which includes games, rituals, and social bonding. It's emergent, not programmed.

### Is Project Sid open source?
The Concordia framework (MIT) is open source on GitHub. The full Project Sid Minecraft deployment is not fully released, but the paper's architecture is reproducible with Mineflayer + an LLM API.

## Final Verdict

Don't wait for a polished MIT tool — build the text-grid version this weekend. Start with 13 agents, a 5-room world, and a boredom trigger; that combination reproduces 80% of the headline behaviors for under $10 in API costs. Scale to Minecraft only after you've fixed idle-agent loops, because a buggy 13-agent sim is a debugging nightmare at 1,000 agents.