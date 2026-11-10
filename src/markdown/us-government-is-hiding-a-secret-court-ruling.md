---
title: "Secret FISA Court Ruling: How to Check If Your Data Was Spied On"
description: "US government hiding a secret FISA court ruling on surveillance? Learn how Section 702 works, how to check if your data was collected, and privacy steps to take."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## The Secret FISA Court Ruling, Explained (And What You Can Actually Do)

A WIRED report has surfaced that the US government is withholding a secret Foreign Intelligence Surveillance Court (FISC) ruling about how it spies on Americans — a story that hit 883 points and 312 comments on Hacker News. The core issue: under **Section 702 of the FISA Amendments Act**, the government collects communications of foreigners abroad, but "incidentally" sweeps up huge volumes of Americans' emails, texts, and calls. A secret court opinion apparently reinterprets how that data can be searched — and the public can't read it.

You can't read the classified ruling. But you *can* understand exactly how the surveillance pipeline touches your data, verify whether you're likely in the collection net, and harden your communications. This guide gives you the concrete, actionable version the news headlines skip.

## How Section 702 Surveillance Actually Reaches Your Data

Section 702 doesn't require a warrant. Instead, the Attorney General and Director of National Intelligence certify "targeting procedures" to the FISC. The collection happens at the infrastructure level — primarily through **upstream collection** (tapping fiber-optic cables and switches) and **PRISM directives** (compelling companies like Google, Meta, Microsoft, and Apple to hand over communications of selected identifiers).

The "incidental collection" problem is the heart of it:

- **Upstream taps** capture entire communication streams. If you email, call, or message someone who is a 702 target, your side of the conversation is stored.
- **"About" collection** (historically) captured communications that merely *mention* a target's selector — even if you never contacted them.
- **Backdoor searches**: FBI and NSA analysts can query the 702 database using US person identifiers (names, emails, phone numbers) — the so-called "backdoor search loophole." The secret ruling reportedly concerns the scope of these queries.

**Key takeaway:** You don't need to be a target. You only need to communicate with, or be mentioned alongside, someone who is.

## Step-by-Step: Assess and Reduce Your Exposure

There is no public "were you spied on?" lookup tool — anyone claiming otherwise is selling something. But you can run a realistic exposure assessment and take mitigation steps.

### Step 1: Map your likely exposure surface
Ask these questions honestly:

1. Do you communicate with journalists, activists, attorneys, or foreign nationals in sensitive regions?
2. Do you use US-based cloud providers (Gmail, iCloud, Outlook, Google Drive) for sensitive conversations?
3. Do you work in defense, journalism, academia, or NGOs that interact with foreign entities?
4. Have you ever been interviewed by or emailed a person later designated as a surveillance target?

Two or more "yes" answers means you should assume some of your communications sit in a 702 repository.

### Step 2: Check what's publicly knowable
- **FISC opinions database**: The public version lives at the FISC website (uscourts.gov). Redacted opinions are posted there — check for the most recent Section 702 certifications and any unsealed opinions.
- **ODNI transparency reports**: The Office of the Director of National Intelligence publishes annual statistical transparency reports showing how many US person queries were run. Compare year-over-year numbers to see trends.
- **Your provider's transparency reports**: Google, Microsoft, and Meta publish government request volumes. Look for "FISA" and "national security letters" line items.

### Step 3: Harden your communications (practical settings)

| Layer | Action | Effort | Effectiveness |
|---|---|---|---|
| Messaging | Enable end-to-end encryption (Signal, WhatsApp E2EE) | Low | High — content protected, metadata still exposed |
| Email | Use E2EE (Proton Mail + PGP) for sensitive threads | Medium | High for content, weak for metadata |
| DNS | Switch to encrypted DNS (DoH/DoT) | Low | Blocks some upstream inspection |
| VPN | Use a reputable no-log VPN | Low | Shifts trust, doesn't defeat targeted collection |
| Cloud storage | Encrypt files before upload (Cryptomator, VeraCrypt) | Medium | High |
| Metadata | Minimize who you contact and how often | High | Reduces selector hits |

### Step 4: Understand the limits
No consumer tool defeats **upstream fiber collection** if a target selector is in your traffic path. Encryption protects *content*; it does not hide *metadata* (who, when, how long) from upstream taps. Be skeptical of any product claiming to "block FISA surveillance."

## Common Misconceptions and What You Should Know

- **"A VPN makes me invisible."** No. A VPN moves the collection point; it doesn't eliminate it. If your traffic crosses a tapped backbone, metadata is still visible.
- **"I'm a US citizen, so I'm protected."** The Fourth Amendment applies, but 702 collection is framed as *foreign* intelligence gathering. Your data is "incidentally" collected and can be queried — that's the loophole the secret ruling concerns.
- **"There's a way to request my surveillance file."** There is no FOIA pathway to individual 702 collection records. FOIA exemptions for classified national security material apply.
- **"The ruling will be released soon."** Historically, FISC opinions surface only after years of litigation and heavy redaction — sometimes never. Don't wait for it; act on what's knowable now.

## Frequently Asked Questions (FAQ)

### Can I find out if the US government collected my communications under Section 702?
No public lookup exists. You can infer exposure from your communication patterns, review ODNI transparency statistics, and check provider transparency reports — but individual collection records are classified and not subject to FOIA release.

### What is the "backdoor search loophole" in FISA Section 702?
It's the practice of US intelligence agencies querying the 702 database using US person identifiers (names, emails, phone numbers) without a warrant. The secret FISC ruling reportedly addresses the scope and safeguards of these queries.

### Does using Signal or a VPN stop Section 702 surveillance?
Partially. Signal protects message content via end-to-end encryption, and a VPN obscures your IP from local observers — but neither hides metadata from upstream fiber collection, and neither prevents targeted collection if a foreign selector is in your communication path.

### Is Section 702 still active in 2026?
Yes. Congress reauthorized Section 702 in April 2024 for two years, meaning it remains in force through 2026 unless Congress acts again. The reauthorization expanded the definition of "electronic communications service provider," broadening who can be compelled to assist.

### Where can I read the FISC opinions that *are* public?
The Foreign Intelligence Surveillance Court publishes redacted opinions and orders on the official US Courts website (uscourts.gov). Recent Section 702 certification opinions are typically posted there, though the ruling in question has not been released.

## Final Verdict

You cannot read the secret ruling, and no tool will tell you definitively whether your data was collected. What you *can* do is stop being a soft target: move sensitive conversations to end-to-end encrypted channels, encrypt files before cloud upload, minimize metadata exposure, and monitor ODNI transparency reports for changes in US person query volumes. Treat the WIRED report as a signal to audit your own communications hygiene — not as a reason to buy a "spy-proof" gadget. The most effective defense against incidental collection is simply not being in the path of a targeted selector, and that starts with knowing who you talk to and how.