## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. Its architecture enforces strict regional data isolation to comply with GDPR and HIPAA mandates.

## Key Elements
- PostgreSQL Databases (Region-isolated instances in `europe-west3` and `us-central1`)
- Cloud SQL for PostgreSQL (Relational storage engine)
- Cloud SQL Auth Proxy (Sidecar proxy for secure connections)
- PgBouncer (Connection pooler)
- Core Telehealth Service
- AI Inference Service
- Schemas (`core_domain`, `consent_ledger`, `ai_audit`)

## Relationships
- Core Telehealth Service -> PostgreSQL Databases: Persists and retrieves patient and consultation data via TCP port 5432 using TLS 1.3 and Cloud SQL Auth Proxy
- AI Inference Service -> PostgreSQL Databases: Stores symptom checker inputs, outputs, and model versions via TCP port 5432 using TLS 1.3 and Cloud SQL Auth Proxy

## Technology Stack
- Cloud SQL for PostgreSQL: Managed relational database ensuring enterprise availability and point-in-time recovery
- Cloud SQL Auth Proxy & mTLS: Secures database transport without static passwords
- PostgreSQL `pgaudit`: Provides comprehensive audit logging for GDPR and HIPAA compliance
- GCP Cloud KMS: Supplies Customer-Managed Encryption Keys (CMEK) for data-at-rest encryption

## Rationale
Region-isolated database instances guarantee that EU health data remains in `europe-west3` and US data in `us-central1`. Immutable schemas and strict IAM controls fulfill regional privacy regulations and AI traceability mandates.