---
title: "Hunger Beats Tenure: 7 Habits Junior Engineers Should Build"
description: "Turn Felix Rieseberg's 'hunger beats tenure' advice into action. A practical guide for junior devs to build visible momentum and outgrow tenure."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What "Hunger Beats Tenure" Actually Means for Junior Engineers

Felix Rieseberg's essay *Hunger Beats Tenure: Advice for Junior Engineers* hit the front page of Hacker News (105 points, 86 comments) because it names a quiet truth most career advice dodges: **in fast-moving engineering orgs, demonstrated drive and visible output outrank years of service.** Tenure gets you a chair. Hunger gets you the interesting project.

The practical takeaway is not "work 80-hour weeks." It's that hunger is a *measurable behavior pattern* — shipping, asking sharp questions, volunteering for the unglamorous-but-critical work, and making your learning legible to others. This guide converts that philosophy into seven concrete habits you can start this week, plus the traps that make "hungry" juniors burn out instead of level up.

## 7 Habits That Turn Hunger Into Promotions

### 1. Ship something visible in your first 30 days
Tenure accumulates passively; hunger compounds actively. Aim for one small, user-facing or team-facing improvement per sprint in your first quarter. A fixed flaky test, a docs page, a 10-line CLI flag — the size matters less than the cadence. Track them in a running log (Notion, a private gist, anything) so you can reference them in 1:1s.

### 2. Ask questions with a hypothesis attached
"Can you help me?" gets you an answer. "I think the cache invalidation happens in `handleUpdate()` because of X — is that right?" gets you a mentor. Senior engineers triage the second kind of question first. It signals you've done the work and respect their time.

### 3. Volunteer for the unowned work
Every team has orphaned tasks: the CI pipeline nobody wants to touch, the error-message audit, the stale runbook. Ownership of a small, unloved system is the fastest way to become indispensable without competing for the "fun" tickets. This is the single highest-leverage move in the essay's spirit.

### 4. Write things down publicly
Internal wikis, PR descriptions, postmortems, design docs. Written artifacts are tenure-proof: they outlive your tenure on the team and get read by people who decide promotions. A junior who writes a clear postmortem reads as a senior to everyone in the incident channel.

### 5. Learn the codebase by fixing bugs, not reading it
Reading 50k lines of code is passive. Fixing a bug forces you through the real call graph. The fastest onboarding path most engineers never use: pick the five oldest open bugs labeled `good-first-issue` and close three of them.

### 6. Build a "brag document" from day one
Keep a running file of: shipped features, incidents handled, reviews given, docs written, people unblocked. Update it weekly. When review season arrives, you're not reconstructing six months from memory — you're quoting it. This is the mechanism that makes hunger *visible* to the people who control your comp.

### 7. Find a "stretch owner" and a "stretch skill"
Pick one senior engineer whose judgment you trust and ask them (explicitly) to review your design docs for a quarter. Pick one skill outside your lane — observability, a second language, product analytics — and spend 2 hours a week on it. Two focused bets beat ten scattered ones.

## Hunger vs. Tenure: What Actually Gets You Promoted

| Factor | Tenure-based approach | Hunger-based approach |
|---|---|---|
| Visibility | Assumed, not built | Deliberately created each week |
| Learning | Passive (reading, waiting) | Active (fixing, shipping, writing) |
| Mentorship | Hoped for | Requested with specific asks |
| Promotion case | "I've been here 2 years" | "Here are 14 shipped artifacts" |
| Risk | Stagnation, quiet layoff | Burnout if unbounded |

### The burnout trap (read this before you go hard)
Hunger without boundaries becomes exploitation. Three guardrails:
- **Cap the "extra" at ~10% of your week** (4 hours). Sustainable hunger beats heroic sprints.
- **Say no to invisible work.** If nobody will read it, don't do it — or make it visible first.
- **Measure outcomes, not hours.** If your brag doc isn't growing, more hours won't fix it; better targeting will.

## Common Issues, Alternatives, and What You Should Know

- **"My manager doesn't notice."** Then make it impossible not to: send a short weekly update (3 bullets: shipped / blocked / learning). It takes 4 minutes and changes how you're perceived.
- **"The team has no unowned work."** Look one layer out: cross-team docs, onboarding guides, test coverage in adjacent services. There's always orphaned work at the seams.
- **"I'm the most junior person in the room."** Good — that's leverage. Ask the questions everyone else is too senior to ask; write the onboarding doc you wish you'd had.
- **Counterpoint from the HN thread:** several commenters argued hunger is worthless without a manager who *rewards* it, and that "hunger" language can mask exploitative cultures. Fair. Vet your manager in interviews by asking: "How do you decide who gets the interesting projects?" If the answer is tenure-based, no amount of hunger will move the needle — and that's a signal about the org, not you.

## Frequently Asked Questions (FAQ)

### What does "hunger beats tenure" mean for junior engineers?
It means demonstrated drive, visible output, and active learning are weighted more heavily than years of service when opportunities (projects, promotions, mentorship) are allocated. Tenure is a floor, not a ceiling.

### How do I show hunger at work without burning out?
Cap discretionary extra effort at roughly 10% of your week, focus on visible artifacts (docs, PRs, postmortems) rather than hours, and track outcomes in a weekly brag document so effort translates into a promotion case.

### Is "hunger beats tenure" bad advice?
It's good advice with a caveat: hunger only pays off in orgs that reward initiative. If your manager allocates projects purely by seniority, the essay's strategy won't work — and that's useful information about whether to stay.

### What should a junior engineer do in their first 90 days?
Ship one visible improvement per sprint, close three `good-first-issue` bugs, write one doc others will read, and start a brag document. Ask questions with hypotheses attached and request one specific mentor for design reviews.

## Final Verdict

Hunger beats tenure — but only *visible, bounded, documented* hunger. If you're a junior engineer reading the Rieseberg essay and wondering what to do Monday morning: start the brag document, claim one orphaned task, and send your manager a three-bullet weekly update. That's the whole strategy. Tenure will arrive on its own; the compounding you have to build yourself. And if after a quarter of doing this your org still rewards only the calendar, you've learned something more valuable than any promotion: where *not* to spend your next two years.