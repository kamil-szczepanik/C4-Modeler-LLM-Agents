## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, HIPAA and GDPR compliance, and seamless operation for users with unstable internet connections.

## Key Elements
- Patients (EU & US) [person, context]
- Licensed Clinicians [person, context]
- EU/US Regional Pharmacies [externalSystem, context]
- Regulatory Authorities / Notified Bodies (EU/US) [externalSystem, context]
- Identity Providers (IDPs) [externalSystem, context] (OAuth2/OIDC)
- Third-Party Video Infrastructure [externalSystem, context]
- API Gateway / BFF [container, container] (Node.js)
- Consultation & Prescriptions Service [container, container] (Java/Spring Boot)
- E-Prescription Adapter [container, container] (Node.js)
- AI Symptom Checker Service [container, container] (Python/FastAPI)
- Consent & Privacy Service [container, container] (Go)
- Regional Databases [container, container] (Cloud SQL PostgreSQL)
- Data Partition Manager [component, container] (PostgreSQL Partitioning)
- Audit Logging Store [component, container] (PostgreSQL Append-Only Tables / pgAudit)
- Consent Indexer [component, container] (PostgreSQL B-Tree/GIN Indexes)
- Patient Data Archival & Purge Manager [component, container] (PostgreSQL Partition Dropping / Retention Jobs)

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
- Backend Services -> Regional Databases (TCP/IP via PostgreSQL wire protocol over mTLS)

## Technology Stack
- GCP (regions: europe-west3, us-central1): Chosen for robust multi-region infrastructure and strict regional isolation compliance.
- Cloud SQL PostgreSQL: Selected for relational data storage with native regional partitioning and security controls.
- Node.js & Java/Spring Boot & Python/FastAPI & Go: Microservice runtimes matched to domain-specific workloads (API/adapters, core business logic, AI, consent management).
- WebRTC & gRPC over mTLS: Used for low-latency video streaming and secure internal microservice communication.
- Cloud KMS with CMEK & pgAudit: Enforces regional encryption-at-rest and immutable database audit logging for regulatory compliance.

## Rationale
This architecture enforces absolute data residency by strictly isolating EU data in `europe-west3` and US data in `us-central1` using regional Cloud SQL instances. Microservices communicate securely via gRPC over mTLS while supporting low-bandwidth video adaptations and comprehensive audit traceability for medical device compliance.