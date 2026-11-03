---
title: "Sageworks Outage: How to Protect Your Bank's Vendor Risk Now"
description: "Sageworks taken offline by Abrigo after a suspected cyberattack. Here's how to build a third-party risk contingency plan and audit your fintech vendors."
pubDate: 2026-11-03
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Sageworks Outage: What Happened and What You Must Do Now

Abrigo has restored its Sageworks risk management application after an outage triggered by "irregular activity" in its environment—but borrower-facing capabilities remain offline, and the suspected cyberattack is a wake-up call for every bank and credit union running third-party risk software. If your institution depends on Sageworks for credit analysis, ALLL calculations, or loan review, the outage window exposed a hard truth: single-vendor concentration is a business continuity risk. This guide gives you a concrete, step-by-step contingency plan to keep lending workflows running, audit your fintech vendor stack, and harden your third-party risk posture—without waiting for the next outage.

## Step-by-Step: Building a Sageworks Contingency Plan

The goal is simple: keep credit decisions, ALLL provisioning, and regulatory reporting moving even when a core risk platform goes dark. Work through these steps in order.

1. **Inventory every Sageworks dependency.** List each workflow the platform touches—credit memos, spreading, stress testing, CECL/ALLL, appraisal review, and any borrower-facing portals. Flag which are "mission-critical within 24 hours" versus "tolerable for a week."
2. **Export your data while access is available.** Pull loan-level data, historical spreads, and model outputs into a controlled, encrypted repository (e.g., a secured SharePoint or on-prem SQL instance). Confirm the export cadence and file formats with your Abrigo account manager.
3. **Stand up a documented manual fallback.** For credit analysis, that means a standardized spreadsheet template with locked formulas for debt service coverage and global cash flow. For ALLL, maintain a parallel model run quarterly so you're never starting from zero.
4. **Define an outage escalation tree.** Name a primary and backup owner for vendor communication, set a 4-hour check-in cadence during incidents, and pre-draft regulator notification language for your examiners.
5. **Test the plan annually.** Run a tabletop exercise where Sageworks is "unavailable for 72 hours" and time how long it takes to produce a credit decision and an ALLL estimate manually.
6. **Document the restore status.** Track which capabilities are live versus down—right now, borrower-facing features are the gap—and communicate that status to affected staff and borrowers.

### Vendor Risk Quick-Audit Checklist

| Control Area | What to Verify | Red Flag |
|---|---|---|
| Data backup | Off-platform, encrypted, tested restore | Backup lives only in vendor cloud |
| Contract terms | RTO/RPO in SLA, breach notification window | No defined recovery time |
| Sub-processors | Full list of downstream vendors | Unknown fourth parties |
| Access controls | MFA, least-privilege, SSO | Shared admin credentials |
| Exit strategy | Data portability clause, export formats | Proprietary-only export |

## Common Issues, Alternatives, and What You Should Know

**Alternatives to evaluate for credit analysis and ALLL:** Moody's Analytics (Lending Suite), nCino (credit + workflow), Baker Hill, and Fiserv's lending tools are the usual comparison set. Each carries its own concentration risk—so the lesson isn't "switch vendors," it's "never rely on one."

**The borrower-facing gap matters.** If your institution uses Sageworks for borrower portals or document collection, route those borrowers to a secure email or e-signature workflow (DocuSign, Adobe Sign) temporarily, and notify them in writing. Keep a log for examiners.

**Cost reality check:** Building a full parallel system is expensive. A pragmatic middle path—quarterly manual ALLL runs plus an encrypted data export—costs a fraction of a second platform license and satisfies most continuity expectations.

**Regulatory angle:** OCC and FDIC examiners increasingly ask for evidence of tested third-party contingency plans. Document this outage response; it becomes audit evidence.

## Frequently Asked Questions (FAQ)

### Is Sageworks still down after the suspected cyberattack?
Abrigo has restored the core Sageworks risk management application, but borrower-facing capabilities remained unavailable as of the latest update. Confirm current status directly with your Abrigo account representative before resuming normal workflows.

### What should banks do if their fintech vendor is hit by a cyberattack?
Activate your third-party incident response plan: freeze non-essential data sharing, verify backups are intact, switch to documented manual fallbacks for critical workflows, and notify regulators per your incident policy. Document every step for audit purposes.

### What is a reasonable RTO for a risk management vendor?
Industry practice targets a recovery time objective of 4–24 hours for mission-critical financial applications, with a recovery point objective under 1 hour. If your contract doesn't specify these, negotiate them at renewal.

### How do I audit a fintech vendor's security posture?
Request their SOC 2 Type II report, penetration test summary, sub-processor list, and breach notification terms. Verify MFA and least-privilege access are enforced, and confirm data export portability in writing.

## Final Verdict

Don't wait for the postmortem—treat this outage as your trigger to build a tested contingency plan. Export your Sageworks data today, document a manual credit and ALLL fallback, and put RTO/RPO language into your next vendor contract. The institutions that rank this as a one-off news story will be the ones scrambling during the next outage; the ones that build a parallel process now will keep lending through it.