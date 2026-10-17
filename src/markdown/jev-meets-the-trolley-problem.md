---
title: "Jev Meets the Trolley Problem: How to Play & Solve It"
description: "Jev meets the Trolley Problem explained: how to play the moral machine, solve every track-switch scenario, and understand the ending."
pubDate: 2026-10-16
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is "Jev Meets the Trolley Problem" and How Do You Play It?

If you clicked the Hacker News link, read Zach Landes' article, and now you're staring at a browser tab wondering *what am I actually supposed to do here* — you're in the right place. **"Jev Meets the Trolley Problem"** is an interactive moral-dilemma experiment where you, the player, control a runaway trolley's path and decide who lives and who dies. Each scenario forces a binary choice: pull the lever or don't. The twist is that "Jev" (the recurring character in the simulation) keeps re-appearing across scenarios, so your earlier decisions compound into a personal ethical profile.

The core takeaway: this isn't a game you "win." It's a decision-logging tool that reveals your moral baseline. But if you want to *complete* every scenario, unlock the alternate endings, and understand what your choices actually mean, this guide walks you through it step by step.

## Step-by-Step: How to Play and Solve Every Scenario

The simulation runs entirely in the browser — no install, no account. Here's the practical workflow:

1. **Open the article URL** (`zachlandes.com/trolley-problem/`) and let the page fully load. The interactive canvas initializes after the text renders.
2. **Read the scenario prompt** at the top of each card. It states the number of people on each track and any special conditions (age, relationship to Jev, prior actions).
3. **Click the lever or the "do nothing" button.** The simulation logs your choice and immediately renders the next scenario.
4. **Track your running tally.** The page keeps a hidden score of utilitarian vs. deontological choices — you'll see it summarized at the end.
5. **Reach the final screen** to get your moral-profile label (e.g., "Consistent Utilitarian," "Rule-Follower," "Chaotic Pragmatist").

### Decision Types You'll Encounter

| Scenario Type | What It Tests | Common "Trap" |
|---|---|---|
| Classic 1-vs-5 | Pure utilitarian math | Overthinking it |
| Jev-involved | Emotional bias | Favoring the named character |
| Self-sacrifice | Altruism vs. self-preservation | Hesitation |
| Loop / repeat | Consistency | Contradicting earlier choices |
| No-win | Moral residue | Refusing to choose |

**Pro tip:** The simulation *remembers* your answers. If you flip-flop between utilitarian and deontological logic, the final profile flags you as "Inconsistent" — which many players find more interesting than a clean label.

## Common Issues, Hidden Mechanics, and What You Should Know

### The page won't load or the canvas is blank
- **Disable ad-blockers** for this domain — some filter lists block the canvas script.
- **Try a hard refresh** (`Ctrl+Shift+R` / `Cmd+Shift+R`). The simulation caches state in `localStorage`, and a stale cache can freeze the first scenario.
- **Use Chrome or Firefox.** Safari occasionally fails to render the lever animation.

### You want to reset your choices
Open DevTools (`F12`), go to **Application → Local Storage**, find the `trolley-state` key, and delete it. Reload the page and you'll start fresh.

### What the HN thread adds
The Hacker News discussion (190 comments, 442 points) is worth reading *after* you play, not before — it's full of people arguing about whether the simulation is a fair test of moral reasoning or just a dressed-up version of the original 1967 Philippa Foot thought experiment. Several commenters point out that **order effects** bias your answers: whichever scenario you see first anchors your later choices. That's a real methodological critique, not just nitpicking.

### Alternatives worth trying
- **Moral Machine (MIT)** — the classic autonomous-vehicle dilemma dataset.
- **The Trolley Problem Game** — a mobile version with cartoon visuals.
- **Absurd Trolley Problems** — a comedic escalation that adds increasingly ridiculous tracks.

If you liked Jev's version, Moral Machine is the most rigorous follow-up because it collects your data for actual research.

## Frequently Asked Questions (FAQ)

### What is the point of "Jev Meets the Trolley Problem"?
It's an interactive moral-psychology experiment that logs your trolley-problem choices and generates a personal ethical profile. There's no winning — the point is self-reflection and comparing your answers to the Hacker News crowd.

### Can I play "Jev Meets the Trolley Problem" on mobile?
Yes, the simulation is responsive and works on iOS Safari and Android Chrome. Tap the lever instead of clicking. For the cleanest experience, rotate to landscape so the track diagram isn't cramped.

### How do I reset my progress in the trolley problem simulation?
Clear the `trolley-state` entry in your browser's Local Storage via DevTools, then reload. There's no in-page reset button as of the current version.

### Is "Jev Meets the Trolley Problem" the same as the original trolley problem?
No. The original is a philosophical thought experiment from Philippa Foot (1967). Jev's version is an interactive adaptation that adds a recurring character and tracks consistency across multiple scenarios.

## Final Verdict

Play it once blind, then play it again knowing the mechanics. The first run tells you who you *think* you are; the second run — where you deliberately test consistency — tells you how your moral reasoning actually holds up under repetition. Skip the HN thread until after your first playthrough so the commentary doesn't poison your instincts. And if you want the rigorous version, graduate to MIT's Moral Machine next.