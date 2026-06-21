# /config — Show/Edit Configuration
# Invoke: /config [key] [value]

Show or edit Mauxx AI configuration.

## Usage

```
/config                          — show all settings
/config model haiku              — change default model
/config budget 100               — set monthly budget
/config loop 24x7                — change loop mode
/config skills all               — enable all skills
/config tools all                — enable all tools
/config preset webapp-fullstack  — set project preset
/config profession developer     — set profession
/config reset                    — reset to defaults
```

## Settings Storage

Saves to `.claude/settings.json` under `claudeMauxxAI` namespace.
