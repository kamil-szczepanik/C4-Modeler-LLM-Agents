## Overview
[Cross-Border Telehealth Platform is a unified SaaS platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance via isolated GCP deployments.]

## Key Elements
- Patients & Licensed Clinicians
- Web & Mobile Apps (Flutter/React)
- API Gateway & BFF (Envoy/Go)
- Core Telehealth Service (Java/Spring Boot)
  - Consultation Session Manager
  - Consent Enforcement Interceptor
  - Telehealth Orchestrator
  - Telehealth Notification & Audit Adapter
- AI Triage Service (Python/FastAPI)
- Consent & Audit Ledger (PostgreSQL)
- E-Prescription Dispatcher (Go)
- AI Triage Model Provider (GCP Vertex AI)
- Identity & Consent Providers

## Relationships
- Patients & Licensed Clinicians -> Web & Mobile Apps [HTTPS/WebRTC]
- Web & Mobile Apps -> API Gateway & BFF [HTTPS]
- API Gateway & BFF -> Core Telehealth Service [gRPC / REST]
- Consultation Session Manager -> Consent Enforcement Interceptor [Internal Method Call]
- Telehealth Orchestrator -> E-Prescription Dispatcher [gRPC]
- Telehealth Notification & Audit Adapter -> Consent & Audit Ledger [PostgreSQL Wire Protocol]
- Core Telehealth Service -> AI Triage Service [gRPC]
- E-Prescription Dispatcher -> Pharmacies & Regional Health Authorities/Payers [REST / HL7 FHIR]

## Technology Stack
- Java / Spring Boot: Implements the Core Telehealth Service business logic and internal component architecture.
- PostgreSQL: Powers the Consent & Audit Ledger with row-level security and Customer-Managed Encryption Keys (CMEK) via Cloud KMS.
- GCP (europe-west3, us-central1): Provides regional cloud infrastructure enforced via VPC Service Controls and strict data residency pipelines.
- Envoy / Go: Manages API Gateway and BFF external traffic routing, TLS termination, and mTLS via SPIFFE/SPIRE.
- GCP Vertex AI: Powers version-pinned inference APIs for the AI Triage Model Provider.

## Rationale
[This architecture uses isolated regional GCP deployments to strictly satisfy EU GDPR and US HIPAA data residency mandates. Asynchronous outbox messaging and robust session recovery ensure low-bandwidth availability and zero audit loss.]