## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and resilience for rural users via regional cloud isolation.

## Key Elements
* Patient Web/Mobile App (Flutter / WASM)
* UI Router & Localization Component
* Offline State & Sync Manager
* API Client Component
* Consent & Profile Controller
* AI Transparency & Accessibility Component
* Telemetry & Error Boundary Component with Data Scrubbing Middleware
* GCP Cloud Endpoints / API Gateway
* Core Telehealth Service (Go / gRPC & REST)
* Consent & Identity Container
* AI Symptom Service (Python / FastAPI)
* GCP Cloud SQL (PostgreSQL) and Pub/Sub

## Relationships
* UI Router delegates to AI Transparency Component and Consent Controller using internal application routing.
* AI Transparency Component and Offline State Manager communicate via HTTPS/REST and WebSockets through the API Client Component.
* API Client Component connects to regional API Gateway using TLS 1.3 / HTTPS.
* API Gateway routes traffic to regional Core Telehealth Service, AI Symptom Service, and Consent Container within GCP `europe-west3` and `us-central1`.

## Technology Stack
* Flutter / WASM: Cross-platform client rendering for web and mobile.
* Hive / SQLite with SQLCipher: Local secure client storage for offline resilience under low bandwidth.
* OpenTelemetry / Firebase Crashlytics: Client-side observability with automated PII scrubbing middleware.
* GCP Cloud Storage & Cloud SQL: Regional data persistence ensuring EU data stays in `europe-west3` and US data in `us-central1`.
* Go & Python / FastAPI: High-performance backend containers for core logic and AI processing.

## Rationale
This architecture enforces strict regional data isolation to meet GDPR and HIPAA requirements while maintaining local offline-first capabilities for rural users. Component-level telemetry with sanitization guarantees accountability and security without compromising patient privacy.