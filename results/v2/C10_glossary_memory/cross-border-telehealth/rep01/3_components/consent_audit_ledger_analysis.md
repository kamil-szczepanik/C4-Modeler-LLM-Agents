## Overview
A unified cross-border telehealth SaaS platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It enforces strict regional data residency and compliance using isolated cloud deployments on GCP.

## Key Elements
- Patients & Licensed Clinicians
- Compliance Auditors & Regulators
- Pharmacies & Regional Health Authorities/Payers
- AI Triage Model Provider (GCP Vertex AI)
- Identity & Consent Providers
- Web & Mobile Apps (Flutter/React)
- API Gateway & BFF (Envoy/Go)
- Core Telehealth Service (Java/Spring Boot)
- AI Triage Service (Python/FastAPI)
- Consent & Audit Ledger (PostgreSQL)
- E-Prescription Dispatcher (Go)

## Relationships
- Patients & Licensed Clinicians -> Web & Mobile Apps (HTTPS/WebRTC)
- Web & Mobile Apps -> API Gateway & BFF (HTTPS)
- API Gateway & BFF -> Core Telehealth Service (gRPC / REST)
- API Gateway & BFF -> AI Triage Service (gRPC / REST)
- API Gateway & BFF -> Identity & Consent Providers (OIDC / SAML)
- Core Telehealth Service -> Consent & Audit Ledger (PostgreSQL Wire Protocol)
- Core Telehealth Service -> E-Prescription Dispatcher (Internal Messaging / gRPC)
- AI Triage Service -> AI Triage Model Provider (Version-pinned inference APIs (mTLS))
- E-Prescription Dispatcher -> Pharmacies & Regional Health Authorities/Payers (REST / HL7 FHIR)
- Compliance Auditors & Regulators -> Consent & Audit Ledger (Auditor Reporting Interface via HTTPS)

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Isolated regional infrastructure ensuring data residency compliance.
- Envoy / Go: API Gateway and backend-for-frontend routing and TLS termination.
- Java / Spring Boot: Core telehealth business logic implementation.
- Python / FastAPI: AI triage service for PHI/PII sanitization and inference.
- Cloud SQL for PostgreSQL: Regionally isolated data persistence secured via GCP Cloud KMS (CMEK), row-level security, and pgcrypto.
- Go: High-throughput implementation for e-prescription dispatching and consent/audit ledger components.
- Flutter / React: Cross-platform client applications.

## Rationale
Isolating regional deployments in GCP (`europe-west3` and `us-central1`) strictly enforces GDPR and HIPAA data residency mandates. Decomposing the Consent & Audit Ledger with cryptographic integrity and dedicated reporting interfaces satisfies EU MDR traceability and audit requirements without exposing raw PHI.