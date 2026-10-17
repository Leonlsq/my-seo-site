---
title: "Ledger Wallet Supply Chain Hack: How to Check If Yours Is Compromised"
description: "How to detect implanted eSIM/LTE chips in store-bought Ledger wallets, verify firmware, and secure your seed phrase after the $71M supply chain attack."
pubDate: 2026-10-15
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Check If Your Store-Bought Ledger Wallet Has a Hidden Chip

If you bought a Ledger hardware wallet from a third-party retailer in Southeast Asia or Europe, you need to verify it **before** you enter your recovery phrase again. An ongoing supply chain attack has compromised store-bought units with implanted eSIM and LTE modules — tiny cellular chips soldered onto the board that silently exfiltrate your 24-word seed phrase the moment you type it in. Losses have already crossed **$71 million and counting**, and the attack is still active.

The good news: this is detectable. The bad news: a factory reset does **not** remove hardware. Below is a concrete, step-by-step verification and remediation guide you can run in under 20 minutes.

## Step-by-Step: Verify Your Ledger Is Genuine

### Step 1 — Physical teardown check (the only 100% reliable method)
1. Power off and disconnect the device.
2. Remove the four Torx T5 screws on the back plate (Ledger Nano S Plus / Nano X use T5; the Stax uses T6).
3. Inspect the PCB for **any component not on Ledger's official board schematic** — specifically:
   - A small rectangular module roughly 15×12 mm (typical LTE Cat-M1/NB-IoT footprint).
   - A micro-SIM or embedded eSIM pad cluster near the USB-C controller.
   - Any antenna trace running along the plastic edge that doesn't terminate at the NFC coil.
4. Photograph the board and compare against Ledger's published teardown images on their support site.

### Step 2 — Bluetooth/NFC anomaly scan
Legitimate Ledger Nano X units broadcast a Bluetooth LE signal **only when unlocked and in pairing mode**. Compromised units with LTE modules often leak RF even when powered off.
- Use a phone app like **nRF Connect** or **Wireshark with an RTL-SDR dongle**.
- Scan for 700–900 MHz (LTE Band 8/20, common in EU/SEA) and 2.4 GHz BLE.
- A powered-off device emitting **any** signal is a confirmed compromise.

### Step 3 — Firmware attestation via Ledger Live
1. Open Ledger Live → **Settings → General → Firmware version**.
2. Click **Verify genuineness**. This runs a cryptographic attestation against Ledger's secure element.
3. A tampered unit will either fail attestation or report a **mismatched secure element serial**.

| Check | Genuine Ledger | Compromised Unit |
|---|---|---|
| PCB components | Matches schematic | Extra LTE/eSIM module |
| RF when powered off | Silent | Emits 700–900 MHz |
| Firmware attestation | Passes | Fails or serial mismatch |
| Bluetooth MAC | Matches box label | Mismatched or absent |
| Weight | 34.5 g (Nano X) | 36–38 g (chip adds mass) |

### Step 4 — Weight and packaging forensics
A planted eSIM + LTE module adds **1.5–3.5 grams**. Weigh your device on a 0.01 g scale. Also check the tamper seal — resealed boxes often show micro-wrinkling on the holographic sticker.

## If You're Compromised: Immediate Recovery Protocol

**Assume your seed phrase is already stolen if you entered it on a suspect device.** Speed matters — attackers typically sweep funds within 6–48 hours.

1. **Do not connect the device to Ledger Live again.** It may trigger a remote wipe or seed push.
2. On a **clean, air-gapped computer or a brand-new phone**, generate a fresh wallet using a *different* vendor (Trezor, BitBox02, or Coldcard).
3. Move all assets to the new wallet in **small test transactions first**, then the full balance.
4. Revoke all token approvals via **revoke.cash** for any DeFi positions.
5. File a report with your local cybercrime unit and Ledger's official security team at security@ledger.com.

## Common Issues and What You Should Know

- **"I bought from Amazon/Shopee/Lazada official store."** Marketplace "official" storefronts have been cloned. Cross-check the seller against Ledger's authorized reseller list.
- **"My device passed attestation."** Attestation checks firmware, not added hardware. A skilled attacker can leave firmware untouched while tapping the secure element's I/O lines.
- **"I only used it once."** One seed entry is enough. There is no safe "test."
- **Buy direct.** Ordering from ledger.com with tracked shipping eliminates the retail interception vector entirely.

## Frequently Asked Questions (FAQ)

### How do I know if my Ledger was tampered with before I bought it?
Weigh it (a Nano X should be 34.5 g), run firmware attestation in Ledger Live, and scan for RF emissions while powered off. If any check fails, treat the seed as compromised.

### Can a factory reset remove the implanted eSIM chip?
No. A reset only wipes firmware storage. The physical LTE module and its firmware persist and will re-arm on next boot.

### Is my Trezor or BitBox02 affected by this supply chain attack?
The reported implants target Ledger units specifically due to their retail distribution in SEA and EU. Trezor and BitBox02 have not been implicated, but always buy direct and verify the tamper seal regardless of brand.

## Final Verdict

If you bought a Ledger from a third-party retailer in Southeast Asia or Europe in the last 12 months, **stop using it today**. Tear it down, weigh it, scan it — and if anything looks off, migrate your funds to a freshly generated wallet on a device bought directly from the manufacturer. The $71 million in losses came from people who trusted a sealed box. Don't be the next line item.