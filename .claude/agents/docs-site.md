---
name: docs-site
description: "Preset for documentation site (Docusaurus + MDX + Algolia search)"
metadata:
  type: agent-preset
  version: 1
  stack:
    framework: ["docusaurus", "vitepress", "astro", "nextra"]
    search: ["algolia", "meilisearch", "typesense"]
  modelTier: "haiku"
---

# Docs Site Preset

**Auto-configures the AI company for documentation site projects.**

## Detected Stack

Triggers when project has:
- `docusaurus.config.js`
- `docs/` directory
- `sidebars.js`
- `*.mdx` files

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Docs Architect** | IA, navigation, search | Sonnet |
| **Technical Writer** | Clear, accurate content | Sonnet + deep-research |
| **Code Sample Tester** | Ensure code blocks work | Sonnet + verify |
| **SEO Specialist** | Meta, OG tags, sitemap | Sonnet |
| **Translator** | Multi-language i18n | Sonnet + deep-research |

## Workflow

```
New Doc → Docs Architect (IA) → Technical Writer (content) → parallel:
  - Code Sample Tester (run examples)
  - SEO Specialist (meta tags)
→ Translator (i18n)
→ Deploy (Vercel/Cloudflare)
```

## Conventions

- **Frontmatter:** title, description, sidebar_position, tags
- **Code blocks:** Always tested in CI
- **Images:** WebP, lazy-loaded, alt text
- **Internal links:** Relative paths
- **i18n:** At least English + one other

## Pre-loaded Skills

- deep-research (technical research)
- frontend-design (page layout)
- code-review
- verify (test code samples)

## Quick Start

```bash
echo "preset: docs-site" >> CLAUDE.md
claude --config .claude/settings.json --task "Add a getting started guide"
```
