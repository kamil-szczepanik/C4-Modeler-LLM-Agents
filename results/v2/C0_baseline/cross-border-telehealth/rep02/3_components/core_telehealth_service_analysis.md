## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency, HIPAA/GDPR compliance, and low-bandwidth resilience.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web / Mobile Client (React / React Native)
- API Gateway (Envoy / Cloud Endpoints)
- Core Telehealth Service (Node.js / NestJS container)
  - Consultation Orchestrator Component
  - Consent & Policy Enforcement Component
  - Prescription Dispatcher Component
  - Telemetry & Metrics Adapter
- OPA (Open Policy Agent) sidecar
- Google Cloud SQL (PostgreSQL with CMEK)
- Pharmacy Partners (EU & US)
- Third-Party WebRTC SFU

## Relationships
- Web / Mobile Client -> API Gateway: Routes user requests [HTTPS / WSS]
- API Gateway -> Core Telehealth Service: Forwards internal requests [gRPC over mTLS]
- Consultation Orchestrator -> Third-Party WebRTC SFU: Manages video and audio streaming sessions [WebRTC / SRTP]
- Consent & Policy Enforcement -> Google Cloud SQL (PostgreSQL): Validates consent records and queries PHI [TCP/TLS 1.3]
- Prescription Dispatcher -> Pharmacy Partners (EU & US): Dispatches regional e-prescriptions [REST / HL7 FHIR over mTLS]

## Technology Stack
- Node.js / NestJS: Chosen for the Core Telehealth Service for modularity and asynchronous I/O handling
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` to enforce physical data residency
- Open Policy Agent (OPA): Provides sub-millisecond, local zero-trust consent and policy evaluations
- PostgreSQL with CMEK: Ensures data at rest is encrypted with customer-managed keys via GCP KMS
- OpenTelemetry: Captures structured audit logs and metrics without leaking PHI

## Rationale
This architecture guarantees strict regional data isolation and regulatory compliance (GDPR/HIPAA) through dedicated multi-region deployments. Furthermore, it ensures high availability and low-bandwidth resilience for rural patients via adaptive bitrate streaming and zero-trust token propagation.