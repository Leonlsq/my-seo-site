---
title: "decomp.dev Shut Down? How to Track Game Decompilation Now"
description: "decomp.dev froze its leaderboard after AI slop broke the index. Here's how to track real game decompilation projects and avoid fake AI forks in 2026."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## decomp.dev Froze Its Leaderboard: Here's How to Track Real Decompilation Projects Now

If you loaded decomp.dev this week and found the leaderboard frozen, the public index closed, or your favorite project suddenly buried under a wall of AI-generated forks, you're not alone. The community hub announced it has **closed its public index of game decompilation projects**, citing AI-driven forks and ports that turned progress into a hollow numbers game. The direct takeaway: the old "watch the leaderboard" workflow is dead, and you need a new way to verify which decompilation projects are actually real. This guide gives you the exact workarounds, verification steps, and alternatives to keep tracking legitimate work in 2026.

## Why the Leaderboard Broke (and What "AI Slop" Actually Means Here)

Before the workarounds, understand the failure mode so you can spot it yourself. The problem wasn't one bad actor — it was a systemic exploit of how decompilation progress is measured.

- **Progress metrics are gameable.** Decompilation "percent complete" is often measured by matching functions or byte-identical code. An AI tool can mass-generate plausible-looking function stubs and inflate a match percentage without producing compilable, correct code.
- **Forks multiply the noise.** A single AI-generated fork can spawn dozens of derivative repos, each claiming progress. The index had no cheap way to distinguish a real fork from a hollow one.
- **Ports muddy attribution.** AI-assisted ports reuse decompiled code with minimal credit, so leaderboard entries stop reflecting actual human effort.
- **The result:** the leaderboard became a numbers game where the top of the chart no longer correlated with real, playable, verified decompilation.

That's why the hub froze the index rather than let it rot. Your job now is to verify projects manually — here's how.

## Step-by-Step: How to Track & Verify Decompilation Projects Without the Leaderboard

Use this workflow to find real projects and confirm they aren't AI-inflated.

1. **Start from primary source repos, not aggregators.** Go directly to the project's GitHub or GitLab page. Check the **commit history**, not the README badge. Real decompilation has a steady cadence of small, reviewable commits — often one function or one file at a time.
2. **Check the "matched functions" claim against the build.** A legitimate project should let you clone and run `make` (or the documented build) and produce a matching ROM/binary. If the repo can't build, the percentage is suspect.
3. **Look at contributor diversity.** A real project has multiple named contributors with long histories. A hollow AI fork often has one account, a burst of commits, and no issue discussion.
4. **Inspect code diffs, not line counts.** Open a random recent commit. Real decompilation diffs contain hand-tuned C matching assembly, with comments explaining register allocation and control flow. AI slop diffs are often repetitive stubs.
5. **Cross-reference community channels.** Check the project's Discord, forum thread, or subreddit. Real projects have active discussion and bug reports; fake ones have none.
6. **Verify licensing and credit.** Confirm the repo credits the original decompilation team and respects the project's license. Ports that strip attribution are a red flag.

**Quick verification checklist:**

| Signal | Real Project | AI Slop Fork |
|---|---|---|
| Builds to matching binary | Yes | Often no |
| Commit cadence | Steady, small | Burst, then dead |
| Contributors | Multiple, named | One account |
| Issue tracker | Active | Empty |
| Code diffs | Hand-tuned C + asm comments | Repetitive stubs |
| Attribution | Clear | Stripped |

## Alternatives & Workarounds: Where to Track Progress Now

With the public index frozen, use these substitutes:

- **GitHub topic and search filters.** Search `topic:decompilation` plus the game name, then sort by "recently updated" and filter by stars and contributors. This surfaces active projects without a central leaderboard.
- **Project-specific progress pages.** Many major projects maintain their own progress dashboards (function match counts, per-file breakdowns) hosted on their own domains or GitHub Pages. Bookmark those directly.
- **Community wikis and forums.** Decompilation communities on Discord and dedicated forums maintain curated project lists that are moderated — slower than an automated index, but far harder for AI slop to game.
- **Local verification scripts.** If you want a personal leaderboard, write a small script that clones candidate repos, runs the documented build, and records whether the binary matches. This is the only metric AI can't fake.

**What to avoid:** any third-party "decompilation tracker" site that appeared after the freeze and ranks projects purely by claimed percentage. These are the exact hollow numbers games the hub was trying to escape.

## Frequently Asked Questions (FAQ)

### Why did decomp.dev freeze its leaderboard?
The hub closed its public index because AI-driven forks and ports inflated progress metrics, making the leaderboard unreliable and breaking the community's ability to distinguish real decompilation work from generated noise.

### Is decomp.dev shut down permanently?
The public index is closed and the leaderboard frozen. Treat it as unavailable for now and rely on direct repo verification and community-maintained lists until the operators announce a verified replacement.

### How can I tell if a decompilation project is AI-generated slop?
Check whether the repo builds to a matching binary, review commit diffs for hand-tuned C matching assembly, confirm multiple named contributors, and verify the issue tracker is active. Hollow forks typically fail the build test and have no real discussion.

### What's the best alternative to the decomp.dev leaderboard?
Use GitHub topic searches sorted by recent activity, project-hosted progress dashboards, and moderated community wikis. For a personal ranking, run local build-verification scripts against candidate repos.

## Final Verdict

The frozen leaderboard is a loss, but it's a fixable one. **Stop trusting any single percentage metric** — including whatever replaces decomp.dev — and start verifying projects at the repo level: build it, read the diffs, check the contributors. If you're a player, follow project-specific dashboards and community wikis. If you're a contributor, keep your commits small, documented, and attributable, because that's now the clearest signal separating real decompilation from AI slop. The numbers game is over; the verification game is just beginning.