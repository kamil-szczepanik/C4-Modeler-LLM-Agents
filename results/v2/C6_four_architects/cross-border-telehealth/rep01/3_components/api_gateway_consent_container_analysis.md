## Overview
- Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.
- Designed with strict regional data residency, consent management, and low-latency handling for unstable connections on GCP.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway & Consent Container (Envoy Proxy, Open Policy Agent, WASM claims extension)
- Core Telehealth Backend (Node.js / Go, Appointment & Consultation Service, E-Prescription Domain Module)
- Video Consultation Service (WebRTC / Janus Media Server on GCP MIGs)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Java / Spring Boot)
- Dedicated Audit & Logging Container (Fluentbit / OpenTelemetry)
- Regional Databases (Cloud SQL PostgreSQL, Cloud Storage, Cloud Firestore in `europe-west3` and `us-central1`)

## Relationships
- Patients & Clinicians -> API Gateway & Consent Container via HTTPS/WSS
- API Gateway & Consent Container -> Core Telehealth Backend via gRPC over mTLS
- API Gateway & Consent Container -> AI Symptom Checker via gRPC over mTLS
- Policy Enforcement Engine -> Dedicated Audit & Logging Container via OpenTelemetry / gRPC
- Core Telehealth Backend -> Regional Databases via SQL over mTLS

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints.
- Envoy Proxy: Manages ingress TLS, WSS signaling, and gRPC routing.
- Open Policy Agent (OPA): Evaluates consent scopes and regional policies.
- WebRTC / Janus Media Server: Delivers video consultations with degraded bandwidth fallback.
- HL7 FHIR & National Standards: Ensures interoperability for US and EU pharmacies.

## Rationale
- Decouples perimeter security and consent enforcement via OPA and Envoy to guarantee GDPR and HIPAA compliance.
- Uses regional GCP deployments and gRPC communication to minimize latency for rural, unstable connections.