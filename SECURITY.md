# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| v2.x | ✅ Active |
| v1.x | ⚠️ Critical fixes only |
| < 1.0 | ❌ End of life |

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities via public GitHub issues.**

Email: security@mauxxai.dev (or use GitHub's private vulnerability reporting)

Include:
- Description of the vulnerability
- Steps to reproduce
- Impact (what could an attacker do?)
- Suggested fix (if any)

We aim to respond within 48 hours.

## Security Features in Mauxx AI

### Current (v2)

- ✅ Auto-mode permissions (skip prompts)
- ✅ Tool accuracy tracking (catches bad behavior)
- ✅ Cost limits (prevents runaway spending)
- ✅ Context guard (prevents OOM)
- ✅ Self-healing with retry limits (prevents infinite loops)
- ✅ Local-first storage (no cloud upload)

### Planned (v7)

- 🔜 SOC2 audit trails
- 🔜 HIPAA compliance mode
- 🔜 GDPR data controls
- 🔜 Encrypted memory at rest
- 🔜 SSO/RBAC
- 🔜 Self-hosted air-gapped mode

## Security Best Practices

When using Mauxx AI:

1. **Set cost limits**: `/config budget $50` prevents runaway spending
2. **Use local models for sensitive code**: `/config model ollama:llama3.1`
3. **Review generated code**: Don't blindly merge AI-generated code
4. **Keep dependencies updated**: System auto-checks for CVEs
5. **Audit memory periodically**: `memory/` contains project context — review before sharing

## Threat Model

### What Mauxx AI Does Well
- Sandboxed tool execution (Claude Code sandbox)
- No network exfiltration by default
- Encrypted API keys in OS keychain
- Audit trail of every action

### What Mauxx AI Doesn't Do (Yet)
- ❌ Code signing for generated code
- ❌ Formal verification of generated algorithms
- ❌ Encrypted memory at rest
- ❌ Multi-tenant isolation

## Known Security Considerations

1. **Permissions bypass**: The `skipDangerousModePermissionPrompt` flag disables Claude Code's safety prompts. Use with caution.
2. **Custom commands**: Skills and commands can execute arbitrary code. Only install trusted ones.
3. **Webhooks**: Cloudflare Worker handles webhook secrets via env vars. Don't commit secrets to git.

## Audit Logs

All tool calls are logged to `logs/accuracy.log`. Review periodically.

```bash
# View recent activity
tail -50 logs/accuracy.log

# Check for errors
grep "failure" logs/accuracy.log
```

## Bug Bounty

Coming in v7. Stay tuned.

## Acknowledgments

We thank the security researchers who have helped improve Mauxx AI.

## Contact

- General questions: GitHub Issues
- Security: security@mauxxai.dev
- Private disclosure: GitHub Security Advisories
