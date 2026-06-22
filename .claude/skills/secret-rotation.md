---
name: secret-rotation
description: "Auto-rotates API keys, secrets, and tokens. Detects compromised credentials, generates new ones, updates deployments."
metadata:
  type: skill
  category: security
  version: 1
---

# Secret Rotation

Automatic secret rotation.

## What It Rotates

- API keys (Anthropic, OpenAI, GitHub, etc.)
- Database passwords
- TLS certificates
- OAuth tokens
- Service account keys

## When It Triggers

- Scheduled (every 30/60/90 days)
- Compromise detected
- User leaves team
- Compliance requirement (SOC2, PCI)
- Manual trigger

## What It Does

1. Generates new secret
2. Stores in vault (HashiCorp Vault, AWS Secrets Manager, 1Password)
3. Updates all environments (staging, prod)
4. Verifies with health checks
5. Revokes old secret
6. Logs to audit trail

## Commands

- `secret-rotate <key>` — rotate now
- `secret-list` — show all
- `secret-audit` — check for issues
- `secret-policy` — set rotation policy

## Free Backends

- 1Password (free personal)
- Bitwarden (free)
- Infisical (free OSS)
- Doppler (free tier)
