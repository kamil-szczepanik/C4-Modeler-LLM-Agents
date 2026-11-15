## Overview
This system is a cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Its core purpose is delivering secure, compliant telemedicine while strictly enforcing regional data residency and granular patient consent.

## Key Elements
- Patients and Clinicians (Users)
- External Pharmacies, Identity Providers (IdP), National Health/Insurance Systems, Regulatory Authorities (External Systems)
- API Gateway / BFF (Envoy / Cloud Endpoints)
- Auth Component (Keycloak)
- Consent Enforcement Component (Java / Spring Boot)
- Audit & Transparency Component (Java / Spring Boot)
- Video Consultation Service (MediaSoup WebRTC SFU)
- AI Symptom Checker Service (Python / FastAPI)
- Integration & Interoperability Service (REST, HL7 FHIR)
- Regional Relational Database (Google Cloud SQL PostgreSQL)
- Regional Data Warehouse / ETL (BigQuery)

## Relationships
- API Gateway -> Auth Component: Validates user identity and OIDC tokens [gRPC / REST]
- API Gateway -> Consent Enforcement Component: Evaluates real-time purpose-based access policies [gRPC]
- Consent Enforcement Component -> Regional Relational Database: Persists purpose-based consent ledgers [JDBC / TLS]
- Consent Enforcement Component -> Audit & Transparency Component: Emits asynchronous access events [Google Cloud Pub/Sub]
- Audit & Transparency Component -> Regional Data Warehouse: Persists long-term compliance audit trails [BigQuery / TLS]

## Technology Stack
- Google Cloud Platform (europe-west3, us-central1): Target cloud provider for region-locked deployments ensuring data residency.
- Keycloak: Handles OIDC/OAuth2 authentication and user federation.
- Java / Spring Boot: Powers custom microservices for consent enforcement and audit management.
- Google Cloud SQL PostgreSQL: Provides regional relational storage without cross-region replication.
- BigQuery: Stores long-term compliance audit and analytics data.
- Google Cloud Pub/Sub: Decouples synchronous consent checks from asynchronous audit logging.

## Rationale
This architecture enforces strict GDPR and HIPAA compliance by isolating EU and US health data within region-locked GCP deployments. Decoupling real-time consent checks from asynchronous auditing guarantees sub-50ms policy evaluation latencies for reliable telehealth sessions.