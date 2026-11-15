## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It guarantees strict regional data residency, regulatory compliance (GDPR/HIPAA/MDR), and high availability for low-bandwidth rural connections.

## Key Elements
- Patients (EU & US) [person, context]
- Licensed Clinicians [person, context]
- EU/US Regional Pharmacies [externalSystem, context]
- Regulatory Authorities / Notified Bodies (EU/US) [externalSystem, context]
- Identity Providers (IDPs) [externalSystem, context]
- Third-Party Video Infrastructure [externalSystem, context]
- API Gateway / BFF [container, container] (Node.js)
  - Ingress Router & Geo-Routing Middleware (Node.js/Express)
  - Consent Enforcement Proxy (Node.js)
  - BFF Aggregator & Payload Optimizer (Node.js)
- Consultation & Prescriptions Service [container, container] (Java/Spring Boot)
- E-Prescription Adapter [container, container] (Node.js)
- AI Symptom Checker Service [container, container] (Python/FastAPI)
- Consent & Privacy Service [container, container] (Go)
- Regional Databases [container, container] (Cloud SQL PostgreSQL)

## Relationships
- Patients (EU & US) -> API Gateway / BFF: Accesses services via HTTPS/TLS 1.3 and WebRTC
- Licensed Clinicians -> API Gateway / BFF: Conducts sessions via HTTPS/TLS 1.3 and WebRTC
- API Gateway / BFF -> Consent & Privacy Service: Verifies consent via gRPC over mTLS
- API Gateway / BFF -> Consultation & Prescriptions Service: Routes requests via gRPC over mTLS
- API Gateway / BFF -> AI Symptom Checker Service: Requests analysis via gRPC over mTLS
- E-Prescription Adapter -> EU/US Regional Pharmacies: Sends prescriptions via HTTPS/REST (HL7 FHIR / EU standards)
- Cross-Border Telehealth Platform -> Identity Providers (IDPs): Authenticates via OAuth2/OIDC
- Regulatory Authorities -> API Gateway / BFF: Audits via HTTPS/TLS 1.3 with mTLS and signed JWT

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for strict data residency.
- Node.js & Express: Powers the API Gateway / BFF, Ingress Router, and E-Prescription Adapter for high-throughput asynchronous processing.
- Java & Spring Boot: Powers the Consultation & Prescriptions Service for enterprise reliability.
- Python & FastAPI: Powers the AI Symptom Checker Service for rapid machine learning integration.
- Go: Powers the Consent & Privacy Service for high-performance memory safety.
- Cloud SQL PostgreSQL: Provides strictly partitioned regional relational databases.
- Google Cloud Load Balancing & Cloud Armor: Secures edge ingress, applies rate limiting, and enforces geo-routing.
- gRPC over mTLS: Secures internal microservice communication.

## Rationale
This architecture uses regional GCP isolation (`europe-west3` and `us-central1`) combined with Cloud SQL PostgreSQL to strictly enforce GDPR and HIPAA data residency mandates. Edge-based consent enforcement and gRPC/mTLS microservices ensure high security, traceability, and low-bandwidth resilience (<300 kbit/s) for rural patients.