---
name: stripe-billing
description: "Stripe integration helper — subscriptions, webhooks, customer portal, invoices"
metadata:
  type: skill
  category: integration
  version: 1
---

# Stripe Billing

Stripe integration made simple.

## What It Does

1. **Generates** Stripe products, prices, coupons
2. **Implements** checkout, customer portal, webhooks
3. **Handles** subscription lifecycle (trials, upgrades, cancellations)
4. **Reconciles** charges with your database
5. **Generates** invoices and reports

## Setup

```bash
stripe-billing init
# Creates .claude/stripe.yaml with your config
```

## Commands

- `stripe-billing create-product <name>` — make product
- `stripe-billing create-price <product-id>` — make price
- `stripe-billing setup-checkout` — generate checkout code
- `stripe-billing setup-portal` — generate customer portal
- `stripe-billing handle-webhook <event>` — webhook handler

## Generated Code

Includes:
- Frontend checkout (React/Next.js)
- Backend API routes (FastAPI/Express)
- Webhook handlers (verified signatures)
- Database schema (subscriptions table)
- Tests