## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, compliance, and interoperability across regional deployments.

## Key Elements
- Regional Database Instances: Cloud SQL PostgreSQL 15 deployed in `europe-west3` and `us-central1`.
- Encrypted Blob Storage: Google Cloud Storage regional buckets with CMEK via Cloud KMS.
- Audit & Compliance Ledger: PostgreSQL extensions, triggers, and Row-Level Security (RLS).
- Backup & Retention Manager: Cloud Storage Lifecycle Rules with object locks.
- Database Migration Manager: Flyway/Go schema migration component.

## Relationships
- Core Telehealth Service, US FHIR Adapter, and EU E-Prescription Gateway -> Regional Database Instances: Persist and retrieve regional data [PostgreSQL wire protocol / TLS 1.3].
- Core Telehealth Service -> Audit & Compliance Ledger: Write immutable symptom-checker logs and consent states [SQL / TLS 1.3].
- Cloud SQL -> Encrypted Blob Storage: Reference secure object URIs for media and prescriptions [Internal GCP API].

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`.
- Cloud SQL PostgreSQL 15: Primary relational database ensuring physical data residency.
- Google Cloud Storage & Cloud KMS: Secure object storage using Customer-Managed Encryption Keys.
- Flyway / Go: Database migration and schema management.

## Rationale
This architecture enforces GDPR and HIPAA compliance by physically separating regional data without default cross-region replication. It guarantees traceability for medical AI outputs and patient consent via immutable ledger patterns and regional CMEK encryption.