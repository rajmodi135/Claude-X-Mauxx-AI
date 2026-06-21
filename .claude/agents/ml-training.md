---
name: ml-training
description: "Preset for ML model training (PyTorch + W&B + HuggingFace)"
metadata:
  type: agent-preset
  version: 1
  stack:
    framework: ["pytorch", "tensorflow", "jax", "huggingface"]
    tracking: ["wandb", "mlflow", "tensorboard"]
    data: ["huggingface", "kaggle", "s3"]
  modelTier: "opus"
---

# ML Training Preset

**Auto-configures the AI company for machine learning projects.**

## Detected Stack

Triggers when project has:
- `train.py`, `model.py`
- `wandb/` or `mlruns/`
- `requirements.txt` with torch/tensorflow
- `*.safetensors`, `*.bin`, `*.pt` files

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **ML Architect** | Model selection, training strategy | Opus |
| **Data Engineer** | Datasets, preprocessing, augmentation | Sonnet + deep-research |
| **Trainer** | Training loop, hyperparams | Sonnet |
| **Evaluator** | Metrics, validation, benchmarks | Sonnet |
| **Deployer** | TorchServe, Triton, HF Spaces | Sonnet |
| **Researcher** | Paper reviews, SOTA comparison | Sonnet + deep-research |

## Workflow

```
New Model → ML Architect (architecture) → Data Engineer (data) → Trainer (train) → 
  parallel:
  - Evaluator (metrics)
  - Researcher (compare to SOTA)
→ Deployer (HF Spaces / API)
```

## Conventions

- **Reproducibility:** Set seeds, log config, save checkpoints
- **Tracking:** W&B or MLflow, never both
- **Data versioning:** DVC or LakeFS
- **Eval:** Held-out test set, never seen during training
- **Deploy:** TorchServe / Triton / HF Inference Endpoints

## Pre-loaded Skills

- deep-research (paper research)
- code-review
- verify (run benchmarks)
- simplify

## Quick Start

```bash
echo "preset: ml-training" >> CLAUDE.md
claude --config .claude/settings.json --task "Fine-tune Llama 3 on customer support data"
```
