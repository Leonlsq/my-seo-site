---
title: "Reduce Blast Radius After PHP2Shell: A Practical Guide"
description: "Learn how to reduce blast radius after PHP2Shell with service account limits, API key scoping, and AI agent permissions that contain breaches fast."
pubDate: 2026-10-29
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Blast Radius Beats CVSS After PHP2Shell

PHP2Shell proved the uncomfortable truth security teams keep relearning: a critical CVSS 9.8 score tells you how bad a vulnerability *could* be, not how bad a breach *will* be in your environment. Attackers weaponized the flaw fast — often before patch windows opened — which means the organizations that survived intact weren't necessarily the fastest patchers. They were the ones whose compromised service accounts, API keys, and AI agents couldn't reach anything valuable. This guide gives you a concrete, step-by-step playbook to shrink your blast radius so that the next PHP2Shell-style exploit becomes a contained incident instead of a company-wide crisis.

The core principle: **assume compromise, then limit what a compromised identity can do.** CVSS measures exploit severity. Blast radius measures your exposure. Only one of those is under your control today.

## Step-by-Step: Shrinking Your Blast Radius in 6 Phases

### Phase 1: Inventory Every Non-Human Identity (Day 1–2)
You can't contain what you can't see. Pull a full list of machine identities across your stack:

- **Service accounts** in your cloud IAM (AWS IAM roles/users, Azure managed identities, GCP service accounts)
- **API keys and tokens** in CI/CD secrets, `.env` files, and vaults
- **AI agents and automation bots** with OAuth grants or long-lived credentials
- **Webhook signing secrets** and integration tokens (Slack, GitHub, payment processors)

Export each identity with: owner, creation date, last-used timestamp, and attached permissions. Anything with no owner or no usage in 90 days is an immediate candidate for revocation.

### Phase 2: Apply Least Privilege to Service Accounts (Day 2–4)
Replace wildcard and admin-level grants with scoped roles. A practical checklist:

| Current Grant | Risky Pattern | Safer Replacement |
|---|---|---|
| `s3:*` on `*` | Full bucket access | `s3:GetObject` on specific prefix |
| `iam:*` | Full IAM control | Read-only + scoped `PassRole` |
| DB superuser | App can DROP tables | Read/write on one schema only |
| Global API token | One key for everything | Per-service keys with TTL |

**Rule of thumb:** if a service account can delete data or create new identities, it should require a break-glass approval, not a standing permission.

### Phase 3: Scope and Rotate API Keys (Day 4–5)
- Set **maximum TTLs** on all keys (90 days max, 24 hours for high-privilege tokens).
- Enable **IP allowlisting** or mTLS where the API supports it.
- Split monolithic keys into per-environment keys (dev/staging/prod never share a token).
- Move secrets out of `.env` files into a secrets manager with audit logging (Vault, AWS Secrets Manager, Doppler).

### Phase 4: Constrain AI Agents and Automation (Day 5–7)
AI agents are the newest blast-radius multiplier because they often hold broad OAuth scopes and act autonomously. Harden them:

1. Give each agent its **own dedicated identity** — never reuse a human admin account.
2. Restrict OAuth scopes to the minimum the agent's task requires (read-only where possible).
3. Enforce **human-in-the-loop approval** for destructive actions (deletes, payments, permission changes).
4. Log every agent action with the triggering prompt or event for forensics.
5. Set rate limits and spend caps so a runaway or hijacked agent can't cause mass damage.

### Phase 5: Add Network and Data Boundaries (Day 7–9)
Identity limits fail if the network is flat. Layer in:

- **Egress filtering** so a compromised service can't exfiltrate data to unknown hosts.
- **Micro-segmentation** between app tiers (web → app → DB only).
- **Read-only replicas** for analytics and AI workloads so a breach can't mutate production data.

### Phase 6: Test the Blast Radius (Ongoing)
Run a quarterly **"assume breach" drill**: pick a service account, simulate its compromise, and document exactly what an attacker could reach. If the answer is "the whole cloud account," you have work to do.

## Common Issues, Alternatives, and What You Should Know

**"Least privilege breaks our apps."** It does — temporarily. Roll out scoped permissions in monitor-only mode first, log denied calls for two weeks, then enforce. This surfaces hidden dependencies without outages.

**"We can't rotate keys without downtime."** Use dual-key rotation: issue a new key, deploy it, verify traffic, then revoke the old one. Most major APIs support overlapping keys.

**"Our AI agent needs broad access to be useful."** Then isolate it: run it in a sandboxed account with read-only data access, and gate write actions behind approval workflows. Broad access with narrow execution beats narrow access that gets bypassed.

**Cost note:** secrets managers and micro-segmentation tooling add spend, but compare it to the average breach cost — containment savings dwarf the tooling bill. Free wins first: revoke unused keys, add TTLs, and split admin roles.

## Frequently Asked Questions (FAQ)

### What does "blast radius" mean in cybersecurity?
Blast radius is the total scope of systems, data, and permissions an attacker can reach after compromising a single identity or vulnerability. It's determined by your permission grants, network segmentation, and credential lifespan — not by the vulnerability's CVSS score.

### Why does blast radius matter more than a CVSS score after PHP2Shell?
CVSS measures theoretical severity; blast radius measures real-world damage potential in *your* environment. A CVSS 9.8 flaw on a tightly scoped service account may cause less damage than a CVSS 7.0 flaw on a wildcard admin key. Attackers exploit fast, so containment matters more than severity ratings.

### How do I reduce the blast radius of a compromised API key?
Scope the key to a single service and environment, set a short TTL, enable IP allowlisting, and monitor usage for anomalies. Rotate keys on a schedule using dual-key overlap to avoid downtime.

### Should AI agents have their own service accounts?
Yes. Every AI agent should have a dedicated identity with minimum OAuth scopes, human approval for destructive actions, full action logging, and rate/spend caps. Never let an agent inherit a human admin account.

## Final Verdict

Stop treating the CVSS score as your risk number. After PHP2Shell, the metric that predicts whether you survive the next critical exploit is blast radius — and it's fully within your control. Start this week with the free, high-impact moves: inventory non-human identities, revoke unused keys, add TTLs, and split admin roles. Then move to scoped service accounts, network segmentation, and AI agent guardrails. Patch fast when you can — but build your defenses assuming the patch won't arrive in time. Containment is the strategy that scales.