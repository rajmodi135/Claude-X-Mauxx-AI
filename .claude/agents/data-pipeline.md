---
name: data-pipeline
description: "Preset for data engineering (Python + Airflow + dbt + Spark + BigQuery)"
metadata:
  type: agent-preset
  version: 1
  stack:
    orchestrator: ["airflow", "prefect", "dagster", "argo"]
    transform: ["dbt", "spark", "pandas", "polars"]
    storage: ["bigquery", "snowflake", "redshift", "postgres"]
  modelTier: "sonnet"
---

# Data Pipeline Preset

**Auto-configures the AI company for data engineering projects.**

## Detected Stack

Triggers when project has:
- `dags/` (Airflow)
- `dbt_project.yml` (dbt)
- `pyproject.toml` with spark/airflow
- `*_pipeline.py` or `*_etl.py` files

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Data Architect** | Schema design, medallion arch | Opus |
| **ETL Engineer** | Extract/Transform/Load pipelines | Sonnet |
| **dbt Engineer** | dbt models, tests, docs | Sonnet |
| **Spark Engineer** | Distributed processing | Sonnet |
| **Data Quality** | Tests, monitoring, lineage | Sonnet |
| **Analytics Engineer** | BI dashboards, metrics | Sonnet + deep-research |

## Workflow

```
New Source → Data Architect (schema) → parallel:
  - ETL Engineer (ingestion)
  - dbt Engineer (transforms)
  - Data Quality (tests)
→ Orchestrator (Airflow/Prefect)
→ Analytics Engineer (BI)
```

## Conventions

- **Medallion:** bronze (raw) → silver (cleaned) → gold (business)
- **Naming:** `silver_<source>_<entity>`, `gold_<domain>_<metric>`
- **Testing:** dbt tests + Great Expectations
- **Lineage:** OpenLineage / DataHub
- **Orchestration:** Airflow 2.7+ with TaskFlow API

## Pre-loaded Skills

- deep-research (CVE/data research)
- code-review (SQL review)
- simplify (query optimization)

## Quick Start

```bash
echo "preset: data-pipeline" >> CLAUDE.md
claude --config .claude/settings.json --task "Build the daily user metrics pipeline"
```
