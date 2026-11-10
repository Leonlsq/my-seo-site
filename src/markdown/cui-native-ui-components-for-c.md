---
title: "CUI for C: Build Native GUIs Without a Framework (2026 Guide)"
description: "Learn how to set up CUI, the native UI component library for C. Step-by-step install, code examples, and honest limitations vs GTK and Qt."
pubDate: 2026-11-10
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is CUI and Should You Use It for Native C GUIs?

CUI is a lightweight library that gives C developers native UI components — buttons, inputs, lists, and windows — without pulling in GTK, Qt, or a webview runtime. It landed on Hacker News with 172 points and 93 comments, and the reaction split cleanly: C programmers loved the idea of GUI code that compiles like a plain C program, while skeptics asked about platform support and maturity. The short answer: CUI is genuinely useful for small desktop tools, internal utilities, and embedded-ish interfaces where a 200 MB framework dependency is absurd. It is not a replacement for Qt on a complex commercial app. This guide walks you through setup, a working example, and the tradeoffs you need to know before committing.

## Step-by-Step: Setting Up CUI and Building Your First Window

CUI is distributed as a header/source library from its GitHub Pages site (`yappologistic.github.io/CUI`). The workflow is intentionally close to raw C: clone, include, link, compile.

### Step 1 — Get the source

```bash
git clone https://github.com/yappologistic/CUI.git
cd CUI
```

### Step 2 — Check your toolchain

| Requirement | Minimum | Notes |
|---|---|---|
| C compiler | C11-compliant (GCC 9+, Clang 10+, MSVC 2019+) | CUI relies on modern struct and atomics support |
| Platform SDK | Win32 / X11 dev headers | Native backends, so dev packages must be installed |
| Build system | Make or CMake | CMake is the safer bet for cross-platform builds |
| RAM | ~50 MB at runtime | Negligible compared to Qt's footprint |

On Debian/Ubuntu, install the X11 development headers first — the most common build failure is a missing `X11/Xlib.h`:

```bash
sudo apt install build-essential libx11-dev libxft-dev
```

### Step 3 — Write a minimal window

```c
#include "cui.h"

int main(void) {
    cui_window *win = cui_window_create("Hello CUI", 480, 320);
    cui_button *btn = cui_button_create("Click me");
    cui_button_on_click(btn, /* callback */ my_handler, NULL);
    cui_window_add(win, btn);
    return cui_window_run(win);
}
```

### Step 4 — Compile and link

```bash
gcc main.c -I./CUI/include -L./CUI/build -lcui -lX11 -o myapp
./myapp
```

### Step 5 — Verify the event loop

CUI runs a blocking event loop via `cui_window_run()`. If your app needs background work, spawn a thread and marshal UI updates back through `cui_post_task()` — never touch widgets from a worker thread directly.

## Common Issues, Limitations, and Alternatives

**Build errors on Linux.** Nine times out of ten it's a missing `-lX11` or missing dev headers. If you see undefined references to `XOpenDisplay`, your link order is wrong — put `-lcui` before the system libs.

**Threading crashes.** CUI widgets are not thread-safe. Any UI mutation from a non-main thread produces intermittent segfaults that are painful to debug. Use the task-posting API.

**High-DPI blurriness.** Native backends inherit OS scaling, but CUI's layout math is pixel-based, so on 150%+ displays you may need to scale your dimensions manually.

### How CUI compares to the alternatives

| Library | Language | Binary size | Learning curve | Best for |
|---|---|---|---|---|
| **CUI** | C | ~100 KB | Low for C devs | Small tools, utilities |
| **GTK4** | C (GObject) | 20–40 MB | Steep | Full Linux desktop apps |
| **Qt** | C++ | 30–80 MB | Steep | Commercial cross-platform apps |
| **Dear ImGui** | C++ | ~1 MB | Low | Debug overlays, tools |
| **raylib** | C | ~2 MB | Low | Games, simple UIs |

The honest tradeoff: CUI gives you the smallest dependency footprint and the most "C-native" feel, but it has a fraction of GTK's widget catalog and community. If you need accessibility APIs, complex data grids, or long-term enterprise support, GTK or Qt remain the responsible choice. If you're building a 3-screen internal tool and refuse to learn GObject, CUI is a legitimate win.

## Frequently Asked Questions (FAQ)

### Is CUI production-ready for commercial software?
Not yet. It's young, the API may change, and the community is small. It's excellent for prototypes, internal tools, and hobby projects. For commercial releases, budget time for pinning a version and potentially patching platform bugs yourself.

### Does CUI work on Windows and macOS?
The project targets Win32 and X11 backends. Windows support is functional; macOS support is the weakest link and often requires community patches. Check the repo's issue tracker before starting a Mac-targeted project.

### Can I use CUI with C++ or other languages?
Yes — it exposes a C ABI, so C++ can include it directly, and bindings for other languages are feasible. Keep in mind you'll lose some of the "pure C" simplicity when mixing paradigms.

### How do I handle high-DPI screens in CUI?
Multiply your widget dimensions and font sizes by the OS scale factor at startup, or set an explicit DPI override in the window config. There is no automatic vector scaling like Qt's.

## Final Verdict

Use CUI if you're a C developer who wants a real native window with a handful of controls and zero framework baggage — it's the fastest path from `main()` to a clickable button. Skip it if your app needs accessibility compliance, a rich widget set, or guaranteed macOS support. The pragmatic move in 2026: prototype in CUI, and only migrate to GTK if the project outgrows it.