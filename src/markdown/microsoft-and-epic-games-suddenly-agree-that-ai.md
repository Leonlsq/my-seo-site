---
title: "AI Theft Claims: How to Opt Out of AI Training Data (2026 Guide)"
description: "Microsoft and Epic Games call AI theft. Learn how to opt out of AI training data, protect your art and code, and check if your work was scraped."
pubDate: 2026-10-29
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Microsoft and Epic Suddenly Agree That AI Is Theft (And What You Can Do)

The viral headline is real: Microsoft and Epic Games have publicly aligned on the position that training generative AI models on unlicensed creative work amounts to "theft." For creators, developers, and gamers, the practical question isn't *whether* this is a philosophical debate — it's **what you can actually do right now to stop your content from being scraped and used for AI training**.

This guide cuts through the corporate statements and gives you a concrete, step-by-step action plan: how to opt out of AI training, how to verify whether your work has already been scraped, and how to lock down your assets across the major platforms (GitHub, ArtStation, Steam, and the open web). If you've ever posted art, code, or a game mod online, this applies to you.

## Step-by-Step: How to Opt Out of AI Training Data Across Major Platforms

The "AI is theft" consensus is driven by the fact that most models were trained on data collected **before** opt-out tools existed. That means your job now is twofold: (1) opt out going forward, and (2) audit what's already out there. Here's the platform-by-platform playbook.

### 1. Block AI Crawlers at the Source (robots.txt + meta tags)

For your own website or portfolio, this is the highest-impact fix. Add these rules to your `robots.txt`:

```
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

Then add this meta tag to every page's `<head>`:

```html
<meta name="robots" content="noai, noimageai">
```

**Important caveat:** `robots.txt` is a *request*, not enforcement. Compliant crawlers (OpenAI's GPTBot, Anthropic's ClaudeBot, Common Crawl's CCBot) honor it. Rogue scrapers won't. Treat this as a deterrent, not a lock.

### 2. Opt Out on Art Platforms (ArtStation, DeviantArt, Adobe)

| Platform | Opt-Out Setting | Location | Enforced? |
|---|---|---|---|
| ArtStation | "NoAI" tag on uploads | Upload dialog → tag | Partial (detection-based) |
| DeviantArt | "NoAI" / "NoML" submission flags | Submission settings | Yes (metadata) |
| Adobe Stock/Firefly | Contributor opt-out | Account → Preferences | Yes (contractual) |
| GitHub | Copilot content exclusion | Repo Settings → Copilot | Yes (for Copilot) |

For **GitHub**, navigate to your repository → **Settings** → **Copilot** → enable **"Exclude this repository from Copilot"**. This prevents Copilot from using your code as context suggestions. It does *not* retroactively remove your code from models already trained.

### 3. Opt Out of Steam and Game-Platform Scraping

If you're an indie dev or modder, your workshop content and store assets are fair game for scrapers. There's no universal Steam opt-out, but you can:

- **Watermark store assets** with visible attribution before uploading.
- **License your mods explicitly** (e.g., CC BY-NC-ND) in the description — this creates a paper trail for DMCA takedowns.
- **Monitor for reposts** using reverse image search (Google Lens, TinEye) on your key art quarterly.

### 4. Audit Whether Your Work Was Already Scraped

Use these free tools to check exposure:

- **Have I Been Trained?** (haveibeentrained.com) — search the LAION dataset by image.
- **Glaze / Nightshade** — apply adversarial noise to art *before* posting to poison future scrapes (works best pre-upload, not retroactively).
- **GitHub Copilot logs** — check if your public repos appear in Copilot suggestions via the content exclusion audit.

## Common Issues, Alternatives, and What You Should Know

**The hard truth about opt-outs:** Opting out now protects *future* training runs. It does **not** remove your data from models already trained (GPT-4, Midjourney v5, Stable Diffusion 1.5, etc.). No tool can do that short-term — it requires model retraining or legal action.

**"NoAI" tags are not legally binding everywhere.** In the US, fair use arguments still dominate litigation. In the EU, the AI Act gives creators stronger opt-out rights under Article 4 (text and data mining exceptions). If you're an EU creator, your opt-out carries more legal weight.

**Alternatives if you want protection without opting out entirely:**
- **Licensing collectives** (e.g., Human Artistry Campaign) that negotiate collective licensing.
- **Poisoning tools** (Nightshade) that degrade model quality if scraped — controversial but legal in most jurisdictions.
- **Private/paid galleries** with login walls that block crawlers by default.

**Cost consideration:** Most opt-out tools are free. Paid options (enterprise DMCA services, legal retainer for takedowns) run $200–$2,000+ depending on scale — only worth it if you're a studio or high-volume creator.

## Frequently Asked Questions (FAQ)

### Did Microsoft and Epic Games really say AI is theft?
They aligned on the principle that training AI on unlicensed creative work without consent or compensation is exploitative. The framing varies by executive, but both companies have pushed for licensing frameworks and creator opt-outs — a notable shift given Microsoft's OpenAI partnership and Epic's Unreal/asset ecosystem.

### How do I stop AI from training on my art?
Add `noai` meta tags and `robots.txt` blocks to your site, enable "NoAI" flags on ArtStation/DeviantArt, and apply Glaze or Nightshade before uploading new work. These deter compliant crawlers but cannot remove already-scraped data.

### Can I remove my data from an AI model that already trained on it?
Not directly. You can request removal from datasets (e.g., LAION) and file DMCA takedowns for infringing outputs, but removing influence from a trained model requires retraining — which only the model owner can do. Legal action is the only enforcement path.

### Is opting out of AI training free?
Yes. Robots.txt, meta tags, platform flags, and tools like Glaze/Nightshade are free. Only legal enforcement or enterprise DMCA services carry costs.

## Final Verdict

The Microsoft–Epic "AI is theft" moment isn't just corporate noise — it's a signal that **creator opt-out infrastructure is finally being taken seriously**. But don't wait for platforms to protect you. Do these three things today: (1) add `noai` meta tags and robots.txt blocks to your site, (2) enable platform-level opt-outs on ArtStation, DeviantArt, and GitHub, and (3) run a Have I Been Trained? audit to see your exposure. Opt-outs won't undo past scraping, but they're the only lever you control right now — and the sooner you pull it, the less of your work ends up in the next training run.