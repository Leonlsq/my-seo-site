---
title: "Windows Server 2022 End of Support: Upgrade Path & Costs"
description: "Windows Server 2022 hit end of mainstream support on Oct 13, 2026. Here's your upgrade path to Server 2025, extended support costs, and ESU options."
pubDate: 2026-10-15
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Windows Server 2022 Just Lost Mainstream Support — Here's Exactly What to Do Next

On **October 13, 2026**, Windows Server 2022 officially exited mainstream support. That means no more free security updates, no more non-security bug fixes, and no more feature requests honored by Microsoft — unless you're on the paid Extended Security Updates (ESU) track. The OS remains in **extended support until October 14, 2031**, but "extended support" only covers security patches, and only if you pay for ESU after the first year. If you're running Server 2022 in production and haven't planned a migration, you now have a shrinking window to move to **Windows Server 2025** or negotiate ESU pricing. This guide breaks down your real options, costs, and a step-by-step upgrade path.

## What "End of Mainstream Support" Actually Changes

Microsoft's lifecycle has two phases. Here's the practical difference for anyone running Server 2022 today:

| Phase | Free Security Updates | Non-Security Fixes | Feature Requests | Support Cost |
|---|---|---|---|---|---|
| Mainstream (until Oct 13, 2026) | ✅ Yes | ✅ Yes | ✅ Yes | Included |
| Extended (Oct 2026 – Oct 2031) | ⚠️ ESU only | ❌ No | ❌ No | Paid after Year 1 |
| ESU Year 1 (Oct 2026 – Oct 2027) | ✅ Free | ❌ No | ❌ No | $0 |
| ESU Year 2 (Oct 2027 – Oct 2028) | ✅ Paid | ❌ No | ❌ No | ~75% of license |
| ESU Year 3 (Oct 2028 – Oct 2029) | ✅ Paid | ❌ No | ❌ No | ~100% of license |

**Key takeaway:** You get one free year of security patches. After October 2027, ESU pricing roughly doubles each year, making migration cheaper than staying put.

## Step-by-Step Upgrade Path to Windows Server 2025

Windows Server 2025 is the direct in-place upgrade target and supports the same hardware generation in most cases. Here's the migration sequence that works for most environments:

1. **Inventory your workloads.** Run `Get-WindowsFeature` and `Get-Service` to list roles. Flag anything still on .NET Framework 3.5, legacy IIS 6.0 compatibility mode, or SMBv1 — these break on Server 2025.
2. **Check hardware compatibility.** Server 2025 requires **TPM 2.0 and UEFI Secure Boot** for the recommended configuration. Older BIOS-only hosts need firmware updates or replacement.
3. **Validate licensing.** Server 2025 uses the same core-based licensing model as 2022. A 16-core minimum per physical processor applies. If you're on Datacenter, in-place upgrade preserves your virtualization rights.
4. **Run the upgrade advisor.** `Windows Server Upgrade Assistant` (downloadable from Microsoft) flags incompatible roles before you commit.
5. **Test in a staging VM first.** Clone your production VM, upgrade the clone, and run your app smoke tests for 72 hours.
6. **Schedule the cutover.** In-place upgrade typically takes 45–90 minutes per server. Rolling upgrades across a cluster avoid downtime.
7. **Re-activate and re-apply GPOs.** Server 2025 resets some local security policies; re-import your baseline.

**Pro tip:** If you're on Azure, use **Azure Migrate** to lift-and-shift instead. It handles the OS upgrade and licensing in one pass and avoids the TPM/Secure Boot headache entirely.

## Common Issues, Alternatives, and What You Should Know

**Issue 1: ESU enrollment is not automatic.** You must manually enroll through the Azure Arc portal or your volume licensing agreement. Servers not enrolled stop receiving patches on **October 13, 2027**, not 2031.

**Issue 2: Third-party app compatibility.** Legacy line-of-business apps built for .NET 4.6 or earlier may fail on Server 2025. Check vendor support matrices before upgrading.

**Issue 3: Hyper-V cluster upgrades.** Mixed-version clusters (2022 + 2025 nodes) are supported for live migration but not for cluster-wide features like Storage Replica. Plan a full cluster rebuild if you rely on those.

**Alternatives if you can't migrate:**
- **Azure Arc + ESU** — cheapest path for small footprints (under 10 servers).
- **Linux migration** — viable for web, DNS, and file servers; not for Active Directory or Exchange.
- **Stay on 2022 with ESU** — only rational if your app vendor has no 2025 certification and no roadmap.

## Frequently Asked Questions (FAQ)

### How long is Windows Server 2022 supported after mainstream ends?
Windows Server 2022 remains in extended support until **October 14, 2031**. However, free security updates end on **October 13, 2027**. After that date, you must pay for Extended Security Updates (ESU) to keep receiving patches.

### Is Windows Server 2022 ESU free?
The **first year of ESU (Oct 2026 – Oct 2027) is free** for on-premises and Azure customers. From Year 2 onward, pricing scales to roughly 75% of the license cost, then 100% in Year 3, doubling annually.

### Can I upgrade Windows Server 2022 to 2025 in-place?
Yes. Microsoft supports an in-place upgrade from Server 2022 to Server 2025 for the same edition (Standard → Standard, Datacenter → Datacenter). You cannot upgrade Standard to Datacenter in-place; that requires a clean install and license change.

### What happens if I don't upgrade or buy ESU?
Your server keeps running, but you stop receiving security patches after October 2027. This creates compliance failures for PCI-DSS, HIPAA, and SOC 2 audits, and exposes you to unpatched CVEs.

## Final Verdict

**Migrate to Windows Server 2025 before October 2027.** The free first-year ESU window is a grace period, not a destination. For most organizations, the cost of ESU Year 2 plus the compliance risk outweighs the migration effort — and Server 2025's in-place upgrade path is mature enough that a staged rollout is low-risk. If you have fewer than 10 servers and no in-house Windows expertise, **Azure Arc + ESU** is the pragmatic short-term fix. Everyone else: start your inventory this quarter, because a 12-month migration runway disappears faster than you think.