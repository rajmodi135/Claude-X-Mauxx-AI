---
name: rust-cli
description: "Preset for Rust CLI tools (Clap + Cargo + crates.io)"
metadata:
  type: agent-preset
  version: 1
  stack:
    language: [rust]
    framework: [clap, structopt]
    build: [cargo, rustc]
  modelTier: sonnet
---

# Rust CLI Preset

For Rust command-line tools.

## Detected Stack

- Cargo.toml with clap
- src/main.rs

## Agents

- CLI Architect (Sonnet)
- Rust Dev (Sonnet)
- Test Dev (cargo test)
- Distributor (crates.io)

## Conventions

- Clap derive API for args
- Error handling with anyhow/thiserror
- Tracing for logging
- cargo-dist for releases
- GitHub Actions for CI

## Quick Start

```bash
echo "preset: rust-cli" >> CLAUDE.md
```