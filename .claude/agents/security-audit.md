---
name: security-audit
description: "Preset for security audit and penetration testing (SAST + DAST + dependency check + manual review)"
metadata:
  type: agent-preset
  version: 1
  stack:
    tools: ["semgrep", "snyk", "trivy", "owasp-zap", "burp"]
  modelTier: "opus"
---

# Security Audit Preset

**Auto-configures the AI company for security audit projects.**

## Detected Stack

Triggers when project mentions:
- "security", "audit", "pentest", "vulnerability"
- Has SAST/DAST tooling already
- Compliance: SOC2, HIPAA, GDPR, PCI-DSS

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Security Architect** | Threat model, attack surface | Opus |
| **SAST Engineer** | Static analysis (Semgrep, CodeQL) | Sonnet + security-review |
| **DAST Engineer** | Dynamic scanning (OWASP ZAP) | Sonnet |
| **Dependency Auditor** | npm audit, Snyk, Trivy | Sonnet |
| **Secrets Scanner** | TruffleHog, git-secrets | Sonnet |
| **Compliance Officer** | SOC2, HIPAA, GDPR | Opus |
| **Pentester** | Manual exploit testing | Opus |

## Default Workflow

```
Audit Request → Security Architect (threat model) → parallel:
  - SAST Engineer (code scan)
  - DAST Engineer (live scan)
  - Dependency Auditor (deps)
  - Secrets Scanner (creds)
→ Pentester (manual)
→ Compliance Officer (standards)
→ Report (CVSS scoring)
```

## Checklist (OWASP Top 10 + extras)

- [ ] A01: Broken Access Control (IDOR, missing authz)
- [ ] A02: Cryptographic Failures (weak ciphers, no TLS)
- [ ] A03: Injection (SQLi, XSS, command injection)
- [ ] A04: Insecure Design (threat model gaps)
- [ ] A05: Security Misconfiguration (default creds, open ports)
- [ ] A06: Vulnerable Components (outdated deps)
- [ ] A07: Auth Failures (weak passwords, no MFA)
- [ ] A08: Software/Data Integrity (CI/CD, deserialization)
- [ ] A09: Logging Failures (missing audit logs)
- [ ] A10: SSRF (unvalidated URL fetches)

## Output Format

```markdown
# Security Audit Report

## Summary
- Total findings: 12
- Critical: 1
- High: 3
- Medium: 5
- Low: 3

## Critical Findings
### [CRIT-001] SQL Injection in /api/users/:id
- CVSS: 9.8
- CWE: CWE-89
- Location: src/api/users.py:42
- Fix: Use parameterized queries
- Effort: 30 min
```

## Pre-loaded Skills

- `security-review` (primary)
- `code-review` (PR review)
- `deep-research` (CVE research)

## Quick Start

```bash
echo "preset: security-audit" >> CLAUDE.md
claude --config .claude/settings.json --task "Audit the auth flow"
```

## Tools Auto-Installed

```bash
# Via apt/brew
semgrep
trivy
trufflehog

# Via npm
snyk
@owasp/zap-cli
```
