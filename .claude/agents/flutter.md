---
name: flutter
description: "Preset for Flutter cross-platform apps (Dart + Flutter SDK + Firebase)"
metadata:
  type: agent-preset
  version: 1
  stack:
    language: [dart]
    framework: [flutter]
    backend: [firebase, supabase]
  modelTier: sonnet
---

# Flutter Preset

For Flutter cross-platform mobile apps.

## Detected Stack

- pubspec.yaml with flutter
- lib/main.dart

## Agents

- Flutter Architect (Sonnet)
- Widget Dev (Sonnet + frontend-design)
- State Manager (Riverpod/Bloc) (Sonnet)
- Firebase Integrator (Sonnet)
- Platform Specialist (iOS/Android) (Sonnet)
- Tester (integration_test) (Sonnet + verify)

## Conventions

- Dart 3+, null safety, records
- Riverpod for state
- go_router for navigation
- freezed for data classes
- json_serializable
- Firebase Auth + Firestore
- integration_test for E2E