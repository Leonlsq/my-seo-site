---
title: "Figma Agent Features & Code Layers Beta: Setup Guide"
description: "Learn how to configure Figma's new agent permissions and use the Code Layers open beta to sync design tokens with production code in minutes."
pubDate: 2026-10-15
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Figma Agents and Code Layers: What Actually Changed for Your Workflow

Figma's latest release introduces two things that will change how you work: a permission framework that defines exactly what AI agents can and cannot do inside your files, and the long-awaited **Code Layers** feature, now in open beta. If you've been burned by an AI tool silently overwriting components or pushing untracked changes, the agent permission model is the fix you've been waiting for. This guide walks you through configuring agent scopes, enabling Code Layers, and avoiding the three most common setup mistakes that break token syncing on day one.

The short version: agents now operate under scoped, revocable permissions tied to your team's role settings, and Code Layers let you map design properties directly to code output without leaving the canvas.

## Step-by-Step: Configuring Agent Permissions and Enabling Code Layers

### Part 1 — Set Up Agent Permissions (Do This First)

1. Open your team workspace and go to **Settings → AI & Agents**.
2. Under **Agent Access**, choose one of three scopes:
   - **Read-Only** — agents can inspect layers, variables, and comments but cannot modify anything. Best for audit or documentation agents.
   - **Scoped Write** — agents can edit only the frames, pages, or component libraries you explicitly tag. Recommended for most teams.
   - **Full Write** — unrestricted editing. Only enable this for sandboxed files, never production libraries.
3. Assign a **role binding**: Viewer, Editor, or Admin. Agents inherit the *lower* of the agent scope and the user role, so an Editor-role agent with Read-Only scope still can't write.
4. Toggle **Require Approval for Structural Changes**. This forces agents to queue changes to components, styles, and variables for human review before committing.
5. Set an **expiry window** (7, 30, or 90 days). Agents auto-revoke at expiry — critical for contractors and temporary automation.

### Part 2 — Enable Code Layers Open Beta

1. Go to **Figma → Preferences → Labs** and toggle **Code Layers** on. It's available on Professional, Organization, and Enterprise plans.
2. Restart the desktop app (browser users: hard refresh with Ctrl/Cmd+Shift+R).
3. In any file, select a frame and open the new **Code** tab in the right panel.
4. Map properties using the syntax below:

| Design Property | Code Layer Syntax | Output |
|---|---|---|
| Fill color variable | `token:color.primary` | `var(--color-primary)` |
| Auto-layout gap | `spacing:8` | `gap: 8px` |
| Corner radius | `radius:md` | `border-radius: 8px` |
| Text style | `type:heading.lg` | `font: 600 24px/32px Inter` |

5. Click **Export → Code Layer JSON** to generate a token file. Drop it into your repo's `tokens/` folder and let your build pipeline consume it.

### Part 3 — Verify the Sync

Run a test change: update a color variable, then check that your Code Layer JSON reflects it within the sync interval (default 5 minutes, configurable down to 60 seconds on Enterprise).

## Common Issues, Workarounds, and What You Should Know

**Issue 1: Code Layers tab is missing.** You're likely on the Starter plan or an outdated desktop build. Update to the latest release — the beta requires a version shipped after the announcement.

**Issue 2: Agent changes get rejected silently.** This happens when the agent's scope is narrower than the target node. Check **Settings → AI & Agents → Activity Log** to see the exact rejection reason.

**Issue 3: Token names don't match your codebase.** Code Layers exports Figma variable names verbatim. Rename your variables to match your CSS custom properties *before* exporting, or you'll spend hours in find-and-replace.

**Cost and plan reality check:** Code Layers is free during open beta but Figma has signaled it will be a paid seat feature at general availability. Agent permissions are available on all paid tiers; the approval workflow and 60-second sync are Enterprise-only.

**Alternatives worth comparing:**

| Tool | Agent Permissions | Design-to-Code Sync | Starting Price |
|---|---|---|---|
| Figma (new) | Scoped + approval queue | Code Layers (beta) | $16/editor/mo |
| Penpot | None | Manual export | Free |
| Sketch | None | Assistants (limited) | $12/editor/mo |

## Frequently Asked Questions (FAQ)

### How do I revoke an agent's access in Figma?
Go to **Settings → AI & Agents → Active Agents**, select the agent, and click **Revoke**. Changes made before revocation remain in version history and can be restored via **File → Show Version History**.

### Is Figma Code Layers free?
Yes during the open beta on Professional, Organization, and Enterprise plans. Figma has indicated it will move to a paid feature at general availability, so build your workflow now while testing is free.

### What's the difference between agent scope and user role in Figma?
Agent scope limits what the agent itself can touch; user role limits what the person who deployed it can do. The effective permission is always the *more restrictive* of the two.

### Can Code Layers export to React or Swift?
The beta exports a token JSON file that any framework can consume. Native React and Swift code generation is on the roadmap but not in the current open beta.

## Final Verdict

If you run any AI automation inside Figma, **configure agent permissions before you touch Code Layers** — the approval queue alone will save you from a production library disaster. Code Layers is genuinely useful for token sync today, but treat the beta export as a staging artifact, not a source of truth, until general availability lands. Teams on Starter should wait; teams on Professional and above should enable both features this week and run a pilot on one component library before rolling out org-wide.