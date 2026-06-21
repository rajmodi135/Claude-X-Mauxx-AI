# Claude x Mauxx AI — Review Completed Work
# Invoke: /review

Review and rate completed work (1-5 stars).

## What It Does
1. Lists recently completed plans
2. User selects one to review
3. Prompts for ratings: accuracy, speed, communication (1-5 each)
4. Optional written review
5. Saves to feedback/reviews/<plan-name>.json
6. Used by Innovation Lead and Memory Keeper for retrospective insights

## Usage
```
/review                     — interactive review
/review <plan-name>         — review specific plan
/review list                — list all reviews
```

## JSON Format
```json
{
  "id": "REV-2026-06-22-001",
  "plan": "plan-agent-skills",
  "ratings": {
    "accuracy": 5,
    "speed": 4,
    "communication": 5
  },
  "review": "Excellent work. The agent-skills system is well-designed.",
  "suggestions": "Could add more unit tests.",
  "createdAt": "ISO-8601"
}
```
