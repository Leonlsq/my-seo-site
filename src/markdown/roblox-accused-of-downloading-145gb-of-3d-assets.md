---
title: "Roblox 145GB Scraping Scandal: How to Protect Your 3D Models"
description: "Open3DLab says a Roblox crawler grabbed 145.5GB of 3D assets. Here's how to audit your models, block scrapers, and opt out of AI training."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Roblox's 145GB Scraping Spree: What Modelers Need to Do Right Now

Open3DLab, an independent 3D modeling community, has publicly accused a web crawler attributed to Roblox of downloading **145.5GB of its data** — including adult-themed 3D assets — under the assumption it's being funneled into AI training pipelines. If you host models on Open3DLab, Sketchfab, or your own portfolio site, this is your wake-up call: **your assets may already be in someone's training set, and there is no automatic way to get them back.**

The direct takeaway: you cannot undo a scrape that already happened, but you *can* audit what's exposed, harden your hosting against future crawlers, and file takedown or opt-out requests where they actually have legal teeth. Below is the exact playbook, ordered by urgency.

## Step-by-Step: Audit, Block, and Opt Out

### Step 1 — Audit What's Publicly Crawlable (15 minutes)

Before you panic, find out what a bot can actually reach.

1. Run `site:open3dlab.com "your-username"` in Google to see indexed pages tied to your account.
2. Check your profile's public/private toggle — most platforms default new uploads to **public**.
3. Use a crawler simulator (Screaming Frog free tier, 500 URLs) pointed at your profile URL to see exactly what a bot sees, including direct `.blend`, `.fbx`, and `.zip` links.
4. Log into Open3DLab and review download counters per model — a sudden spike on obscure uploads is a red flag.

### Step 2 — Block Crawlers at the Source

If you self-host models, add these rules to `robots.txt` **today**:

```
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: Amazonbot
Disallow: /

User-agent: anthropic-ai
Disallow: /
```

Then add a `Content-Signal` header or meta tag for the newer opt-out standard:

```html
<meta name="robots" content="noai, noimageai">
```

**Caveat that matters:** `robots.txt` is voluntary. A crawler that ignores it — which is exactly what Open3DLab alleges — will not be stopped by these rules. They only create a paper trail proving you opted out, which strengthens any later takedown claim.

### Step 3 — Rate-Limit and Fingerprint

On your own server (Nginx example), throttle aggressive scrapers:

```nginx
limit_req_zone $binary_remote_addr zone=models:10m rate=5r/m;

location /downloads/ {
    limit_req zone=models burst=3 nodelay;
    limit_req_status 429;
}
```

Pair this with Cloudflare's **Bot Fight Mode** or a WAF rule blocking requests with no `Referer` and a generic user agent. This won't stop a determined scraper with rotating IPs, but it kills the lazy 80%.

### Step 4 — File Opt-Out and DMCA Requests

| Platform | Opt-Out Mechanism | Realistic Outcome |
|---|---|---|
| Open3DLab | Contact site admin; platform-level block | Site can block the crawler IP range |
| Sketchfab | Account settings → AI training toggle | Honored for future crawls only |
| ArtStation | "NoAI" tag + support ticket | Enforced on-platform, not off |
| Your own site | `robots.txt` + DMCA to host | DMCA works if the *host* is US-based |

For DMCA, identify the hosting provider of the infringing dataset (often Hugging Face, GitHub, or a cloud bucket), not Roblox itself. Send a notice to the **host's designated agent** — that's the address with legal force.

## What You Should Know Before You Rely on Opt-Outs

- **145.5GB is not huge.** That's roughly 30,000–70,000 mid-poly models. It's a targeted scrape of a specific community, not a web-wide sweep — which suggests deliberate sourcing, not an accident.
- **Adult content inclusion changes the legal picture.** If the scraped assets include adult material, that triggers separate platform ToS violations and, depending on jurisdiction, content-handling obligations that a generic "AI training" defense doesn't cover.
- **Roblox has not confirmed the attribution.** Treat "attributed to Roblox" as an allegation until Roblox responds. Crawlers can spoof user agents.
- **Opt-outs are forward-looking.** No major platform currently deletes your data from an already-trained model. The only real remedy is legal pressure or dataset removal.
- **Watermarking works better than blocking.** Embed a visible signature or hidden metadata in your models before upload. If your asset surfaces in a generated output, you have proof of provenance.

### Should you delete your uploads?

For most creators, **no** — you lose portfolio traffic for zero protection against data already scraped. Instead: set new uploads to private-by-default, add `noai` metadata, and keep a dated record of your opt-out actions. That record is your leverage.

## Frequently Asked Questions (FAQ)

### Did Roblox really download 145GB of 3D models for AI training?

Open3DLab alleges a crawler attributed to Roblox pulled 145.5GB including adult assets. Roblox has not confirmed the attribution or the purpose. Treat it as a credible allegation, not a confirmed fact.

### How do I stop AI crawlers from scraping my 3D models?

Add `noai` meta tags and block known AI user agents (GPTBot, CCBot, Google-Extended) in `robots.txt`, rate-limit downloads on your own server, and enable your platform's AI opt-out toggle. None of these stop a crawler that ignores the rules — they only document your refusal.

### Can I get my models removed from an AI training dataset?

Only via a DMCA takedown to the dataset's hosting provider or a legal request to the model owner. Platforms cannot retroactively remove your data from a trained model. File notices early and keep copies.

### Is Open3DLab safe to keep using?

Yes, with precautions: set uploads to private, monitor download counts, and avoid uploading assets you can't afford to see scraped. The platform itself is a victim here, not the culprit.

## Final Verdict

The 145GB scrape is a warning shot, not a one-off. **Do the 15-minute audit today**, add `noai` metadata to every new upload, and stop treating any public model host as a private vault. You can't un-scrape 145GB, but you can make your next 145GB dramatically harder to take — and document every refusal so you're first in line when the legal reckoning arrives.