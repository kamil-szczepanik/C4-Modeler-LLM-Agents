## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces regional data residency and compliance via strict privacy, interoperability, and audit controls.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web & Mobile Client Apps (Flutter / React Native)
- API Gateway (Google Cloud API Gateway / Apigee)
- Core Telehealth Service (Spring Boot / Java)
- AI Symptom Checker Service (FastAPI / Python)
- Interoperability & E-Prescription Service (Node.js) containing:
  - FHIR & National Standard Transformer (TypeScript)
  - Gateway Dispatcher & Circuit Breaker (TypeScript / Resilience4js)
  - Dispensation Event Poller / Webhook Handler (Node.js)
  - Compliance Audit Logger (TypeScript)
- WebRTC SFU Media Relay (LiveKit on GKE)
- Data & Security Layer (Cloud SQL, Cloud Storage, GCP Cloud KMS, GCP Service Mesh)
- External Networks (EU National E-Prescription Gateways and US Pharmacy Networks)

## Relationships
- API Gateway -> Interoperability & E-Prescription Service: Routes interoperability requests [gRPC with mTLS via GCP Service Mesh]
- Gateway Dispatcher -> EU/US Networks: Exchanges e-prescription data [HTTPS / REST, HL7 FHIR and EU standards with TLS 1.3 & mTLS]
- Dispensation Webhook Handler -> Core Telehealth Service: Publishes status updates [gRPC]
- Core Telehealth Service -> Data & Security Layer: Persists data [PostgreSQL, GCP Cloud KMS]

## Technology Stack
- Node.js & TypeScript: Interoperability service core for high asynchronous I/O performance
- Resilience4js: Circuit breaking for external gateway downtime handling
- gRPC with mTLS: Internal container communication via GCP Service Mesh
- HL7 FHIR & EU Standards: Regional e-prescription data interoperability
- GCP Cloud KMS (HSM-backed): Cryptographic signing and PHI/PII application-layer encryption
- GCP Cloud Logging: Immutable audit log storage for HIPAA and GDPR accountability

## Rationale
This architecture ensures strict cross-border health data residency and regional compliance for GDPR and HIPAA. Furthermore, its modular, decoupled components guarantee robust availability during unstable network conditions and traceable medical device outputs.