---
name: i18n-helper
description: "Internationalization helper — extracts translatable strings, manages locale files, finds missing translations"
metadata:
  type: skill
  category: localization
  version: 1
---

# i18n Helper

Internationalization made easy.

## What It Does

1. **Extracts** translatable strings from source code
2. **Detects** missing translations across locales
3. **Suggests** translations using AI
4. **Validates** translation files (JSON, YAML, .po, .properties)

## Supported Formats

- JSON (i18next, react-intl)
- YAML (Rails, Symfony)
- .po/.pot (gettext)
- .properties (Java)
- .ts (Qt)

## Commands

- `i18n-helper extract` — extract strings
- `i18n-helper check` — find missing
- `i18n-helper fill` — auto-fill with AI
- `i18n-helper validate` — check syntax
