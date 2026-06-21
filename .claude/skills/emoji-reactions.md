---
name: emoji-reactions
description: "Quick 👍/👎 reactions on outputs. Tracks user satisfaction, adjusts tool accuracy."
metadata:
  type: skill
  category: feedback
  version: 1
---

# Emoji Reactions Skill

Quick reactions on any output.

## Usage

- 👍 — approve
- 👎 — reject
- 🔥 — excellent
- 💩 — bad
- ⭐ — save to memory
- ❓ — need more info

## Storage

All reactions saved to `feedback/reactions/<date>.json` for analysis.

## Integration

Used by Innovation Lead to adjust tool accuracy weights and the Memory Keeper to extract lessons.
