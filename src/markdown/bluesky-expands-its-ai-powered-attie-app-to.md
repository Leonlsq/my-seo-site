---
title: "How to Build a Game on Bluesky Attie: 2026 Setup Guide"
description: "Bluesky Attie now lets anyone build websites and games. Here's how to set up your first vibe-coded app, embed it on Bluesky, and avoid common errors."
pubDate: 2026-10-16
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Bluesky Attie Just Opened the Floodgates: Here's How to Actually Build Something

Bluesky has expanded its experimental **Attie** platform into full "social vibe coding" territory — meaning you can now prompt your way into building interactive games, quizzes, and full websites that plug directly into the Bluesky audience. The catch? Attie is still experimental, the onboarding flow isn't obvious, and most "how do I use this" searches return news articles instead of instructions. This guide skips the hype and walks you through the actual build-and-publish loop, plus the errors you'll hit along the way.

The short version: Attie is an AI-assisted app builder layered on top of Bluesky's AT Protocol. You describe what you want, the AI generates a working app, and you publish it to a shareable link that Bluesky users can interact with using their existing handles. No hosting bill, no domain purchase, no dev environment.

## How to Build and Publish Your First Attie App (Step-by-Step)

Before you start, confirm you meet the baseline requirements:

- **A Bluesky account** in good standing (new accounts under 48 hours old may not see the Attie beta flag)
- **The latest Bluesky app** (iOS/Android) or desktop web session — Attie's builder is mobile-first but works on desktop
- **A clear, single-sentence prompt** — vague prompts are the #1 cause of broken first builds

### Step 1: Find the Attie entry point

Attie does not live in your main feed. Open Bluesky, tap your profile, then look for **Attie (Beta)** under the experimental features section. If it's missing, update your app and force-close it once — the flag rolls out in waves.

### Step 2: Write a build prompt that actually works

The AI responds far better to structured prompts than creative ones. Use this template:

```
Build a [type of app] where users [core action].
It should have [2-3 features max].
Style it [simple/retro/neon/minimal].
```

A working example: *"Build a quiz where users guess which planet a fact describes. It should have 10 questions, a score screen, and a share button. Style it retro."*

### Step 3: Test in the sandbox before publishing

Attie generates a live preview. Do not skip this. Check three things:

1. **Tap targets** — buttons under 44px fail on mobile
2. **Loop logic** — quizzes and games must have a defined end state, or they hang
3. **Share hook** — confirm the "post to Bluesky" button generates a valid card preview

### Step 4: Publish and pin it

Hit **Publish**, then copy the generated `bsky.app/attie/...` link. Pin it to your profile so visitors can find it without scrolling your feed. Apps published this way inherit your handle's identity, which is why engagement spikes compared to anonymous link sharing.

### Step 5: Iterate from the prompt history

Every rebuild is versioned. You can roll back a broken change without losing your published link — a feature most no-code builders still charge for.

## Common Attie Errors and How to Fix Them

| Error | Likely Cause | Fix |
|---|---|---|
| "Build failed — ambiguous intent" | Prompt too broad | Add a user count and one core action |
| App loads but buttons dead | Missing state handler | Reprompt: "add click handlers to all buttons" |
| Share card shows blank | No meta description generated | Manually add a title + one-line description |
| Preview works, published version doesn't | Stale cache | Wait 5 minutes, then hard-refresh |
| Attie tab missing entirely | Account too new / app outdated | Update app, wait 48h, check again |

**What Attie is genuinely good at:** quizzes, polls, single-screen games, landing pages, and interactive threads. **What it struggles with:** anything requiring persistent user accounts, real-time multiplayer, or external API calls. If your idea needs a database, Attie isn't the tool yet.

### Attie vs. the Alternatives

- **vs. Glitch/Replit:** Those give you real code and real hosting, but zero built-in audience. Attie trades flexibility for distribution.
- **vs. Carrd:** Carrd makes cleaner static sites, but no games and no social graph.
- **vs. raw vibe-coding tools (Cursor, Bolt):** You'll get better code, but you still have to deploy it and convince people to visit.

The honest cost analysis: Attie is free during beta. Expect a paid tier once it exits experimental status — likely tied to Bluesky's existing premium subscription.

## Frequently Asked Questions (FAQ)

### Do I need to know how to code to use Bluesky Attie?
No. Attie is fully prompt-driven. You describe the app in plain language and the AI generates the working build. Basic logic thinking helps — knowing that a quiz needs questions, answers, and a score — but syntax knowledge isn't required.

### Can I make money from an Attie game or website?
Not directly yet. Attie has no built-in monetization, ads, or tipping integration as of the 2026 beta. Your realistic path is building an audience through the app, then monetizing off-platform via subscriptions or sponsorships.

### Is Attie available on desktop or only mobile?
Both. The builder is optimized for mobile, but the full prompt-to-publish flow works in a desktop browser session. Desktop is actually better for longer prompts and testing share cards.

### What happens to my Attie app if Bluesky shuts the experiment down?
Because Attie runs on the AT Protocol, published apps are portable in theory — but there's no one-click export yet. Back up your prompts manually. If portability matters, keep a copy of your build logic somewhere outside Bluesky.

## Final Verdict

If you've been waiting for a reason to try vibe coding, Attie is the lowest-friction entry point that exists right now — the audience is already there, the hosting is handled, and the prompt-to-publish loop takes under ten minutes once you know the steps above. Build something small and single-purpose first: a quiz, a poll, a one-screen game. Skip anything that needs accounts or multiplayer until Attie matures. And screenshot your working prompts, because the beta will change fast and your build history is your only safety net.