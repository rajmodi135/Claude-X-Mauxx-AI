---
name: api-mocker
description: "Mocks API responses for development and testing. Generates realistic mock data from OpenAPI/GraphQL schemas."
metadata:
  type: skill
  category: development
  version: 1
---

# API Mocker

Generates realistic mock APIs for development.

## What It Does

1. Reads OpenAPI/GraphQL spec
2. Generates mock server (FastAPI/Express)
3. Returns realistic data (faker.js for JS, faker for Python)
4. Persists state in memory
5. Supports stateful scenarios (login → fetch user)

## Features

- Per-endpoint response customization
- Latency simulation (configurable)
- Error rate simulation
- Stateful (POST creates, GET returns)
- Auth simulation (JWT, OAuth)

## Commands

- `api-mocker start` — start mock server
- `api-mocker spec <file>` — load spec
- `api-mocker scenario <name>` — load scenario
- `api-mocker stop` — stop server

## Output

```
Mock server running on http://localhost:9000
Endpoints:
  GET  /api/users       → list users (200, 50ms latency)
  POST /api/users       → create user (201, 100ms)
  GET  /api/users/:id   → get user (200)
  DELETE /api/users/:id → delete user (204)
```