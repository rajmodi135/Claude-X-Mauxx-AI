# Claude × Mauxx AI — Examples

This directory contains example skills and plugins to inspire your own.

## Structure

```
examples/
├── README.md
├── skills/         ← Example skills (drop into .claude/skills/)
│   ├── auto-commit.md
│   ├── smart-search.md
│   ├── perf-monitor.md
│   ├── i18n-helper.md
│   └── schema-validator.md
└── plugins/        ← Example plugins (integrations)
    ├── figma-sync.md
    ├── github-monitor.md
    ├── sentry-monitor.md
    └── stripe-billing.md
```

## Using Examples

Copy to your project:

```bash
# Copy a skill
cp examples/skills/auto-commit.md .claude/skills/

# Copy a plugin
cp examples/plugins/figma-sync.md .claude/skills/
```

## Creating Your Own

See `PLUGIN_SDK.md` for the full guide.

## Contributing

Submit your own example via PR!
