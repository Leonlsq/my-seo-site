---
title: "OpenShell Setup Guide: Run Safe AI Agent Fleets in 2026"
description: "Step-by-step OpenShell tutorial: install NVIDIA's sandboxed runtime, configure policies, and safely run autonomous AI agent fleets on Linux."
pubDate: 2026-10-23
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## OpenShell Setup: How to Run a Safe, Private AI Agent Fleet (2026 Tutorial)

NVIDIA's **OpenShell** just hit Hacker News (342 points, 181 comments), and the question everyone's asking is simple: *how do I actually run autonomous AI agents without handing them my SSH keys, API tokens, and home directory?* OpenShell is an open-source, sandboxed runtime designed to isolate fleets of AI agents so a rogue `rm -rf` or a prompt-injected agent can't nuke your machine. This guide walks you through installing it, writing your first policy, and running a multi-agent fleet safely—with the exact commands and config files you need. If you've been running agents in bare Docker containers or, worse, directly on your host, this is the upgrade path.

## Step-by-Step: Installing and Configuring OpenShell

OpenShell is built around three ideas: **process isolation**, **capability-scoped permissions**, and **auditable agent sessions**. Here's how to get a working setup on Linux (Ubuntu 22.04+ recommended) in about 15 minutes.

### Step 1: Prerequisites and Install

You'll need a recent kernel with namespace support, plus Go 1.22+ if building from source.

```bash
# Clone the repo
git clone https://github.com/NVIDIA/OpenShell.git
cd OpenShell

# Build the runtime and CLI
make build

# Install the CLI to your path
sudo install -m 755 ./bin/openshell /usr/local/bin/openshell

# Verify
openshell version
```

### Step 2: Initialize a Sandbox Profile

OpenShell uses declarative **profiles** to define what an agent can touch. Create a minimal profile for a read-only research agent:

```yaml
# profiles/researcher.yaml
name: researcher
runtime: sandboxed
filesystem:
  read: ["/workspace/input"]
  write: ["/workspace/output"]
network:
  allow:
    - "api.openai.com:443"
    - "api.anthropic.com:443"
  deny: ["*"]
resources:
  cpu: "2"
  memory: "4Gi"
  timeout: "30m"
```

Load it with:

```bash
openshell profile apply profiles/researcher.yaml
```

### Step 3: Launch Your First Agent

```bash
openshell run --profile researcher --agent ./my_agent_binary
```

The agent now runs inside a namespace-isolated process tree with a seccomp filter, a read-only root filesystem, and network access limited to the two allowlisted endpoints. Anything else—`curl` to an arbitrary host, writes outside `/workspace/output`—fails closed and logs the violation.

### Step 4: Scale to a Fleet

For multiple agents, OpenShell supports a supervisor mode:

```bash
openshell fleet start --profile researcher --replicas 5 \
  --supervisor-port 9090 --log-dir /var/log/openshell
```

Monitor with `openshell fleet status` and inspect violations with `openshell audit tail`.

### Key Capabilities at a Glance

| Feature | What It Does | Why It Matters |
|---|---|---|
| Filesystem scoping | Per-agent read/write allowlists | Blocks data exfiltration and accidental deletion |
| Network egress policy | Domain:port allowlists | Stops prompt-injected agents from calling rogue endpoints |
| Seccomp + namespaces | Syscall filtering, PID/network isolation | Limits blast radius of exploits |
| Session audit logs | Structured JSON per agent action | Forensics and compliance |
| Resource caps | CPU, memory, wall-clock timeout | Prevents runaway loops burning tokens/CPU |

## Common Issues, Pitfalls, and Alternatives

**Issue 1: Agent can't reach a legitimate API.** Your egress policy is too tight. Add the exact `host:port` to the `network.allow` list—wildcards are intentionally unsupported to prevent policy drift.

**Issue 2: Write failures inside `/workspace/output`.** Check that the directory exists and is owned by the sandbox UID. OpenShell does not auto-create output paths.

**Issue 3: Fleet agents can't talk to each other.** Inter-agent communication requires an explicit `peers` block in the profile; the default is deny-all, which trips up multi-agent orchestration frameworks.

**Alternatives worth knowing:** Docker + gVisor gives stronger kernel isolation but requires more plumbing for per-agent policy. Firecracker microVMs are excellent for untrusted code but heavier per-agent overhead. OpenShell's niche is *many lightweight agents with fine-grained, auditable policy*—closer to a "firewall for agents" than a full VM stack.

**Cost angle:** OpenShell itself is free and open-source. Your real costs are LLM API tokens and compute for replicas. A 5-agent fleet at 2 vCPU / 4Gi each needs roughly 10 vCPU and 20Gi RAM—fine on a single mid-range cloud instance.

## Frequently Asked Questions (FAQ)

### What is NVIDIA OpenShell used for?
OpenShell is a sandboxed runtime for running fleets of autonomous AI agents safely. It isolates each agent's filesystem, network, and syscalls so a misbehaving or prompt-injected agent can't access sensitive host data or call unauthorized services.

### Is OpenShell free and open-source?
Yes. OpenShell is published on GitHub under NVIDIA's open-source repository and can be built from source with `make build`. There's no license fee; you only pay for your own compute and LLM API usage.

### Does OpenShell work on macOS or Windows?
The primary target is Linux, since it relies on kernel namespaces and seccomp. macOS and Windows users should run it inside a Linux VM (e.g., Lima or WSL2), which adds a layer of isolation anyway.

### How is OpenShell different from Docker?
Docker isolates processes but shares a kernel and defaults to broad network access. OpenShell defaults to deny-all networking, enforces per-agent filesystem allowlists, and produces structured audit logs designed specifically for agent workloads.

## Final Verdict

If you're running more than one autonomous agent on a machine you care about, **OpenShell is worth adopting now**—especially if you're on Linux and already comfortable with YAML profiles. The deny-by-default networking and audit logs alone justify the 15-minute setup. Start with a single sandboxed agent, tighten your egress rules to exact endpoints, then scale to a fleet once your audit logs look clean. Skip it only if you need full VM-level isolation (use Firecracker) or you're locked to macOS/Windows without a Linux VM. For everyone else building agent fleets in 2026, this is the runtime to standardize on.