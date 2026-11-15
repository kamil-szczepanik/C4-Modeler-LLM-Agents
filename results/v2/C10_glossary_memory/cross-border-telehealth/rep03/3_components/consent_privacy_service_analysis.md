## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and robust low-bandwidth availability.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- EU/US Regional Pharmacies
- Regulatory Authorities / Notified Bodies (EU/US)
- Identity Providers (IDPs) (OAuth2/OIDC)
- Third-Party Video Infrastructure
- API Gateway / BFF (Node.js)
- Consultation & Prescriptions Service (Java/Spring Boot)
- E-Prescription Adapter (Node.js)
- AI Symptom Checker Service (Python/FastAPI)
- Consent & Privacy Service (Go)
- Regional Databases (Cloud SQL PostgreSQL)

## Relationships
- Patients (EU & US) -> API Gateway / BFF via HTTPS/TLS 1.3 and WebRTC
- Licensed Clinicians -> API Gateway / BFF via HTTPS/TLS 1.3 and WebRTC
- API Gateway / BFF -> Consultation & Prescriptions Service via gRPC over mTLS
- Consultation & Prescriptions Service -> E-Prescription Adapter via gRPC over mTLS
- E-Prescription Adapter -> EU/US Regional Pharmacies via HTTPS/REST (HL7 FHIR / EU national standards)
- API Gateway / BFF -> AI Symptom Checker Service via gRPC over mTLS
- API Gateway / BFF -> Consent & Privacy Service via gRPC over mTLS
- Cross-Border Telehealth Platform -> Identity Providers (IDPs) via OAuth2/OIDC
- Regulatory Authorities / Notified Bodies (EU/US) -> API Gateway / BFF via HTTPS/TLS 1.3 with mTLS and signed JWT

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for scalability and managed services.
- GCP Regions (`europe-west3`, `us-central1`): Enforces strict regional data residency requirements.
- Cloud SQL PostgreSQL: Partitioned regional databases ensuring local data isolation.
- gRPC over mTLS: High-performance, secure internal service-to-service communication.
- Node.js, Java (Spring Boot), Python (FastAPI), Go: Polyglot container runtimes optimized for specific domain requirements.

## Rationale
The architecture segregates regional data into dedicated GCP locations to strictly satisfy GDPR and HIPAA compliance mandates. Polyglot microservices combined with gRPC over mTLS provide secure, low-latency interoperability while supporting resilient degraded-mode video consultations.