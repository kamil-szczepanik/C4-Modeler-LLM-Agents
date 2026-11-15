## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional compliance, high availability for rural users, and traceable AI outputs.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Compliance Authorities
- API Gateway (Cloud Run / Envoy)
- Core Telehealth Backend (Node.js / NestJS)
- AI Symptom Service (Python / FastAPI)
- Video Media Server (LiveKit / WebRTC)
- Interoperability Worker (Go)
- Cloud SQL (PostgreSQL), BigQuery, Cloud Pub/Sub with DLQs
- EU National E-Prescription Gateways, US Pharmacy Systems, OAuth2/OIDC Identity Providers

## Relationships
- Patients & Clinicians access the API Gateway via HTTPS/REST and WebRTC.
- API Gateway communicates with regional Core Telehealth Backend via gRPC over VPC.
- Core Backend stores data in regional Cloud SQL and validates consent (R-04).
- Video Media Server uses WebRTC to stream consultations, prioritizing audio under 300 kbit/s.
- AI Symptom Service logs inputs/outputs to BigQuery for EU MDR traceability (R-07).
- Interoperability Worker processes e-prescriptions (R-02) asynchronously via regional Cloud Pub/Sub to external national gateways.

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Enforces regional data residency (R-05).
- Node.js / NestJS & Python / FastAPI: Core business logic and AI processing.
- LiveKit / WebRTC: Low-bandwidth resilient video/audio consultations (R-06).
- Cloud SQL (PostgreSQL) & BigQuery: Regionalized data storage and compliance logging.
- Cloud Pub/Sub: Asynchronous messaging with Dead Letter Queues for robust e-prescription delivery.
- Istio / Cloud Service Mesh: mTLS encryption across all container communications.
- Cloud KMS & Secret Manager: CMEK data encryption and runtime secret retrieval.

## Rationale
This multi-region GCP architecture guarantees strict GDPR and HIPAA data separation while maintaining low-latency access for rural users. Asynchronous messaging and robust security controls ensure high availability and regulatory compliance for cross-border healthcare delivery.