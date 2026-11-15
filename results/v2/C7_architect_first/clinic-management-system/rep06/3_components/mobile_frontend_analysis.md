## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It utilizes a secure, offline-capable mobile frontend communicating with hybrid cloud infrastructure to ensure high availability and regulatory compliance.

## Key Elements
- Medical Staff & Administrators, Patients, Billing Specialists (Users)
- API Gateway (Envoy / Nginx)
- Mobile Frontend (React Native / Flutter)
  - Authentication & Session Manager (React Native Keychain / Flutter Secure Storage)
  - EMR & Scheduling View Module (React Native / Flutter UI Widgets)
  - API Client & Offline Sync Engine (WatermelonDB / Isar)
  - OTA Update & Telemetry Manager (Sentry SDK / Native OTA runtime)
  - Security & RASP Enclave (Native Security Libraries)
- CockroachDB (Distributed SQL)
- Redis (In-memory Data Store)

## Relationships
- Security & RASP Enclave -> API Gateway: Sends mTLS-pinned, authenticated requests [HTTPS/JSON]
- Authentication & Session Manager -> API Gateway: Validates tokens & sends requests [HTTPS/JSON]
- EMR & Scheduling View Module -> API Client & Offline Sync Engine: Reads/Writes cached clinical data [Local IPC]
- OTA Update & Telemetry Manager -> Secure Cloud Storage: Fetches signed bundle updates [HTTPS]

## Technology Stack
- React Native / Flutter: Cross-platform mobile application development framework
- WatermelonDB / Isar: Encrypted local caching with AES-256 for offline-first resilience
- Sentry SDK: Real-time telemetry and privacy-compliant crash tracking
- React Native Keychain / Flutter Secure Storage: Secure enclave token storage

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict client-side PHI scrubbing, AES-256 local encryption, and remote cryptographic erasure. It meets high-availability and performance requirements via offline-first synchronization, P95 latency tracking, and Over-The-Air patching.