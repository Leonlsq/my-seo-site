---
title: "Sanstun Rust WireGuard: Setup Guide & Is It Worth It?"
description: "Learn how to build a parallel-friendly WireGuard tunnel in Rust with Sanstun. Step-by-step setup, sans-IO explained, and Firezone integration tips."
pubDate: 2026-10-31
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Sanstun Explained: Why Rust Developers Are Switching to Sans-IO WireGuard

If you clicked through from the Firezone blog post or the Hacker News thread (152 points, 40 comments) and thought, "Okay, but how do I actually *use* this?" — this guide is for you. Sanstun is a **sans-IO, parallel-friendly WireGuard implementation written in Rust**. The "sans-IO" part is the headline: it means the library handles all the cryptography, handshake state machines, and packet parsing, but leaves the actual socket I/O to *you*. That decoupling is what makes it parallel-friendly — you can run thousands of tunnels in a single process without blocking threads on syscalls.

The direct takeaway: Sanstun is **not a drop-in replacement for `wg-quick`**. It's a library for developers building VPN clients, mesh networks, or Firezone-style gateways. If you're an end user looking for a WireGuard GUI, skip to the alternatives section. If you're a Rust engineer who wants deterministic, testable, embeddable WireGuard — read on.

## Step-by-Step Guide: Building Your First Sanstun Tunnel

Sanstun assumes you bring your own event loop (Tokio, smol, or even a bare `epoll` loop). Here's the practical path from `cargo add` to a working handshake.

### 1. Add the dependency and check your toolchain
```toml
[dependencies]
sanstun = "0.1"   # verify the latest version on crates.io before pinning
tokio = { version = "1", features = ["full"] }
```
Sanstun targets recent stable Rust. Confirm with `rustc --version` — anything from the last 12 months is safe.

### 2. Generate or import your keys
Sanstun expects raw Curve25519 keys. Generate a keypair once and store the private half securely:
```rust
use sanstun::crypto::KeyPair;
let keys = KeyPair::generate();
println!("public: {:?}", keys.public_key());
```

### 3. Configure the tunnel (the sans-IO core)
Unlike `wg-quick`, you configure Sanstun programmatically. The essential parameters are:

| Parameter | What it does | Typical value |
|---|---|---|
| `private_key` | Your identity | 32-byte Curve25519 |
| `peer_public_key` | Remote identity | 32-byte Curve25519 |
| `preshared_key` | Optional PSK layer | 32 bytes or `None` |
| `persistent_keepalive` | NAT hole-punching | `25` seconds |
| `allowed_ips` | Routing filter | `0.0.0.0/0` or split |

### 4. Drive the state machine yourself
This is the key difference from traditional WireGuard. You feed inbound packets into Sanstun and get outbound packets back — no sockets touched:
```rust
// Pseudocode of the sans-IO loop
let mut tunnel = Tunnel::new(config);
loop {
    let (inbound, src) = udp_socket.recv_from(&mut buf).await?;
    if let Some(outbound) = tunnel.decapsulate(inbound)? {
        handle_plaintext(outbound);
    }
    if let Some(reply) = tunnel.tick(Instant::now())? {
        udp_socket.send_to(&reply, peer_addr).await?;
    }
}
```
Because `tick()` is time-driven, you can **test the entire handshake in a unit test** with a fake clock — no network required. That's the real superpower.

### 5. Parallelize across tunnels
Spawn one lightweight task per tunnel (or batch them in a `FuturesUnordered`). Since Sanstun never blocks on I/O, a single Tokio worker thread can multiplex hundreds of tunnels. For Firezone-style deployments, this is how you scale from 100 to 10,000 peers without thread explosion.

## Common Issues, Alternatives, and What You Should Know

**Common gotchas reported in the HN thread and issue trackers:**
- **No `wg-quick` config parser.** You must translate `.conf` files yourself. Community crates like `wireguard-config` help, but expect manual mapping of `AllowedIPs`.
- **You own the MTU.** Sans-IO means no automatic MTU discovery — set it explicitly (typically 1420 for IPv4 UDP) or you'll see silent fragmentation.
- **Timer discipline matters.** If you forget to call `tick()`, rekeying and keepalives stall. Wire it into your event loop's timer wheel.
- **Not a userspace TUN driver.** Sanstun gives you plaintext IP packets; you still need `tun`/`tun-tap` crates to route them into the kernel.

**How it compares to the alternatives:**

| Implementation | Language | Sans-IO? | Best for |
|---|---|---|---|
| WireGuard-go | Go | No | Reference userspace tool |
| BoringTun | Rust | Partial | Cloudflare's userspace client |
| **Sanstun** | Rust | **Yes** | Embedding, testing, mass parallelism |
| `wg-quick` | Shell/kernel | N/A | End users, simple hosts |

**Cost analysis:** Sanstun is MIT/Apache dual-licensed and free. The real "cost" is engineering time — budget a few days to integrate the event loop if you're new to sans-IO patterns.

## Frequently Asked Questions (FAQ)

### What does "sans-IO" actually mean in Sanstun?
It means the library contains zero socket, file, or timer syscalls. You hand it bytes and timestamps; it hands back bytes and state transitions. This makes it deterministic, portable (WASM-friendly), and trivially testable.

### Is Sanstun a replacement for `wg-quick` or the WireGuard kernel module?
No. Sanstun is a library for developers. End users who just want a VPN should keep using `wg-quick`, the kernel module, or a GUI client. Sanstun targets people *building* those tools.

### Can Sanstun run in WebAssembly or embedded environments?
Yes — that's a core benefit of sans-IO. Since it never touches the OS directly, you can compile it to WASM or run it on constrained targets, provided you supply your own I/O and clock.

### Does Sanstun support the full WireGuard protocol including PSK and roaming?
It implements the standard Noise-based handshake, optional preshared keys, and rekeying. Roaming (peer address changes) is handled by *your* I/O layer since Sanstun doesn't track sockets — you update the peer address you pass in.

## Final Verdict

**Sanstun is worth adopting if** you're a Rust developer building a VPN client, mesh network, or Firezone-style gateway and you value testability and massive parallelism over turnkey convenience. The sans-IO design pays off the moment you need to unit-test a handshake or run 10,000 tunnels on a handful of threads.

**Skip it if** you want a working VPN in five minutes, need automatic MTU/config parsing, or aren't comfortable owning the event loop. In that case, `wg-quick` or BoringTun will serve you better today.

For teams already in the Firezone ecosystem or writing Rust networking code, Sanstun is the most ergonomic parallel-friendly WireGuard core available right now — just budget the integration time before you commit.