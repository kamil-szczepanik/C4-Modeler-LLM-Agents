## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, privacy, and regulatory compliance across regions.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Local Pharmacies, Regulatory Officers
- Flutter/React Native Web and Mobile Apps
- Kong API Gateway/BFF
- Spring Boot Core Telehealth Service
- FastAPI AI Symptom Checker
- Node.js E-Prescription Service
- Java Consent Management Service
- Node.js/Go Billing & Localization Container
- GCP Cloud SQL (PostgreSQL) instances (EU & US)
- GCP Cloud Storage, GCP Cloud Pub/Sub, Cloud KMS

## Relationships
- Spring Boot Core Telehealth Service -> GCP Cloud SQL (PostgreSQL): Reads/writes relational health data [PostgreSQL Protocol with CMEK, TLS 1.3]
- FastAPI AI Symptom Checker -> GCP Cloud SQL (PostgreSQL): Persists AI recommendations and inputs [PostgreSQL Protocol with TLS 1.3, CMEK]
- Node.js E-Prescription Service -> GCP Cloud SQL (PostgreSQL): Persists e-prescription audit trails [PostgreSQL Protocol with TLS 1.3, Cloud SQL IAM Auth]
- Java Consent Management Service -> GCP Cloud SQL (PostgreSQL): Stores consent records and audit metadata [PostgreSQL Protocol with CMEK]
- Node.js/Go Billing & Localization Container -> GCP Cloud SQL (PostgreSQL): Persists billing and regional configs [PostgreSQL Protocol with CMEK]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for regional isolation.
- PostgreSQL v15+ (GCP Cloud SQL): Relational database with High Availability and regional deployment.
- PgBouncer: Connection pooler for managing ephemeral microservice connections.
- Cloud KMS: Customer-Managed Encryption Keys (CMEK) for data-at-rest.
- Cloud SQL IAM Authentication & Workload Identity: Secure, passwordless database access control.
- PostgreSQL pgaudit Extension: Detailed logging of DDL/DML operations for PHI/PII compliance.

## Rationale
Independent regional Cloud SQL instances with zero cross-region replication strictly enforce GDPR and HIPAA data residency mandates. High Availability configurations, connection pooling, and CMEK encryption guarantee reliable sub-second query performance and robust security for sensitive healthcare workflows.