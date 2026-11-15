## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and resilience for low-bandwidth connections.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Kong API Gateway / BFF
- Spring Boot Core Telehealth Service (Java, Spring Boot)
- FastAPI AI Symptom Checker & Node.js E-Prescription Service
- Java Consent Management Service
- GCP Cloud SQL (PostgreSQL), GCP Cloud Storage, & GCP Cloud Pub/Sub
- GCP Cloud KMS & Secret Manager

## Relationships
- Kong API Gateway -> Spring Boot Core Telehealth Service: Routes telehealth requests securely via gRPC / Anthos Service Mesh (mTLS)
- Spring Boot Core Telehealth Service -> GCP Cloud SQL: Persists relational health data using PostgreSQL Protocol with CMEK
- Spring Boot Core Telehealth Service -> GCP Cloud Storage: Stores clinical documents via HTTPS / GCP API with CMEK
- Spring Boot Core Telehealth Service -> GCP Cloud Pub/Sub: Publishes telemetry and events via GCP Pub/Sub API with payload encryption

## Technology Stack
- Java & Spring Boot: Chosen for robust enterprise workflows, dependency injection, and security integrations
- GCP (europe-west3, us-central1): Ensures localized data residency for EU and US compliance
- GCP Cloud KMS & Secret Manager: Secures PHI encryption and dynamic credential retrieval
- Spring Security & OAuth2: Enforces token-based authentication and role-based access control

## Rationale
This architecture guarantees strict regional data isolation to meet GDPR and HIPAA mandates while supporting secure, real-time telehealth workflows. The resilience engine and container hardening ensure continuous availability for rural patients and robust security against emerging threats.