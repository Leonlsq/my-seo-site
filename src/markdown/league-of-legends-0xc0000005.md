---
title: "How to Fix 0xC0000005 Error in League of Legends"
description: "Encountering the 0xC0000005 error in League of Legends? Read our complete step-by-step troubleshooting guide to fix it quickly."
tags: ["League of Legends", "Troubleshooting"]
---

## Why does the 0xC0000005 happen?

The **0xC0000005 error** is a Windows access violation error that commonly appears when League of Legends crashes right as the loading screen reaches **100%**. In most cases, the game client is attempting to read or write to a memory address it doesn't have permission to access, causing an immediate crash to desktop.

Based on reports from the official forums, there are two leading culprits. First, **memory access conflicts** can occur due to corrupted game files, outdated drivers, or unstable RAM overclocking profiles. Second, **antivirus software** may falsely flag a League of Legends process (such as `LeagueClient.exe` or the Vanguard anti-cheat module) and block its memory access mid-load. Identifying which cause applies to your system is the key to a permanent fix.

## How to fix 0xC0000005 (Step-by-Step)

1. **Add League of Legends to your antivirus exceptions list.** Open your security software (Windows Defender, Norton, Avast, etc.), navigate to the **Exclusions** or **Allow List** settings, and add the entire Riot Games installation folder (typically `C:\Riot Games`). Also whitelist `LeagueClient.exe`, `League of Legends.exe`, and `vgc.exe`.

2. **Repair your game files.** Open the **Riot Client**, click your profile icon, select **Settings**, and choose **Repair**. This scans for corrupted or missing files that may be triggering the memory access violation, and replaces them automatically.

3. **Update your graphics drivers.** Visit the NVIDIA, AMD, or Intel website and install the latest driver for your GPU. Outdated drivers are a frequent source of access violations during the loading phase.

4. **Disable conflicting overlays and run as administrator.** Close Discord, MSI Afterburner, and other overlay tools. Then right-click the **League of Legends** shortcut, select **Properties > Compatibility**, and check **Run this program as an administrator**.

## Summary

The 0xC0000005 error is frustrating, but it's almost always fixable. Start by whitelisting League of Legends in your antivirus, then repair your game files and update your drivers. In the vast majority of cases, these steps resolve the crash at 100% loading. If the issue persists, consider testing your RAM with Windows Memory Diagnostic or submitting a ticket to Riot Support with your crash logs.