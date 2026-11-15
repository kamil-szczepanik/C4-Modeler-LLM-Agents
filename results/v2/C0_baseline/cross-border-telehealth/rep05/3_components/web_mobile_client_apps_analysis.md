## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Core purpose is delivering secure, compliant healthcare services across regions while supporting unstable rural network conditions.]

## Key Elements
- Web & Mobile Client Apps (Flutter / React Native)
- UI Layer & State Manager (Flutter / React Native)
- Offline Local Store (SQLite / WatermelonDB with SQLCipher)
- API Client & Sync Engine (gRPC-Web / REST with OpenAPI)
- Local Consent & Session Manager
- Local Telemetry & Audit Wrapper
- API Gateway (GCP Cloud Endpoints / Envoy)
- Regional Cloud Infrastructure (GCP regions europe-west3 and us-central1)

## Relationships
- Patients and Licensed Clinicians -> Web & Mobile Client Apps: Accesses via HTTPS and WebSockets
- UI Layer -> Offline Local Store & API Client: Communicates via in-memory method calls
- API Client -> API Gateway: Communicates via HTTPS / gRPC-Web (JSON/Protobuf over HTTP/2)
- Web & Mobile Client Apps -> Regional Identity Providers: Authenticates via OAuth 2.0 with PKCE

## Technology Stack
- Flutter / React Native: Enables cross-platform mobile and web client deployment
- SQLite / WatermelonDB with SQLCipher: Provides encrypted offline-first data caching for intermittent connectivity
- gRPC-Web / OpenAPI REST: Ensures low-overhead synchronization over constrained networks
- iOS Keychain / Android Keystore with Secure Enclave: Secures token storage and hardware-backed cryptographic audit signing

## Rationale
[This architecture enforces regional data residency and strict regulatory compliance (GDPR/HIPAA) by dynamically routing traffic to GCP regions europe-west3 and us-central1. An offline-first client design with local encrypted storage and audit signing ensures continuous availability and traceability for rural users with unstable connections.]