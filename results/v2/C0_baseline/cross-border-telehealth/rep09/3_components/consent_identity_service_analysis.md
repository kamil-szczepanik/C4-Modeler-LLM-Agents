## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces regional data residency and strict privacy compliance.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web/Mobile Frontend (Flutter)
- Consent & Identity Service (Keycloak / PostgreSQL)
- Telehealth Service (Go / WebRTC)
- Prescription & Record Service (Java / Spring Boot)
- AI Orchestrator & Audit Service (Python / FastAPI)
- Regional Ingress (Cloud Load Balancing & Envoy)

## Relationships
- Web/Mobile Frontend -> Consent & Identity Service: Authenticates users and manages consent [OAuth2/OIDC / HTTPS]
- Telehealth Service -> Consent & Identity Service: Validates identity and authorization [gRPC with mTLS]
- Prescription & Record Service -> Consent & Identity Service: Validates prescription access [gRPC with mTLS]
- All internal services -> WORM Storage: Streams immutable audit logs [HTTPS]

## Technology Stack
- GCP (europe-west3, us-central1): Guarantees strict regional data residency for EU and US compliance.
- Keycloak / PostgreSQL (Cloud SQL): Manages identity, OAuth2/OIDC, and purpose-based GDPR/HIPAA consent.
- Redis (Memorystore): Provides low-latency token caching and revocation checks.
- Istio / Anthos Service Mesh: Enforces strict mTLS and SPIFFE ID verification.

## Rationale
Regional deployment in GCP isolates EU and US health data to satisfy strict GDPR and HIPAA residency mandates. Using Keycloak with custom SPIs and short-lived tokens ensures secure, traceable, and performant consent management.