---
name: spring-boot
description: "Preset for Spring Boot backend (Java 17+ Spring Boot 3 + Postgres + JUnit + Mockito)"
metadata:
  type: agent-preset
  version: 1
  stack:
    language: [java, kotlin]
    framework: [spring-boot, spring-mvc, spring-webflux]
    database: [postgres, mysql, mongodb]
  modelTier: sonnet
---

# Spring Boot Preset

For Java/Kotlin Spring Boot projects.

## Detected Stack

- pom.xml, build.gradle
- src/main/java
- application.yml / application.properties

## Agents

- Spring Architect (Opus)
- Controller Dev (Sonnet)
- Service Dev (Sonnet)
- Repository Dev (Sonnet)
- Test Dev (JUnit + Mockito)
- Build Engineer (Gradle/Maven)

## Conventions

- Layered: Controller → Service → Repository
- DTOs for input/output
- OpenAPI 3.0 with springdoc-openapi
- JUnit 5 + Mockito for testing
- Gradle wrapper or Maven wrapper