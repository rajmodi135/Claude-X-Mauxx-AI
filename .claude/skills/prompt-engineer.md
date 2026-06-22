---
name: prompt-engineer
description: "Optimizes AI prompts for cost, accuracy, and speed. A/B tests variants."
metadata:
  type: skill
  category: ai
  version: 1
---

# Prompt Engineer

Optimizes prompts through systematic A/B testing.

## What It Does

1. Takes a base prompt
2. Generates variants (different phrasings, structures)
3. A/B tests against metrics (accuracy, cost, speed)
4. Tracks winner over time
5. Suggests improvements

## Metrics Tracked

- Accuracy (correctness)
- Cost (tokens)
- Speed (latency)
- User satisfaction
- Token efficiency

## Commands

- `prompt-engineer test <prompt>` — A/B test
- `prompt-engineer optimize <prompt>` — find best variant
- `prompt-engineer stats` — show history
- `prompt-engineer export` — export winner

## Example

```
Base:  "Fix the bug in login"
Best:  "Identify the authentication issue in src/auth/login.py and suggest a fix"
       (87% accuracy, 2x faster)
```
