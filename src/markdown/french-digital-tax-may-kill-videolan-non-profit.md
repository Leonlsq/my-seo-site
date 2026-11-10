---
title: "French Digital Tax vs VLC: How to Support VideoLan in 2026"
description: "Worried the French digital tax may kill VideoLan? Here's how VLC users can support the non-profit, plus workarounds and alternatives to protect playback."
pubDate: 2026-10-31
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## French Digital Tax vs VLC: What Actually Happens to VideoLan (and What You Can Do)

If you saw VideoLan's tweet warning that France's digital tax framework could "kill" the non-profit behind VLC, you're probably asking a practical question: **will VLC still work, and what do I do about it?** Here's the direct answer: VLC's codebase is open source (GPLv2/GPLv3) and hosted on GitHub, so the player itself won't vanish overnight. The real risk is to VideoLan's *funding, legal overhead, and development pace* — the non-profit's ability to pay lawyers, maintain infrastructure, and ship updates. This guide breaks down the mechanics, gives you concrete ways to support VideoLan, and covers workarounds if distribution or updates slow down.

## What the French Digital Tax Means for a Non-Profit Like VideoLan

France's digital services tax (often called the "GAFA tax") targets large companies with significant French revenue — but the compliance *burden* and legal exposure can spill onto smaller entities depending on how thresholds and definitions are applied. VideoLan is a small French non-profit with a global user base of roughly **hundreds of millions of downloads** for VLC. The tension: a non-profit with tiny revenue can face disproportionate administrative and legal costs.

Key context from the community discussion (107 points, 95 comments on Hacker News):

- **VideoLan is French-registered** — it's legally exposed to French tax rules in a way a US or German foundation wouldn't be.
- **VLC has near-zero monetization** — no ads, no telemetry, no paid tiers. Revenue comes from donations and occasional corporate support.
- **The tax itself isn't the killer — the compliance cost is.** Small orgs spend proportionally more on accountants and lawyers than giants do.

> **Bottom line:** The threat is operational, not technical. VLC will keep playing your files. What's at risk is the *velocity* of updates, security patches, and platform support (especially on mobile app stores and new OS versions).

## How to Support VideoLan Right Now (5 Concrete Steps)

1. **Donate directly.** VideoLan accepts donations via its official site (videolan.org). Even €5–€10 offsets legal/accounting overhead. This is the highest-impact action.
2. **Buy from the official store.** VideoLan sells VLC-branded merchandise and cones (the traffic-cone mascot). Revenue goes straight to the non-profit.
3. **Contribute code or docs.** VLC is on GitHub under `videolan/vlc`. Bug reports, translations (VLC supports 80+ languages via Weblate), and patch reviews reduce paid workload.
4. **Mirror the downloads.** If you run infrastructure, hosting a VLC mirror reduces bandwidth costs for the project.
5. **Spread accurate info.** Correct the misconception that "VLC is shutting down" — panic drives users to sketchy third-party APK sites, which is a real security risk.

### Donation impact table

| Action | Effort | Impact on VideoLan |
|---|---|---|
| One-time donation (€10) | 2 min | Directly offsets legal/accounting costs |
| Monthly donation (€3/mo) | 5 min | Predictable funding for infrastructure |
| Merch purchase | 5 min | Revenue + brand visibility |
| Code/docs contribution | Hours | Reduces paid development load |
| Running a download mirror | Setup once | Cuts hosting costs |

## If VLC Updates Slow Down: Practical Workarounds

If legal costs delay releases, you still need reliable playback and **security patches**. Here's how to stay safe without depending on a single distribution channel:

- **Verify your download source.** Only use `videolan.org` or your OS's official package manager (apt, dnf, Homebrew, winget, F-Droid). Avoid random "VLC APK" sites — they're a common malware vector.
- **Pin a known-good version.** On Linux: `sudo apt install vlc=3.0.x` (check `apt-cache policy vlc`). On Windows, keep the last signed installer.
- **Use package-manager builds.** Distros like Debian and Fedora rebuild VLC from source and apply their own security patches — you're insulated from upstream release delays.
- **Enable automatic security updates** for your OS so codec and library CVEs (e.g., in FFmpeg, which VLC bundles) get patched at the system level.
- **Keep a fallback player installed.** mpv (open source, actively maintained, excellent codec support) and MPC-HC/MPC-BE on Windows are solid backups.

### VLC vs. fallback players (2026)

| Player | Open source | Cross-platform | Best for |
|---|---|---|---|
| VLC | Yes (GPL) | Windows, macOS, Linux, iOS, Android | Universal format support |
| mpv | Yes (GPL) | Windows, macOS, Linux | Power users, scripting, quality |
| MPC-BE | Yes (GPL) | Windows | Lightweight Windows playback |
| PotPlayer | No | Windows | Feature-rich but closed source |

## Frequently Asked Questions (FAQ)

### Is VLC shutting down because of the French digital tax?
No. VideoLan has warned about financial and legal pressure, not a shutdown. VLC's source code is open and mirrored on GitHub, so the software can't simply disappear — the concern is funding, legal costs, and slower updates.

### Will VLC stop working on my device?
Your installed copy keeps working. The realistic risks are delayed security patches and slower support for new OS versions or app-store policy changes. Keep your OS updated and download only from official sources.

### How can I donate to VideoLan?
Visit the official VideoLan website (videolan.org) and use the donation link, or buy merchandise from the official store. Avoid third-party "donate for VLC" pages that aren't linked from videolan.org.

### What's the safest alternative to VLC if updates stall?
mpv is the strongest open-source alternative with active maintenance and broad codec support. On Windows, MPC-BE is a lightweight option. Always install from official repos or the project's own site.

## Final Verdict

Don't panic-uninstall VLC — it's still one of the safest, most capable media players available, and its open-source nature means it can't be "killed" by a tax bill. But do take the warning seriously: **donate if you can, download only from official sources, and keep a maintained fallback like mpv ready.** The single most useful thing you can do today is send €5 to VideoLan and stop sharing links to unofficial APK mirrors — that combination protects both the project and your own device.