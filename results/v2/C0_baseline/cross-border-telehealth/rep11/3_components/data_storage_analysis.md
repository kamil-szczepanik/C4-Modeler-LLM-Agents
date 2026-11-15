## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. Its core purpose is delivering compliant telemedicine services while enforcing strict regional data residency and patient consent controls.

## Key Elements
* Patients (EU and US) & Licensed Clinicians
* Web & Mobile App (React / Flutter)
* API Gateway (Cloud Endpoints / Envoy)
* Core Services Container (Spring Boot / Java)
* AI Symptom Checker Container (Python / FastAPI / PyTorch / MLflow)
* Data Storage Container components: Relational Database Instance (Cloud SQL PostgreSQL), Object Storage Bucket (Google Cloud Storage), Key Management Service (Cloud KMS / CMEK), Data Access Proxy (Envoy / PostgREST), Change Data Capture (Google Cloud Datastream)
* External Pharmacies, Regional Payment Gateways, Health Authorities & Auditors

## Relationships
* Core Services Container -> Data Access Proxy: Reads and writes transactional data via gRPC and JDBC over mTLS
* AI Symptom Checker Container -> Object Storage Bucket: Logs model artifacts and telemetry via gRPC and HTTPS
* Data Access Proxy -> Relational Database Instance: Evaluates patient consent and executes queries via PostgreSQL row-level security
* Change Data Capture -> Google Cloud Pub/Sub: Publishes transactional deltas for offline delta-sync payloads

## Technology Stack
* Google Cloud Platform (regions: `europe-west3`, `us-central1`): Enforces regional data residency constraints
* Cloud SQL PostgreSQL & Google Cloud Storage: Persists structured healthcare data and unstructured audit logs
* Cloud KMS: Manages localized Customer-Managed Encryption Keys (CMEK) for cryptographic data isolation
* Envoy / PostgREST & Google Cloud Datastream: Powers the Data Access Proxy and enables low-bandwidth delta-sync

## Rationale
This architecture uses regional GCP isolation and VPC Service Controls to guarantee strict GDPR and HIPAA compliance. Decoupling data access through a proxy ensures robust consent enforcement and traceable AI outputs without sacrificing availability for rural users.