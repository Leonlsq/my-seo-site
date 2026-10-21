---
title: "OpenBSD 8.0 Upgrade Guide: Arc, ARM64 Hibernation & 64-vCPU"
description: "Step-by-step OpenBSD 8.0 upgrade guide covering Intel Arc GPU setup, ARM64 hibernation, and 64-vCPU guest tuning for bhyve and QEMU."
pubDate: 2026-10-21
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## OpenBSD 8.0: How to Upgrade Safely and Unlock Arc, Hibernation, and 64-vCPU Guests

OpenBSD 8.0 just landed, and the headline features — Intel Arc GPU support, ARM64 hibernation, and 64-vCPU guests — are the exact reasons most people will attempt an upgrade this cycle. But "record still intact" doesn't mean "upgrade is automatic." This guide walks you through a **safe, reversible upgrade path**, then shows you how to actually *configure* the three marquee features so they work on day one instead of silently failing. If you've ever run `sysupgrade` and rebooted into a black screen or a machine that won't resume from suspend, this is the playbook you want.

Before touching anything, confirm your current release and take a snapshot:

```sh
uname -a
doas syspatch          # apply pending patches first
```

If you're on a VPS or bare metal with no console access, **do not** skip the snapshot step. OpenBSD's upgrade is reliable, but a failed `fw_update` for firmware (especially for Arc) can leave you without a display.

## Step-by-Step: Upgrade to OpenBSD 8.0 and Enable the New Features

### Step 1 — Back up and snapshot

- **Bare metal:** boot a live image and `dd` your root partition, or use ZFS snapshots if you run root-on-ZFS.
- **VPS:** create a provider snapshot. This is your only rollback if `fw_update` bricks the NIC firmware.

### Step 2 — Run the official upgrade

```sh
doas sysupgrade
```

`sysupgrade` fetches the 8.0 sets, unpacks them, and reboots. Watch the output for `fw_update` warnings — these matter for Arc.

### Step 3 — Re-apply patches and firmware

```sh
doas syspatch
doas fw_update -v
```

The `-v` flag is important on 8.0: it prints which firmware packages were skipped, so you can catch a missing Arc or Wi-Fi blob before you chase a phantom driver bug.

### Step 4 — Intel Arc GPU setup

Arc support in 8.0 relies on the updated DRM stack plus firmware. Verify detection with:

```sh
dmesg | grep -i arc
pcidump -v | grep -i vga
```

If the card shows up but you get no accelerated output, confirm the firmware package installed (`inteldrm-firmware`) and that you're on a recent `xenodm`/`Xorg`. Arc's kernel driver is solid, but userspace acceleration on OpenBSD is still conservative — expect **2D and basic 3D**, not gaming-class performance.

### Step 5 — ARM64 hibernation

Hibernation on ARM64 in 8.0 requires a swap partition at least as large as RAM. Check:

```sh
swapctl -l
```

Then test with:

```sh
doas zzz -Z
```

If resume fails, the usual culprits are (1) swap too small, (2) a device driver that doesn't support quiesce, or (3) firmware that resets the controller on resume. Check `dmesg` after the failed resume attempt.

### Step 6 — 64-vCPU guests (bhyve / QEMU)

On capable hosts, 8.0 raises the guest vCPU ceiling to 64. Allocate carefully:

| Setting | Recommendation | Notes |
|---|---|---|
| `-c` (bhyve vCPUs) | ≤ physical cores | Oversubscription hurts more than helps |
| Guest RAM | Match workload | Hibernation needs RAM = swap |
| `vmm` max | Check `sysctl kern.vmm` | Confirm host limit first |

```sh
vmctl start -c 64 -m 32G myguest
```

Start with 16 vCPUs and scale up while watching host load — 64 vCPUs on a 16-core box will thrash.

## Common Issues, Alternatives, and What You Should Know

- **Arc black screen after upgrade:** usually a missing firmware blob. Re-run `fw_update -v` and reboot.
- **Hibernation resumes to a frozen console:** disable the offending driver or increase swap.
- **64-vCPU guest won't boot:** confirm your host CPU exposes the needed features and that `vmm` is enabled at boot.
- **Alternatives:** if Arc acceleration is critical, FreeBSD's DRM port is further along; if you need maximum guest density, Linux KVM still leads. OpenBSD wins on **security posture and simplicity**, not raw virtualization throughput.

## Frequently Asked Questions (FAQ)

### Is OpenBSD 8.0 worth upgrading to right now?
Yes for security patches and ARM64 hibernation. If you depend on Arc 3D acceleration for daily work, test on a spare machine first — userspace support is functional but not mature.

### Does OpenBSD 8.0 support Intel Arc out of the box?
The kernel driver and firmware are included, but you must run `fw_update` and verify with `dmesg`. Acceleration is limited to 2D and basic 3D.

### How much swap do I need for ARM64 hibernation?
At least as much as your installed RAM. Use `swapctl -l` to confirm before testing with `zzz -Z`.

### Can I run 64-vCPU guests on any OpenBSD 8.0 host?
No. You need sufficient physical cores and a host that exposes the required CPU features. Start lower and scale up.

## Final Verdict

Upgrade to OpenBSD 8.0 — the security record and the ARM64 hibernation alone justify it. Treat Intel Arc as **"works, but don't expect a gaming rig,"** and size your 64-vCPU guests to your actual hardware. Snapshot first, run `fw_update -v`, and test hibernation before you rely on it. Do that, and 8.0 is a clean, boring, secure win — exactly what OpenBSD users want.