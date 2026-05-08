# Latest Releases

*Last updated: 2026-05-08 00:15:31 UTC*

## Aztec CLI

**Latest Version:** v4.2.1

**Published:** 2026-05-07T08:33:35Z

**URL:** https://github.com/AztecProtocol/aztec-packages/releases/tag/v4.2.1

**Release Notes:**

Release 4.2.1 is a **MANDATORY** single-fix patch on top of 4.2.0. 

The on-chain check for "has this payload already been proposed?" was timing out at the RPC layer so signaling was suppressed across the validator set. This hotfix release restores governance signaling. 

## Bug Fixes

- **Sequencers could not signal governance payloads on long-lived rollups** ([#23001](https://github.com/AztecProtocol/aztec-packages/pull/23001)): The "has this payload already been proposed?" check used `e

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

**Latest Version:** 1.37.2

**Published:** 2026-05-05T13:48:59Z

**URL:** https://github.com/NethermindEth/nethermind/releases/tag/1.37.2

**Release Notes:**

# Release notes

# Release notes

## Overview

This release fixes healthcheck and Archive Invalid Block issues on 1.37.1

## What's Changed
* healthcheck fix by @svlachakis in https://github.com/NethermindEth/nethermind/pull/11482
* Disable ParallelWorldState by @LukaszRozmej  https://github.com/NethermindEth/nethermind/commit/cd1c5ec650c3d686fbb5890e4ca04fb0cec44a79

**Full Changelog**: https://github.com/NethermindEth/nethermind/compare/1.37.1...1.37.2

#### Build signatures

T

---

