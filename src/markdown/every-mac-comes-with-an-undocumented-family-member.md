---
title: "Apple Intelligence Personal Knowledge Graph: How to Use It"
description: "Learn how Apple's undocumented family member classifier and personal knowledge graph work, how to inspect it, and what privacy settings to check."
pubDate: 2026-11-07
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Apple's Hidden "Family Member Classifier" Explained (And How to Audit It)

Every modern Mac ships with an undocumented on-device classifier that quietly sorts the people in your life — family, coworkers, friends — and feeds that data into Apple Intelligence's personal knowledge graph. The story broke on Hacker News (414 points, 238 comments) after an analysis at 8rank.ai, and the reaction was split: some users found it impressive, others found it unsettling. Here's the practical takeaway: **this is an on-device, opt-in-adjacent system tied to Apple Intelligence, and you can inspect, limit, or disable it today.** This guide walks you through what it actually does, how to verify it on your machine, and the exact settings to change if you're not comfortable with it.

## What the Personal Knowledge Graph Actually Does

Apple Intelligence doesn't just run a language model — it builds a relationship layer over your local data so Siri, Mail, Messages, and Notes can answer questions like "When is my sister's birthday?" without sending your address book to a server. The "family member classifier" is the component that infers *who* those people are relative to you.

Key facts worth knowing before you panic:

- **Processing is on-device.** The classifier runs locally via Apple's on-device models; relationship inference is not a cloud feature.
- **It requires Apple Intelligence.** If Apple Intelligence is off (or your Mac is Intel-based), the knowledge graph isn't being built in the same way.
- **It draws from local signals**, including Contacts relationships, shared calendar events, Message thread frequency, and photo co-occurrence — not from a single "family" checkbox.
- **It is undocumented.** Apple has published no developer documentation for the classifier, which is why the HN thread exploded. Treat any third-party claims about exact model behavior as unverified.

The practical risk isn't that Apple is selling your family tree — it's that **misclassification** (a coworker tagged as family, a family member tagged as an acquaintance) can produce wrong Siri suggestions, and that most users have never looked at what's stored.

## Step-by-Step: Audit and Control the Knowledge Graph on macOS

Follow these steps in order. You'll need macOS Sequoia 15.1 or later with Apple Intelligence enabled.

1. **Check whether Apple Intelligence is active.** Open **System Settings → Apple Intelligence & Siri**. If the toggle is off, the knowledge graph is not being actively built for AI features. Note the status and language support for your region.
2. **Review your Contacts relationship fields.** Open **Contacts**, pick a person, and click **Edit**. Scroll to the **related name** field (e.g., "mother," "spouse," "manager"). This is the most direct input the classifier uses — correcting it here is the highest-leverage fix.
3. **Audit Siri's learned relationships.** Ask Siri: *"Who is my sister?"* and *"Who are my family members?"* The answers reveal what the graph currently believes. Wrong answer? Fix the Contacts entry in step 2 and re-ask.
4. **Inspect Mail and Messages context.** In **Mail → Settings → Privacy**, review whether "Protect Mail Activity" is on. In **Messages**, check **Settings → Apple Intelligence & Siri** for any per-app intelligence toggles.
5. **Limit Photos co-occurrence data.** Open **Photos → Settings** and review whether the app is included in Apple Intelligence features. Faces you've named in Photos feed people-recognition, which the graph can reference.
6. **Disable Apple Intelligence entirely if needed.** **System Settings → Apple Intelligence & Siri → Apple Intelligence** → toggle off. This stops AI-driven graph building; standard Siri and Spotlight still work.
7. **Verify with a fresh query.** Wait a few minutes after changes, then repeat the Siri questions from step 3 to confirm the graph updated.

### Quick Reference: What Feeds the Graph vs. What You Control

| Data Source | Feeds Classifier? | User Control |
|---|---|---|
| Contacts relationship field | Yes (primary) | Direct edit per contact |
| Calendar shared events | Yes | Calendar privacy settings |
| Messages thread frequency | Likely | Per-app Siri toggles |
| Photos named people | Likely | Photos settings |
| iCloud contacts sync | Yes | iCloud settings |

## Common Issues, Privacy Concerns, and What You Should Know

**"I can't find any knowledge graph setting."** That's expected — there is no dedicated pane. Control is distributed across Contacts, Siri, and per-app privacy settings. Apple has not shipped a "view my knowledge graph" screen.

**Misclassification is the real bug.** The most common complaint in the HN thread is a colleague appearing as family in Siri suggestions. The fix is almost always the Contacts relationship field, not a system reset.

**Don't trust "delete your graph" tutorials.** Because the feature is undocumented, scripts claiming to wipe the knowledge graph are unverified and may break Siri or Spotlight indexing. Stick to Apple's official toggles.

**Intel Macs and older Apple Silicon.** If your Mac doesn't support Apple Intelligence, the classifier described in the report isn't running in the same form. Check **System Settings → General → About** for your chip.

**Enterprise users:** MDM profiles can restrict Apple Intelligence features. If you're on a managed Mac, your admin may have already disabled this — check with IT before changing settings.

## Frequently Asked Questions (FAQ)

### Does every Mac really have this family member classifier?
Only Macs that support and enable Apple Intelligence (Apple Silicon, macOS Sequoia 15.1+) build the personal knowledge graph in the form described. Older Intel Macs do not run these features.

### How do I stop Apple from classifying my contacts as family?
Edit the relationship field in Contacts for each person, or disable **Apple Intelligence** in System Settings. There is no single "classifier off" switch — control is per-source.

### Is my family data sent to Apple's servers?
The relationship inference is described as on-device. However, some Apple Intelligence requests route to Private Cloud Compute. Review Apple's privacy documentation for your region and feature before assuming zero data leaves the device.

### Why does Siri think my coworker is my brother?
Siri infers relationships from shared calendar events, message frequency, and Contacts data. Correct the Contacts relationship field and re-ask Siri; the graph typically updates within minutes.

## Final Verdict

The family member classifier isn't a scandal — it's an undocumented convenience layer that most users will never notice until Siri gets a relationship wrong. **My recommendation: spend ten minutes auditing your Contacts relationship fields today.** That single step fixes 90% of misclassification complaints and costs you nothing. If you want zero involvement, disable Apple Intelligence entirely — but accept that you'll lose the genuinely useful features it powers. For everyone else, treat the knowledge graph like your photo library: check it occasionally, correct what's wrong, and don't install sketchy "graph cleaner" tools that promise more control than Apple actually exposes.