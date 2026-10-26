---
title: "PaperPilot Setup Guide: Self-Host a Zero-Cloud PDF Engine"
description: "Step-by-step guide to install PaperPilot, the pure-Rust PDF engine with WASM and MCP. Learn setup, MCP integration, and zero-cloud PDF processing."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## PaperPilot Setup Guide: Run a Zero-Cloud PDF Engine Locally in 15 Minutes

PaperPilot hit the Hacker News front page with 222 points and 79 comments for one reason: it processes PDFs entirely on your machine, written in pure Rust, compiled to WebAssembly, and exposed to AI agents through the Model Context Protocol (MCP). No cloud uploads, no API keys, no data leaving your laptop. If you searched for this tool after seeing the HN thread, you want to know one thing — **how do I actually run it?** This guide walks you through cloning, building, and wiring PaperPilot into an MCP-capable AI client like Claude Desktop, plus the workarounds for the build errors most people hit on the first try.

The core value proposition is simple: PDF parsing, text extraction, and document manipulation traditionally require either paid cloud APIs or heavyweight Python stacks (PyMuPDF, pdfplumber). PaperPilot replaces both with a single Rust binary and a WASM build for browser use. That means your contracts, medical records, and financial statements never touch a third-party server.

## Step-by-Step Guide: Install and Configure PaperPilot

### Prerequisites Checklist

Before you start, confirm your environment meets these requirements:

| Requirement | Minimum Version | Why It Matters |
|---|---|---|
| Rust toolchain | 1.75+ (stable) | PaperPilot uses recent edition features |
| `wasm-pack` | 0.12+ | Required only for the WASM build |
| Node.js | 18+ | Needed for MCP client testing |
| Git | Any recent | To clone the repo |
| OS | Linux, macOS, Windows (WSL2) | Native Windows builds are less tested |

### Step 1: Clone and Build the Core Engine

```bash
git clone https://github.com/KrushnaVardhanReddy/PaperPilot.git
cd PaperPilot
cargo build --release
```

The release build takes 3–6 minutes on a modern laptop. If `cargo build` fails with a linker error on macOS, run `xcode-select --install` first. On Ubuntu, install `build-essential` and `pkg-config`.

### Step 2: Verify the Binary Works

```bash
./target/release/paperpilot --help
```

You should see subcommands for `extract`, `info`, and `serve` (the MCP server mode). If the binary runs but `extract` returns empty text on a scanned PDF, that's expected — PaperPilot does not ship OCR. You'll need a separate OCR pass (see the troubleshooting section below).

### Step 3: Build the WASM Target (Browser Use)

```bash
wasm-pack build --target web
```

This generates a `pkg/` directory you can import into any static site. Serve it with `python3 -m http.server` and open the included demo page to test drag-and-drop PDF parsing in the browser — fully offline after the page loads.

### Step 4: Wire PaperPilot into an MCP Client

This is the step most people get wrong. PaperPilot's MCP server exposes PDF tools to AI agents. Add this block to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, `%APPDATA%\Claude\` on Windows):

```json
{
  "mcpServers": {
    "paperpilot": {
      "command": "/absolute/path/to/PaperPilot/target/release/paperpilot",
      "args": ["serve"]
    }
  }
}
```

Restart the client and confirm the `paperpilot` server shows a green status indicator. Then test with a prompt like: *"Use PaperPilot to extract the tables from report.pdf and summarize the totals."*

### Step 5: Test End-to-End

Drop a 20-page PDF into your working directory and ask your agent to extract metadata and full text. A healthy run completes in under 2 seconds for text-based PDFs. If it hangs, check that you used an **absolute path** in the config — relative paths are the #1 cause of silent MCP failures.

## Common Issues, Alternatives, and What You Should Know

**Issue 1: Empty text extraction on scanned PDFs.** PaperPilot is a parser, not an OCR engine. Workaround: run `ocrmypdf input.pdf output.pdf` first, then feed the output to PaperPilot.

**Issue 2: MCP server not appearing in Claude Desktop.** Verify the binary path with `which paperpilot` or `realpath`, then check the client's log file. On macOS, logs live at `~/Library/Logs/Claude/mcp*.log`.

**Issue 3: WASM build size.** The default build is ~1.2 MB gzipped, which is fine for most sites but heavy for mobile-first pages. Use `wasm-opt -Oz` to shave 20–30%.

### How PaperPilot Compares

| Tool | Cloud Required | Language | MCP Support | OCR Built-In |
|---|---|---|---|---|
| **PaperPilot** | No | Rust/WASM | Yes | No |
| PyMuPDF | No | Python | No | No |
| Adobe PDF Services API | Yes | REST | No | Yes |
| pdfplumber | No | Python | No | No |

The differentiator is MCP support — none of the Python incumbents expose a native MCP server, so PaperPilot is currently the only zero-cloud PDF engine an AI agent can call as a tool without a custom wrapper.

## Frequently Asked Questions (FAQ)

### Is PaperPilot free to use commercially?
Yes. The repository is open source, so you can self-host and integrate it into commercial products without per-document fees — the main cost advantage over Adobe PDF Services, which charges per API call.

### Does PaperPilot work with ChatGPT or only Claude?
The MCP server follows the open Model Context Protocol spec, so any MCP-compatible client can connect. Claude Desktop has the most mature support today; other clients require manual config edits.

### Can PaperPilot handle password-protected PDFs?
Limited support. The parser can detect encryption but decryption of AES-256 PDFs is unreliable in the current build. Decrypt with `qpdf --decrypt` first if you hit errors.

## Final Verdict

PaperPilot is worth installing **if** you handle sensitive PDFs and want AI agents to read them without cloud exposure. The 15-minute setup is a real barrier compared to a one-line pip install, but the payoff — a single Rust binary with WASM and MCP support — is unique in the ecosystem. Skip it if you need OCR or heavy layout reconstruction; pair it with `ocrmypdf` or stick with PyMuPDF for now. For privacy-first AI document workflows, this is the tool to bookmark.