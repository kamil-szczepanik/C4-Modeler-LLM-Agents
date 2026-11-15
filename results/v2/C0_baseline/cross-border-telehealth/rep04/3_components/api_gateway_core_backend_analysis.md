## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance with GDPR and HIPAA.

## Key Elements
- Patients, Licensed Clinicians, Pharmacy Partners, Compliance & Audit Officers
- Global Identity Provider (IdP)
- Web/Mobile Frontend App (React / Flutter)
- API Gateway / Core Backend (Go / Node.js)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Plugin architecture)
- Video Session Manager (WebRTC SFU)
- Regional Redis Cache, Regional Kubernetes (GKE) Clusters

## Relationships
- Web/Mobile Frontend App -> API Gateway / Core Backend: Sends API requests via HTTPS / gRPC with protobuf compression
- API Gateway / Core Backend -> AI Symptom Checker: Requests AI symptom analysis via mTLS / Internal API
- API Gateway / Core Backend -> Interoperability Adapter: Triggers e-prescription routing via mTLS / Internal API
- API Gateway / Core Backend -> Global Identity Provider (IdP): Authenticates users via OAuth 2.0 / OIDC with DPoP

## Technology Stack
- Go: Chosen for the API Gateway / Core Backend to ensure high throughput and low latency.
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` to enforce regional data residency.
- Regional Redis Cache: Used by the Idempotency & Retry Coordinator for safe transaction retries without cross-border leaks.
- OpenTelemetry: Implemented for distributed tracing with PHI/PII payload scrubbing.

## Rationale
This architecture enforces strict regional data isolation and consent management at the API gateway layer to satisfy GDPR and HIPAA requirements. Using lightweight protocols like gRPC and protobuf compression ensures high availability and resilience for rural patients on unstable connections.