---
name: cache-manager
description: "Manages prompt cache, response cache, and computation cache. Optimizes for 90% discount on repeated patterns."
metadata:
  type: skill
  category: performance
  version: 1
---

# Cache Manager

Smart caching for AI workflows.

## What It Caches

- Prompt templates (90% discount on hits)
- API responses (TTL-based)
- Embeddings (vector cache)
- Compilation artifacts
- Test results

## Strategies

- LRU eviction
- TTL-based expiration
- Semantic deduplication
- Hash-based fingerprinting
- Smart invalidation on file change

## Commands

- `cache-manager stats` — hit rate, savings
- `cache-manager clear` — clear all
- `cache-manager clear <key>` — specific key
- `cache-manager warm <prompt>` — pre-warm

## Integration

- prompt caching (Anthropic native, 90% off)
- Redis (free tier on Upstash)
- Local file cache
