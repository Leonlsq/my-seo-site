---
title: "Sonarr Torrent Poisoning: How to Fix Fake Files & Malware"
description: "Torrent sites poisoned my Sonarr setup with fake files. Here's how to detect Sonarr torrent poisoning, fix it, and harden your *arr stack fast."
pubDate: 2026-10-16
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Sonarr Torrent Poisoning: Why Your Downloads Keep Failing

If you run a Sonarr + qBittorrent stack, there's a growing attack you need to know about: **torrent poisoning**. Someone uploads fake releases to public trackers with names that look identical to real ones, Sonarr grabs them automatically, and you end up with garbage files, failed imports, or worse — malware. This isn't a bug in Sonarr. It's a supply-chain attack on the torrent ecosystem itself, and it was documented in detail by a developer whose Sonarr instance was repeatedly targeted.

The short version: **public trackers are untrusted input**. If your Sonarr accepts anything without quality gates, size validation, or indexer filtering, you're a target. Here's how to detect it and lock your stack down.

## How Torrent Poisoning Works (And How to Stop It)

The attack pattern is consistent. An attacker uploads a file to a public tracker with a title matching a popular show — correct season, episode, resolution, and release group naming. Sonarr's indexer sees it, matches it against your quality profile, and downloads it. The file is either corrupted, a password-protected archive, a fake `.exe`, or a tiny file masquerading as a 4K rip.

### Detection Checklist

- **File size mismatch**: A "1080p" episode that's 40 MB instead of 1.5 GB
- **Extension anomalies**: `.exe`, `.scr`, `.bat`, or password-protected `.rar` in a video release
- **Import failures**: Sonarr logs "No files found are eligible for import"
- **Repeated re-downloads**: Same episode grabs over and over from different fake releases
- **Suspicious release groups**: Names you've never seen on private trackers

### Step-by-Step Fix

1. **Enable minimum file size limits.** In Sonarr, go to *Settings → Quality* and set per-quality min/max sizes. A 1080p episode should never be under 300 MB.
2. **Add required and ignored words.** *Settings → Indexers → Restrictions*. Add "password", "protected", "exe" to ignored terms.
3. **Switch to private trackers.** This is the single biggest fix. Poisoning is overwhelmingly a public-tracker problem.
4. **Use multiple indexers with priority.** Sonarr's *Settings → Indexers* lets you rank trusted sources higher so they're tried first.
5. **Enable "Reject if no files found"** in your download client integration to stop infinite retry loops.
6. **Run a post-download validation script.** Tools like `unpackerr` and custom bash hooks can scan for archives and flag them before import.
7. **Isolate your download client.** Run qBittorrent in Docker with read-only mounts and no host network access.

## Common Issues and Hardening Your Stack

The biggest mistake home-server operators make is treating Sonarr as "set and forget." It isn't. The moment you point it at public indexers, you've opened an automated pipeline that will download *anything* matching a regex.

| Risk | Mitigation | Difficulty |
|---|---|---|
| Fake releases | Private trackers + size limits | Easy |
| Malware in archives | Ignore "rar/exe" terms | Easy |
| Infinite retry loops | Reject no-files-found | Easy |
| Indexer compromise | API key rotation | Medium |
| Container escape | Docker isolation | Medium |

Also worth knowing: **Sonarr's indexer sync** (Prowlarr/Jackett) can propagate bad indexers across your whole stack. Audit your Prowlarr indexers monthly and remove anything you don't recognize.

If you can't access private trackers, consider **Usenet** as an alternative. It has its own poisoning issues but far fewer, and providers like Frugal Usenet or Newshosting offer retention guarantees that make fake posts easier to spot.

## Frequently Asked Questions (FAQ)

### What is torrent poisoning in Sonarr?
Torrent poisoning is when someone uploads fake or malicious files to public trackers with names designed to trick automated tools like Sonarr into downloading them. The goal is usually to spread malware, waste bandwidth, or disrupt automated media servers.

### Can Sonarr get a virus from torrents?
Sonarr itself won't execute files, but it *will* download them. If your download client auto-extracts archives or you manually open a fake `.exe`, you can absolutely get infected. Isolate your download client and never open downloaded archives manually.

### How do I stop Sonarr from downloading bad releases?
Set minimum file sizes per quality, add ignored words like "password" and "exe," prioritize private trackers, and enable "reject if no files found." These four changes stop the vast majority of poisoning attempts.

### Is Sonarr safe to use in 2026?
Yes, with proper configuration. The tool is safe; the *sources* you connect it to are the risk. Treat public indexers as hostile and you'll be fine.

## Final Verdict

Torrent poisoning isn't going away — it's getting smarter. The fix isn't abandoning Sonarr; it's **hardening it**. Start with size limits and ignored words today (five minutes of work), then move to private trackers or Usenet as your primary source. If you're running anything on public indexers without restrictions, you're not running a media server — you're running an open door. Lock it down.