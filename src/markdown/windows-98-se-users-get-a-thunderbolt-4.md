---
title: "How to Install the Windows 98 Thunderbolt 4 Driver (AI Vibe-Coded Guide)"
description: "Step-by-step guide to install the experimental AI vibe-coded USB4 and Thunderbolt 3/4 driver on Windows 98 SE, Me, XP, Vista, and 7, plus fixes and risks."
pubDate: 2026-10-21
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Install the Experimental Thunderbolt 4 Driver on Windows 98 SE (and What Actually Works)

A developer has released an experimental, AI-assisted ("vibe-coded") driver that brings USB4 and Thunderbolt 3/4 support to Windows 98 SE — plus Windows Me, XP, Vista, and 7. If you saw the headline and want to try it on a retro rig, here's the honest reality: this is a **proof-of-concept driver**, not a plug-and-play solution. It can enumerate a Thunderbolt controller and basic USB tunneling on supported chipsets, but hot-plug, PCIe tunneling (eGPU, NVMe), and DisplayPort passthrough are largely broken or untested. This guide walks you through safe installation, what to expect, and how to roll back if your retro build misbehaves.

## What the Driver Actually Supports (Specs & Compatibility Table)

Before you touch a floppy image or ISO, match your hardware to the table below. The driver targets the **Intel JHL-series and Maple Ridge (JHL8540) Thunderbolt controllers** with a USB4-compatible firmware. Older Alpine Ridge (JHL6540) and Titan Ridge (JHL7540) chips are hit-or-miss.

| OS | Boot Support | USB Tunneling | PCIe Tunneling | DisplayPort Alt Mode | Hot-Plug |
|---|---|---|---|---|---|
| Windows 98 SE | ✅ (experimental) | ⚠️ Partial | ❌ | ❌ | ❌ |
| Windows Me | ✅ (experimental) | ⚠️ Partial | ❌ | ❌ | ❌ |
| Windows XP (SP3) | ✅ | ⚠️ Partial | ❌ | ❌ | ❌ |
| Windows Vista | ✅ | ✅ | ❌ | ⚠️ | ⚠️ |
| Windows 7 (x86/x64) | ✅ | ✅ | ❌ | ⚠️ | ⚠️ |

**Key caveats:**
- **No PCIe tunneling** means no external GPU, no Thunderbolt NVMe enclosures, and no Thunderbolt-to-10GbE adapters.
- **DisplayPort Alt Mode** is untested on 98/Me/XP; expect a black screen if you chain a monitor.
- **Firmware matters more than the driver.** You need a controller running firmware that exposes the legacy USB4 compatibility path — most retail docks ship with newer firmware that breaks this.

## Step-by-Step: Installing the Driver on Windows 98 SE

Follow this exactly. Skipping steps is the #1 cause of "VXD not found" boot loops.

1. **Back up your drive first.** Use a tool like Norton Ghost or a raw `dd` image to an external USB 2.0 drive. This driver touches the PCI bus enumeration layer.
2. **Verify your controller.** Boot into a Linux live USB and run `lspci -nn | grep -i thunderbolt`. You need a JHL8540 or JHL-series ID. If you see nothing, stop here.
3. **Download the driver package** from the project's repository (GitHub mirror). Extract to a FAT32 floppy image or a CD-R — Windows 98 SE cannot read the driver from a USB4-attached drive (chicken-and-egg problem).
4. **Boot into Safe Mode** (hold Ctrl during the "Starting Windows 98" splash).
5. **Open Device Manager** → look for "PCI System Peripheral" or an unknown "USB4 Host Router" device.
6. **Update Driver** → "Specify a location" → point to the extracted `\WIN98\` folder.
7. **Reboot normally.** On first boot, the driver will attempt to enumerate the controller. If you see a "Thunderbolt controller initialized" message in `C:\BOOTLOG.TXT`, you're in business.
8. **Test with a USB 2.0 device only.** Do not plug in a Thunderbolt dock or NVMe enclosure on the first boot.

### Windows XP / Vista / 7 Quick Notes
- **XP:** Use the `\WINXP\` INF. You may need to disable driver signature enforcement via `gpedit.msc`.
- **Vista/7:** The `\WIN7\` package includes a signed `.cat` file — install via `pnputil` if Device Manager refuses.

## Common Issues and Workarounds

- **"Cannot find VXD TB4DRV" on boot:** Your controller firmware is too new. Downgrade the controller firmware (risky) or abandon the experiment.
- **Boot hang after install:** Boot into Safe Mode, open `SYSTEM.INI`, and comment out the `device=TB4DRV.386` line under `[386Enh]`.
- **USB devices not detected:** The driver only supports USB 2.0 tunneling on 98/Me. USB 3.x devices will fail enumeration.
- **Blue screen on shutdown:** Known bug in the 98 SE build. Use the "Restart in MS-DOS mode" option as a workaround.

**Alternatives if this fails:**
- **USB 2.0 PCI card** (e.g., VIA VT6212) — reliable, cheap, works out of the box on 98 SE.
- **FireWire (IEEE 1394)** — still the best retro external storage path for 98/Me.
- **Modern host bridge** — run a Linux VM with USB passthrough on a modern machine if you need Thunderbolt peripherals.

## Frequently Asked Questions (FAQ)

### Is the Windows 98 Thunderbolt 4 driver safe to install?
It's experimental and unsigned. It can corrupt your boot configuration or cause boot loops. Only install it on a backed-up retro build you can afford to reimage.

### Does this driver enable eGPU or external NVMe on Windows 98?
No. PCIe tunneling is not implemented. The driver only handles USB tunneling and basic controller enumeration. eGPU and NVMe enclosures will not work.

### Which Thunderbolt controllers are supported?
Primarily Intel JHL8540 (Maple Ridge) and select JHL-series controllers with compatible firmware. Alpine Ridge and Titan Ridge support is inconsistent.

### Will it work on Windows 7 with a Thunderbolt dock?
Partially — USB tunneling works on Windows 7, but DisplayPort Alt Mode and hot-plug are unreliable. Test with a single USB device before trusting a full dock.

## Final Verdict

This AI vibe-coded driver is a **fascinating technical curiosity, not a daily-driver solution**. If you're a retro computing enthusiast with a spare JHL8540 card and a backed-up Windows 98 SE build, it's worth an afternoon of experimentation — the USB 2.0 tunneling alone is a neat trick. But if you need reliable Thunderbolt 4 on legacy hardware, skip it and use a **USB 2.0 PCI card or FireWire** instead. The driver is a milestone, not a product — treat it accordingly.