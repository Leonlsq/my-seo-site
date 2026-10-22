---
title: "Plex 4K DoVi HDR10 Infinite Spinning Circle Fix (2026)"
description: "Plex 2026.20.0 beta stuck on infinite spinning circle with 4K DoVi HDR10 on iOS/tvOS? Here are the real fixes and workarounds that work."
pubDate: 2026-10-22
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Fix the Plex 4K DoVi HDR10 Infinite Spinning Circle on iOS and tvOS

If you updated to the Plex 2026.20.0 beta on iOS or tvOS and your 4K Dolby Vision (DoVi) or HDR10 files now hang on an infinite spinning circle instead of playing, you are not alone. The bug is documented in the official Plex forums thread (page 5 of the 2026.20.0 beta report) and has been amplified on Hacker News, where users connected the playback regression to Plex's reported layoff of its entire player team. The direct takeaway: **this is a client-side playback/transcoding negotiation bug, not a corrupted file and not your TV.** You can work around it today by forcing a Direct Play path, disabling DoVi on the client, or rolling back the beta — and this guide walks through each fix in order of effort.

## Step-by-Step Fixes (Try in This Order)

### Fix 1: Force Direct Play and Disable Transcoding on the Client
The spinning circle is most often the client failing to negotiate a DoVi/HDR10 stream and looping on a transcode decision. Force the client to stop asking the server to transcode.

1. Open Plex on iOS/tvOS → **Settings → Video Quality**.
2. Set **Home Streaming** to **Maximum** and **Remote Streaming** to **Maximum**.
3. Enable **Play Smaller Videos at Original Quality**.
4. Under **Advanced**, turn **off** "Automatically Adjust Quality."
5. Reopen the 4K DoVi file and start playback.

If the file now plays, the culprit is the transcode path, not the file.

### Fix 2: Disable Dolby Vision on the Client (HDR10 Fallback)
DoVi Profile 5 and Profile 8 files are the most commonly reported failures. Forcing an HDR10 fallback sidesteps the broken DoVi pipeline.

- **tvOS (Apple TV 4K):** Settings → Video and Audio → **Match Content** → set **Match Dynamic Range** to **Off**, then set the Apple TV output to **HDR10** (not Dolby Vision). Restart the Plex app.
- **iOS (iPhone/iPad):** Settings → Display & Brightness → disable **Dolby Vision** auto-switching where available, then relaunch Plex.

This trades a small color-grading difference for a working stream.

### Fix 3: Roll Back the Beta
If you are on the 2026.20.0 beta specifically, the fastest permanent fix is to leave the beta channel.

1. Delete the beta app from the device.
2. Reinstall the current **stable** Plex release from the App Store.
3. In the Plex web app, go to **Settings → Server → Transcoder** and confirm **Enable HDR tone mapping** is set appropriately for your hardware.

Beta builds are where player regressions land first — especially with a reduced player team.

### Fix 4: Server-Side Transcode Workaround
If you must stay on the beta, pre-transcode the problem files so the client never has to negotiate DoVi.

| Setting | Recommended Value | Why |
|---|---|---|
| Video codec | H.264 (High) | Broadest client compatibility |
| Container | MP4 | Avoids DoVi signaling issues |
| HDR handling | Tone-map to SDR or force HDR10 | Skips broken DoVi path |
| Audio | AAC 5.1 | Prevents audio/video desync loops |

Use HandBrake or Tdarr to batch-convert your 4K DoVi library to HDR10/SDR MP4 as a stopgap.

## What You Should Know (Information Gain)

- **This is a client bug, not a server bug.** Your media server and files are fine; the iOS/tvOS player is failing to complete the DoVi/HDR10 handshake.
- **The timing is not a coincidence.** Plex reportedly laid off its entire player team, and this beta regression is the kind of issue that team historically caught before stable release. Expect slower fixes on the beta channel.
- **Jellyfin and Infuse are viable alternatives** if you need reliable 4K DoVi playback *today*. Infuse on Apple TV handles DoVi Profile 5/8 natively and is the most common community recommendation in the HN thread.
- **Do not factory reset your Apple TV or rebuild your library.** Multiple users report doing this with no effect — the bug follows the app version, not the device state.

## Frequently Asked Questions (FAQ)

### Why does Plex spin forever on 4K Dolby Vision but play 1080p fine?
The 1080p path uses standard H.264/SDR negotiation, which is stable. 4K DoVi/HDR10 requires the client to negotiate dynamic range and tone mapping, and that handshake is what regressed in the 2026.20.0 beta. Forcing Direct Play or an HDR10 fallback bypasses the broken step.

### Did Plex laying off the player team cause this bug?
Plex has not officially confirmed causation, but the regression appeared in a beta build released around the reported layoffs, and community analysis on the Plex forums and Hacker News points to reduced player-team QA. Treat it as a strong correlation, not a confirmed cause.

### Is there a permanent fix yet?
As of the 2026.20.0 beta, no official patch has shipped. The reliable permanent fix is rolling back to the stable release. Watch the Plex forums thread for a hotfix build.

### Will switching to Jellyfin or Infuse fix 4K DoVi playback?
Yes — Infuse (Apple TV/iOS) and Jellyfin with a compatible client both handle DoVi Profile 5/8 more reliably than the current Plex beta. If 4K DoVi is core to your setup, this is the lowest-friction escape hatch.

## Final Verdict

**Do not stay on the 2026.20.0 beta if you watch 4K Dolby Vision content.** Roll back to the stable Plex release first — it is the only fix that reliably restores playback without compromising your HDR experience. If you need DoVi playback on Apple hardware and cannot wait for a Plex hotfix, install **Infuse** as a secondary player and keep Plex for library management. Given the reported player-team layoffs, expect beta regressions to persist longer than usual, so treat stable builds as your default and only opt into betas on a secondary device.