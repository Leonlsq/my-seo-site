---
title: "West Bank Press Safety: How to Verify & Document Attacks"
description: "How to verify and safely document West Bank settler attacks on journalists and olive farmers using OSINT tools, metadata, and legal protocols."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Verify and Safely Document West Bank Settler Attacks

When reports surfaced that Israeli settlers attacked olive farmers and a Washington Post journalist in the West Bank — the incident involving reporter Heidi Levine, as covered by The Guardian and discussed on Hacker News — the immediate question for most people isn't *what* happened, but *how do I confirm this is real and not manipulated?* This guide is a practical, tool-by-tool playbook for verifying, archiving, and safely documenting conflict footage and eyewitness claims, whether you're a journalist, a researcher, or a citizen who wants to avoid spreading misinformation.

The core takeaway up front: **never share a conflict clip until you've run it through metadata extraction, reverse image search, and geolocation checks.** Below is the exact workflow, with the specific tools and parameters you need.

## Step-by-Step Verification & Documentation Workflow

### Step 1: Extract and Inspect Metadata
Before trusting any photo or video, pull its embedded data.

- **Photos:** Use `exiftool` (command line) or the free **ExifToolGUI**. Run:
  ```
  exiftool image.jpg
  ```
  Look for `CreateDate`, `GPSLatitude`, `GPSLongitude`, and `Model` (camera). A missing GPS tag doesn't mean fake — but a GPS tag placing the file in a different country *does* mean suspect.
- **Videos:** Use **MediaInfo** to read container metadata, then **InVID-WeVerify** (free browser extension) to extract keyframes and run reverse searches.

### Step 2: Reverse Image / Video Search
- **Google Lens** and **Yandex Images** (Yandex often outperforms Google for Middle East footage).
- **TinEye** for exact-match detection — it catches recycled older clips.
- For video, extract 3–5 keyframes with InVID, then search each frame individually.

### Step 3: Geolocate the Scene
Cross-reference visible landmarks against satellite imagery.

| Tool | Use Case | Cost |
|------|----------|------|
| Google Earth Pro | Terrain, road matching | Free |
| Sentinel Hub Playground | Recent satellite (10m resolution) | Free |
| Bing Maps Bird's Eye | Building footprints | Free |
| SunCalc | Shadow direction → time of day | Free |

Use **SunCalc** to check whether shadows in a clip are consistent with the claimed time. A "morning" attack with afternoon shadows is a red flag.

### Step 4: Chronolocate
Confirm the timestamp matches the claimed event date. Check weather archives (e.g., **Meteostat**) — if the clip shows clear skies but the region had storms that day, verify further.

### Step 5: Archive Immediately
Conflict footage disappears fast. Archive to:
- **Wayback Machine** (web.archive.org/save/)
- **archive.today**
- Local hash: run `sha256sum file.mp4` and store the hash — this proves the file wasn't altered later.

### Step 6: Document Safely (For Field Journalists)
If you're physically documenting:
1. **Enable lock-screen emergency SOS** on your phone and share live location with a trusted editor.
2. **Use encrypted cloud backup** (Proton Drive, Tresorit) — not local-only storage.
3. **Wear identifiable PRESS markings** and carry press credentials visibly.
4. **Record in short clips** (30–60s) so a single seizure doesn't wipe all footage.
5. **File a timestamped report** with CPJ (Committee to Protect Journalists) and RSF immediately after any incident.

## Common Issues, Alternatives & What You Should Know

- **"The metadata was stripped."** Social platforms (X, WhatsApp, Telegram) strip EXIF on upload. Always request the **original file** from the source, not the reposted version.
- **"AI-generated footage."** Run suspicious clips through **Hive AI Detector** or **Deepware Scanner**. Look for warped hands, inconsistent shadows, and unnatural motion blur.
- **"I can't geolocate it."** Fall back to **open-source corroboration**: match the clip against at least two independent eyewitness accounts or agency wire reports (AP, Reuters, AFP).
- **Legal note:** Under the Geneva Conventions, journalists are civilians and protected persons; deliberate targeting is a war crime. Documenting attacks — not just reporting them — creates an evidentiary record for future accountability.

## Frequently Asked Questions (FAQ)

### How do I verify if a West Bank attack video is real?
Extract metadata with ExifTool, run keyframes through InVID-WeVerify and Yandex reverse search, then geolocate landmarks against Google Earth and check shadow direction with SunCalc. Require at least two independent corroborating sources before sharing.

### What tools do journalists use to safely document conflict zones?
InVID-WeVerify for verification, Proton Drive or Tresorit for encrypted backup, SunCalc for chronolocation, and CPJ/RSF reporting channels for incident documentation. Field journalists also use live-location sharing and short-clip recording to protect footage.

### Is it legal to film Israeli settler attacks in the West Bank?
Yes — filming in public spaces and documenting human rights incidents is protected activity. Journalists are protected civilians under international humanitarian law. Always prioritize personal safety and report incidents to press-freedom organizations afterward.

## Final Verdict

Don't amplify raw conflict footage without verification — that's how misinformation spreads and how real victims get lost in the noise. Build a fixed workflow: **ExifTool → InVID → Yandex → Google Earth → SunCalc → Archive with hash.** Bookmark this checklist, install the free tools today, and treat every unverified clip as guilty until proven authentic. Verification isn't skepticism for its own sake — it's the difference between documenting an attack and accidentally erasing it.