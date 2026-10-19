---
title: "Plex Movie Ticket Ads: How to Opt Out & What Data It Shares"
description: "Plex now uses your watch data to sell movie theater tickets. Here's how to opt out of Plex ad tracking, what discovery data is shared, and privacy settings to change."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Plex Is Now Selling Movie Theater Tickets — Here's How to Control What It Shares

Plex has expanded its free ad-supported streaming (FAST) business into movie ticketing, partnering with studios and advertisers to surface theater showtimes and ticket links inside the app. The engine behind those recommendations is **discovery data** — what you search for, browse, and click inside Plex. If that sounds like a privacy trade-off you didn't sign up for, the good news is Plex exposes granular controls. This guide shows you exactly which settings to change, what data actually leaves your account, and how to keep the recommendations without handing over a full behavioral profile.

The short version: Plex's ticketing push is opt-out, not opt-in. You have roughly four switches to flip in **Settings → Privacy** to minimize data sharing, and two of them affect ad personalization directly. Let's walk through them.

## What Plex Actually Shares (and What It Doesn't)

Before you panic-toggle everything, understand the data model. Plex separates **account data** (email, payment, watch history synced across devices) from **advertising identifiers** used by its ad partners.

| Data Type | Used For | Shared With Studios/Advertisers? | Toggle Location |
|---|---|---|---|
| Watch history (server) | Recommendations, resume playback | No (stays on your server) | N/A — local |
| Discovery searches & clicks | Content recommendations, ticket prompts | Aggregated + device ID | Settings → Privacy |
| Ad ID / device identifier | Targeted ads, frequency capping | Yes, with ad partners | Settings → Privacy |
| Approximate location (IP-based) | Local showtimes, regional ads | Yes, coarse only | Settings → Privacy |
| Email / account info | Billing, account recovery | No | N/A |

The critical detail: **your self-hosted library watch history is not what's being monetized.** Plex's ticketing play relies on activity inside the free streaming catalog and discovery features — searches, trailer views, "where to watch" clicks, and the ad ID attached to your devices. That's a much narrower dataset than most users assume, but it's still worth locking down.

## Step-by-Step: How to Opt Out of Plex Ad Tracking

Do this on the **web app** (app.plex.tv) first — it exposes every toggle. Mobile and TV apps have a subset.

1. **Sign in** at app.plex.tv and click your **profile avatar** (top right).
2. Open **Account Settings** → **Privacy**.
3. Toggle **"Advertise to me"** to **OFF**. This disables personalized ads and stops your ad ID from being used for targeting. You'll still see ads on free content, but they'll be contextual, not behavioral.
4. Toggle **"Send playback data to Plex"** to **OFF** if you don't want viewing telemetry feeding recommendation and ad models.
5. Under **"Data sharing with partners,"** disable **"Share data with third parties for marketing purposes."** This is the switch most directly tied to the studio/advertiser pipeline.
6. **Reset your advertising ID** (Android/iOS apps: Settings → Privacy → Reset Ad ID). This severs the link between your past behavior and future targeting.
7. **Review connected devices.** Remove old TVs, consoles, or shared accounts you no longer use — each carries its own ad identifier.

After step 3 and 5, ticket prompts and showtime ads still appear, but they're driven by coarse signals (region, catalog popularity) rather than your individual clickstream.

## Common Issues, Workarounds, and What You Should Know

- **"The toggle keeps reverting."** Plex settings sync per-account, but TV apps cache the old value. Force-close the app or sign out/in on the TV to refresh.
- **"I still see ticket ads."** Expected. Opting out of *personalization* doesn't remove ads from free content — it only stops your data from being used to target them. Removing ads entirely requires **Plex Pass** (which also unlocks hardware transcoding and DVR).
- **Managed users and shared accounts.** Each managed user inherits the home admin's ad settings in some app versions. Verify per-profile if you share a server.
- **Cost angle.** Plex Pass runs about $6.99/month or ~$119.99 lifetime. If ad-free streaming plus privacy is the goal, that's the cleanest path — and it keeps your self-hosted library untouched.
- **Alternative:** If ticketing integrations annoy you, pin your own library to the home screen and hide the free "Movies & Shows" rows via **Settings → Online Media Sources → Disable**. This removes the discovery surface entirely — and with it, the ticket prompts.

## Frequently Asked Questions (FAQ)

### Does Plex sell my personal watch history to advertisers?
No. Your self-hosted library watch history stays on your server. What's shared for advertising is discovery activity (searches, clicks, trailer views) plus a device ad ID — and only if you leave the relevant privacy toggles on.

### How do I stop Plex from showing movie ticket ads?
You can't remove ads from free content without Plex Pass, but you can disable the discovery surface: go to **Settings → Online Media Sources** and turn off "Movies & Shows" and "Discover." This eliminates the ticket prompt rows entirely.

### Is opting out of Plex ad tracking permanent?
It's persistent per account, but app updates and re-installs can reset device-level ad IDs. Re-check **Settings → Privacy** after major app updates and reset your ad ID periodically.

### Does Plex Pass remove the ticketing ads?
Yes — Plex Pass removes ads from free content, which also removes the ticketing prompts tied to them. Your own media library is unaffected either way.

## Final Verdict

The Plex ticketing expansion is a monetization move, not a data grab of your personal library — but the defaults are generous to advertisers. **Spend five minutes in Settings → Privacy**: kill "Advertise to me," disable third-party marketing sharing, and reset your ad ID. If the ticket prompts still bother you, either hide the Online Media Sources rows or spring for Plex Pass. Do the privacy pass today; it's the highest-value five minutes you'll spend in the app this month.