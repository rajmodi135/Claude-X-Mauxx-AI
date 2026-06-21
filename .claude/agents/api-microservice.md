---
name: api-microservice
description: "Preset for API microservice (FastAPI/Express/Go + Docker + K8s + observability)"
metadata:
  type: agent-preset
  version: 1
  stack:
    language: ["python", "typescript", "go", "rust"]
    framework: ["fastapi", "express", "gin", "actix"]
    deployment: ["docker", "kubernetes", "cloud-run", "lambda"]
  modelTier: "sonnet"
---

# API Microservice Preset

**Auto-configures the AI company for backend microservice projects.**

## Detected Stack

Triggers when project has:
- `Dockerfile` or `docker-compose.yml`
- `k8s/`, `kubernetes/`, or `helm/` directory
- API framework (FastAPI, Express, Gin)
- OpenAPI/Swagger spec

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **API Architect** | Endpoints, contracts, versioning | Opus (architecture) |
| **API Dev** | Endpoints, middleware, validation | Sonnet |
| **DB Specialist** | Queries, indexes, migrations | Sonnet |
| **Container Engineer** | Dockerfile, multi-stage builds | Sonnet |
| **K8s Engineer** | Manifests, Helm charts, ingress | Sonnet |
| **Observability** | Logging, metrics, tracing | Sonnet |
| **Security** | API security, OWASP | Sonnet + security-review |
| **Load Tester** | k6, locust, wrk | Sonnet |

## Default Workflow

```
New Endpoint Request → API Architect (design) → API Dev (implement) → 
  parallel:
    - DB Specialist (query)
    - Container Engineer (image)
    - Observability (logs/metrics)
  → Security (audit) → Load Tester (perf)
```

## Conventions

- **API:** REST + OpenAPI 3.0 spec
- **Errors:** RFC 7807 (problem+json)
- **Logging:** Structured JSON with correlation IDs
- **Metrics:** Prometheus format
- **Tracing:** OpenTelemetry
- **Health:** /health/live, /health/ready

## Pre-loaded Skills

- `code-review` (PR review)
- `security-review` (audit)
- `verify` (run + test)
- `simplify` (cleanup)

## Deployment Targets

- **Docker:** Multi-stage, non-root user, healthcheck
- **K8s:** Liveness/readiness probes, resource limits, HPA
- **Cloud Run / Lambda:** Auto-scaling, cold-start optimized

## Quick Start

```bash
# In a new project:
echo "preset: api-microservice" >> CLAUDE.md
claude --config .claude/settings.json
```

## Example Plan

```markdown
# Plan: Add /api/v1/users endpoint

Priority: P1 | Steps: 5 | Est. cost: $0.06

## Steps
1. API Architect: Design endpoint (REST + OpenAPI)
2. API Dev: Implement with Pydantic validation
3. DB Specialist: Add users table + index on email
4. Observability: Add metrics + structured logs
5. Load Tester: Benchmark 1K req/sec
6. Security: Audit for IDOR, rate-limit

## Agents
- API Architect (Opus)
- API Dev
- DB Specialist
- Observability
- Load Tester
- Security
```
