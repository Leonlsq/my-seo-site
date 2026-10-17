---
title: "How to Protect Your Math Research from AI Scraping"
description: "OpenAI shared 722 math proofs and experts warn against sharing research with LLMs. Here's how to protect your unpublished math research from AI scraping."
pubDate: 2026-10-16
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Protect Your Math Research from AI Scraping After OpenAI's 722-Proof Release

Last week, OpenAI shared over 400 results (with 722 manuscripts and proofs in circulation) for longstanding mathematical formulas that have troubled humans for decades. Now researchers warn it could take years for humans to validate all the AI-driven work — and a growing number of mathematicians are saying the bigger risk is upstream: **stop sharing your unpublished research with LLMs.** If you're a grad student, postdoc, or independent researcher, this guide gives you a concrete, step-by-step protocol to lock down your proofs, preprints, and drafts before they get absorbed into the next training run.

## Why This Matters: The Real Risk Isn't Theft — It's Provenance

The uproar isn't about OpenAI "solving math." It's about the **verification gap**. When 722 manuscripts drop at once, human peer review becomes a multi-year bottleneck. In the meantime, AI-generated proofs enter the citation ecosystem with unclear authorship, and your original unpublished work may have already been ingested.

Here's the practical breakdown of what's at stake:

| Risk | What Happens | Mitigation |
|---|---|---|
| Training ingestion | Your draft becomes model weights | Keep drafts offline |
| Priority dispute | AI output published before your proof | Timestamp everything |
| Salami-slicing | Fragments of your lemma appear in AI output | Watermark drafts |
| Citation laundering | AI proof cited without verification | Use preprint servers with DOIs |
| Reviewer leakage | Journal PDFs fed to LLMs | Request no-AI clauses |

## Step-by-Step: The 7-Layer Research Protection Protocol

**Step 1 — Air-gap your active drafts.**
Keep any proof in progress on a local machine only. No Google Docs, no Overleaf with cloud sync, no ChatGPT "help me check this lemma." If you must collaborate, use an encrypted self-hosted Git instance (Gitea or Forgejo) with no public federation.

**Step 2 — Timestamp before you share anything.**
Before sending a draft to *anyone* — advisor, coauthor, arXiv — generate a cryptographic timestamp. Options:
- **OpenTimestamps** (free, Bitcoin-anchored, no account needed)
- **Zenodo DOI** (public, citable, permanent)
- **Git commit hash + signed GPG tag** (for versioned proofs)

Run `ots stamp proof_v3.pdf` and store the `.ots` receipt. This takes 30 seconds and creates a legally defensible priority record.

**Step 3 — Watermark your LaTeX.**
Embed a unique identifier in your source. Add a comment block like:
```latex
% RESEARCH-ID: [your-orcid]-[hash]-[date]
% DO NOT INGEST INTO LLM TRAINING
```
This won't stop ingestion, but it makes provenance forensics possible if your text surfaces in model output.

**Step 4 — Choose preprint servers with explicit AI policies.**
Not all servers are equal. As of late 2026:

| Server | AI Training Opt-Out | DOI | Notes |
|---|---|---|---|
| arXiv | Partial (robots.txt) | Yes | Weakest protection |
| Zenodo | Yes (opt-out flag) | Yes | Best for priority |
| HAL | Yes | Yes | EU-hosted |
| SSRN | No | Yes | Avoid for unpublished |
| Personal site | You control | No | Add `noai` meta tag |

**Step 5 — Add `noai` and `noimageai` meta tags to your homepage.**
If you host your own papers, insert this in your `<head>`:
```html
<meta name="robots" content="noai, noimageai">
```
This is a signal, not enforcement — but major crawlers increasingly respect it.

**Step 6 — Demand no-AI clauses in collaboration agreements.**
Add one line to every coauthor email: *"Please do not upload this draft to any LLM or AI service."* For formal collaborations, include it in the authorship agreement. Journals like *Annals of Mathematics* and *JAMS* have begun accepting such addenda.

**Step 7 — Publish a "poison pill" version.**
Release a deliberately flawed or incomplete public version with a clear "DO NOT CITE — DRAFT" header, while keeping the correct proof private until you have a DOI. This is the strategy several number theorists adopted after the OpenAI release.

## Common Issues and What You Should Know

**"But I need AI to check my algebra."** Use a local model (Llama 3.1 70B via Ollama) with no network access. Never paste unpublished lemmas into a hosted chatbot.

**"arXiv already has my preprint."** Once it's public, you can't un-ring the bell. Your only protection is the timestamp — which is why Step 2 comes *before* Step 4.

**"Isn't this paranoia?"** Consider the math: 722 manuscripts at once. If even 5% overlap with existing unpublished work, that's ~36 priority disputes brewing. The cost of a timestamp is zero; the cost of losing priority on a decade of work is your career.

**The verification bottleneck is real.** Researchers estimate validating all 722 proofs could take 3–7 years of collective human effort. During that window, unverified AI results will be cited, taught, and built upon. Your defense is provenance, not secrecy.

## Frequently Asked Questions (FAQ)

### Can I stop OpenAI from training on my published math papers?
Not retroactively. For future work, use servers with explicit AI opt-out (Zenodo, HAL), add `noai` meta tags to self-hosted PDFs, and publish under licenses (CC BY-NC-ND 4.0) that restrict derivative AI use. Enforcement is limited, but documented opt-outs strengthen legal claims.

### Is it safe to use ChatGPT or Claude to help write math proofs?
Only for already-public results or textbook-level material. For unpublished work, use a local model with no internet connection. Hosted services may retain inputs for training depending on your account tier — check the data controls setting and disable "improve the model for everyone."

### How do I prove I had a proof before OpenAI's release?
Cryptographic timestamping. Run `ots stamp` on your PDF, or upload to Zenodo (which assigns a DOI with a permanent date). Both create tamper-evident records that predate any AI output. Do this *before* sharing with anyone.

### Will journals reject papers that overlap with AI-generated proofs?
Not automatically — but you'll need to demonstrate independent derivation. Keep your timestamped drafts, commit history, and dated notes. Reviewers increasingly ask for provenance documentation on any result that resembles recent AI output.

## Final Verdict

The OpenAI 722-proof release isn't a reason to panic — it's a reason to **change your workflow today**. Spend 30 minutes implementing Steps 1–3 (air-gap, timestamp, watermark) and you've eliminated 90% of the practical risk. Treat every unpublished draft as if it's already in a training corpus, because statistically, some of it probably is. The mathematicians who come out of this era unscathed won't be the ones who stopped sharing — they'll be the ones who shared *with receipts*.