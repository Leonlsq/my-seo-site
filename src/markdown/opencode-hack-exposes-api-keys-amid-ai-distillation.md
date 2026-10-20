---
title: "OpenCode API Key Leak: How to Revoke Keys & Secure Your Repo"
description: "OpenCode exposed API keys in a breach tied to AI distillation attacks. Here's how to revoke leaked keys, rotate secrets, and lock down your AI coding setup fast."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## OpenCode API Key Leak: What Actually Happened and What You Must Do First

OpenCode, the open-source AI coding agent, has confirmed that a small number of users had the API keys they configured for external model providers exposed in a security breach — with early reporting tying the incident to **AI distillation attacks**, where attackers probe a product to harvest model behavior and, in some cases, the credentials powering it. If you run OpenCode with your own OpenAI, Anthropic, or other provider keys, the single most important takeaway is this: **treat any key that touched OpenCode as compromised until you've rotated it.** This guide walks you through revocation, rotation, container hardening, and the config changes that stop a repeat — in about 15 minutes.

## Step-by-Step: Revoke, Rotate, and Re-Secure OpenCode

### Step 1 — Identify every key OpenCode could have seen
OpenCode stores provider credentials in a local config file, typically `~/.config/opencode/opencode.json` (or `auth.json` depending on version), and reads them from environment variables. Audit both:

```bash
# Check config files
cat ~/.config/opencode/opencode.json 2>/dev/null
cat ~/.config/opencode/auth.json 2>/dev/null

# Check environment variables
env | grep -iE 'OPENAI|ANTHROPIC|GEMINI|OPENROUTER|GROQ|DEEPSEEK'
```

List every provider key you've ever pasted into OpenCode. Include keys you only used once — distillation attacks target exactly those low-attention credentials.

### Step 2 — Revoke before you rotate
Revocation kills the old key; rotation alone can leave a valid-but-leaked key alive if the old one isn't deleted. Do this per provider:

| Provider | Where to revoke | Typical propagation |
|---|---|---|
| OpenAI | platform.openai.com → API keys → Revoke | Immediate |
| Anthropic | console.anthropic.com → API keys → Delete | Immediate |
| Google Gemini | aistudio.google.com → API keys → Delete | ~1–5 min |
| OpenRouter | openrouter.ai → Keys → Delete | Immediate |
| Groq | console.groq.com → API Keys → Delete | Immediate |
| DeepSeek | platform.deepseek.com → API Keys → Delete | Immediate |

### Step 3 — Issue new keys with least privilege
- Create a **new** key per provider, never reusing the old name.
- Set **spend/usage limits** on each key (OpenAI and Anthropic both support project-level budgets).
- Where supported, scope keys to a single project rather than account-wide.
- Store new keys in environment variables or a secrets manager — **not** committed files.

### Step 4 — Purge secrets from your repo and shell history
If your key ever lived in a tracked file, removing it in a new commit is not enough — it stays in Git history.

```bash
# Remove from shell history
history | grep -iE 'sk-|api_key'   # inspect
# then delete those lines or clear with: history -c

# Scrub Git history (git-filter-repo recommended)
git filter-repo --path ~/.config/opencode/opencode.json --invert-paths
```

Add defensive ignores immediately:

```gitignore
opencode.json
auth.json
.env
.env.*
!.env.example
```

### Step 5 — Lock down your OpenCode runtime
- **Run OpenCode in a container or VM** with no host credential mounts.
- Set `chmod 600` on config files: `chmod 600 ~/.config/opencode/*.json`.
- Disable telemetry/logging that could capture request headers.
- Pin OpenCode to a reviewed release tag rather than tracking `main`.

## Common Issues, Alternatives, and What You Should Know

**"I don't see the breach email — am I safe?"** Not necessarily. The notification went to a *small number* of affected users, but the underlying exposure vector (keys stored in a shared or logged location) may apply to you. Rotate anyway; the cost is minutes.

**Distillation attacks explained:** Attackers systematically query an AI product to reconstruct model behavior or harvest credentials embedded in client-side configs. OpenCode's bring-your-own-key model means a leaked config is a leaked wallet — your provider bill, not OpenCode's, absorbs the abuse.

**Watch your billing dashboards for 72 hours** after rotation. Look for spikes, unfamiliar model usage, or requests from unexpected regions. If you see anomalies, contact provider support with timestamps.

**Alternatives if you want to reduce key exposure:**
- Route through a **proxy/gateway** (e.g., LiteLLM) so the client holds one scoped token, not raw provider keys.
- Use **provider-hosted auth** or short-lived tokens where available.
- Prefer **local models** (Ollama, LM Studio) for sensitive repos — no external key at all.

**Cost reality check:** A leaked OpenAI key can run hundreds of dollars in hours. Setting a hard monthly cap is the cheapest insurance you'll ever buy.

## Frequently Asked Questions (FAQ)

### Did the OpenCode breach expose my API keys to the public?
OpenCode notified a small number of users that keys used with external providers were exposed in the breach. Whether *your* specific key leaked depends on your setup — but if you can't confirm otherwise, assume exposure and revoke immediately.

### How do I know if my OpenCode API key was leaked?
Check your inbox for an OpenCode notification, then cross-reference provider usage logs and billing for unexpected activity. The only reliable remediation is revocation plus rotation, regardless of confirmation.

### Are AI distillation attacks the same as a data breach?
No. Distillation attacks harvest model behavior or embedded credentials through systematic querying; a breach is unauthorized access to stored data. They can overlap — harvested keys enable further abuse — which is why rotation is the priority.

### Should I stop using OpenCode after this incident?
Not necessarily. Keep it if you run it sandboxed with scoped, budget-capped keys and no committed secrets. If you can't guarantee that hygiene, use a proxy or local models instead.

## Final Verdict

Don't wait for a confirmation email to act. **Revoke every provider key that ever touched OpenCode, issue new scoped keys with hard spend limits, scrub your Git history, and run OpenCode in an isolated environment.** The breach was limited, but the lesson is universal: in bring-your-own-key AI tooling, your credentials are the blast radius. Treat them that way and OpenCode remains a genuinely useful tool — just one you now operate with a security-first config.