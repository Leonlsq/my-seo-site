---
title: "Dan Luu's 'Be More Ambitious' Essay: 7 Hard Lessons for Devs"
description: "Dan Luu's ambitious software essay hit 589 HN points. Here's a practical breakdown of why teams ship small and 7 concrete tactics to build bigger software in 2026."
pubDate: 2026-10-25
tags: ['Tech', 'Guide', 'Software Engineering']
---

## Why Your Team Keeps Shipping Small: The Real Problem Behind Dan Luu's Essay

Dan Luu's essay "We should be more ambitious with the software we build" hit 589 points and 582 comments on Hacker News, and the reaction tells you everything: engineers *know* they're building too small, but almost nobody has a repeatable process for building bigger. This guide skips the philosophical debate and gives you the practical playbook — concrete tactics, tradeoffs, and a checklist you can bring to your next sprint planning. The short version: ambition isn't a mindset problem, it's an incentive, architecture, and risk-budgeting problem. Fix those three and bigger software follows.

## The Core Diagnosis: Why Ambitious Projects Die

Luu's central argument is that the industry has drifted toward incremental, low-risk work — CRUD apps, thin wrappers, and feature flags on top of legacy systems — while the tools and infrastructure to build genuinely ambitious software have never been better. The HN thread surfaced recurring root causes. Here's the consolidated list:

| Root Cause | How It Shows Up | Typical Symptom |
|---|---|---|
| Risk aversion | Small PRs, "let's not touch that" | 5-year-old TODOs nobody owns |
| Short tenure | 18-month average engineer stint | Nobody sees a project to completion |
| Metric theater | Velocity points, not outcomes | Shipping features, not capabilities |
| Legacy gravity | Every change requires 3 approvals | Refactors never happen |
| Missing "boring" investment | No observability, no CI depth | Fear of breaking prod |
| Talent underuse | Senior engineers doing ticket work | Quiet quitting via small scope |

The pattern: **ambition is a systems property, not an individual trait.** If your org punishes failure and rewards small, visible wins, you get small software — regardless of how talented your team is.

## 7 Concrete Tactics to Build More Ambitious Software

These are actionable, ordered by leverage. Pick two and run them this quarter.

1. **Create a "big bets" budget.** Allocate 15–20% of engineering capacity to one project that would take 6+ months. Protect it in planning like headcount — not like a side project. If it gets raided every sprint, it dies.
2. **Write a one-page "ambition brief" before any large project.** Include: the user-visible capability, the smallest demo that proves it, the top three failure modes, and a kill criterion. Luu's implicit point — ambition without a kill criterion is just gambling.
3. **Instrument before you build.** Ambitious systems fail silently. Ship tracing, structured logs, and a staging environment that mirrors prod *first*. Teams that skip this retreat to small changes within two quarters.
4. **Buy the boring parts.** Use managed databases, hosted queues, and off-the-shelf auth. Ambition should go into your differentiator, not your Postgres tuning. The HN thread was blunt: "every hour on undifferentiated infrastructure is an hour not spent on the hard thing."
5. **Hire and retain for completion.** Ask candidates to describe a project they saw from zero to production. Tenure matters more than raw skill for ambitious work — a 3-year engineer who finished something beats a 9-month genius who didn't.
6. **Change the review culture.** Small PRs are good; small *thinking* is not. Require design docs for anything over two weeks of work, and review the design, not just the diff.
7. **Celebrate the boring middle.** Most ambitious projects die in month four, when the demo works but the edge cases don't. Publicly reward the engineers grinding through that phase.

## What You Should Know: Tradeoffs and Common Traps

**Ambition ≠ rewrite.** The most common failure mode after reading an essay like Luu's is a "big rewrite" that burns a year. Ambitious software can be built incrementally — strangler-fig patterns, feature-flagged migrations, and parallel-run systems all let you go big without a flag day.

**Small teams can be ambitious; large teams often can't.** Coordination costs scale faster than ambition. A 5-person team can ship a new database engine; a 500-person org needs a program office to ship a settings page. If you're in a large org, your ambition budget should be *one team*, not the whole department.

**The tooling argument cuts both ways.** Modern infrastructure (cloud, LLMs, managed services) lowers the cost of ambitious projects — but it also lowers the cost of small ones, which is why the median project got smaller. The essay's real ask is to use the surplus for scope, not for speed.

**Watch for "ambition theater."** Big roadmaps, big slides, no shipped capability. The test is simple: can a user do something in 90 days they couldn't do before? If not, it's not ambition, it's planning.

## Frequently Asked Questions (FAQ)

### What is Dan Luu's "We should be more ambitious with the software we build" about?
It's an essay arguing that the software industry has become too incremental — teams ship small, low-risk features while the underlying tools make large, ambitious projects more feasible than ever. The core claim is that ambition is constrained by incentives and process, not by technical capability.

### Why did the essay get 589 points on Hacker News?
Because it named a frustration most engineers feel but rarely articulate: they're capable of more, but their organizations reward small, safe work. The 582-comment thread became a cathartic catalog of legacy systems, risk aversion, and short tenures.

### How do I convince my manager to fund a more ambitious project?
Bring a one-page ambition brief: the user-visible capability, a 90-day proof point, the top risks, and a kill criterion. Frame it as risk-managed scope, not a moonshot. Managers fund projects with exit ramps, not open-ended bets.

### Is ambitious software always better than incremental software?
No. Incremental delivery is the right default for mature products and regulated environments. Ambition pays off when there's a real capability gap — a new market, a broken workflow, or a platform shift. The essay's point is that the *option* to go big should exist, not that every project should be big.

## Final Verdict

Luu's essay is a diagnosis, not a prescription — so treat it as a checklist, not a manifesto. If you do one thing this quarter, do this: carve out a protected 15% capacity budget for a single 6-month project, write a one-page ambition brief with a kill criterion, and instrument the system before you build it. That combination — protected scope, explicit risk, and observability — is what separates teams that ship ambitious software from teams that write blog posts about wanting to. The tools are already good enough. The missing piece is the process, and that's on you.