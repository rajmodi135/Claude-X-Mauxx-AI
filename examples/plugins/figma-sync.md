---
name: figma-sync
description: "Sync Figma designs with code. Export tokens, generate components, track implementation status"
metadata:
  type: skill
  category: design
  version: 1
---

# Figma Sync

Two-way sync between Figma designs and code.

## What It Does

1. **Exports** design tokens (colors, typography, spacing) → CSS variables / Tailwind config
2. **Imports** Figma components → React/Vue components
3. **Tracks** implementation status (which designs are coded)
4. **Notifies** on design changes

## Commands

- `figma-sync export <file-id>` — export tokens
- `figma-sync import <frame-id>` — generate components
- `figma-sync status` — show implementation status
- `figma-sync watch <file-id>` — watch for changes

## Requirements

- Figma API key (in env: `FIGMA_API_KEY`)
- Project-specific config in `.claude/figma.yaml`

## Output

```css
/* Auto-generated from Figma */
:root {
  --color-primary: #ff00ff;
  --color-bg: #0a0a1a;
  --space-1: 4px;
  --space-2: 8px;
  --radius-md: 8px;
}
```