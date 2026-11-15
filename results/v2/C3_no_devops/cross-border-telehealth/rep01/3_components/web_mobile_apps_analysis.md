## Overview
[Cross-Border Telehealth Platform enabling video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, offline resilience, and regulatory compliance.]

## Key Elements
- Patients, Caregivers, Licensed Clinicians
- Web & Mobile Apps Container (React / Flutter)
- API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Service (Go / Spring Boot)
- Video Media Server (WebRTC / LiveKit SFU)
- AI Inference & Audit Service (Python / FastAPI)
- Prescription Integration Service (Node.js)
- Regional Databases (Cloud Spanner / Cloud SQL in `europe-west3` and `us-central1`)

## Relationships
- Patients & Clinicians -> Web & Mobile Apps: HTTPS / REST
- Web & Mobile Apps -> API Gateway: HTTPS / REST and gRPC over TLS
- API Gateway -> Core Services: gRPC over TLS within GCP
- Web & Mobile Apps -> Video Media Server: WebRTC with SRTP and DTLS-SRTP

## Technology Stack
- React / Flutter: Cross-platform web and mobile UI framework with offline-first capabilities
- SQLite / IndexedDB: Local storage for PHI with encryption at rest
- WebRTC / LiveKit SFU: Adaptive video consultations for low bandwidth connections down to 300 kbit/s
- GCP (`europe-west3` & `us-central1`): Regional cloud provider enforcing data residency constraints
- OAuth 2.0 / OpenID Connect: Secure token-based authentication and session handling

## Rationale
[Decomposing the client application into specialized components ensures strict adherence to GDPR and HIPAA data residency mandates. The chosen technology stack guarantees secure, low-bandwidth video streaming and traceable AI interactions across diverse international jurisdictions.]