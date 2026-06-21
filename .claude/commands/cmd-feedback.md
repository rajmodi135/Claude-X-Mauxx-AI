# /feedback — Quick Feedback
# Invoke: /feedback

Send a quick thumbs up/down reaction or comment on current work.

## Usage

```
/feedback            — interactive feedback
/feedback list       — show recent feedback
```

## What It Does
1. Captures current context (plan, step, output)
2. Records reaction (up/down/neutral)
3. Optionally adds a comment
4. Saves to feedback/feedback/<timestamp>.json

## JSON Format

```json
{
  "id": "FB-2026-06-22-001",
  "type": "reaction|comment",
  "reaction": "up|down|neutral",
  "comment": "optional text",
  "context": { "plan": "plan-name", "step": 3 },
  "createdAt": "ISO-8601"
}
```
