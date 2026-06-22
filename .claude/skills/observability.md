---
name: observability
description: "Adds tracing, metrics, and logging to any project. OpenTelemetry-compatible."
metadata:
  type: skill
  category: monitoring
  version: 1
---

# Observability

Adds tracing, metrics, and structured logging.

## Three Pillars

1. **Logs** — structured JSON with correlation IDs
2. **Metrics** — counters, gauges, histograms (Prometheus format)
3. **Traces** — distributed traces (OpenTelemetry)

## Auto-Generates

- Logger setup (Python/Node/Go/Rust)
- Metrics collection
- Distributed tracing middleware
- Health check endpoints
- OpenTelemetry exporter

## Backends (Free Tier)

- Jaeger (local)
- SigNoz (free cloud)
- Grafana Cloud (free tier)
- Datadog (limited free)
- New Relic (limited free)
- Honeycomb (free tier)

## Commands

- `observability setup` — install + configure
- `observability add <endpoint>` — instrument endpoint
- `observability dashboard` — show local view
