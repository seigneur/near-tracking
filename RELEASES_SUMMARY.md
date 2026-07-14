# Latest Releases

*Last updated: 2026-07-14 00:14:47 UTC*

## Aztec CLI

**Latest Version:** v5.0.0

**Published:** 2026-07-13T12:33:01Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v5.0.0

**Release Notes:**

```
  ██    ██  ██████
  ██    ██  ██
   ██  ██   ██████
    ████        ██
     ██     ██████

        A Z T E C
```

*v 5 · 0 · 0 — none of the wait, twice the pace, half the gates.*

**Date:** 2026-07-11 · **Tag:** `v5.0.0` · **Baseline:** `v4.4.0` · **First stable v5 — supported on testnet AND mainnet**

Install: `aztec-up install 5.0.0` · Docker: `aztecprotocol/aztec:5.0.0`

## Summary

v5.0.0 is the first stable release of the v5 line and the first Aztec release supported on both testnet a

---

## NEAR Protocol

**Latest Version:** 2.13.0

**Published:** 2026-07-09T13:07:41Z

**URL:** https://github.com/near/nearcore/releases/tag/2.13.0

**Release Notes:**

```
CODE_COLOR: CODE_YELLOW_MAINNET
RELEASE_VERSION: 2.13.0
PROTOCOL_UPGRADE: TRUE
DATABASE_UPGRADE: TRUE
SECURITY_UPGRADE: FALSE
```

# [NOTE] Check your `state_sync.sync` setting in config.json
2.13 no longer accepts the old centralized (external-storage) state sync. If your `config.json` has `state_sync.sync` set to `ExternalStorage`, like the following:
```
{
  "state_sync": {
    "sync": {
      "ExternalStorage": {
        "location": { "GCS": { "bucket": "..." } },
       

---

## Nethermind

**Latest Version:** 1.39.0

**Published:** 2026-07-08T17:56:34Z

**URL:** https://github.com/NethermindEth/nethermind/releases/tag/1.39.0

**Release Notes:**

# Release notes

This release focuses on node robustness, Flat DB durability — alongside the eth/71 wire protocol, a reworked discovery stack, a large JSON-RPC features-and-correctness batch, continued Block-level Access Lists (EIP-7928) maturation, and a broad round of EVM, precompile, and state performance work.

> **OP Karst reminder:** the OP **Karst** hardfork (shipped in 1.38.1 and included here) activates on OP **Mainnet: Wed, Jul 8, 2026 at 16:00:01 UTC**. OP Stack operators must be 

---

