---
title: "Collabora vs Microsoft Office: Why Formatting Breaks & How to Fix It"
description: "Danish government ditched Collabora after formatting failures. Learn why DOCX styles break in open-source suites and 7 fixes to prevent layout chaos."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Collabora Broke Denmark's Office Migration (And Why Your DOCX Files Break Too)

Denmark's digitization ministry abandoned Collabora in under six months—and the culprit wasn't licensing costs or security. It was **style and paragraph formatting**. Employees watched bullet lists drift, headers resize, and paragraph spacing collapse the moment a DOCX round-tripped between Collabora and Microsoft Office. If you've ever opened a Word document in LibreOffice or Collabora and found your carefully aligned tables scrambled, you're hitting the exact same wall.

Here's the direct takeaway: **Collabora is not broken—it's just interpreting OOXML differently than Microsoft does.** The fix isn't abandoning open-source software. It's understanding where the two engines diverge and applying the right workarounds before you share a single file. This guide breaks down the root causes, gives you a step-by-step formatting-stability checklist, and tells you when Collabora is genuinely worth it.

## Collabora vs Microsoft Office: Where Formatting Actually Breaks

The Danish failure wasn't random. It clustered around a handful of known OOXML compatibility gaps. Here's what breaks and why:

| Feature | Microsoft Office Behavior | Collabora Behavior | Severity |
|---|---|---|---|
| **Paragraph spacing** | Uses `w:spacing` with context-dependent "auto" | Rounds to fixed points, ignores context | High |
| **Style inheritance** | Cascading with "based-on" chains | Partial cascade; orphaned styles reset | High |
| **Table autofit** | Recalculates on open | Preserves stale widths, overflows margins | Medium |
| **Numbered lists** | Continuous numbering across sections | Restarts or renumbers unpredictably | High |
| **Font substitution** | Ships Calibri/Cambria metrics | Substitutes (e.g., Carlito) with different kerning | Medium |
| **Track changes** | Full fidelity | Loses comment anchors on export | Medium |
| **Headers/footers** | Linked-to-previous section logic | Breaks link on section insert | Low |

The pattern: **Microsoft's engine is stateful and context-aware; Collabora's is more literal.** A paragraph marked "space after: auto" gets a fixed value in Collabora, which then compounds across a 40-page policy document.

## Step-by-Step: 7 Fixes to Stop DOCX Formatting Drift

Follow these in order. Each one eliminates a specific failure class the Danish ministry hit.

1. **Lock paragraph spacing to explicit values.** In Word, select all (Ctrl+A) → Paragraph → set "Before/After" to fixed points (e.g., 6pt), never "Auto." Save. Collabora now has nothing to misround.

2. **Flatten style inheritance before export.** Run Word's *Styles Pane → Options → "Show only styles in use"* and delete orphaned styles. Fewer inheritance chains = fewer resets.

3. **Convert "auto" table widths to fixed.** Select each table → Table Properties → uncheck "Preferred width: Auto" → set explicit cm/inches. This kills the overflow bug.

4. **Restart-proof your numbered lists.** Use a single multilevel list definition per document (Define New Multilevel List), not per-section restarts. Collabora honors one continuous definition far more reliably.

5. **Embed or standardize fonts.** If your org uses Calibri, install **Carlito** (metric-compatible) on Collabora servers. It's the officially recommended substitute and preserves line breaks.

6. **Test the round-trip before rollout.** Open → edit → save in Collabora → reopen in Word. Check: page count, table alignment, list numbering, header links. Any drift = fix at the source, not in Collabora.

7. **Use ODT internally, DOCX only at the boundary.** For documents that never leave your org, ODT eliminates the OOXML translation layer entirely. Convert to DOCX only for external sharing.

**Pro tip:** Collabora Online 24.x added improved `w:spacing` handling, but it's still not 1:1. Always validate against your actual Word version—Office 2019 and Microsoft 365 render differently too.

## What You Should Know Before Migrating (The Denmark Lesson)

The Danish collapse wasn't a Collabora product failure—it was a **change-management and validation failure**. Three hard truths:

- **Pilot with your real documents, not sample files.** The ministry tested generic docs; employees used complex policy templates with nested tables and tracked changes.
- **Budget for a formatting QA layer.** Enterprises running Collabora successfully (e.g., several EU public bodies) maintain a "document hygiene" standard: fixed spacing, no auto-widths, standardized fonts. It's a one-time cost that pays off permanently.
- **Hybrid is legitimate.** Many orgs keep Word for authoring complex documents and use Collabora/Nextcloud for review, co-editing, and read-only access. That split avoids the round-trip problem entirely.

**Cost reality check:** Microsoft 365 E3 runs ~$36/user/month. Collabora Online via a Nextcloud partner is roughly $2–$8/user/month at scale. The savings are real—but only if you invest the saved budget into document standards and a small QA workflow. Skip that, and you repeat Denmark's six-month collapse.

## Frequently Asked Questions (FAQ)

### Why does my Word document lose formatting in Collabora?
Collabora interprets OOXML more literally than Microsoft Office. "Auto" spacing, inherited styles, and table autofit get resolved to fixed values, which then compound across pages. Locking explicit values before export prevents most drift.

### Is Collabora a viable Microsoft Office replacement in 2026?
For organizations willing to standardize document templates and validate round-trips, yes—at a fraction of Microsoft's cost. For teams that author complex, heavily styled documents daily and share them externally, a hybrid model (Word for authoring, Collabora for collaboration) is safer.

### What font replaces Calibri in Collabora?
**Carlito** is the metric-compatible open-source substitute for Calibri, and **Caladea** substitutes Cambria. Installing them on your Collabora server preserves line breaks and pagination.

### Did Denmark really abandon open-source over formatting?
Reports indicate the digitization ministry's Collabora pilot ended in under six months, with employees citing style and paragraph formatting frustrations among the complaints. It reflects a validation gap, not a fundamental flaw in open-source office suites.

## Final Verdict

**Don't blame Collabora—blame the round-trip.** If you're evaluating it as a Microsoft Office replacement, run a two-week pilot using your ten messiest real documents, apply the seven fixes above, and measure drift. If your team authors simple-to-moderate documents, Collabora delivers 80–90% of Microsoft's cost savings with a manageable formatting discipline. If your workflow lives and dies on pixel-perfect complex templates shared externally, keep Word for authoring and deploy Collabora for co-editing. The Danish ministry skipped the validation step; you don't have to.