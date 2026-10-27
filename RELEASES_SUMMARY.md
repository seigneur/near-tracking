# Latest Releases

*Last updated: 2026-10-27 00:02:12 UTC*

## Aztec CLI

**Latest Version:** v6.0.0

**Published:** 2026-10-22T12:20:46Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v6.0.0

**Release Notes:**

```
   v5   L1 ▕░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▏ L2    24–108s
   v6   L1 ▕████████▏ L2                          12–30s

                   A Z T E C  ·  6 · 0 · 0
```

**Date:** 2026-10-22 · **Tag:** `v6.0.0` · **Baseline:** `v5.2.1` · Major release

npm: `@aztec-foundation/bb.js@6.0.0` (note the new `@aztec-foundation` scope) · crates.io: `barretenberg-rs 6.0.0` · Noir: `v1.0.0-rc.3`

## Summary

v6.0.0 is the protocol, proving system and L1 contracts behind the v6 rollup proposed i

---

## NEAR Protocol

**Latest Version:** 2.14.0

**Published:** 2026-10-26T18:59:52Z

**URL:** https://github.com/near/nearcore/releases/tag/2.14.0

**Release Notes:**

```
CODE_COLOR: CODE_YELLOW_MAINNET
RELEASE_VERSION: 2.14.0
PROTOCOL_UPGRADE: TRUE
DATABASE_UPGRADE: TRUE
SECURITY_UPGRADE: FALSE
```

# Protocol Changes
* Remove gas rewards: executing a `FunctionCall` no longer pays part of the burned gas back to the contract account as a reward. The `burnt_gas_reward` parameter is changed from 30% (3/10) to 0%. See [HSP-027](https://gov.near.org/t/hsp-027-remove-the-near-developer-gas-rebate/42213)
* Added an `ml_dsa_verify` host function so contracts can ver

---

## Nethermind

**Latest Version:** 2.2.2

**Published:** 2026-10-26T16:59:58Z

**URL:** https://github.com/NethermindEth/nethermind/releases/tag/2.2.2

**Release Notes:**

# Release notes

A patch release on top of 2.2.1 with the October 2026 out-of-band .NET security updates. See the [Microsoft announcement](https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/) for details of the fixed vulnerabilities.

There are no Nethermind code, database-format, or configuration changes, so you can upgrade in place from any 2.2.x version. Consensus behavior and fork schedules are the same as in 2.2.1.

## Overview

2 changes since 2.2.1:



---

