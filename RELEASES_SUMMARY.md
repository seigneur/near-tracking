# Latest Releases

*Last updated: 2026-06-05 00:23:00 UTC*

## Aztec CLI

**Latest Version:** v4.3.1

**Published:** 2026-06-04T10:12:30Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v4.3.1

**Release Notes:**

Date: 2026-06-04
Tag: v4.3.1
Base: v4.3.0
Range: v4.3.0..v4.3.1 — three bug fixes

---
## Summary

`v4.3.1` is a recommended patch on top of `v4.3.0`. It ships three bug fixes: a partial-epoch-proof failure mode in the prover-node when the prior epoch is still pending, a block-stream tips-store bug where finalized drifting ahead of proven could orphan still-live block data, and a release-tooling fix that re-stamps the actual aztec_version into published noir-contracts artifacts (`v4.3.0`

---

## NEAR Protocol

**Latest Version:** 2.12.0

**Published:** 2026-06-03T12:57:44Z

**URL:** https://github.com/near/nearcore/releases/tag/2.12.0

**Release Notes:**

```
CODE_COLOR: CODE_YELLOW_MAINNET
RELEASE_VERSION: 2.12.0
PROTOCOL_UPGRADE: TRUE
DATABASE_UPGRADE: TRUE
SECURITY_UPGRADE: FALSE
```

# Protocol Changes
* The contract runtime has been upgraded to use the new Wasmtime-based runtime.
* The contract runtime now allows for bulk memory instructions in Wasm code.

# Non-protocol Changes
* Fix VM compilation and cache metrics (`near_vm_runner_compilation_seconds`, `near_vm_compiled_contract_cache_*`) not being reported for contract deplo

---

## Nethermind

**Latest Version:** 1.38.0

**Published:** 2026-06-02T15:47:15Z

**URL:** https://github.com/NethermindEth/nethermind/releases/tag/1.38.0

**Release Notes:**

# Release notes

This release improves node robustness, restart safety, RPC compatibility, and runtime performance, especially for Flat DB users, RPC-heavy workloads, and chains relying on upcoming hardfork or EIP support.

## Overview

> Full diff: [https://github.com/NethermindEth/nethermind/compare/1.37.2…release/1.38.0](https://github.com/NethermindEth/nethermind/compare/1.37.2%E2%80%A6release/1.38.0)
> 

372 changes since 1.37.2. Highlights include the Taiko Unzen hardfork, paralle

---

