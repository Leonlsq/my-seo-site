---
title: "Bad Certificate Tricks Explained: Why Your TLS Cert Fails Validation"
description: "Learn why self-signed and malformed TLS certificates break validation, plus step-by-step fixes for OpenSSL, curl, browsers, and Python."
pubDate: 2026-11-10
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Your TLS Certificate Fails Validation (And How to Fix It)

You generated a certificate, pointed your app at it, and got hit with `SSL: CERTIFICATE_VERIFY_FAILED`, `unable to get local issuer certificate`, or a browser warning that won't go away. The certificate "looks fine" in OpenSSL, yet every client rejects it. This guide explains the mechanics behind bad certificate tricks — the deliberate ways certificates get built wrong — and gives you concrete fixes for OpenSSL, curl, Python, Node.js, and browsers. The core takeaway: most validation failures are not bugs in the client. They are missing SANs, broken chains, wrong key usage, or hostname mismatches baked into the certificate itself.

## Step-by-Step Guide / Key Specs Comparison

### Step 1: Diagnose the certificate before touching client config

Run this first. It tells you whether the problem is the cert or the client:

```bash
openssl s_client -connect example.com:443 -servername example.com -showcerts </dev/null 2>/dev/null | openssl x509 -noout -text
```

Check five fields in the output:

| Field | What to verify | Common failure |
|---|---|---|
| `Subject Alternative Name` | Must contain the exact hostname | CN-only certs fail on modern clients |
| `Basic Constraints` | `CA:FALSE` for leaf certs | Leaf marked as CA breaks chains |
| `Key Usage` | `Digital Signature, Key Encipherment` | Missing KU rejected by strict validators |
| `Extended Key Usage` | `TLS Web Server Authentication` | Wrong EKU causes `unsupported certificate purpose` |
| `Not Before / Not After` | Current date inside window | Clock skew or expired cert |

### Step 2: Fix the most common failure — missing SAN

Modern browsers, Chrome, curl ≥7.65, and Python ≥3.7 ignore the Common Name entirely. If your cert has only `CN=example.com`, it fails. Regenerate with a SAN:

```bash
openssl req -new -key server.key -out server.csr \
  -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:www.example.com,IP:127.0.0.1"
```

Wildcards work only for a single label: `*.example.com` matches `api.example.com` but **not** `a.b.example.com` and **not** `example.com` itself.

### Step 3: Repair a broken certificate chain

`unable to get local issuer certificate` means the server isn't sending the intermediate. Concatenate it:

```bash
cat server.crt intermediate.crt > fullchain.crt
```

Then serve `fullchain.crt`. Verify with:

```bash
openssl verify -CAfile root.crt -untrusted intermediate.crt server.crt
```

### Step 4: Trust a self-signed cert correctly (per client)

- **curl:** `curl --cacert myca.crt https://localhost:8443`
- **Python requests:** `requests.get(url, verify='/path/to/myca.crt')`
- **Node.js:** `NODE_EXTRA_CA_CERTS=/path/to/myca.crt node app.js`
- **System-wide (Linux):** copy to `/usr/local/share/ca-certificates/` then `sudo update-ca-certificates`
- **macOS:** `sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain myca.crt`

Never use `verify=False` or `-k` in production — it disables hostname checking and revocation entirely.

## Common Issues, Alternatives, or What You Should Know

**"Bad certificate tricks" in the wild.** The referenced project demonstrates how certificates can be crafted to pass one validator and fail another — for example, a cert with a valid SAN but a mismatched EKU, or a chain where the intermediate is signed by a different root than the leaf claims. These are useful for testing your validation logic, but they also show why you should never roll your own parser.

**Clock skew.** A container with a stale clock will reject a perfectly valid cert. Check with `date -u` and sync via NTP or `chrony`.

**IP vs. DNS SANs.** `127.0.0.1` must appear as `IP:127.0.0.1`, not `DNS:127.0.0.1`. Mixing these is a frequent local-dev failure.

**Let's Encrypt rate limits.** If you're regenerating certs repeatedly while debugging, you'll hit the 5-per-week duplicate limit. Use the staging endpoint (`--server https://acme-staging-v02.api.letsencrypt.org/directory`) during testing.

**Alternatives to self-signed certs for local dev:** `mkcert` generates a locally-trusted CA in one command; `step-ca` offers short-lived certs with automated rotation.

## Frequently Asked Questions (FAQ)

### Why does my certificate work in curl but fail in Chrome?
Chrome enforces Certificate Transparency and stricter EKU checks. A cert without SCTs (for public CAs) or with a missing `serverAuth` EKU will pass curl but trigger `ERR_CERT_INVALID` in Chrome.

### How do I fix "certificate has expired" without regenerating?
You can't extend an expired cert — validity is signed. Regenerate the cert with the same key and redeploy, or automate renewal with certbot/acme.sh and a reload hook.

### What's the difference between a bad certificate and a bad chain?
A bad certificate has wrong fields (SAN, EKU, dates). A bad chain is missing or misordered intermediates. `openssl verify` distinguishes them: chain errors mention "issuer," cert errors mention the specific field.

### Can a certificate be valid for one hostname and invalid for another?
Yes. SANs are exact-match (plus single-label wildcards). A cert for `example.com` will fail for `www.example.com` unless both are listed.

## Final Verdict

Treat every validation error as a certificate problem until proven otherwise. Run the `openssl s_client` diagnostic first, confirm SANs and the chain, then fix the cert — not the client. Disabling verification is a debugging shortcut, never a solution. If you're building local services, switch to `mkcert` and stop hand-rolling self-signed certs; it eliminates 90% of the failures covered here in under a minute.