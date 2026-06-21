---
name: api-docs
description: "Generates interactive API documentation (Swagger UI, Redoc) from OpenAPI specs"
metadata:
  type: skill
  category: documentation
  version: 1
---

# API Docs Generator

Generates beautiful API documentation.

## What It Does

1. **Reads** OpenAPI 3.0/3.1 spec
2. **Generates** interactive HTML docs (Swagger UI or Redoc)
3. **Hosts** on local dev server
4. **Deploys** to Vercel/Netlify on merge
5. **Watches** for spec changes

## Output

- Interactive endpoint explorer
- Try-it-out console
- Request/response examples
- Schema explorer
- Authentication tester

## Commands

- `api-docs generate` — generate static HTML
- `api-docs serve` — start local server
- `api-docs deploy` — deploy to production
- `api-docs validate` — validate spec

## Stack Support

- OpenAPI 3.0/3.1
- GraphQL (via graphql-docs)
- gRPC (via grpc-gateway)
- Postman Collections (import)