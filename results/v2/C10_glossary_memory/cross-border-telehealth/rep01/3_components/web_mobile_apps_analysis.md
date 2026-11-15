## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, HIPAA/GDPR compliance, and resilient access for rural users.

## Key Elements
- Patients & Licensed Clinicians
- Web & Mobile Apps (Flutter/React)
- API Gateway & BFF (Envoy/Go)
- Core Telehealth Service (Java/Spring Boot)
- AI Triage Service (Python/FastAPI)
- Consent & Audit Ledger (PostgreSQL)
- E-Prescription Dispatcher (Go)
- AI Triage Model Provider (GCP Vertex AI)
- Identity & Consent Providers

## Relationships
- Patients & Licensed Clinicians -> Web & Mobile Apps: HTTPS/WebRTC
- Web & Mobile Apps -> API Gateway & BFF: HTTPS with certificate pinning and short-lived JWTs
- API Gateway & BFF -> Core Telehealth Service: gRPC / REST
- API Gateway & BFF -> AI Triage Service: gRPC / REST
- Core Telehealth Service -> Consent & Audit Ledger: PostgreSQL Wire Protocol
- Core Telehealth Service -> E-Prescription Dispatcher: Internal Messaging / gRPC
- AI Triage Service -> AI Triage Model Provider: Version-pinned inference APIs (mTLS)
- E-Prescription Dispatcher -> Pharmacies & Regional Health Authorities/Payers: REST / HL7 FHIR

## Technology Stack
- Flutter/React: Cross-platform UI for resilient local-first client state and offline caching in rural areas.
- WebRTC: Low-bandwidth video consultations supporting degraded connections below 300 kbit/s.
- GCP Cloud CDN / Cloud Storage: Global static asset delivery isolated across `europe-west3` and `us-central1`.
- PostgreSQL: Structured data storage secured via Customer-Managed Encryption Keys (CMEK) via Cloud KMS.
- GCP Vertex AI: Managed infrastructure for AI symptom-checker inference.

## Rationale
This architecture ensures strict regional data residency and compliance via isolated GCP region deployments while supporting low-bandwidth rural connectivity. Modular microservices and explicit client security controls protect sensitive health data across international borders.