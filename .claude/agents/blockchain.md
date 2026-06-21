---
name: blockchain
description: "Preset for blockchain development (Solidity + Hardhat + Ethers + OpenZeppelin)"
metadata:
  type: agent-preset
  version: 1
  stack:
    contracts: ["solidity", "vyper"]
    framework: ["hardhat", "foundry", "truffle"]
    frontend: ["ethers", "wagmi", "viem", "rainbowkit"]
  modelTier: "opus"
---

# Blockchain Preset

**Auto-configures the AI company for blockchain / Web3 projects.**

## Detected Stack

Triggers when project has:
- `hardhat.config.js` / `foundry.toml`
- `contracts/` directory with `.sol` files
- `package.json` with ethers/wagmi

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Smart Contract Architect** | Contract design, gas optimization | Opus + security-review |
| **Solidity Dev** | Contract implementation | Sonnet + security-review |
| **Auditor** | Security audit, formal verification | Opus + security-review |
| **Frontend Dev** | Web3 UI, wallet connection | Sonnet + frontend-design |
| **Deployer** | Testnet/mainnet deployment | Sonnet |
| **Researcher** | EIPs, governance research | Sonnet + deep-research |

## Workflow

```
New Feature → Smart Contract Architect (design) → Solidity Dev (implement) → 
  parallel:
  - Auditor (security review)
  - Gas optimizer
→ Test (Hardhat/Foundry test suite)
→ Deployer (testnet first, then mainnet)
→ Frontend Dev (UI integration)
```

## Conventions

- **Solidity:** 0.8.21+, use OpenZeppelin contracts
- **Testing:** Hardhat + Chai, 100% coverage
- **Security:** Slither, Mythril, formal verification
- **Gas:** Optimize storage layout, pack structs
- **Upgradeability:** UUPS proxy pattern preferred
- **Audit:** Always before mainnet

## Pre-loaded Skills

- security-review (PRIMARY)
- code-review
- deep-research (EIP research)
- verify (run tests)

## Quick Start

```bash
echo "preset: blockchain" >> CLAUDE.md
claude --config .claude/settings.json --task "Add an ERC-4626 vault"
```

## ⚠️ Security First

All smart contract code is reviewed by Opus. The Auditor agent runs Slither, Mythril, and property-based tests before deployment.
