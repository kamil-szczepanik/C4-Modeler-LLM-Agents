## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency, HIPAA/GDPR compliance, and low-bandwidth availability.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- API Gateway / BFF (Node.js)
- Consultation & Prescriptions Service (Java/Spring Boot)
- E-Prescription Adapter (Node.js)
- AI Symptom Checker Service (Python/FastAPI)
- Consent & Privacy Service (Go)
- Regional Databases (Cloud SQL PostgreSQL)
- Third-Party Video Infrastructure & Identity Providers (IDPs)

## Relationships
- Patients/Clinicians -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
- API Gateway / BFF -> AI Symptom Checker Service (gRPC over mTLS)
- AI Symptom Checker Service -> Consent & Privacy Service (gRPC over mTLS)
- E-Prescription Adapter -> EU/US Regional Pharmacies (HTTPS/REST)
- AI Symptom Checker Service -> Regional Databases (PostgreSQL over mTLS)

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance.
- Google Kubernetes Engine (GKE): Hosts regional container workloads.
- Python/FastAPI & PyTorch: Powers the AI Symptom Checker Service and inference engine.
- gRPC over mTLS: Secures internal service-to-service communication.
- Cloud SQL PostgreSQL: Stores partitioned regional data.

## Rationale
Partitioning data across GCP regions guarantees compliance with GDPR and HIPAA mandates. Using gRPC over mTLS and asynchronous processing secures internal communications and maintains high availability during peak loads.