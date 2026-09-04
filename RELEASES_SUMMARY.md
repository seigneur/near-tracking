# Latest Releases

*Last updated: 2026-09-04 00:02:09 UTC*

## Aztec CLI

**Latest Version:** v5.2.0

**Published:** 2026-08-17T08:53:53Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v5.2.0

**Release Notes:**

```
  ▁▂▃▅▇█▇▅▃▂▁▁▂▃▅▇█▇▅▃▂▁▁▂▃▅▇█▇▅▃▂▁▁▂▃▅▇█▇▅▃▂▁▁▂▃▅▇█▇▅▃▂▁

                   A Z T E C  ·  5 · 2 · 0
```

**Date:** 2026-08-17 · **Tag:** `v5.2.0` · **Baseline:** `v5.1.0` · Minor release

Install: `aztec-up install 5.2.0` · Docker: `aztecprotocol/aztec:5.2.0`

## Summary

A maintenance release focused on running nodes: prover nodes use much less memory, epoch proving recovers from faults instead of giving up, p2p and mempool handling is hardened, and several L1 interactions stop wasting ga

---

## NEAR Protocol

**Latest Version:** 2.13.4

**Published:** 2026-09-03T15:03:23Z

**URL:** https://github.com/near/nearcore/releases/tag/2.13.4

**Release Notes:**

```
CODE_COLOR: CODE_RED_MAINNET, CODE_RED_TESTNET
RELEASE_VERSION: 2.13.4
PROTOCOL_UPGRADE: FALSE
DATABASE_UPGRADE: FALSE
SECURITY_UPGRADE: TRUE
```
This release fixes critical flaws in nearcore that could cause node crash/DoS.
Upgrade as soon as possible to avoid node downtime.

---

## Nethermind

**Latest Version:** 1.39.3

**Published:** 2026-08-06T13:46:24Z

**URL:** https://github.com/NethermindEth/nethermind/releases/tag/1.39.3

**Release Notes:**

> [!IMPORTANT]
> This is a mandatory update for all node operators. Please upgrade at your earliest convenience.

# Release notes

A patch release on top of 1.39.2 with reliability and hardening fixes across block processing, networking, and request decoding. No consensus or database-format changes, so it's a drop-in upgrade from any 1.39.x version.

## Overview

3 changes since 1.39.2:

- Hardened ABI decoding against malformed input (#12588)
- Fixed pooled-memory cleanup in block p

---

