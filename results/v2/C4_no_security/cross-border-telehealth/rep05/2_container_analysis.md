## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring high availability and regulatory compliance.

## Key Elements
* Patients & Clinicians (External Clients)
* External Pharmacies, Identity Providers, and National Health Systems
* API Gateway / BFF (Envoy / Cloud Endpoints)
* Video Consultation Service (MediaSoup WebRTC SFU)
* AI Symptom Checker Service (Python/FastAPI)
* Integration & Interoperability Service
* Consent & Identity Service (Keycloak)
* Regional Relational Database (Google Cloud SQL PostgreSQL)
* Regional Data Warehouse / ETL (BigQuery)

## Relationships
* Patients & Clinicians to API Gateway via HTTPS / WebSockets / WebRTC (UDP/TCP)
* API Gateway to Internal Containers via gRPC / REST
* Integration & Interoperability Service to External Pharmacies via regional standards and HL7 FHIR (REST)
* AI Symptom Checker to Immutable Regional Storage via TLS

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints (R-05)
* MediaSoup (WebRTC SFU): Delivers adaptive bitrate video consultations for unstable connections <300 kbit/s (R-06)
* Python / FastAPI: Powers the AI symptom checker with model version logging (R-07)
* Google Cloud SQL (PostgreSQL): Manages transactional healthcare records and granular consents (R-04)
* BigQuery: Processes anonymized regional analytics via ETL without violating privacy laws

## Rationale
Mirrored regional clusters in GCP completely isolate EU and US data to satisfy strict GDPR and HIPAA mandates. Decoupled microservices with adaptive WebRTC streaming and robust regional interoperability ensure reliable cross-border care under varying network conditions.