## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces regional data residency and compliance via isolated GCP deployments in `europe-west3` and `us-central1`.

## Key Elements
- Patients & Licensed Clinicians [person, context]
- Web & Mobile Apps [container] (Flutter/React)
- API Gateway & BFF [container] (Envoy/Go)
  - Edge Router & TLS Terminator [component] (Envoy Proxy)
  - Rate Limiting & Resilience Proxy [component] (Envoy/Go)
  - Patient & Clinician BFF Service [component] (Go)
  - Audit & Metadata Interceptor [component] (Go)
- Core Telehealth Service [container] (Java/Spring Boot)
- AI Triage Service [container] (Python/FastAPI)
- Consent & Audit Ledger [container] (PostgreSQL)
- E-Prescription Dispatcher [container] (Go)
- AI Triage Model Provider [externalSystem, context] (GCP Vertex AI)
- Identity & Consent Providers [externalSystem, context]

## Relationships
- Patients & Licensed Clinicians -> Web & Mobile Apps: Accesses telehealth features [HTTPS / WebRTC]
- Web & Mobile Apps -> API Gateway & BFF: Sends client requests [HTTPS]
- API Gateway & BFF -> Core Telehealth Service: Routes business logic requests [gRPC / mTLS]
- API Gateway & BFF -> AI Triage Service: Routes symptom-checker requests [gRPC / mTLS]
- Core Telehealth Service -> Consent & Audit Ledger: Persists audit logs and consent [PostgreSQL Wire Protocol]
- AI Triage Service -> AI Triage Model Provider: Requests symptom inference [Version-pinned inference APIs / mTLS]
- E-Prescription Dispatcher -> Pharmacies & Regional Health Authorities/Payers: Dispatches prescriptions [REST / HL7 FHIR]

## Technology Stack
- Envoy Proxy: Handles edge routing, TLS termination, WAF, and rate limiting.
- Go: Powers the BFF service, e-prescription dispatcher, and resilience proxies for high performance.
- Java / Spring Boot: Implements core telehealth business logic.
- Python / FastAPI: Powers local PHI/PII sanitization for the AI Triage Service.
- PostgreSQL: Stores consent and audit ledger data with CMEK encryption.
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency and cloud infrastructure.

## Rationale
The architecture ensures GDPR and HIPAA compliance by enforcing strict regional data separation between the EU and US deployments. The BFF pattern and payload optimization maintain high availability and usability for rural patients on unstable connections below 300 kbit/s.