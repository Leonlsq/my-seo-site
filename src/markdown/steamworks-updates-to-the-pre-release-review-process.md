---
title: "Steamworks Pre-Release Review Changes: What Devs Must Do"
description: "Steamworks updated its pre-release review process. Here's what changed, how to submit your build for review, and how to avoid launch delays."
pubDate: 2026-11-04
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Steamworks Pre-Release Review Changes: What Devs Actually Need to Do

Valve quietly updated the Steamworks pre-release review process, and if you're a developer with a launch on the calendar, this affects your build submission timeline directly. The short version: the review window, build requirements, and store-page readiness checks have shifted, and the biggest risk is assuming the old "submit two weeks before launch" rule still protects you. It doesn't — not reliably. Below is a practical breakdown of what changed, a step-by-step submission checklist, and the specific mistakes that get builds bounced back to you with a delayed launch date.

If you heard about this via the r/gamedev thread (originally posted by u/doublah), you already know the community reaction was a mix of confusion and mild panic. This guide cuts through that and gives you an actionable path from "build is ready" to "review approved."

## What Changed in the Pre-Release Review Process

The core shift is that Valve now expects your **store page and build to be in a near-final state** at the moment you request review — not "mostly there." Reviewers are checking store assets, build functionality, and compliance items together rather than in sequence. Practically, that means fewer back-and-forth cycles but a harder first pass.

Here's the comparison between how most devs *think* it works and how it actually works now:

| Item | Old Assumption | Current Reality |
|---|---|---|
| Review lead time | ~2 weeks before launch | Request as early as possible; 2 weeks is a floor, not a guarantee |
| Store page state | Can be WIP during review | Must be review-ready: capsule art, screenshots, description, tags |
| Build readiness | Can submit "near-final" | Must be launch-candidate quality, playable end-to-end |
| Compliance | Checked late | Checked during review (age gates, content descriptors) |
| Re-submission | Quick re-review | Each rejection costs you calendar days |

The takeaway: **treat the review request as a launch gate, not a formality.**

## Step-by-Step: Submitting Your Build for Pre-Release Review

Follow this order to minimize rejection risk.

1. **Finalize your store page first.** Complete capsule images at all required sizes, at least 5 screenshots, a trailer (strongly recommended), full description, and accurate tags. Reviewers flag incomplete pages immediately.
2. **Lock your build.** Upload the exact build you intend to ship. Run a full playthrough — including the first 30 minutes, which get the most scrutiny — and verify no crash-on-launch, no missing assets, no placeholder text.
3. **Complete the content survey.** Fill out the age rating and content descriptor questionnaire accurately. Mismatches between your survey and actual content are a common rejection cause.
4. **Verify compliance items.** Check your EULA, privacy policy link (if you collect data), and any required regional disclosures.
5. **Submit the review request** via the Steamworks dashboard as early as your build allows — ideally 3–4 weeks out, not 2.
6. **Monitor the dashboard daily.** Respond to reviewer notes within 24 hours; slow responses are the #1 cause of self-inflicted delays.
7. **Hold a buffer.** Plan a 5–7 day contingency window between expected approval and your launch date.

## Common Rejection Causes and How to Avoid Them

These are the issues that most frequently send builds back:

- **Incomplete store page assets.** Missing capsule variants or low-res screenshots. Fix: run through the store page checklist in Steamworks before requesting review.
- **Build crashes or soft-locks.** Even in optional content. Fix: test on a clean Windows machine with no dev tools installed.
- **Content survey mismatches.** You marked "no violence" but the tutorial has combat. Fix: re-read every descriptor question literally.
- **Broken external links.** Dead privacy policy or Discord links. Fix: click every link in your store description.
- **Missing localization on required fields.** Fix: complete all mandatory-language fields even if you only ship English.

### What About the Timeline If You Get Rejected?

Each rejection restarts a review cycle. If you're rejected at the two-week mark, you're now inside your launch window with no approval — meaning either a delayed launch or a "coming soon" page flip. The fix is structural: **submit early and treat the first pass as the only pass.**

## Frequently Asked Questions (FAQ)

### How far in advance should I submit my build for Steam pre-release review?
Aim for 3–4 weeks before your planned launch date. Two weeks is the minimum most devs cite, but it leaves no buffer for a rejection and re-review cycle.

### Does the updated review process apply to updates and DLC, or only new releases?
The stricter store-page and build-readiness expectations apply primarily to new releases and major content launches. Routine patches generally don't require pre-release review, but significant updates that change store-facing content can trigger a check.

### Can I launch if my review is still pending?
No. You need approval before your release goes live. If you're not approved by launch day, your options are to delay the launch or hold the store page — you cannot ship unapproved.

### What happens if my store page isn't fully complete when I request review?
The request is likely to be rejected or returned with notes, costing you calendar days. Complete the page fully before submitting.

## Final Verdict

If you're launching on Steam in the next few months, **assume the review process is stricter than the last time you shipped** and build your schedule around a 3–4 week lead time with a one-week buffer. The developers who get burned are the ones who submit a "good enough" build two weeks out and hope. The ones who sail through finalize the store page, lock a clean build, and submit early. Do the boring prep work first — it's the difference between a launch date and a launch *delay*.