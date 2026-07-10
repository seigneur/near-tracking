# Latest Releases

*Last updated: 2026-07-10 00:20:57 UTC*

## Aztec CLI

**Latest Version:** v4.4.0

**Published:** 2026-06-27T07:57:53Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v4.4.0

**Release Notes:**

Date: 2026-06-27
Tag: v4.4.0
Base: v4.3.1
Range: v4.3.1..v4.4.0

---

## Summary

`v4.4.0` is a **strongly recommended** upgrade on top of `v4.3.1`. It contains important security fixes that harden the node against crash and sync-stall vectors, plus a new **auto-shutdown** feature designed to support zero-downtime rollup upgrades.

**All node operators should upgrade as soon as possible.**

No migration steps required.

---

### ⚠ Breaking Changes

- `ENABLE_VERSION_CHECK` (CLI: `--enable-versio

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

