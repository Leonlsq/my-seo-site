---
title: "Northflank Breach: How to Rotate Leaked AI API Keys Fast"
description: "Northflank breach exposed customers' AI API keys. Follow this step-by-step guide to rotate OpenAI, Anthropic, and Gemini keys, audit usage, and lock down secrets."
pubDate: 2026-11-02
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Northflank Breach Exposed Your AI API Keys — Here's How to Rotate Them Now

Northflank has confirmed a security breach that allowed unauthorized parties to abuse customers' stored AI API keys. If you host anything on Northflank — or you've ever pasted an OpenAI, Anthropic, or Google Gemini key into its secret manager or environment variables — treat that key as compromised right now. The direct takeaway: **rotate every credential stored on Northflank within the next hour**, starting with your AI provider keys, because those are the ones attackers are actively burning through. This guide walks you through the exact rotation sequence, how to spot abuse in your billing dashboard, and how to prevent a repeat.

## Step-by-Step Guide to Rotating Compromised AI API Keys

Work through this in order. Each step takes 2–5 minutes, and the whole process should take under 30 minutes for a typical stack.

### Step 1: Inventory every secret stored on Northflank
Before you rotate anything, list what's exposed. Check these locations in your Northflank dashboard:

- **Secret Groups** (project-level and organization-level)
- **Environment variables** on each service
- **Build arguments** that reference API keys
- **CI/CD integrations** and webhook signing secrets
- **Container registry credentials**

Export or screenshot the list. You'll need it to verify nothing is missed.

### Step 2: Revoke first, create second
The single biggest mistake is creating a new key before revoking the old one. Revoke first so the attacker's window closes immediately.

| Provider | Where to Revoke | Where to Create New |
|---|---|---|
| OpenAI | platform.openai.com → API keys → Revoke | Same page → "Create new secret key" |
| Anthropic | console.anthropic.com → API Keys → Delete | Same page → "Create Key" |
| Google Gemini | aistudio.google.com → Get API key → Delete | Same page → "Create API key" |
| Azure OpenAI | Azure Portal → Key Vault / resource → Regenerate Key 1 & 2 | Same resource → Keys and Endpoint |
| AWS Bedrock | IAM → Users → Security credentials → Deactivate access key | Same user → Create access key |

### Step 3: Check for abuse before you delete the evidence
Before revoking, screenshot your **usage dashboards** for the last 7 days. You need this for chargeback disputes and to understand the blast radius.

- **OpenAI:** Usage → filter by project → look for spikes in unfamiliar models (e.g., `gpt-4o` calls you never made).
- **Anthropic:** Console → Usage → check token counts per day against your baseline.
- **Google:** Cloud Console → APIs & Services → Quotas → check Gemini API request counts.

If you see usage from IP ranges or regions you don't operate in, note the timestamps — providers sometimes credit fraudulent usage if you report within 24–48 hours.

### Step 4: Deploy new keys with scoped permissions
Don't just swap the string. Tighten it:

1. **Create project-scoped keys** instead of org-wide keys where the provider supports it (OpenAI Projects, Anthropic Workspaces).
2. **Set spend limits** on each key — e.g., a $50/month hard cap on a dev key.
3. **Restrict by IP** if your Northflank services egress from static IPs (Northflank supports static egress IPs on paid plans).
4. **Use separate keys per environment** — never share a production key with staging.

### Step 5: Update Northflank and redeploy
Update each Secret Group and environment variable, then trigger a redeploy so running containers pick up the new values. Verify by checking service logs for successful API calls.

### Step 6: Rotate everything else too
Northflank's advisory says rotate **all** credentials, not just AI keys. That includes:

- Database passwords
- JWT signing secrets (rotating these logs out all users — plan for it)
- OAuth client secrets
- Webhook signing keys (Stripe, GitHub, etc.)
- SSH deploy keys

## Common Issues, Alternatives, and What You Should Know

**"My old key still works after I deleted it."** Some providers have propagation delays of up to 5 minutes. Don't panic — but don't assume the key is dead until you get a 401 from a test call.

**Billing disputes.** OpenAI and Anthropic both review fraudulent usage claims case-by-case. File a support ticket within 48 hours with your usage screenshots and the Northflank incident reference. Approval isn't guaranteed, but it's your best shot.

**Should you leave Northflank?** Not necessarily — but if you stored long-lived, org-wide keys there, that's a configuration failure on your side too. Alternatives like Railway, Render, and Fly.io face the same class of risk; the fix is secret hygiene, not platform-hopping. That said, if Northflank's post-incident transparency (timeline, root cause, remediation) disappoints you over the coming weeks, migrating is reasonable.

**Better long-term pattern:** stop storing raw AI keys in hosting platforms at all. Put a thin proxy (e.g., LiteLLM, Cloudflare AI Gateway) in front of your providers, store the real key only in the proxy's secret store, and give Northflank a scoped proxy token with rate limits and logging. If that token leaks, your exposure is capped.

## Frequently Asked Questions (FAQ)

### Did the Northflank breach expose my AI API keys in plaintext?
Northflank has advised customers to treat all stored credentials and secrets as compromised and rotate them immediately. Assume plaintext exposure and rotate — don't wait for forensic confirmation.

### How do I know if my OpenAI or Anthropic key was abused after the Northflank breach?
Check your provider usage dashboards for unexpected spikes, unfamiliar models, or traffic from regions you don't operate in. Compare against your 30-day baseline and screenshot everything before revoking.

### Can I get a refund for AI API usage stolen via the Northflank breach?
Possibly. OpenAI and Anthropic review fraudulent-usage claims individually. Report within 24–48 hours with usage screenshots and the incident reference; credits are discretionary, not guaranteed.

### Do I need to rotate database passwords and JWT secrets too, or just AI keys?
Rotate everything stored on Northflank: database passwords, JWT signing secrets, OAuth secrets, webhook signing keys, and deploy keys. AI keys are just the ones attackers monetize fastest.

## Final Verdict

Rotate your AI API keys **today** — revoke before you recreate, screenshot your usage first, and set spend caps on every new key. Then go further than Northflank's advisory requires: move long-lived provider keys behind a proxy, scope every key to a single project, and separate keys per environment. The breach is Northflank's failure, but the blast radius was your secret architecture. Fix both starting now.