---
title: "One-Sender Email App Setup: Prefix Inboxes Explained"
description: "Learn how to set up one-sender inboxes with prefix routing, temporary addresses, and custom domains. Fix bounce errors and stop spam in 2026."
pubDate: 2026-10-15
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is a One-Sender Inbox and Why Should You Care?

If you have ever handed your email address to a newsletter, a SaaS trial, or a sketchy download page, you already know the pain: the second your address leaks, the spam never stops. The "Show HN" project making the rounds — an email app that accepts **only one sender per inbox** — attacks that problem at the root. Instead of filtering spam after it arrives, it refuses to accept mail from anyone except the first sender who writes to that address.

The core idea is simple but powerful. You get three inbox types:

- **One Sender** — locks to the first domain (or first email account for Gmail/Outlook) that sends mail. Everyone else bounces.
- **Temporary** — self-destructs after 24 hours, 7 days, etc., then bounces incoming mail.
- **Prefix** — declare a prefix like `service` and invent any suffix on the fly (`service-netflix`, `service$bank`), each creating a fresh one-sender inbox automatically.

This guide walks you through setup, the prefix workflow, and the most common bounce errors you will hit while testing. If you are migrating off Gmail aliases or a catch-all domain, this is the practical playbook.

## Step-by-Step: Setting Up Prefix Inboxes With Your Own Domain

The prefix system is where this app earns its keep. Here is the exact workflow.

1. **Bring your own domain.** Point your MX records to the app's mail servers. If you use Cloudflare DNS, add the MX entries at priority 10 and disable any existing catch-all forwarding rules that would intercept mail first.
2. **Declare your prefix.** Choose a short, memorable word — `service`, `shop`, `signup`. This becomes the namespace root. You only declare it once.
3. **Invent suffixes freely.** You do **not** pre-create inboxes. Typing `service-netflix` at signup creates the inbox the moment Netflix sends its first confirmation email.
4. **Let the lock engage.** The first sender to hit `service-netflix@yourdomain.com` claims it. Every subsequent sender bounces.
5. **Forward or archive.** Route confirmed mail to your real inbox, or leave it in the app and let the AI/MCP layer summarize it.

### Prefix Naming Rules That Actually Work

| Character | Example | Use Case |
|-----------|---------|----------|
| Hyphen `-` | `service-netflix` | Clean, readable, safe for most forms |
| Dollar `$` | `service$bank` | Bypasses forms that reject hyphens |
| Dot `.` | `service.amazon` | Mimics sub-addressing habits |

**Pro tip:** Use `$` for financial and banking signups. Plenty of legacy forms strip hyphens but pass the dollar sign through untouched.

## Common Issues: Bounce Errors and How to Fix Them

The one-sender lock is aggressive by design, which means you will trip over it during testing. Here is what breaks and why.

- **"Message rejected — sender not authorized."** You are emailing from a second address. This is expected. The inbox locked to whoever wrote first. Create a new suffix instead of fighting it.
- **Gmail/Outlook lock to account, not domain.** The app deliberately locks these to the specific email account rather than the whole `gmail.com` domain — otherwise every Gmail user on Earth would collide. If you sign up with a Gmail alias, the real account owns the inbox.
- **Temporary inbox still receiving after expiry.** Check whether you enabled "keep received messages." The inbox bounces new mail but retains old messages unless you toggle deletion.
- **Prefix inbox not auto-creating.** Almost always a DNS propagation delay. Wait 15–30 minutes after adding MX records, then send a test from a fresh address.
- **Forwarding loops.** If your destination inbox forwards back into the app, you create an infinite bounce. Whitelist the app's sending domain in your primary provider.

### One-Sender vs Temporary vs Prefix: Which Should You Use?

| Inbox Type | Lifespan | Best For | Weakness |
|------------|----------|----------|----------|
| One Sender | Permanent | Newsletters, single vendors | Breaks if vendor changes sending domain |
| Temporary | 24h–7d | Trials, one-time downloads | Mail lost after expiry |
| Prefix | Permanent | Unlimited signups, banking, shopping | Requires custom domain |

## Frequently Asked Questions (FAQ)

### How do I stop spam with a one-sender email inbox?
Give every service a unique prefix address. When spam arrives, you know exactly which vendor leaked your address, and the one-sender lock blocks everyone else automatically. No filtering rules required.

### Can I use a one-sender inbox without my own domain?
Yes, but the prefix feature works best with a custom domain. Without one, you are limited to the provider's shared domain, which reduces the uniqueness that makes prefix routing effective.

### What happens when a legit sender changes their sending domain?
The inbox bounces the new domain because it locked to the old one. You will need to create a fresh suffix and update the vendor. This is the main trade-off of strict one-sender locking.

### Is the MCP/AI integration required to use the app?
No. Bring-your-own-AI via the MCP server is optional. The core inbox routing, locking, and forwarding all work without any AI layer attached.

## Final Verdict

If you sign up for more than five services a month, this app solves a real problem that filters and aliases only patch. The **prefix inbox system is the killer feature** — it turns your domain into an infinite, self-organizing spam firewall. Start with a temporary inbox to test the bounce behavior, then graduate to prefixes once your MX records settle. Just budget 20 minutes for DNS and expect a few bounce errors while you learn the lock rules. For anyone running a custom domain in 2026, it is worth the setup.