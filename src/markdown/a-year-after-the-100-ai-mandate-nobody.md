---
title: "AI-Written Code Unreadable? How to Fix the 100% AI Mandate"
description: "Stuck with unreadable AI-generated code a year after an AI mandate? Use this audit and remediation playbook to regain control of your codebase."
pubDate: 2026-11-10
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Nobody Understands Your Code After the 100% AI Mandate

If your engineering team mandated "100% AI-generated code" a year ago and now your senior devs can't explain how the billing service works, you're not alone. The viral r/ClaudeCode thread and the 155-comment Hacker News discussion (121 points) describe a predictable failure mode: velocity went up, comprehension went down, and now every incident is a scavenger hunt. The fix is not "ban AI." The fix is a structured **code comprehension remediation program** — an audit, a documentation layer, and guardrails that force AI output to be explainable before it merges. Below is the exact playbook to run this week.

## Step-by-Step Remediation Playbook

### Phase 1: Triage the Codebase (Days 1–3)

1. **Generate a comprehension heatmap.** Run a static analysis pass (e.g., `radon cc`, `sonar-scanner`, or `eslint --max-warnings 0`) and tag every file with: author type (AI/human), last-touched date, cyclomatic complexity, and test coverage.
2. **Flag the "dark zones."** Any file with AI origin, complexity >15, and coverage <40% is a dark zone. In most mandated-AI codebases, 20–30% of files land here.
3. **Rank by blast radius.** Sort dark zones by number of downstream imports. Fix the top 10 first — that's where incidents originate.

### Phase 2: Build the Comprehension Layer (Days 4–10)

| Artifact | Owner | Tool | Acceptance Criteria |
|---|---|---|---|
| Module README | File owner | Markdown | Explains *why*, not just *what* |
| ADR (Architecture Decision Record) | Tech lead | `adr-tools` | One per non-trivial AI-generated module |
| Inline "intent comments" | Original author | IDE + LLM | Every function >20 lines has a 1-sentence intent |
| Runbook | On-call | Notion/Confluence | Reproduces any alert in <10 min |

4. **Reverse-engineer intent with AI — carefully.** Prompt your assistant: *"Explain this module's data flow and list three assumptions it makes."* Then have a human verify each assumption against tests. Do not accept the explanation as truth; treat it as a hypothesis.
5. **Write characterization tests before refactoring.** Use `approvaltests` or golden-master snapshots to lock current behavior, so any cleanup is provably safe.

### Phase 3: Enforce Explainability at Merge Time (Ongoing)

6. **Add a "comprehension gate" to CI.** Require every PR with >100 AI-generated lines to include: a linked ADR, a reviewer sign-off, and at least one new test.
7. **Rotate code ownership monthly.** Force humans to read AI code they didn't prompt — this is the single highest-leverage habit.
8. **Track a "bus factor" metric.** If fewer than two engineers can explain a module, it fails the gate.

## Common Issues, Workarounds, and What You Should Know

- **"We can't slow down to document."** You already are — every incident caused by unreadable code costs 4–8 engineer-hours. Documentation is cheaper than 3 a.m. debugging.
- **AI explanations are confidently wrong.** LLMs will invent intent. Always cross-check against tests and git history (`git log -p --follow`).
- **Tooling shortcuts:** `Sourcegraph` for cross-repo search, `CodeSee` for visual maps, `Sourcery` for AI-assisted refactor suggestions — but none replace a human reviewer.
- **Cost reality:** A 50-engineer team spending 2 hours/week on comprehension work costs ~$5,200/month at $130/hr loaded rate — versus a single major outage, which typically runs $9,000+/minute for customer-facing systems.
- **Don't rewrite everything.** Target the top 10 dark zones; a full rewrite reintroduces the same problem with fresh AI code.

## Frequently Asked Questions (FAQ)

### How do I audit a codebase that was 100% AI-generated?
Start with static analysis (complexity + coverage), tag files by origin and blast radius, and prioritize the 10 highest-risk modules. Build characterization tests before touching anything.

### Is AI-generated code actually worse to maintain?
Not inherently — the problem is *unreviewed* AI code. Studies and the HN thread both point to the same cause: AI output merged without comprehension gates. Add explainability requirements and the maintainability gap closes.

### What's the fastest way to make AI code readable?
Generate intent comments and ADRs with AI assistance, verify them against tests, and enforce a merge gate requiring human sign-off on any large AI-generated diff.

## Final Verdict

A 100% AI mandate isn't the mistake — skipping the comprehension layer is. Run Phase 1 triage this week, stand up the comprehension gate within two sprints, and track bus factor as a first-class metric. Teams that do this keep the velocity gains; teams that don't will keep writing postmortems about code nobody understands.