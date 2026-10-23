---
title: "Move Slow and Fix Things: 2024 Dev Guide to Safer Refactors"
description: "A practical 2024 guide to the 'move slow and fix things' philosophy: safer refactoring steps, tech debt metrics, and when to pick it over fast shipping."
pubDate: 2026-10-23
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What "Move Slow and Fix Things" Actually Means for Your Codebase

The phrase "Move Slow and Fix Things" — popularized by a 2024 essay on endler.dev and discussed heavily on Hacker News — is a deliberate counter-mantra to "Move fast and break things." The core argument: velocity without maintenance creates compounding interest on technical debt, and the fix is to slow down *strategically* before shipping, not to stop shipping. If you landed here after reading the essay, the practical question is: **how do you actually apply this to a real project without tanking your delivery speed?** This guide gives you a concrete workflow, measurable metrics, and the specific scenarios where "slow and fix" beats "fast and break."

The direct takeaway: treat "slow" as *front-loaded correctness* (design reviews, tests, migration plans) and "fix" as *continuous debt paydown* (scheduled refactors, observability). Teams that do this routinely ship *faster* over a 12-month horizon because they spend less time firefighting.

## Step-by-Step: Implementing a "Fix Things" Workflow in Your Team

Here's a repeatable process you can adopt this sprint. Each step maps to a concrete artifact, not a vague principle.

1. **Inventory your debt (Week 1).** List every known issue in a single tracker with three fields: *impact* (1–5), *frequency* (how often it bites), and *fix cost* (hours). Score = impact × frequency ÷ cost. Fix the top 10 first.
2. **Add a "correctness gate" to CI (Week 1–2).** Before merging, require: passing unit tests, a lint pass, and one reviewer sign-off. This is the literal "slow" — 10–20 minutes of friction that prevents hours of debugging.
3. **Set a debt budget (Week 2).** Allocate a fixed percentage of each sprint to fixes. A common split that works for small teams:
   - **70%** new features
   - **20%** debt/refactor
   - **10%** bug triage and on-call
4. **Write migration plans before touching schemas.** Any database or API change gets a written rollback step. No exceptions.
5. **Instrument before you optimize.** Add logging/metrics to the module you're about to refactor so you can prove the fix worked.
6. **Ship in small, reversible increments.** One logical change per PR. If a deploy breaks, you revert one commit, not five.
7. **Review debt monthly.** Re-score the tracker; celebrate closed items publicly to keep the habit alive.

### Quick comparison: "Move Fast" vs. "Move Slow and Fix"

| Dimension | Move Fast & Break | Move Slow & Fix |
|---|---|---|
| Time to first ship | Days | Days–weeks |
| Time to 12-month feature | Often slower (firefighting) | Usually faster (stable base) |
| Incident rate | High | Low–moderate |
| Onboarding new devs | Painful | Smoother (tests/docs exist) |
| Best for | Prototypes, throwaway MVPs | Production systems, regulated code |

## Common Issues, Trade-offs, and What You Should Know

**Pitfall 1: "Slow" becomes "stuck."** The philosophy is not an excuse for analysis paralysis. Cap design reviews at one meeting; if no decision, default to the smallest reversible option.

**Pitfall 2: Fixing debt nobody feels.** Prioritize by *frequency of pain*, not by aesthetic preference. A messy but stable module is lower priority than a clean-looking one that pages you at 3 a.m.

**Pitfall 3: No rollback = no speed.** The single biggest lever for safe velocity is deploy reversibility. Blue-green deploys, feature flags, and one-change-per-PR make "slow" cheap.

**When to ignore this advice:** greenfield prototypes and hackathon MVPs where the code will be thrown away. There, speed genuinely wins — just don't let the prototype silently become production.

**Cost reality check:** a 20% debt budget on a 5-person team is roughly one full-time engineer's worth of maintenance. Frame it to stakeholders as *incident prevention*, not overhead — track mean time to recovery (MTTR) before and after to prove ROI.

## Frequently Asked Questions (FAQ)

### What does "move slow and fix things" mean?
It's a software development philosophy that prioritizes correctness, testing, and maintenance over raw shipping speed. The idea is that slowing down before release and continuously fixing technical debt produces faster long-term delivery and fewer production incidents than "move fast and break things."

### Is "move slow and fix things" the opposite of "move fast and break things"?
Not strictly opposite — it's a correction. Both value shipping, but "slow and fix" front-loads quality work (tests, reviews, migration plans) and schedules debt paydown, whereas "move fast" defers that work and pays for it later in outages and rewrites.

### How much time should a team spend on fixing technical debt?
A common starting point is 15–25% of each sprint, adjusted by incident rate. If you're firefighting weekly, push toward 30% temporarily until MTTR drops; if the system is stable, 10–15% is often enough to stay ahead.

### Does moving slow hurt startup velocity?
Short-term, slightly — you add review and testing friction. Long-term, teams that maintain their codebase typically ship features faster because they spend less time on emergency fixes and rewrites. Measure feature lead time over 6–12 months to see the real effect.

## Final Verdict

"Move Slow and Fix Things" is not a slogan to adopt wholesale — it's a **budgeting discipline**. If you run a production system, adopt the 70/20/10 sprint split, add a correctness gate to CI, and require rollback plans for every schema change. If you're prototyping, ship fast and be honest that the code is disposable. The teams that win are the ones that *know which mode they're in* and switch deliberately rather than by accident. Start with one measurable change this week: score your top 10 debt items and schedule the highest-impact fix into your next sprint.