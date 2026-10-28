---
title: "Windows 11 on a CD-ROM: How NTDEV's Tiny11 ISO Works"
description: "NTDEV squeezed Windows 11 onto a single CD-ROM. Here's how the tiny11 whole ISO works, its limits, and how to test it safely in a VM."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How Did Windows 11 Fit on a Single CD-ROM?

NTDEV, the developer behind the **tiny11** project, has demonstrated a Windows 11 install that fits entirely on a single **700 MB CD-ROM** — a feat that sounds impossible given that Microsoft's official Windows 11 ISO weighs in at roughly **5.5 GB to 7 GB**. The short answer: this is a stripped-down, heavily compressed experiment, not a daily-driver operating system. The "whole ISO" build removes most of Windows' servicing stack, modern apps, and driver payloads, then applies aggressive compression so the install image lands under the ~700 MB CD-R limit. If you're here because you saw the headline and want to know whether you can (or should) try it, this guide covers how it works, what breaks, and how to run it safely.

## What's Inside the CD-ROM Build: Specs and Trade-offs

NTDEV's whole-ISO concept differs from the original tiny11 in one key way: earlier tiny11 releases were *installable* but still needed a larger USB or DVD because the compressed image exceeded CD capacity. The "whole ISO" version pushes the entire bootable image under the CD-ROM threshold. Here's the practical breakdown:

| Feature | Official Windows 11 ISO | tiny11 (standard) | tiny11 "whole ISO" (CD-ROM) |
|---|---|---|---|
| Media size | ~5.5–7 GB | ~2–3 GB | Under ~700 MB |
| Boots from CD/DVD | No (too large) | Usually USB | Yes |
| Windows Update | Full | Partial | Largely disabled |
| Microsoft Store | Included | Removable | Removed |
| Defender | Included | Optional | Stripped/limited |
| Recommended use | Production | Low-spec PCs | Testing, retro hardware, demos |

**What gets cut to hit 700 MB:**
- **WinSxS component store** — the servicing folder is massively reduced, which is why updates often fail.
- **Modern apps and Store** — Calculator, Photos, Store, and UWP dependencies are removed.
- **Driver payloads** — only a minimal generic driver set remains, so expect missing Wi-Fi or GPU drivers.
- **Recovery and language packs** — extra locales and WinRE are trimmed.
- **Compression** — the image uses high-ratio compression (LZX/ESD-style) to shrink the payload further.

## How to Test the CD-ROM Windows 11 Build Safely (Step-by-Step)

Do **not** install this on your main PC. Use a virtual machine or a spare machine. Here's the safe path:

1. **Download from the official source only.** Get the ISO from NTDEV's verified channels (GitHub/X). Third-party mirrors frequently bundle malware into modified Windows images.
2. **Verify the checksum.** Compare the SHA-256 hash against the one published by NTDEV before doing anything else.
3. **Set up a VM.** Use VirtualBox or VMware with **2 GB RAM minimum, 2 CPU cores, and a 20 GB virtual disk**. Enable a legacy BIOS or UEFI boot as required by the image.
4. **Attach the ISO as a virtual CD.** In VirtualBox: *Settings → Storage → Add Optical Drive → Choose Disk File*. This mimics the CD-ROM boot exactly.
5. **Boot and install.** The installer is trimmed, so expect a faster but more limited OOBE (out-of-box experience). Skip network setup if Wi-Fi drivers are absent.
6. **Install drivers manually.** Have your network and chipset drivers on a second virtual disk or USB passthrough, because Windows Update will likely be non-functional.
7. **Snapshot before experimenting.** Take a VM snapshot so you can roll back after testing.

**If you insist on physical hardware:** burn to a CD-R at low speed (8x–16x) for reliability, and only use a retired PC you don't depend on.

## Common Issues, Alternatives, and What You Should Know

**Expect these failures:**
- **Windows Update errors** — the reduced WinSxS store causes update rollbacks (common error codes like 0x800f081f).
- **Missing drivers** — no Wi-Fi, Bluetooth, or GPU acceleration out of the box.
- **No Store or Defender** — you'll need to source security software and apps manually.
- **Activation quirks** — modified images may not activate cleanly with a standard retail key.

**Better alternatives depending on your goal:**
- **Low-spec PC you actually use?** Use standard **tiny11** on a USB drive instead — it retains more functionality.
- **Just want a lighter Windows?** Try **Windows 11 LTSC** or a debloated install via tools like **Chris Titus Tech's WinUtil** on a full ISO.
- **Testing/curiosity?** The CD-ROM build is perfect for a VM demo or retro hardware showcase — not production.

## Frequently Asked Questions (FAQ)

### Can I install the CD-ROM Windows 11 build on a real PC?
Technically yes, if your machine boots from CD/DVD and meets minimum RAM. But with drivers, updates, and Store removed, it's unsuitable as a daily driver. Use a VM or spare hardware.

### Is the tiny11 whole ISO safe to download?
Only if you get it from NTDEV's official GitHub or verified social channels and check the SHA-256 hash. Modified Windows images from random mirrors are a common malware vector.

### Why does Windows 11 normally need 5+ GB but this fits on 700 MB?
Because NTDEV strips the servicing stack, apps, drivers, and language packs, then applies high-ratio compression. The result boots and installs but loses most update and app functionality.

### Does the CD-ROM build still get security updates?
Largely no. The reduced component store breaks Windows Update, and Defender is stripped. Treat it as an offline test image, not a secure OS.

## Final Verdict

NTDEV's CD-ROM Windows 11 is an **impressive engineering demo, not a usable OS**. If you're curious, run it in a VM with a verified ISO and a snapshot ready — it's a fun experiment and a great showcase of how much of Windows is optional bloat. But for any real machine, stick with **standard tiny11 on USB**, **Windows 11 LTSC**, or a debloated full install. The 700 MB milestone is a headline, not a recommendation.