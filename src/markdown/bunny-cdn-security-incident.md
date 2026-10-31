---
title: "Bunny CDN Security Incident: How to Audit Your Account Now"
description: "Worried about the Bunny CDN security incident? Learn how to audit API keys, rotate credentials, and harden your pull zones step by step."
pubDate: 2026-10-31
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Bunny CDN Security Incident: What Actually Happened and What You Should Do

If you woke up to the Bunny CDN status page incident (`p6gf1by9kr7m`) trending on Hacker News, your first question is probably: *am I exposed, and what do I change right now?* The short answer: treat this like a credential-hygiene fire drill. Whether the incident involved unauthorized access to account tooling, a leaked token, or a misconfigured permission surface, the remediation playbook is the same — **rotate secrets, scope permissions, and verify your pull zones**. This guide gives you a concrete, step-by-step audit you can run in under 30 minutes, plus the exact settings most users overlook.

The core takeaway: **don't wait for a full post-mortem to rotate API keys and purge-keys.** CDN accounts are high-value targets because a compromised key can redirect traffic, inject content, or rack up bandwidth bills. Below is the practical checklist.

## Step-by-Step: Audit and Harden Your Bunny CDN Account

Work through these in order. Each step is independent, so you can parallelize with a teammate.

### 1. Inventory every API key
- Go to **Dashboard → Account Settings → API Keys**.
- List each key, its creation date, and its last-used timestamp.
- **Delete any key you don't recognize** or that hasn't been used in 90+ days.
- Note: Bunny lets you scope keys per **pull zone**, **storage zone**, or **account-wide**. Account-wide keys are the biggest risk — downgrade them.

### 2. Rotate the keys you actually need
1. Create a **new** key with the minimum scope (e.g., purge-only for a CI pipeline).
2. Deploy the new key to your app/CI secrets manager.
3. Confirm traffic and purges still work.
4. **Revoke the old key.** Never leave both live "just in case."

### 3. Rotate storage zone passwords
Storage zones use separate credentials from API keys. If you use Bunny Storage for origin or static assets:
- Regenerate the **storage zone password** under **Storage → [zone] → Password**.
- Update any S3-compatible clients (rclone, AWS SDK, WordPress offload plugins) with the new value.

### 4. Check pull zone origin and hostname config
A compromised key can silently repoint a pull zone. Verify:
- **Origin URL** points to your real server, not an unknown host.
- **Custom hostnames** and **SSL certificates** are ones you issued.
- **Edge rules / rewrites** don't contain injected redirects.
- **Blocked/hotlink protection** settings are as you left them.

### 5. Review billing and traffic anomalies
- Open **Billing → Usage** and compare the last 7 days to your baseline.
- A sudden spike in bandwidth or requests from unexpected regions is a red flag.
- Set a **billing alert / usage cap** if you haven't already.

### 6. Enable account-level protections
| Setting | Where | Recommended |
|---|---|---|
| Two-factor auth (2FA) | Account → Security | **On** |
| IP allowlist for API | API key settings | On for admin keys |
| Key expiry | API key creation | 90 days max |
| Billing usage alerts | Billing | On |

## Common Issues, Workarounds, and What You Should Know

**"I rotated my key and my site broke."** Usually a cached purge key or an environment variable that wasn't updated. Check your CI secrets and any WordPress/Next.js plugins that store the key separately.

**"I can't tell if I was affected."** Bunny's status page and any follow-up email are your source of truth. Absent a direct notice, assume *possible* exposure and rotate anyway — rotation is cheap; a hijacked pull zone is not.

**Alternatives if you want to diversify risk:** Cloudflare (free tier, strong WAF), Fastly (enterprise), or AWS CloudFront (deep IAM integration). Many teams run **Bunny for cost + Cloudflare for DNS/WAF** as a layered setup. See the comparison below.

| Provider | Free tier | Best for | Key scoping |
|---|---|---|---|
| Bunny CDN | Trial only | Low-cost global edge | Per-zone keys |
| Cloudflare | Yes | WAF + DNS | Token scopes |
| CloudFront | Limited | AWS-native | IAM policies |

**Information-gain tip:** Bunny's per-zone key scoping is genuinely useful — most incidents escalate because teams use one account-wide key everywhere. Split keys by function (purge, storage, reporting) so a single leak has blast-radius limits.

## Frequently Asked Questions (FAQ)

### Was the Bunny CDN security incident a data breach?
Check the official status page incident (`p6gf1by9kr7m`) and any account email for scope. Regardless of classification, the safe move is to rotate API keys and storage passwords immediately — that remediation is correct whether or not your specific account was touched.

### How do I rotate a Bunny CDN API key safely?
Create a new scoped key, deploy it to your secrets manager, verify purges/traffic, then revoke the old key. Never run two live keys longer than needed for the cutover.

### Does Bunny CDN support two-factor authentication?
Yes — enable 2FA under Account → Security. Pair it with IP allowlisting on admin API keys for defense in depth.

### Should I switch CDN providers after this incident?
Not necessarily. If your keys are rotated and scoped, staying is reasonable given Bunny's pricing. If you need built-in WAF or enterprise SLAs, evaluate Cloudflare or Fastly.

## Final Verdict

**Rotate first, investigate second.** The Bunny CDN security incident is a reminder that CDN credentials are as sensitive as database passwords. Spend 30 minutes today: inventory keys, revoke stale ones, scope the rest per-zone, enable 2FA, and set billing alerts. If you're running a single account-wide key across every service, that's the real vulnerability — fix it now, regardless of how this specific incident resolves.