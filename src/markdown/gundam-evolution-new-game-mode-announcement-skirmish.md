---
title: "Gundam Evolution Skirmish Mode: How to Play on Side 7"
description: "Learn how to install Side 7, unlock the new Skirmish Team Deathmatch mode, and fix common connection errors in Gundam Evolution's private server."
pubDate: 2026-11-04
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Gundam Evolution Skirmish Mode: What It Is and How to Access It

Bandai Namco sunset *Gundam Evolution* in November 2023, but the private server project **Side 7** has kept the hero shooter alive — and on November 4, 2026, its maintainers announced **Skirmish**, a Team Deathmatch mode that never shipped during the official live service. If you're searching for how to actually play it, here's the short answer: Skirmish is **not** available through Steam's public build. You need a Side 7 account, the community launcher, and a patched client that points to the Side 7 backend. This guide walks you through the full setup, the exact match settings, and the fixes for the connection errors most new players hit on their first launch.

## Step-by-Step: Playing Skirmish on the Side 7 Private Server

The setup takes roughly 15–20 minutes if your client is already installed. Follow these steps in order — skipping the launcher verification step is the #1 cause of "server not found" errors.

1. **Remove the official Steam build from your launch path.** Side 7's launcher conflicts with Steam's DRM handshake. You can keep the game files, but launch only through the Side 7 launcher, not the Steam library entry.
2. **Create a Side 7 account** on the community portal and verify your email. Accounts are free, but unverified accounts are limited to spectator mode.
3. **Download the Side 7 launcher** and point it at your existing *Gundam Evolution* install directory (default: `C:\Program Files (x86)\Steam\steamapps\common\GundamEvolution`).
4. **Let the launcher patch the client.** The Skirmish update is a delta patch of roughly 1.8–2.4 GB depending on your base version. Do not interrupt this step — a partial patch corrupts the `paks` folder and forces a full re-download.
5. **Log in through the launcher**, not the in-game login screen. In-game login is disabled on Side 7.
6. **Select Skirmish from the Play menu.** If the mode is greyed out, your client patch is outdated — re-run the launcher's "Verify Files" option.

### Skirmish Mode Rules at a Glance

| Setting | Skirmish (Side 7) | Standard Point Capture |
|---|---|---|
| Objective | Team Deathmatch (kill count) | Capture/hold zones |
| Score to win | 50 kills (default) | Point threshold |
| Respawn | Instant wave respawn (5s) | Timed respawn |
| Match length | ~8–10 minutes | ~12–15 minutes |
| Unit lock | No duplicate restriction by default | Duplicate restricted |
| Friendly fire | Off | Off |

Skirmish removes the objective layer entirely, so mobility units like **Barbatos** and **Zaku II (Melee)** gain disproportionate value — there's no reason to hold ground, only to trade kills efficiently. If you're coming from Point Capture, expect a much faster, more aggressive meta.

## Common Issues and What You Should Know

**"Failed to connect to matchmaking" on Skirmish queue.** This is almost always a stale session token. Log out of the launcher completely, delete the `%appdata%\Side7\session.cache` file, and log back in. The token expires after 24 hours of inactivity and the launcher doesn't always refresh it.

**Mode missing from the Play menu.** Check your launcher version against the pinned announcement in the Side 7 Discord. Skirmish requires launcher build 2.4+; older builds show the mode but fail silently on queue.

**High ping / rubber-banding.** Side 7 runs regional relays. In the launcher settings, set your region manually instead of leaving it on "Auto" — Auto frequently routes EU players to NA relays during off-peak hours.

**Is this legal / will my account be banned?** Side 7 operates independently of Bandai Namco and does not touch official accounts. There is no live-service account left to ban. That said, the project relies on community donations and volunteer moderation — treat it as a preservation effort, not a guaranteed permanent service.

**What Skirmish is *not*:** it isn't a ranked mode, it doesn't award progression currency, and there's no matchmaking skill bracket yet. It's a casual TDM playlist — good for warmups and for experiencing cut content, not for competitive play.

## Frequently Asked Questions (FAQ)

### Is the Gundam Evolution Skirmish mode official?
No. Skirmish was never released during the 2022–2023 live service. It's a community-restored mode implemented by the Side 7 private server maintainers, announced November 4, 2026.

### Do I need to own Gundam Evolution on Steam to play Skirmish?
You need the game client files, which most players already have from the free-to-play era. Side 7 does not distribute the full client — only patches — so new players must source the base install separately.

### Why is Skirmish greyed out in my Play menu?
Your launcher or client patch is outdated. Update to launcher build 2.4 or later and run "Verify Files" before relaunching.

### Can I play Skirmish with friends in a party?
Yes. Party queue is supported up to six players. Cross-region parties work but will inherit the host's relay region, which can spike ping for off-region members.

## Final Verdict

If you played *Gundam Evolution* before the shutdown, Skirmish is worth the 20-minute setup — it's the fastest, most chaotic version of the game's combat loop, and it's genuinely novel content rather than a rehash. Install the Side 7 launcher, patch to build 2.4+, and set your region manually before your first queue. If you're brand new and don't have the base client files, the barrier is higher and the mode is casual-only, so temper your expectations. Either way, verify your patch before you blame the servers — nine out of ten "Skirmish won't load" reports are outdated clients.