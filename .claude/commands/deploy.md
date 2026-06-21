# /deploy — Deploy Project
# Invoke: /deploy [target]

Deploy the current project to a target.

## Targets

- `vercel` — Vercel (auto-detect framework)
- `netlify` — Netlify
- `cloudflare-pages` — Cloudflare Pages
- `aws` — AWS (S3 + CloudFront)
- `fly` — Fly.io
- `railway` — Railway
- `docker` — Docker Hub
- `k8s` — Kubernetes cluster
- `npm` — npm registry (for libraries)
- `pypi` — PyPI (for Python packages)

## Usage

```
/deploy vercel       — deploy to Vercel
/deploy docker       — build + push Docker image
/deploy npm          — publish to npm
/deploy k8s          — apply manifests
/deploy --dry-run    — show what would happen
```

## Pre-Deploy Checks

- Run tests
- Build artifacts
- Lint check
- Security scan
- Update CHANGELOG
