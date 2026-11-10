---
title: "OpenSSH 10.6p2 Alpine Fix: No-PAM Workaround Guide"
description: "Fix the OpenSSH 10.6p2 build failure on Alpine Linux without PAM. Step-by-step configure flags, Dockerfile patch, and verification commands."
pubDate: 2026-11-05
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## OpenSSH 10.6p2 on Alpine: Why Your Build Breaks Without PAM

If you maintain Alpine Linux containers or minimal images, the OpenSSH 10.6p2 release notes likely sent you straight to a broken `./configure` or a failed `apk` upgrade. The short version: OpenSSH 10.6p2 tightened its build-time assumptions around authentication backends, and on Alpine — which ships **musl libc** and **no PAM by default** — the default configuration path can fail or produce a binary that refuses to start with a PAM-related error. The workaround is to explicitly disable PAM at configure time and rebuild against Alpine's `libressl`/`openssl` stack. Below is the exact sequence that gets you a working `sshd` on Alpine 3.20/3.21 in under five minutes.

## Step-by-Step: Building OpenSSH 10.6p2 on Alpine Without PAM

The core fix is passing `--without-pam` (and, on some Alpine versions, `--with-ssl-engine=no`) so the configure script never probes for PAM headers that don't exist. Here's the full reproducible flow.

### 1. Install build dependencies

```bash
apk add --no-cache build-base zlib-dev openssl-dev linux-headers \
  wget tar make
```

Note: do **not** install `linux-pam-dev` — its absence is expected, and the flag below tells configure to skip it cleanly.

### 2. Fetch and extract the source

```bash
wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-10.6p2.tar.gz
tar xzf openssh-10.6p2.tar.gz
cd openssh-10.6p2
```

### 3. Configure with PAM explicitly disabled

```bash
./configure \
  --prefix=/usr \
  --sysconfdir=/etc/ssh \
  --with-privsep-path=/var/empty \
  --without-pam \
  --with-ssl-engine=no \
  --with-md5-passwords=no
```

The two flags that matter most:

| Flag | Why it's required on Alpine |
|------|-----------------------------|
| `--without-pam` | Skips PAM header/library detection; prevents the configure abort and the "PAM is not supported" runtime error. |
| `--with-ssl-engine=no` | Alpine's OpenSSL build often lacks engine support; avoids link errors. |

### 4. Compile and install

```bash
make -j"$(nproc)"
make install
```

### 5. Verify the binary has no PAM linkage

```bash
ldd /usr/sbin/sshd | grep -i pam   # should return nothing
/usr/sbin/sshd -V                  # should print OpenSSH_10.6p2
```

If `ldd` shows a `libpam.so` dependency, your configure step silently picked up a stale `config.cache` — run `make distclean` and repeat step 3.

### 6. Dockerfile patch (for container users)

```dockerfile
FROM alpine:3.21
RUN apk add --no-cache build-base zlib-dev openssl-dev linux-headers wget tar \
 && wget -q https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-10.6p2.tar.gz \
 && tar xzf openssh-10.6p2.tar.gz \
 && cd openssh-10.6p2 \
 && ./configure --prefix=/usr --sysconfdir=/etc/ssh \
      --with-privsep-path=/var/empty --without-pam --with-ssl-engine=no \
 && make -j"$(nproc)" && make install \
 && cd / && rm -rf /openssh-10.6p2*
```

This produces a lean image with no PAM footprint — the whole point of Alpine.

## Common Issues and What You Should Know

- **`configure: error: PAM headers not found`** — you forgot `--without-pam`. Re-run configure from a clean tree.
- **`sshd: PAM is not supported`** at runtime — you installed a binary built *with* PAM onto a system *without* it. Rebuild as above.
- **Upgrading via `apk upgrade openssh`** — Alpine's package maintainers will eventually ship a patched build; until then, pinning the source build is the safe path. Track the Alpine `aports` changelog for the official fix.
- **Key-based auth still works** — disabling PAM does not affect public-key or password auth via `/etc/passwd`; it only removes PAM modules (e.g., `pam_tally2` lockouts, LDAP/SSSD integration). If you rely on those, you need `linux-pam` installed and a *different* build path.
- **Security note** — 10.6p2 is a security-relevant release; don't stay on older 10.x builds waiting for the package manager. Rebuild now.

## Frequently Asked Questions (FAQ)

### How do I fix OpenSSH 10.6p2 on Alpine without PAM?
Rebuild from source with `./configure --without-pam --with-ssl-engine=no`, then `make && make install`. Verify with `ldd /usr/sbin/sshd | grep pam` returning empty.

### Does disabling PAM break SSH login on Alpine?
No. Public-key and standard password authentication via `/etc/passwd` and `/etc/shadow` continue to work. Only PAM-dependent features (LDAP, SSSD, account lockout modules) are lost.

### Is there an official Alpine package fix for OpenSSH 10.6p2?
Check the Alpine `aports` repository for `main/openssh`. Until the patched package lands, the source-build workaround above is the recommended stopgap.

### Why does OpenSSH 10.6p2 fail on musl but work on glibc distros?
The failure stems from configure-time PAM detection assumptions, not musl itself. Explicitly passing `--without-pam` resolves it on any libc.

## Final Verdict

For Alpine users, the OpenSSH 10.6p2 workaround is a two-flag fix: **`--without-pam` and `--with-ssl-engine=no`**. Rebuild from source today, verify with `ldd`, and watch the Alpine aports repo for the official patched package. Don't delay the upgrade — 10.6p2 carries security fixes, and a five-minute source build beats running a vulnerable `sshd` while you wait.