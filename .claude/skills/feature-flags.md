---
name: feature-flags
description: "Feature flag management — gradual rollouts, A/B testing, kill switches"
metadata:
  type: skill
  category: deployment
  version: 1
---

# Feature Flags

Manage feature flags for safe rollouts.

## What It Does

1. **Defines** flags in `feature-flags.yaml`
2. **Wraps** code with flag checks
3. **Rolls out** to % of users
4. **A/B tests** with metrics
5. **Kill switches** for instant disable

## Flag Format

```yaml
flags:
  new_checkout:
    description: "New checkout flow"
    state: gradual_rollout
    rollout:
      - segment: internal_users
        percent: 100
      - segment: all_users
        percent: 10
    kill_switch: true

  dark_mode:
    state: on
    segments: [all_users]
```

## Usage

- `feature-flags add <name>` — create flag
- `feature-flags set <name> on|off|rollout` — change state
- `feature-flags rollout <name> <pct>` — set rollout %
- `feature-flags kill <name>` — instant disable
- `feature-flags report` — show usage stats

## Integration

Works with `code-review` (warns on hardcoded flags) and `verify` (tests both states).