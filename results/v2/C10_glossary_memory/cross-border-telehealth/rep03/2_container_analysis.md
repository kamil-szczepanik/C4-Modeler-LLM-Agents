## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, regulatory compliance, and low-bandwidth availability.

## Key Elements
* Patients (EU & US) [person, context]
* Licensed Clinicians [person, context]
* EU/US Regional Pharmacies [externalSystem, context]
* Regulatory Authorities / Notified Bodies (EU/US) [externalSystem, context]
* Identity Providers (IDPs) [externalSystem, context] (OAuth2/OIDC)
* Third-Party Video Infrastructure [externalSystem, context]
* API Gateway / BFF [container, Node.js]
* Consultation & Prescriptions Service [container, Java/Spring Boot]
* E-Prescription Adapter [container, Node.js]
* AI Symptom Checker Service [container, Python/FastAPI]
* Consent & Privacy Service [container, Go]
* Regional Databases [container, Cloud SQL PostgreSQL]

## Relationships
* Patients (EU & US) -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
* Licensed Clinicians -> API Gateway / BFF (HTTPS/TLS 1.3 and WebRTC)
* API Gateway / BFF -> Consultation & Prescriptions Service (gRPC over mTLS)
* Consultation & Prescriptions Service -> E-Prescription Adapter (gRPC over mTLS)
* E-Prescription Adapter -> EU/US Regional Pharmacies (HTTPS/REST with national EU standards and US HL7 FHIR)
* API Gateway / BFF -> AI Symptom Checker Service (gRPC over mTLS)
* API Gateway / BFF -> Consent & Privacy Service (gRPC over mTLS)
* Cross-Border Telehealth Platform -> Identity Providers (IDPs) (OAuth2/OIDC)
* Regulatory Authorities / Notified Bodies (EU/US) -> API Gateway / BFF (HTTPS / TLS 1.3 with mTLS and signed JWT)

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider utilizing regions `europe-west3` and `us-central1` for strict data residency.
* Google Kubernetes Engine (GKE): Isolated regional container clusters for workload deployment.
* Anthos Service Mesh (Istio): Enforces zero-trust networking, mTLS (TLS 1.3), and service-to-service authorization.
* Cloud SQL (PostgreSQL): Provides strictly partitioned regional relational databases for data residency compliance.
* Google Cloud KMS & Secret Manager: Secures data-at-rest with regional Customer-Managed Encryption Keys (CMEK) and manages runtime secrets.

## Rationale
Isolated regional GKE clusters and partitioned Cloud SQL instances guarantee that EU health data remains in `europe-west3` and US data in `us-central1`, satisfying GDPR and HIPAA constraints. The decoupled E-Prescription Adapter and dedicated Consent & Privacy Service ensure robust regional interoperability, clinical workflow continuity, and strict auditability for EU MDR compliance.