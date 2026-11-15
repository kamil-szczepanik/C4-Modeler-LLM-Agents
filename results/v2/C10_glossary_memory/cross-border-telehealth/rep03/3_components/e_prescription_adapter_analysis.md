## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability across diverse networks.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- EU/US Regional Pharmacies
- Regulatory Authorities / Notified Bodies (EU/US)
- Identity Providers (IDPs)
- Third-Party Video Infrastructure
- API Gateway / BFF (Node.js)
- Consultation & Prescriptions Service (Java/Spring Boot)
- E-Prescription Adapter (Node.js)
- AI Symptom Checker Service (Python/FastAPI)
- Consent & Privacy Service (Go)
- Regional Databases (Cloud SQL PostgreSQL)

## Relationships
- Patients (EU & US) -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
- Licensed Clinicians -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
- API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over mTLS)
- Consultation & Prescriptions Service -> E-Prescription Adapter (gRPC over mTLS)
- E-Prescription Adapter -> EU/US Regional Pharmacies (HTTPS/REST with national EU standards and US HL7 FHIR)
- API Gateway / BFF -> AI Symptom Checker Service (gRPC over mTLS)
- API Gateway / BFF -> Consent & Privacy Service (gRPC over mTLS)
- Cross-Border Telehealth Platform -> Identity Providers (IDPs) (OAuth2/OIDC)
- Regulatory Authorities / Notified Bodies (EU/US) -> API Gateway / BFF (HTTPS / TLS 1.3 with mTLS and signed JWT)

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing europe-west3 and us-central1 regions for regional isolation.
- Node.js & Express: Powers the API Gateway/BFF and E-Prescription Adapter containers.
- Java & Spring Boot: Powers the Consultation & Prescriptions Service for enterprise reliability.
- Python & FastAPI: Powers the AI Symptom Checker Service for rapid machine learning integration.
- Go: Powers the Consent & Privacy Service for high-performance consent validation.
- Cloud SQL PostgreSQL: Stores regional data securely with strict residency and row-level security.
- gRPC over mTLS: Secures internal service-to-service communication.

## Rationale
This architecture guarantees strict regional data residency by partitioning services and databases across GCP regions to comply with GDPR and HIPAA. Furthermore, decoupled microservices and gRPC communication ensure resilience, traceability, and low-bandwidth adaptability for rural users.