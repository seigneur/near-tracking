# Latest Releases

*Last updated: 2026-04-29 00:15:42 UTC*

## Aztec CLI

**Latest Version:** v4.2.0

**Published:** 2026-04-15T14:08:32Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v4.2.0

**Release Notes:**

# Framework (Aztec.nr, Aztec.js, etc) Release Notes: v4.1.3 → v4.2.0

**Date:** 2026-04-14
**Range:** `v4.1.3..v4.2.0` (2026-04-02 → 2026-04-14)
**Commits:** 135 framework-relevant commits

Full migration instructions for every breaking change below live in [`docs/docs-developers/docs/resources/migration_notes.md`](docs/docs-developers/docs/resources/migration_notes.md).

---

## Breaking Changes

### Aztec.nr

- **[Aztec.nr]** Capsule operations are now scoped by `AztecAddress`. `

---

## NEAR Protocol

**Latest Version:** 2.11.1

**Published:** 2026-04-21T12:59:33Z

**URL:** https://github.com/near/nearcore/releases/tag/2.11.1

**Release Notes:**

```
CODE_COLOR: CODE_RED_MAINNET, CODE_RED_TESTNET
RELEASE_VERSION: 2.11.1
PROTOCOL_UPGRADE: FALSE
DATABASE_UPGRADE: FALSE
SECURITY_UPGRADE: TRUE
```

This release fixes critical flaws in nearcore code that could cause node crash.
Upgrade as soon as possible to avoid node downtime.

---

## Nethermind

**Latest Version:** 1.37.1

**Published:** 2026-04-28T23:31:32Z

**URL:** https://github.com/NethermindEth/nethermind/releases/tag/1.37.1

**Release Notes:**

# Release notes

## Overview

> This release replaces 1.37.0

540 Changes across 2,651 Files. Major worldstate backend refactor, RocksDB snapshots, flat storage for snap sync, block-level access lists (EIP-7928), initial zkEVM groundwork, and a large round of JSON-RPC and EVM hot-path optimizations.

## Breaking changes

- **eth/66 and eth/67 dropped**; `eth/69` is now default and `eth/70` added and activated (#9938, #10246)
- **Engine API versioning reworked** (#10786)
- **Vault and

---

