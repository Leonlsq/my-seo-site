---
title: "Candiru Zero-Click Ads: How to Block Spyware on Your Phone"
description: "Candiru spyware spread via targeted ads in zero-click attacks. Learn how to block malicious ad delivery, harden your browser, and audit your phone now."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Candiru Zero-Click Ads: What Actually Happened and How to Protect Your Phone

The Candiru spyware campaign against Al Jazeera Media Network confirmed a scary reality: you don't have to click anything to get infected. Researchers found that **rendering a malicious targeted advertisement was enough** to deliver the Candiru (DevilsTongue) implant to victim devices. No tap, no download prompt, no suspicious link — just an ad loading on screen. If you're searching for "how to block zero-click spyware" or "protect phone from malicious ads," this guide gives you a concrete, layered defense you can implement in under 30 minutes.

The core takeaway: **ad delivery networks are now an attack surface**, and your defense is a stack of ad-blocking, browser hardening, and OS-level lockdown — not a single antivirus app.

## Step-by-Step Guide: Harden Your Device Against Zero-Click Ad Delivery

Zero-click attacks exploit the rendering pipeline, so every layer below targets how ads and web content reach your device.

### 1. Install a DNS-level ad and tracker blocker (highest impact)
This blocks ad requests before they ever render — the single most effective mitigation.

- **Android:** Set Private DNS to `dns.adguard-dns.com` (Settings → Network & Internet → Private DNS → Provider hostname).
- **iOS:** Install a DNS profile or use an on-device blocker like AdGuard (free tier covers Safari).
- **Desktop:** Use NextDNS or Pi-hole with curated blocklists (e.g., OISD, AdGuard DNS filter).

### 2. Lock down your browser
- Enable **strict tracking prevention** (Safari), **Enhanced Tracking Protection: Strict** (Firefox), or install **uBlock Origin** (Firefox/desktop Chrome).
- Disable **JavaScript** for untrusted sites where possible — many zero-click ad exploits require JS execution.
- Turn off **auto-play media** and **pop-up windows** entirely.

### 3. Patch aggressively — same-day for OS and browser
Candiru-class exploits chain known vulnerabilities. Enable automatic updates:

| Platform | Setting to Enable | Why It Matters |
|---|---|---|
| iOS | Settings → General → Software Update → Automatic Updates | Patches WebKit rendering flaws |
| Android | Play Protect + monthly security patch channel | Closes browser/WebView holes |
| Chrome/Edge | Auto-update + "Always use secure connections" | Blocks exploit delivery chains |
| Safari | Advanced → Advanced Tracking & Fingerprinting Protection | Reduces ad targeting surface |

### 4. Use Lockdown Mode (iOS) or Advanced Protection (Android)
- **iOS 16+:** Settings → Privacy & Security → **Lockdown Mode** — disables many rendering features exploited by zero-click chains.
- **Android:** Enable **Advanced Protection** in Chrome and Google Play Protect's enhanced scanning.
- **High-risk individuals (journalists, activists):** Consider GrapheneOS or a hardened browser like Brave with shields set to "Aggressive."

### 5. Audit for compromise indicators
Zero-click spyware often leaves traces. Check for:
- Unexpected battery drain or data spikes (Settings → Battery/Data usage).
- Unknown configuration profiles (iOS: Settings → General → VPN & Device Management).
- Unfamiliar apps with accessibility or device-admin permissions.
- For deep assurance, use **MVT (Mobile Verification Toolkit)** by Amnesty Security Lab to scan backups for Candiru/DevilsTongue indicators.

## Common Issues, Alternatives, and What You Should Know

**"I blocked ads but still see them in apps."** In-app ads bypass browser blockers. Use DNS-level filtering (step 1) or a firewall like NetGuard (Android) to catch app traffic.

**"Will Lockdown Mode break my phone?"** It disables some features (link previews, unknown FaceTime callers, certain web fonts) but is fully reversible and recommended for at-risk users.

**"Is antivirus enough?"** No. Traditional mobile antivirus rarely detects zero-click implants because they exploit legitimate rendering processes. Layered defense beats single-tool reliance.

**Alternatives comparison:**

| Tool | Platform | Cost | Best For |
|---|---|---|---|
| AdGuard DNS | All | Free | Set-and-forget ad blocking |
| NextDNS | All | Free tier | Custom blocklists, logging |
| Lockdown Mode | iOS | Free | High-risk individuals |
| MVT | Desktop (scan) | Free | Compromise detection |
| GrapheneOS | Pixel | Free | Maximum hardening |

**Reality check on costs:** All core mitigations above are free. Paid DNS (NextDNS Pro ~$20/yr) adds analytics but isn't required for protection.

## Frequently Asked Questions (FAQ)

### What is a zero-click attack and how does Candiru use it?
A zero-click attack compromises a device without any user interaction. In this campaign, simply **rendering a malicious targeted ad** triggered the exploit chain that installed Candiru's DevilsTongue spyware — no tap or download needed.

### Can I get Candiru spyware just by browsing a website?
The reported vector was malicious ad delivery to specific high-value targets, not random browsing. However, the technique proves ad networks can be weaponized, so blocking ads and patching your browser significantly reduces exposure.

### Does Lockdown Mode stop zero-click spyware?
Lockdown Mode dramatically shrinks the attack surface by disabling many web rendering features exploited in zero-click chains, but no single setting is a guaranteed cure. Combine it with DNS filtering and prompt updates.

### How do I check if my phone has spyware like Candiru?
Look for battery/data anomalies, unknown configuration profiles, and suspicious permissions. For a rigorous check, run Amnesty's **MVT** toolkit against a device backup to scan for known indicators.

## Final Verdict

The Candiru ad-delivery campaign is a wake-up call, not a reason to panic. **Do these three things today:** set a DNS-level ad blocker, enable automatic OS/browser updates, and turn on Lockdown Mode if you're a journalist, activist, or high-profile target. That combination neutralizes the exact rendering path this attack exploited — and it costs you nothing but 30 minutes. If you handle sensitive communications, add a periodic MVT scan to your routine. Defense in layers is the only honest answer to zero-click threats.