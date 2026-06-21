# Claude x Mauxx AI — Open Support Ticket
# Invoke: /support

Open a support ticket for a bug, complaint, feature request, or question.

## What It Does
1. Prompts for ticket type (bug|complaint|feature|question|other)
2. Prompts for subject and description
3. Auto-attaches context: current plan, step, files, session ID
4. Creates feedback/tickets/TKT-<date>-<id>.json
5. Assigns priority based on type (P0 for bugs, P1 for complaints, P2 for features)
6. Support Team agent is notified on next iteration

## Usage
```
/support                 — open interactive ticket
/support <type> <desc>   — quick ticket
/support list            — show all open tickets
/support close <id>      — close a ticket
```

## Ticket JSON Format
```json
{
  "id": "TKT-2026-06-22-001",
  "type": "bug|complaint|feature|question",
  "priority": "P0|P1|P2|P3",
  "status": "open|triaged|in_progress|resolved|closed",
  "subject": "Brief title",
  "description": "Full description",
  "context": {
    "project": "/path/to/project",
    "plan": "plan-name",
    "step": 3,
    "files": ["file:line"],
    "sessionId": "..."
  },
  "comments": [],
  "createdAt": "ISO-8601",
  "updatedAt": "ISO-8601"
}
```
