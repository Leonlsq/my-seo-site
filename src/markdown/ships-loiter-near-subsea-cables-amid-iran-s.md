---
title: "Subsea Cable Attack Risk: How to Protect Your Internet Backup"
description: "Iran threatens subsea cables. Learn how to check your ISP's redundancy, set up failover, and keep internet running during a cable outage."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Iran's Subsea Cable Threat: How to Keep Your Internet Online If Cables Get Cut

Iran has warned it will target subsea communications cables if the US escalates military strikes — and ships have reportedly been loitering near key cable routes. For most people this sounds like distant geopolitics, but the practical question is simple: **what happens to your internet if a major cable is severed, and how do you stay online?** The short answer: single-ISP households and businesses are exposed, but a redundancy plan (dual-WAN, cellular failover, or satellite backup) keeps you connected through most cable-level disruptions. This guide gives you a concrete checklist to audit your exposure and build a failover setup this week.

## Why Subsea Cables Matter More Than You Think

Roughly **99% of intercontinental internet traffic** travels through undersea fiber-optic cables — not satellites. A handful of chokepoints (Red Sea, Strait of Hormuz, Mediterranean, and North Atlantic routes) carry a disproportionate share of traffic between Europe, Asia, and the Middle East.

What a cable cut actually does depends on your location:

| Scenario | Likely Impact | Who Feels It First |
|---|---|---|
| One cable cut on a major route | Minor slowdowns; traffic reroutes | Users on single-path ISPs |
| Multiple simultaneous cuts (Red Sea-style) | Latency spikes, packet loss, cloud app timeouts | Cloud-dependent businesses, gamers, remote workers |
| Regional cable hub disabled | Multi-hour to multi-day outages | Countries with few landing points |
| Coordinated attack on chokepoints | Widespread degradation, not total blackout | Everyone, but severity varies by ISP redundancy |

The key insight: **major outages are usually about routing concentration, not total cable loss.** ISPs with diverse paths barely notice; ISPs that buy transit through a single corridor get hammered.

## Step-by-Step: Audit and Build Your Internet Failover Plan

### Step 1: Check your ISP's redundancy (10 minutes)
- Look up your ISP's upstream providers (search "[ISP name] peering/transit" or check a BGP looking glass like bgp.he.net).
- If all their transit flows through one region (e.g., a single Middle East or Red Sea corridor), you're exposed.
- Ask support directly: "Do you have diverse international transit paths, and what's your failover procedure during a cable cut?" A vague answer is a red flag.

### Step 2: Add a second connection (the core fix)
For homes and small offices, a **dual-WAN router with automatic failover** is the highest-value upgrade:

1. Buy a router with dual-WAN or multi-WAN support (e.g., models from TP-Link Omada, Asus, Ubiquiti, or a pfSense/OPNsense box).
2. Connect your primary ISP to WAN1 and a second ISP (fiber + cable, or fiber + 5G) to WAN2.
3. Enable **failover mode** (not load-balance) so WAN2 only activates when WAN1 drops.
4. Set health-check pings to reliable IPs (e.g., 1.1.1.1 and 8.8.8.8) with a 5–10 second interval.
5. Test by unplugging WAN1 — your connection should recover in under 30 seconds.

### Step 3: Add cellular or satellite as a last resort
- **5G/LTE failover modem**: Cheapest option; works if local towers stay up. Expect 20–100 Mbps depending on signal.
- **Satellite (Starlink, etc.)**: Independent of terrestrial cables, but higher latency (25–60 ms) and weather-sensitive. Best for rural or high-risk regions.
- Keep a **prepaid SIM** activated and tested — don't discover it's expired during an outage.

### Step 4: Harden your critical workflows
- Enable **offline mode** in cloud apps (Google Drive, OneDrive, Outlook) so work continues during sync failures.
- Configure **local DNS fallback** (router-level DoH to Cloudflare/Quad9) to survive upstream DNS outages.
- For gamers: expect latency spikes during reroutes; use wired Ethernet and a router with **SQM/QoS** to keep jitter manageable.

## Common Issues, Alternatives, and What You Should Know

- **Failover doesn't trigger fast enough?** Most consumer routers take 10–60 seconds to detect a dead WAN. Lower the health-check interval, but don't go below 5 seconds or you'll get false positives.
- **Double NAT problems:** If your second ISP uses CGNAT, port forwarding and some VPNs break. Test before you rely on it.
- **VPN won't fix a cut cable.** A VPN changes your path, not the physical infrastructure. It can help if your ISP's *routing* is bad, but not if the cable itself is down.
- **Cost reality check:** Dual-ISP home setups typically add $30–$80/month. Cellular failover adds $10–$40/month. For remote workers and small businesses, that's cheap insurance against a multi-day outage.
- **Don't panic-buy satellite hardware** based on headlines alone. Assess your actual risk: are you in a region with few landing points and a single-corridor ISP? If not, dual-WAN is enough.

## Frequently Asked Questions (FAQ)

### Will Iran actually cut subsea cables, and would it take down the internet?
Iran has threatened cable infrastructure as leverage, and ships loitering near cable routes raise real concerns — but a total internet shutdown is unlikely. Modern cable networks have multiple redundant paths, and cutting one or two cables typically causes slowdowns and rerouting rather than a blackout. The risk is concentrated in regions with few landing points and ISPs without diverse transit.

### How do I know if my internet is vulnerable to a subsea cable cut?
Check whether your ISP has multiple, geographically diverse international transit providers using a BGP looking glass (bgp.he.net). If all their upstream traffic funnels through one corridor (e.g., the Red Sea or Strait of Hormuz), you're exposed. The fix is a second ISP with a different path plus a dual-WAN failover router.

### What's the cheapest way to keep internet during a cable outage?
A 5G/LTE failover modem paired with a dual-WAN router is the cheapest reliable option — typically $10–$40/month for the cellular line plus a one-time router cost. Keep a tested prepaid SIM ready. Satellite backup (e.g., Starlink) is more resilient to terrestrial outages but costs more and adds latency.

### Does a VPN protect me if subsea cables are attacked?
No. A VPN encrypts and reroutes your traffic, but it still travels over the same physical cables. It can help if your ISP's routing is degraded and the VPN has diverse paths, but it cannot restore connectivity if the underlying infrastructure is severed.

## Final Verdict

Don't wait for a headline-grabbing outage to act. **Audit your ISP's redundancy today, then add a dual-WAN failover router with a second connection** — that single upgrade covers the vast majority of cable-cut scenarios for homes and small businesses. If you're in a high-risk region or run mission-critical operations, layer in a tested cellular or satellite backup and enable offline modes in your cloud apps. Total cost is modest; the payoff is staying online when everyone else is refreshing a dead page.