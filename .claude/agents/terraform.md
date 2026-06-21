---
name: terraform
description: "Preset for Terraform/OpenTofu infrastructure (AWS/GCP/Azure)"
metadata:
  type: agent-preset
  version: 1
  stack:
    language: [hcl]
    providers: [aws, gcp, azure, kubernetes]
    state: [s3, gcs, azurerm, terraform-cloud]
  modelTier: sonnet
---

# Terraform Preset

For infrastructure as code projects.

## Detected Stack

- *.tf files
- providers.tf, main.tf, outputs.tf
- terraform.tfstate

## Agents

- Cloud Architect (Opus)
- IaC Dev (Terraform HCL)
- Security Reviewer (Opus)
- Cost Analyzer (Sonnet)
- State Manager (Sonnet)

## Conventions

- Module structure: modules/project/env
- Remote state with locking
- terragrunt for multi-env
- pre-commit hooks (terraform fmt, validate)
- Infracost for cost estimates
- tflint + tfsec for quality