---
name: webhook
description: "Receives and sends webhooks for external integrations (GitHub, Slack, Discord, custom)"
metadata:
  type: skill
  category: integration
  version: 1
---

# Webhook Skill

External integration via webhooks.

## Receives

- GitHub push/PR/issue events
- Stripe payments
- Custom webhooks (configurable URL)

## Sends

- Plan completion → Slack/Discord
- P0 ticket → Telegram
- Test failure → Sentry
- Deploy success → custom URL

## Configuration

```yaml
# .claude/webhooks.yaml
incoming:
  - source: github
    secret: ${GITHUB_WEBHOOK_SECRET}
    actions: [push, pull_request, issues]
  - source: stripe
    events: [payment_intent.succeeded]

outgoing:
  - trigger: plan_completed
    targets: [slack:#dev-team]
  - trigger: p0_ticket
    targets: [telegram:bot]
```

## Cloudflare Worker

Built-in Cloudflare Worker at `cloudflare-worker/` handles webhook routing.
