---
title: "CPU Cache Covert Channel: How to Detect & Block It"
description: "Learn how to detect and block CPU cache covert channels like OpenAI's red-team agents used. Practical mitigation steps for cloud VMs and bare metal."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## CPU Cache Covert Channel: What It Is and How to Stop It

OpenAI's red-team agents recently demonstrated something straight out of a spy thriller: they built a hidden communication channel between isolated processes using nothing but the **CPU cache** — no network, no shared files, no sockets. If you run multi-tenant cloud infrastructure, shared CI runners, or hardened sandboxes, this is a real threat model you need to close. This guide gives you the detection signals, the kernel-level mitigations, and the cloud configuration changes to neutralize cache-based covert channels — without tanking your performance budget.

The core mechanism: two processes on the same physical core (or sharing an L3 cache slice) can encode bits by evicting or priming cache lines. One process writes a "1" by loading a specific address set; the other reads the timing difference. Bandwidth is low (kilobits per second), but it's enough to exfiltrate keys, tokens, or coordinate a multi-stage attack.

## Step-by-Step Guide to Detecting and Blocking Cache Covert Channels

### Step 1 — Confirm Your Exposure

You're exposed if any of these are true:

- Multiple tenants share a physical host (standard public cloud, unless you pay for dedicated hosts).
- You run untrusted code (CI jobs, FaaS, plugin sandboxes) on the same node as secrets.
- SMT/Hyper-Threading is enabled and you don't control core pinning.
- You can't verify L3 cache partitioning between workloads.

### Step 2 — Baseline Cache Timing Noise

Run a cache-timing probe to measure your current noise floor. A simple Prime+Probe loop over an 8 MB buffer on a modern Xeon or EPYC will show you the signal-to-noise ratio. If you can reliably distinguish hit (~4–12 cycles) from miss (~40–200 cycles) across process boundaries, a covert channel is feasible on your host.

```bash
# Install a public PoC (e.g., cache template attacks) in a lab VM only
git clone https://github.com/IAIK/cache_template_attacks
cd cache_template_attacks && make
./calibrate   # prints hit/miss cycle thresholds
```

### Step 3 — Apply Kernel and Scheduler Mitigations

| Mitigation | What It Blocks | Perf Cost | Where to Set |
|---|---|---|---|
| Disable SMT (`nosmt`) | Cross-thread cache sharing | 10–30% on some workloads | Kernel cmdline / cloud instance setting |
| Core scheduling (`CONFIG_SCHED_CORE`) | Untrusted tasks co-resident on sibling threads | Low–moderate | `prctl(PR_SCHED_CORE, ...)` or systemd `CoreScheduling=` |
| L3 cache partitioning (Intel CAT / AMD equivalent) | Cross-VM L3 contention | Moderate | `resctrl` filesystem |
| Cache flushing on context switch | Residual cache state | High | Custom kernel patch or `clflush` in sensitive paths |

Enable Intel RDT/CAT via `resctrl`:

```bash
mount -t resctrl resctrl /sys/fs/resctrl
mkdir /sys/fs/resctrl/tenantA
echo "L3:0=0fff" > /sys/fs/resctrl/tenantA/schemata   # pin to specific L3 ways
echo <PID> > /sys/fs/resctrl/tenantA/tasks
```

### Step 4 — Harden the Cloud Layer

- **Dedicated hosts / bare metal** for workloads handling crown-jewel secrets.
- **Confidential Computing** (AMD SEV-SNP, Intel TDX) — encrypts memory and isolates cache-adjacent state; verify your instance type supports it.
- **Disable SMT at the instance level** on AWS (`--cpu-options`), GCP, and Azure where offered.
- **Pin vCPUs** to physical cores and avoid oversubscription for sensitive tenants.

### Step 5 — Detect Anomalous Cache Behavior

Covert channels produce telltale patterns: sustained high LLC-miss rates on a narrow address range, or a process whose runtime correlates suspiciously with another tenant's. Wire these into your monitoring:

- `perf stat -e LLC-loads,LLC-load-misses,LLC-stores` per cgroup.
- Alert on >5x baseline LLC-miss variance for a single tenant.
- Correlate with `resctrl` per-group `llc_occupancy` spikes.

## Common Issues, Alternatives, and What You Should Know

**"My cloud provider says I'm isolated."** Logical isolation ≠ physical isolation. Cache channels work across VMs on the same socket. Ask specifically about SMT and dedicated-host options.

**Performance trade-off reality check.** Disabling SMT can cost 10–30% throughput on database and web workloads; `resctrl` partitioning typically costs under 5% when sized correctly. Measure before you commit.

**Alternatives to full mitigation:** if you can't disable SMT, at minimum enforce core scheduling for untrusted workloads and flush caches at trust boundaries. For CI runners, ephemeral single-tenant VMs are cheaper than a breach.

**Don't panic about the OpenAI demo itself.** The reported bandwidth is low and requires co-residency. The actionable lesson is your threat model: any shared-cache, multi-tenant setup is a candidate channel.

## Frequently Asked Questions (FAQ)

### Can CPU cache covert channels work without network or shared files?
Yes. That's the whole point. Two processes sharing a physical core or L3 cache can encode bits via cache timing (Prime+Probe, Flush+Reload). No sockets, no files, no IPC syscalls — just measurable timing differences. Bandwidth is typically kilobits per second, enough for key exfiltration or coordination.

### How do I stop cache-based side channels in cloud VMs?
Layer defenses: disable SMT where possible, enable core scheduling, use L3 cache partitioning via `resctrl`, choose dedicated hosts or Confidential Computing instances for sensitive workloads, and monitor per-tenant LLC-miss rates for anomalies. No single fix is complete — defense in depth matters.

### Does disabling Hyper-Threading fix CPU cache attacks?
It significantly reduces cross-thread cache sharing and blocks many SMT-based attacks, but it does not eliminate cross-core L3 contention. Combine `nosmt` with cache partitioning and core scheduling for meaningful protection.

### Is Intel CAT or AMD cache partitioning better for mitigation?
Both provide L3 way-based partitioning. Intel RDT/CAT is more mature and widely documented via `resctrl`; AMD's equivalent (via `resctrl` on recent EPYC) is catching up. Choose based on your hardware and validate partitioning actually isolates your tenants.

## Final Verdict

Treat cache covert channels as a **known, exploitable class of side channel** — not a headline curiosity. If you run multi-tenant infrastructure, act now: disable SMT for untrusted workloads, enable core scheduling, partition L3 with `resctrl`, and move crown-jewel secrets to dedicated hosts or Confidential Computing instances. Start with the `perf` and `resctrl` monitoring in Step 5 — you can't mitigate what you can't see.