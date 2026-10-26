---
title: "CompUSA Y2K Store Tour: Relive the 2000 PC Era Setup"
description: "Rare 2000 CompUSA footage explained: recreate the Y2K PC era with period-correct specs, translucent iMacs, Presarios, and retro gaming hardware."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What the CompUSA November 2000 Footage Actually Shows (And How to Rebuild It)

A newly surfaced archival tour of the CompUSA NYC store from November 2000 is more than nostalgia bait — it's a time capsule of the exact hardware that defined the Y2K PC era. If you watched that footage and found yourself searching for "CompUSA 2000 store tour," "translucent iMac G3 specs," or "how to build a Y2K retro PC," this guide converts that nostalgia into an actionable plan. Below you'll find the period-correct specs from that era, a step-by-step build guide for a Y2K-era retro rig, and the pitfalls nobody warns you about when buying 25-year-old hardware.

The footage captures a store mid-transition: Apple's translucent Bondi Blue and Graphite iMac G3s sitting near Compaq Presario 5000-series towers with their smoky acrylic front panels, alongside shelves of beige CRTs, boxed Sound Blaster cards, and dial-up accessories. That mix is your shopping list.

## Step-by-Step: Build a Period-Correct Y2K Retro PC (2000 Spec)

Here's a concrete build recipe based on what was actually on those CompUSA shelves in November 2000.

### Target Specs (Late 2000 Baseline)

| Component | Period-Correct Pick | Why It Matches the Footage |
|---|---|---|
| CPU | Intel Pentium III 800EB or AMD Athlon 900 (Socket A) | Flagship consumer chips of Q4 2000 |
| Motherboard | Intel i815E or VIA KT133 chipset | Standard in Presario/HP-era towers |
| RAM | 128–256 MB PC133 SDRAM | Typical retail config; 256 MB was "loaded" |
| GPU | NVIDIA GeForce2 MX or 3dfx Voodoo 3 3000 | Budget 3D cards sold alongside CompUSA bundles |
| Storage | 20–40 GB 7200 RPM IDE HDD | Standard OEM drive size in 2000 |
| Optical | 12x DVD-ROM or 8x4x32 CD-RW | DVD was the premium upsell |
| OS | Windows 98 SE or Windows Me | Windows 2000 for the "pro" crowd |
| Display | 17" CRT (1024x768 @ 85 Hz) | The dominant retail monitor |

### Build Steps

1. **Source the case first.** Look for a late-90s/early-2000s ATX mid-tower with a translucent or smoked acrylic front bezel — this is the visual signature of the Compaq Presario 5000 line seen in the footage. Local recyclers and eBay "retro PC" listings are your best bet.
2. **Verify the motherboard caps.** Before buying any Socket 370 or Socket A board, inspect for bulging or leaking capacitors. The 1999–2001 capacitor plague hit this generation hard.
3. **Install Windows 98 SE from CD.** Use a CD-ROM drive, not USB — Win98 SE has no native USB boot support. Have a floppy or a bootable CD ready.
4. **Cap RAM at 512 MB or less.** Windows 98 SE becomes unstable above 512 MB without patches; 256 MB is the sweet spot for authenticity and stability.
5. **Use a period GPU driver.** For GeForce2 MX, use Detonator 6.xx–12.xx era drivers. For Voodoo 3, use the final 3dfx reference drivers (1.07.00).
6. **Set the CRT to 1024x768 @ 85 Hz.** This matches the flicker-free sweet spot most 17" CRTs of the era could sustain.

## Common Issues, Alternatives, and What You Should Know

**Issue 1: IDE drives are dying.** 25-year-old spinning disks fail at high rates. Workaround: use an IDE-to-SD or IDE-to-CF adapter for reliability while keeping the period look. A CF card in an IDE adapter reads as a standard drive to Win98.

**Issue 2: Capacitor plague.** As noted, motherboards and PSUs from 1999–2001 are notorious. Recap or replace the PSU with a modern unit (verify ATX 2.x compatibility with your board's -5V needs; some older boards require it).

**Issue 3: Driver hunting.** Archive.org and VOGONS (the vintage computer forum) host driver mirrors. Download and burn drivers to CD before you start, since the machine won't have internet without a dial-up or Ethernet setup.

**Alternatives to a full build:**
- **Emulation route:** DOSBox-X and PCem run period software without hardware headaches — cheaper but less authentic.
- **Prebuilt retro sellers:** Expect $300–$600 for a tested, recapped Y2K rig; DIY typically runs $150–$350 depending on GPU.
- **The iMac G3 path:** If the translucent iMacs in the footage are your target, a working G3 (233–500 MHz) runs $100–$250, but check for failed PRAM batteries and yellowed plastics.

## Frequently Asked Questions (FAQ)

### What store was in the viral CompUSA footage from November 2000?
The footage shows the CompUSA location in New York City, captured in November 2000 during the peak of the Y2K PC retail era, featuring iMac G3s, Compaq Presarios, and CRT displays.

### How much does it cost to build a Y2K-era retro PC in 2026?
A DIY build using period-correct parts typically costs $150–$350, while tested prebuilt retro systems from specialist sellers run $300–$600. The GPU and CRT monitor are usually the largest line items.

### Can I run Windows 98 SE on modern hardware?
Not reliably. Modern chipsets lack Win98 driver support. Use period hardware (Socket 370/A) or virtualization/emulation tools like PCem or 86Box for an accurate experience.

### Why do 2000-era motherboards fail so often?
The 1999–2001 capacitor plague caused widespread premature failure of electrolytic capacitors. Always inspect and ideally recap boards from this era before use.

## Final Verdict

The CompUSA footage is a perfect excuse to build a Y2K retro rig — but go in with realistic expectations. **Recommended path:** buy a tested Socket 370 or Socket A board with fresh caps, pair it with a GeForce2 MX or Voodoo 3, use an IDE-to-CF adapter for storage reliability, and run Windows 98 SE at 1024x768 on a real CRT. Budget $250 and a weekend. If you only want the software nostalgia, skip the hardware and use 86Box — you'll get 90% of the experience for zero dollars and no capacitor anxiety.