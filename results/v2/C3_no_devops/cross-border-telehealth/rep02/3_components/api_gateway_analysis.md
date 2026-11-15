## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and compliance using GCP regions.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web & Mobile Client Containers (Flutter / React Native)
- API Gateway (Envoy-based Cloud Endpoints / Apigee)
- Claims-Driven Geo-Routing Filter, Consent & Policy Enforcement Filter, and Telemetry & Resilience Proxy
- Core Telehealth Backend and Patient Consent Service (Node.js / Go in GKE)
- AI Inference Wrapper Service (Python / FastAPI)
- GCP Cloud SQL (PostgreSQL) and Cloud Storage with Cloud KMS

## Relationships
- Clients -> Claims-Driven Geo-Routing Filter: HTTPS/gRPC via mTLS with client certificate pinning
- Claims-Driven Geo-Routing Filter -> Consent & Policy Enforcement Filter: Internal gRPC
- Consent & Policy Enforcement Filter -> Telemetry & Resilience Proxy: Internal gRPC
- Telemetry & Resilience Proxy -> Core Telehealth Backend: gRPC over mTLS (`europe-west3` / `us-central1`)

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints for EU and US health data.
- Envoy / Apigee: Powers the API Gateway filters for geo-routing, consent validation, and resilience.
- gRPC over mTLS: Secures microservice communication with cryptographically signed JWTs.
- PostgreSQL & Cloud KMS: Provides encrypted relational storage compliant with GDPR and HIPAA.

## Rationale
This architecture guarantees regulatory compliance by cryptographically binding data residency and consent validation at the API edge. It ensures high availability and accountability for rural users and traceable AI medical diagnostics.