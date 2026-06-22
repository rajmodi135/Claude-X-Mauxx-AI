---
name: notifier
description: "Sends notifications via Telegram, Slack, Discord, Email based on events"
metadata:
  type: skill
  category: integration
  version: 1
---

# Notifier

Multi-channel notifications.

## Triggers

- P0 ticket created
- Plan completed
- Build failed
- Deploy success/failure
- Cost budget exceeded
- Accuracy tier unlocked

## Channels

- Telegram (recommended for personal)
- Slack (team)
- Discord (community)
- Email (formal)
- SMS (critical only, via Twilio)

## Commands

- `notifier config <channel>` — set up
- `notifier test <channel>` — test message
- `notifier rules` — show triggers

## Config

```yaml
# .claude/notifier.yaml
telegram:
  bot_token: ${TELEGRAM_BOT_TOKEN}
  chat_id: ${TELEGRAM_CHAT_ID}

slack:
  webhook_url: ${SLACK_WEBHOOK}

rules:
  - trigger: plan_completed
    channels: [telegram, slack]
  - trigger: p0_ticket
    channels: [telegram, slack, sms]
```
