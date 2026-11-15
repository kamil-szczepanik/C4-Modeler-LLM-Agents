## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance using GCP.

## Key Elements
- **Users**: Patients (EU & US), Licensed Clinicians
- **External Systems**: Pharmacies (EU & US), External AI Inference Provider, Identity Providers, Billing & Insurance Providers, Regulatory Auditors
- **Containers**: API Gateway (Cloud Endpoints / Envoy), Web & Mobile Apps, Core Telehealth Service, Video Media Server (WebRTC / LiveKit SFU), AI Inference & Audit Service, Prescription Integration Service, Audit & Compliance Reporting Service, Regional Databases (Cloud Spanner / Cloud SQL)
- **API Gateway Internal Components**: Envoy Lua/Wasm Regional Routing Filter, JWT & Consent Validation Filter, Regional Rate Limiter, Circuit Breaker & Fallback Filter, Access Log Exporter
- **Infrastructure**: Google Cloud Armor, Google Secret Manager, Cloud Memorystore (Regional Redis)

## Relationships
- Web & Mobile Apps -> API Gateway: Send requests [HTTPS / REST and gRPC over TLS]
- API Gateway -> Core Telehealth Service: Route requests [mTLS via Istio Service Mesh]
- API Gateway -> Cloud Memorystore (Regional): Fetch rate limit quotas [RESP / TCP]
- API Gateway -> Cloud Logging: Stream sanitized access logs [HTTPS / Cloud Logging API]

## Technology Stack
- **API Gateway**: Cloud Endpoints / Envoy proxy for edge routing, rate limiting, and WAF protection.
- **Security & Compliance**: Google Cloud Armor for WAF/DDoS, Google Secret Manager for credentials, Istio Service Mesh for mTLS.
- **Data & Caching**: Cloud Memorystore (Redis) deployed regionally (`europe-west3` and `us-central1`) for local rate-limiting.
- **Logging**: Fluent Bit / Cloud Logging for async, PHI-stripped access log export.

## Rationale
Regionalized infrastructure ensures strict compliance with EU GDPR and US HIPAA mandates by keeping patient data within its originating region (`europe-west3` or `us-central1`). Edge security controls and regional circuit breaking maintain system availability for unstable rural connections without compromising data privacy.