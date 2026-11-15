## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, regulatory compliance, and low-bandwidth availability.]

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- EU/US Regional Pharmacies
- Regulatory Authorities / Notified Bodies (EU/US)
- Identity Providers (IDPs)
- Third-Party Video Infrastructure
- API Gateway / BFF
- Consultation & Prescriptions Service (Java/Spring Boot)
- E-Prescription Adapter
- AI Symptom Checker Service
- Consent & Privacy Service
- Regional Databases (Cloud SQL PostgreSQL)
- Consultation Session Manager
- Prescription Domain Controller
- Cloud Memorystore (Redis)

## Relationships
- Patients (EU & US) -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
- Licensed Clinicians -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
- API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over mTLS)
- Consultation Session Manager -> Third-Party Video Infrastructure (HTTPS/WebSocket over TLS 1.3)
- Prescription Domain Controller -> Regional Databases (JDBC over mTLS)
- Consultation & Prescriptions Service -> Consent & Privacy Service (gRPC over mTLS)
- Consultation Session Manager -> Regional Databases (Redis Protocol over mTLS)
- E-Prescription Adapter -> EU/US Regional Pharmacies (HTTPS/REST with national EU standards and US HL7 FHIR)

## Technology Stack
- Java/Spring Boot: Core backend implementation for Consultation & Prescriptions Service.
- GCP Cloud SQL PostgreSQL: Regionally partitioned relational storage for strict data residency.
- GCP Cloud Memorystore (Redis): Ephemeral caching for session states and prescription drafts.
- Google Kubernetes Engine (GKE): Container orchestration with strict regional node anti-affinity.
- WebRTC: Adaptive bitrate video streaming for low-bandwidth rural connections.
- gRPC over mTLS: Secure internal communication protocol between microservices.
- GCP Cloud KMS: Column-level database encryption and CMEK for cached PHI.

## Rationale
[Strict regional partitioning on Google Cloud Platform guarantees compliance with GDPR and HIPAA data residency mandates. Microservice decomposition and ephemeral Redis caching ensure resilient, low-bandwidth session management for rural users without compromising security.]