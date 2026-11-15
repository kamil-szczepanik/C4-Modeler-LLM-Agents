## Overview
Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and robust handling of unstable rural connections.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Compliance Authorities
- API Gateway (Google Cloud Run / Envoy)
- Core Telehealth Backend (Node.js / NestJS)
- AI Symptom Service (Python / FastAPI)
- Video Media Server (LiveKit / WebRTC)
- Regional Google Cloud Memorystore (Redis)
- Google Cloud Armor WAF

## Relationships
- Patients & Clinicians -> API Gateway: HTTPS/REST, WebRTC
- API Gateway -> Regional VPC Backends: gRPC over VPC (mTLS 1.3)
- API Gateway -> Identity Providers: OAuth2/OIDC via HTTPS
- API Gateway -> Regional Redis: Internal TCP

## Technology Stack
- Google Cloud Platform (gcp): Primary cloud provider spanning europe-west3 and us-central1 regions for data residency.
- Envoy Proxy (Cloud Run): Edge routing, WASM consent filters, and rate-limiting to support unstable connections.
- Google Cloud Armor: WAF for API threat protection and DDoS mitigation.
- Google Cloud Memorystore (Redis): Low-latency distributed rate limiting per region.

## Rationale
This architecture guarantees strict regional data residency required by GDPR and HIPAA by deploying isolated regional instances. Envoy and Cloud Run ensure scalable, secure edge routing and reliable degraded performance for rural users.