---
name: security-scanner
description: "Scans code for common security issues: SQL injection, XSS, secrets, weak crypto, OWASP Top 10"
metadata:
  type: skill
  category: security
  version: 1
---

# Security Scanner Skill

Real-time security scanning.

## What It Scans

| Category | Examples |
|----------|----------|
| Injection | SQL injection, command injection, LDAP injection |
| XSS | Stored, reflected, DOM-based |
| Auth | Missing auth, broken access control, IDOR |
| Crypto | Weak ciphers, hardcoded keys, no TLS |
| Secrets | API keys, passwords, tokens in code |
| Dependencies | Known CVEs |
| Config | Debug mode, default creds, open ports |

## Output Format

```
🔒 Security Scan Results

Critical (1):
  ⚠ CRIT-001 SQL Injection in src/api/users.py:42
  Fix: Use parameterized queries

High (2):
  ⚠ HIGH-001 Hardcoded API key in src/config.py:18
  ⚠ HIGH-002 Outdated dependency lodash@4.17.15 (CVE-2021-23337)

Medium (3):
  ⚡ MED-001 Missing rate limiting on /api/login
  ...

Score: 7.2/10 (Acceptable)
```

## Commands

- `/security scan` — full scan
- `/security secrets` — just secret scan
- `/security deps` — just dependency check
- `/security report` — generate report
