---
title: "Wine on OpenBSD: How to Install and Run Windows Apps in 2026"
description: "Step-by-step guide to installing Wine on OpenBSD, compiling the port, configuring the kernel, and fixing common wineboot and DLL errors."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Wine Ported to OpenBSD: What It Actually Means for You

The OpenBSD ports mailing list recently saw a submission to bring **Wine** — the Windows API translation layer — into the OpenBSD ports tree. If you've been waiting years to run a Windows-only application on OpenBSD, this is the closest you've gotten. But before you `pkg_add wine` and expect Steam to boot, understand what this port is and isn't.

**The short version:** this is an early-stage port, not a polished binary package. It targets Wine's 32-bit/64-bit Windows compatibility layer on OpenBSD's `amd64` platform, and it depends on a handful of OpenBSD-specific quirks — most notably `W^X` enforcement and the lack of a Linux-style `mmap` behavior that Wine historically relies on. You will likely need to compile it yourself, patch the kernel sysctl limits, and accept that DirectX-heavy games are still out of reach. Productivity apps, older Win32 tools, and some installers are the realistic target.

This guide walks you through the install, the configuration, and the fixes for the errors you'll hit first.

## Step-by-Step: Installing Wine on OpenBSD

### 1. Verify your OpenBSD version and architecture
Wine on OpenBSD is `amd64`-only for now. Confirm with:

```
uname -m        # should print amd64
uname -r        # 7.6 or newer recommended
```

### 2. Fetch the port from the mailing list submission
The port lives in the `openbsd-ports` thread. Clone or download the `wine` port skeleton and drop it into `/usr/ports/emulators/wine`:

```
cd /usr/ports/emulators
git clone https://github.com/openbsd/ports.git wine-src   # or use the tarball from the ML post
```

If you're using the mailing list attachment, extract it and place the `Makefile`, `distinfo`, and `pkg/` directory in the correct location.

### 3. Install build dependencies
Wine needs a compiler toolchain plus a few libraries:

```
doas pkg_add gcc%11 gmake bison flex freetype libpng libjpeg-turbo \
  fontconfig gettext-tools pkgconf
```

### 4. Build and install
```
cd /usr/ports/emulators/wine
doas make install
```

Expect a 30–90 minute build on a modern CPU. If `make` fails on `W^X` violations, jump to the troubleshooting section below.

### 5. Initialize the Wine prefix
```
export WINEPREFIX=$HOME/.wine
wineboot --init
```

### 6. Test with a Win32 binary
```
wine notepad.exe
```

If a window appears, your base layer works.

### Key configuration parameters

| Setting | Value | Why it matters |
|---|---|---|
| `kern.maxfiles` | `65536` | Wine opens many file handles |
| `kern.shminfo.shmall` | `2097152` | Shared memory for Wine's heap |
| `WINEARCH` | `win64` (or `win32`) | Must match your target app |
| `WINEDLLOVERRIDES` | `mscoree,mshtml=` | Disables Mono/Gecko prompts |
| `WINEDEBUG` | `-all` | Silences noisy logs |

## Common Issues and Fixes

**`wineboot: cannot allocate memory`** — OpenBSD's default `kern.shminfo` limits are too low. Add to `/etc/sysctl.conf`:
```
kern.shminfo.shmmax=268435456
kern.shminfo.shmall=2097152
```
Then `doas sysctl -p /etc/sysctl.conf`.

**`mmap: Permission denied` / W^X errors** — OpenBSD enforces write-xor-execute. Wine's JIT and some DLL loaders try to map RWX pages. Workarounds: run Wine under `pledge`-friendly mode with `WINEDEBUG=-all` and prefer apps that don't use a JIT. There is no clean fix yet; upstream is working on a `mprotect`-based shim.

**Missing `libwine.so`** — Ensure `/usr/local/lib` is in your `LD_LIBRARY_PATH`:
```
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

**Installer crashes on `mscoree`** — Set `WINEDLLOVERRIDES="mscoree,mshtml="` before running the installer.

**Alternatives worth knowing:** if Wine fails, consider **qemu-user** for a Linux chroot, or run Windows apps in a VM via `vmm(4)`. Neither is as lightweight as Wine, but both sidestep W^X entirely.

## Frequently Asked Questions (FAQ)

### Can I install Wine on OpenBSD with pkg_add yet?
Not from official mirrors. As of the mailing list submission, Wine is a ports-tree candidate only. You must build from source until it's committed and packaged.

### Does Wine on OpenBSD run Steam or DirectX games?
No. DXVK and Vulkan translation aren't functional under OpenBSD's graphics stack, and W^X blocks several shader JIT paths. Expect Win32 productivity apps, not AAA games.

### Is the Wine port stable enough for daily use?
Treat it as experimental. It's suitable for testing and simple Win32 utilities. For production, use a VM.

## Final Verdict

The Wine port to OpenBSD is a genuine milestone for the platform's desktop ambitions, but it's a **developer preview, not a daily driver**. If you're a tinkerer who wants to help test and file bugs, build it today, patch your sysctls, and report W^X failures upstream. If you need to run Windows software reliably right now, a `vmm(4)` VM with a Windows or Linux guest is still the pragmatic choice. Watch the `openbsd-ports` list — once the port lands and the JIT shim matures, this becomes genuinely interesting.