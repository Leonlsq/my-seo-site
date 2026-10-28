---
title: "Ad Tracking on Starlink: How to Block Discover-Tech Ads"
description: "Learn how to block Discover-Tech ad tracking linked to Starlink surveillance. Step-by-step DNS, VPN, and browser fixes to stop cross-app tracking."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Block Discover-Tech Ad Tracking on Starlink and Mobile Apps

If you use Starlink or any satellite internet connection, a new Citizen Lab and Confiant report should be on your radar. Researchers linked Israeli ad tech firm **Discover-Tech** to a suspected surveillance effort that exploited online ad auctions to track users across nearly **200,000 websites and mobile apps**. TrendAI separately flagged related activity under the codename **SHADOW-EARTH-79**. The key takeaway: ad impressions alone don't confirm spyware infection, but ad auctions are being used as a tracking vector. Here's exactly how to harden your devices and network against this class of cross-site ad tracking — starting today.

## Step-by-Step: Block Ad Auction Tracking on Your Network

You don't need to be a target to act. The same defenses stop Discover-Tech-style tracking and 90% of everyday ad surveillance. Work through these in order — each layer adds protection.

### 1. Set a Filtering DNS Resolver (Fastest Win)
DNS filtering blocks ad and tracker domains before a connection is made. This is the single highest-impact change for Starlink users because it applies to every device on your router.

- **Cloudflare Zero Trust (1.1.1.2 / 1.1.1.3)** — free, blocks known malware and tracking domains.
- **NextDNS** — free tier with 300,000 queries/month; add blocklists like *OISD*, *AdGuard DNS filter*, and *HaGeZi Multi Pro*.
- **Quad9 (9.9.9.9)** — free, privacy-focused, blocks malicious domains.

**On Starlink:** Open the Starlink app → **Settings → Router/Wi-Fi → DNS** (or set DNS manually on each device if your firmware hides it). Enter your chosen resolver's IPs. Reboot the router and confirm at `dnsleaktest.com`.

### 2. Deploy a Network-Wide Ad Blocker
For full coverage, run a local DNS sinkhole:

| Tool | Best For | Cost | Setup Time |
|---|---|---|---|
| **Pi-hole** | Raspberry Pi owners, full network control | ~$35 hardware | 30–45 min |
| **AdGuard Home** | Beginners, built-in UI + DoH | Free | 15 min |
| **NextDNS** | Zero hardware, cloud-based | Free/paid | 5 min |

Point your Starlink router's DNS to the Pi-hole or AdGuard Home IP. This blocks ad-auction beacons at the source across every phone, laptop, and smart TV on the network.

### 3. Harden Mobile Apps (Where Discover-Tech Ads Appeared)
Because the reported tracking ran through in-app ads, browser extensions alone won't help. On mobile:

- **iOS:** Settings → Privacy & Security → **Tracking** → toggle off *Allow Apps to Request to Track*. Then enable **Lockdown Mode** if you handle sensitive work.
- **Android:** Settings → Privacy → **Ads** → *Delete advertising ID*. Install **AdGuard** (sideload APK) for system-wide filtering via local VPN.
- **Both:** Revoke unnecessary permissions (Location, Contacts) from any app you don't actively use.

### 4. Use a Trusted VPN on Sensitive Networks
The report specifically raised concerns about tracking across sensitive networks. A reputable no-log VPN (Mullvad, Proton VPN) encrypts DNS and traffic so ad-auction requests can't be tied to your IP. Avoid free VPNs — many monetize through the same ad ecosystems.

### 5. Browser-Level Defense
- Install **uBlock Origin** (Firefox/Chrome) — blocks ad-auction scripts and tracking pixels.
- Enable **Firefox Total Cookie Protection** or Safari's **Advanced Tracking and Fingerprinting Protection**.
- Disable third-party cookies in Chrome: Settings → Privacy → *Block third-party cookies*.

## What You Should Know Before Panicking

Context matters. Here's what the research does and doesn't prove:

- **Ad impressions ≠ infection.** Seeing a Discover-Tech ad does not mean your device is compromised. The concern is the *tracking mechanism*, not confirmed spyware on your phone.
- **Scale is the story.** Ads across ~200,000 sites and apps means the reach is broad — which is why network-level blocking beats app-by-app whack-a-mole.
- **Starlink is a vector, not a culprit.** The tracking exploits ad auctions that travel over any ISP. Satellite users aren't uniquely targeted, but sensitive-network use warrants extra caution.
- **SHADOW-EARTH-79** is TrendAI's codename for related activity — treat it as a cluster label, not a specific malware family you can "scan for."

**Verification step:** After applying DNS + blocker changes, check your setup at `d3ward.github.io/toolz/adblock` and confirm blocklists are updating daily in your Pi-hole/AdGuard dashboard.

## Frequently Asked Questions (FAQ)

### Is Discover-Tech spying on my Starlink connection?
No evidence suggests Discover-Tech targets Starlink specifically. Researchers linked the firm to ad-based tracking that can run over any network, including Starlink. Ad impressions alone don't confirm spyware — but blocking ad trackers at the DNS level neutralizes the vector regardless.

### Does blocking ads actually stop ad-auction tracking?
Yes, largely. Most ad-auction tracking relies on DNS lookups and script calls to tracker domains. A filtering DNS resolver plus a network blocker like Pi-hole or AdGuard Home stops those requests before data is sent, which is why it's the most effective single fix.

### What is SHADOW-EARTH-79?
SHADOW-EARTH-79 is a codename TrendAI assigned to activity it identified as related to the Discover-Tech findings. It functions as a threat-cluster label for researchers — not a consumer tool or malware name you can download a scanner for.

### Will a VPN stop this kind of ad tracking?
A no-log VPN hides your IP and encrypts DNS, which breaks IP-based correlation in ad auctions. It won't stop in-app tracking that uses device IDs, so pair a VPN with advertising-ID resets and a DNS blocker for full coverage.

## Final Verdict

Don't wait for a headline to confirm you're affected. The smartest move is a **layered defense**: set a filtering DNS resolver (NextDNS or Cloudflare 1.1.1.2) today, add **Pi-hole or AdGuard Home** for network-wide blocking if you're on Starlink, and reset your mobile advertising ID. Total cost: **$0–$35**, total time: under an hour. That stack neutralizes ad-auction tracking — Discover-Tech-linked or otherwise — and protects every device on your network. Treat this report as a reminder to close the ad-tracking door, not a reason to panic.