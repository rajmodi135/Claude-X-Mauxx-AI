---
name: mobile-app
description: "Preset for React Native + Expo + iOS/Android mobile app development"
metadata:
  type: agent-preset
  version: 1
  stack:
    framework: ["react-native", "expo", "flutter", "swift", "kotlin"]
    state: ["redux", "zustand", "mobx", "riverpod"]
    build: ["eas", "xcode", "gradle", "fastlane"]
  modelTier: "sonnet"
---

# Mobile App Preset

**Auto-configures the AI company for mobile app development.**

## Detected Stack

Triggers when project has:
- `app.json` (Expo)
- `pubspec.yaml` (Flutter)
- `*.xcodeproj` (iOS native)
- `build.gradle` (Android native)

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Mobile Architect** | Cross-platform vs native decision | Opus |
| **React Native Dev** | RN/Expo components, navigation | Sonnet + frontend-design |
| **Flutter Dev** | Widgets, state management | Sonnet + frontend-design |
| **iOS Dev** | Swift, SwiftUI, Xcode | Sonnet |
| **Android Dev** | Kotlin, Jetpack Compose | Sonnet |
| **Build Engineer** | EAS, Fastlane, signing | Sonnet |
| **App Store** | TestFlight, Play Store submit | Sonnet |
| **Mobile QA** | Detox, Maestro E2E | Sonnet + verify |

## Workflow

```
New Feature → Mobile Architect (cross-platform vs native) → parallel:
  - UI Dev (RN/Flutter/Swift/Kotlin)
  - State Mgmt Dev
  - API integration Dev
→ Build Engineer (EAS/Fastlane)
→ Mobile QA (Detox/Maestro)
→ App Store (submit if ready)
```

## Conventions

- **iOS:** Swift 5.9+, SwiftUI preferred, async/await
- **Android:** Kotlin 1.9+, Jetpack Compose preferred
- **RN:** TypeScript, function components, Expo managed
- **Flutter:** Dart 3, riverpod for state

## Pre-loaded Skills

- frontend-design (UI/UX)
- code-review (PR review)
- verify (run on simulator)
- simplify (cleanup)
- security-review (mobile security)

## Quick Start

```bash
echo "preset: mobile-app" >> CLAUDE.md
claude --config .claude/settings.json --task "Build the login screen"
```
