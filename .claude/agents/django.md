---
name: django
description: "Preset for Django web apps (Django 5 + DRF + Postgres + Celery)"
metadata:
  type: agent-preset
  version: 1
  stack:
    language: [python]
    framework: [django, django-rest-framework]
    database: [postgres, sqlite, mysql]
  modelTier: sonnet
---

# Django Preset

For Python Django web applications.

## Detected Stack

- requirements.txt with Django
- manage.py
- settings.py

## Agents

- Django Architect (Opus)
- Model Dev (Sonnet)
- View/Serializer Dev (Sonnet)
- API Dev (DRF) (Sonnet)
- Frontend Dev (Django templates) (Sonnet)
- Test Dev (pytest-django) (Sonnet)
- Celery Dev (async tasks) (Sonnet)

## Conventions

- Django 5+ with async views
- DRF for APIs
- pytest-django for tests
- Celery + Redis for async
- Whitenoise for static files
- Gunicorn for production
- Sentry for error tracking