## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces strict regional data residency, regulatory compliance, and auditability across borders.

## Key Elements
- EU Clinical Database (`europe-west3`): Cloud SQL for PostgreSQL storing EU patient records and logs.
- US Clinical Database (`us-central1`): Cloud SQL for PostgreSQL storing US patient records.
- Blob Storage (`europe-west3` & `us-central1`): Cloud Storage buckets with regional locking.
- Core Telehealth Backend: Node.js / Go microservices.
- AI Symptom Checker: Containerized AI service.
- Consent Management Container: Service managing purpose-based patient consent.
- DevOps Tooling: Cloud KMS, PgBouncer, Terraform, Cloud Logging.

## Relationships
- Core Telehealth Backend -> EU/US Clinical Databases: Reads/writes health data via TLS 1.3 [PostgreSQL protocol via internal VPC].
- AI Symptom Checker -> Clinical Databases: Appends traceability logs [PostgreSQL protocol].
- Consent Management Container -> Clinical Databases: Executes consent mutations [PostgreSQL protocol].

## Technology Stack
- Cloud SQL for PostgreSQL: Provides managed relational storage with regional isolation.
- Cloud Storage: Delivers regional blob storage for unstructured assets.
- Cloud KMS: Manages region-specific cryptographic keys for data erasure.
- PgBouncer: Handles connection pooling for high concurrency.
- Terraform: Automates infrastructure provisioning with strict isolation rules.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating EU and US data regionally. It balances the right-to-erasure with medical audit requirements via cryptographic shredding.