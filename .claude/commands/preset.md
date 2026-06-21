# /preset — Set Project Preset
# Invoke: /preset <name>

Load a preset agent configuration for your project type.

## Usage

```
/preset                          — list available presets
/preset webapp-fullstack         — React/Vue + FastAPI + DB
/preset api-microservice         — API + Docker + K8s
/preset security-audit           — SAST + DAST + compliance
/preset perf-tuning              — profiling + benchmarks
```

## Auto-Detection

If no preset specified, auto-detects from project files.
