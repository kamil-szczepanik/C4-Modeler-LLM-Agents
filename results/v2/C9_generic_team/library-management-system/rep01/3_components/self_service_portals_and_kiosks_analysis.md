## Overview
[Library Management System provides catalogue management, circulation, and self-service portals for public and academic libraries. The architecture ensures EU-only data residency and meets sub-800ms search performance.]

## Key Elements
* Library Patrons and Staff
* Self-Service Portals and Kiosks (Web/Mobile UI)
* API Gateway
* Observability & Logging Container
* Configuration & Feature Management Container
* Core Domain Services

## Relationships
* Library Patrons and Staff -> Self-Service Portals and Kiosks: Accesses via HTTPS [HTTPS]
* Self-Service Portals and Kiosks -> API Gateway: Communicates using REST [HTTPS/REST]
* Self-Service Portals and Kiosks -> Observability & Logging Container: Forwards telemetry and heartbeats [HTTPS]
* Self-Service Portals and Kiosks -> Configuration & Feature Management Container: Fetches dynamic configurations [HTTPS]

## Technology Stack
* Frontend Architecture: Modular component-driven design system for code sharing across web and kiosks.
* Resilience: Circuit Breaker and Retry pattern with exponential backoff for handling transient network failures.
* Security: Strict CSP headers, XSS sanitization, zero-trust short-lived tokens, and encrypted IndexedDB for local storage.
* Compliance & Telemetry: Client-side PII redaction to enforce EU-only data residency requirements.

## Rationale
[The architecture prioritizes client-side optimization, local caching, and robust resilience patterns to guarantee high performance on constrained kiosk hardware. Strict security controls and telemetry redaction ensure compliance with EU data residency requirements.]