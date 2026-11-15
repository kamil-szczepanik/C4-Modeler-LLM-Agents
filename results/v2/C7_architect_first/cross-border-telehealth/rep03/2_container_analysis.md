## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data isolation to comply with GDPR and HIPAA requirements.

## Key Elements
- Patients and Clinicians (Users)
- Web & Mobile Frontend Applications (Flutter/React)
- API Gateway (Envoy / Google Cloud API Gateway)
- Consultation Service with WebRTC SFU (Go)
- AI Symptom Checker Service (Python/FastAPI)
- E-Prescription & Interoperability Service (Node.js/Java)
- Data Storage Layer (Cloud SQL PostgreSQL + Cloud Storage)
- External Pharmacies and Identity Providers

## Relationships
- Patients/Clinicians to API Gateway via HTTPS (REST/JSON) and WSS (WebSockets)
- API Gateway to Microservices via gRPC over mTLS
- Microservices to Data Storage via SSL-enforced TCP/Postgres
- E-Prescription Service to External Pharmacies via HL7 FHIR (US) and national standards (EU)

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for regional data residency
- Cloud Service Mesh & SPIFFE/SPIRE: Enforces secure internal mTLS communication
- Cloud KMS / Cloud HSM: Provides regional CMEK and digital signing for non-repudiation
- OpenTelemetry: Handles distributed tracing with edge PII/PHI scrubbing

## Rationale
Isolating containers and datastores within regional GCP zones guarantees compliance with GDPR and HIPAA data residency mandates. Using gRPC over mTLS and WebRTC SFU ensures secure, low-latency, and resilient communication for unstable rural networks.