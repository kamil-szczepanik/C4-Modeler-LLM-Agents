## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability.

## Key Elements
- Patients & Licensed Clinicians
- Pharmacies & Regional Health Authorities/Payers
- AI Triage Model Provider (GCP Vertex AI)
- Identity & Consent Providers
- Web & Mobile Apps (Flutter/React)
- API Gateway & BFF (Envoy/Go)
- Core Telehealth Service (Java/Spring Boot)
- AI Triage Service (Python/FastAPI): PHI Sanitizer Component, Inference Orchestrator Component, Audit Logger Component, Clinical Feedback Collector Component
- Consent & Audit Ledger (PostgreSQL)
- E-Prescription Dispatcher (Go)

## Relationships
- Patients & Licensed Clinicians -> Web & Mobile Apps (HTTPS/WebRTC)
- Web & Mobile Apps -> API Gateway & BFF (HTTPS)
- API Gateway & BFF -> Core Telehealth Service (gRPC / REST)
- API Gateway & BFF -> AI Triage Service (gRPC / REST)
- Core Telehealth Service -> Consent & Audit Ledger (PostgreSQL Wire Protocol)
- Core Telehealth Service -> E-Prescription Dispatcher (Internal Messaging / gRPC)
- AI Triage Service -> AI Triage Model Provider (Version-pinned inference APIs (mTLS))
- E-Prescription Dispatcher -> Pharmacies & Regional Health Authorities/Payers (REST / HL7 FHIR)
- API Gateway & BFF -> Identity & Consent Providers (OIDC / SAML)

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for data residency.
- Python & FastAPI: Powers the modular AI Triage Service components.
- PostgreSQL & Cloud KMS: Stores immutable audit logs secured via Customer-Managed Encryption Keys.
- OpenTelemetry & Cloud Monitoring: Provides distributed tracing and observability.

## Rationale
The architecture uses region-isolated GCP deployments to satisfy GDPR and HIPAA data residency mandates. Decomposing the AI Triage Service ensures local PHI sanitization, EU MDR traceability, and fallback resilience for unstable connections.