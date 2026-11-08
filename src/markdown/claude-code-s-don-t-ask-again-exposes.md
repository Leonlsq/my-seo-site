---
title: "Claude Code Leaked Passwords? How to Fix 'Don't Ask Again"
description: "Stop Claude Code and AI agents from leaking secrets to GitHub. Step-by-step fix for the 'Don't Ask Again' bug that exposed 1,122 files."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Claude Code's "Don't Ask Again" Leaked Secrets: The 5-Minute Fix

If you clicked "Don't Ask Again" in Claude Code or another AI coding agent, you may have unknowingly approved a command that writes your `.env` secrets, API keys, or database passwords into a public GitHub repo. A new Apiiro security report found **1,122 public GitHub files** containing credentials leaked exactly this way. The root cause isn't a Claude vulnerability—it's a **permission-persistence design flaw**: once you suppress a prompt, the agent can repeat the same class of command indefinitely without asking again. This guide shows you how to audit what you approved, revoke the persistent permission, rotate any exposed secrets, and lock down your workflow so it can't happen again.

## Step-by-Step: Audit and Fix the "Don't Ask Again" Exposure

Work through these steps in order. Do the audit first—rotation before audit means you may rotate a key that gets re-leaked by a still-active permission.

### Step 1: Find what you auto-approved
Claude Code stores persistent tool permissions in your user and project settings. Check these locations:

- **Project-level:** `.claude/settings.json` and `.claude/settings.local.json` inside the repo root
- **User-level:** `~/.claude/settings.json` (or `%USERPROFILE%\.claude\settings.json` on Windows)

Open each file and look for an `allow` array under `permissions`. Any entry like `Bash(git push:*)`, `Bash(cat:*)`, or broad wildcards such as `Bash(*)` is a red flag. A wildcard on `cat`, `echo`, or `curl` is what lets an agent read a `.env` and pipe it into a commit.

### Step 2: Revoke the persistent permission
Edit the `allow` list and remove the broad entries. Replace wildcards with narrow, explicit commands:

```json
{
  "permissions": {
    "allow": ["Bash(npm test:*)", "Bash(git status:*)"],
    "deny": ["Bash(cat .env:*)", "Bash(git push:*)"]
  }
}
```

The `deny` list is your safety net—entries there always override `allow`. Deny anything that reads secret files or pushes to remotes.

### Step 3: Scan your repos for leaked secrets
Run a secret scanner across every repo you've used an AI agent in:

- **gitleaks:** `gitleaks detect --source . --verbose` (fast, free, CI-friendly)
- **TruffleHog:** `trufflehog git file://. --only-verified` (verifies live credentials)
- **GitHub native:** enable **Secret Scanning** + **Push Protection** in Settings → Code security

Also check commit history, not just the current tree—`git log -p | grep -iE 'api[_-]?key|password|secret|token'` catches secrets that were committed and later deleted.

### Step 4: Rotate everything that touched a public file
If a scanner flags a live key, **assume it's compromised**. Rotate in this order: cloud provider keys (AWS/GCP/Azure), database passwords, third-party API tokens, then SSH keys. Revoke old keys at the provider—deleting the file does not revoke the credential.

### Step 5: Re-harden the agent
| Setting | Recommended value | Why |
|---|---|---|
| `permissions.allow` | Explicit commands only | Blocks wildcard auto-approval |
| `permissions.deny` | `.env`, `*.pem`, `git push` | Hard stop on secret reads/pushes |
| `.gitignore` | `.env`, `.env.*`, `*.pem`, `secrets/` | Prevents accidental staging |
| GitHub Push Protection | Enabled | Blocks secrets at the server |
| Pre-commit hook | gitleaks `protect --staged` | Catches secrets before commit |

## Common Issues, Alternatives, and What You Should Know

**"I never clicked Don't Ask Again."** The setting can also be inherited from a shared `.claude/settings.json` committed by a teammate or a template repo. Audit project-level settings even if you don't remember approving anything.

**"The secret was deleted in a later commit."** Git history is permanent. The 1,122 files Apiiro found were public—crawlers and attackers index commit history, not just HEAD. You must rotate, not just delete.

**Alternatives to Claude Code's permission model:** Cursor and Aider offer similar per-command approval, but the same persistence trap exists. The safe pattern is universal: **deny-list secret paths, never allow wildcards, and keep `.env` out of any directory the agent can `cat`.** Consider running agents in a container with read-only mounts of your source and no access to `~/.ssh` or `~/.aws`.

**Cost of a leak:** A single exposed AWS key can rack up thousands in crypto-mining charges within hours. GitHub's own data shows leaked secrets are exploited within minutes of becoming public—speed of rotation matters more than anything else.

## Frequently Asked Questions (FAQ)

### Did Claude Code itself get hacked?
No. The Apiiro report describes a **permission-persistence flaw in how users approve agent commands**, not a breach of Anthropic's servers. The agent did what it was told after a user suppressed a prompt.

### How do I know if my repo is one of the 1,122 affected files?
You can't rely on a public list—Apiiro's count is aggregate. Run gitleaks or TruffleHog on your own repos and enable GitHub Secret Scanning. If a verified credential is flagged, treat it as exposed.

### Does "Don't Ask Again" apply to all commands or just one?
It persists the **specific command pattern** (e.g., `Bash(git push:*)`). But broad patterns like `Bash(*)` or `Bash(cat:*)` effectively approve everything in that class, which is how secrets get read and pushed.

### Is it safe to keep using Claude Code after this?
Yes—with a deny-list and no wildcards. The tool is fine; the default "approve broadly" habit is the risk. Treat every "Don't Ask Again" click as a permanent security policy change.

## Final Verdict

The "Don't Ask Again" leak isn't a reason to abandon AI coding agents—it's a reason to stop clicking that button carelessly. **Do this today:** open your `.claude/settings.json`, strip every wildcard from `allow`, add a `deny` list for `.env` and `git push`, run gitleaks on every repo an agent has touched, and rotate anything it flags. Then enable GitHub Push Protection so a future slip gets blocked at the server, not discovered in a blog post. Five minutes of config now beats a compromised cloud bill later.