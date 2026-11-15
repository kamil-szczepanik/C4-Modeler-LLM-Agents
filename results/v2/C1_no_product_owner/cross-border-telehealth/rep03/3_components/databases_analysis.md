## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Ensures strict regional data residency, regulatory compliance, and high availability on GCP.

## Key Elements
- EU Patient Database (`Cloud SQL PostgreSQL - EU`)
- US Patient Database (`Cloud SQL PostgreSQL - US`)
- AI Audit Log Store (`Cloud Storage - Audit`)
- Shared Migration & Schema Manager (`Flyway`)
- Core Telehealth Service
- AI Symptom Checker Container
- GCP Cloud KMS

## Relationships
- Core Telehealth Service -> EU Patient Database [PostgreSQL Wire Protocol / TLS 1.3]
- Core Telehealth Service -> US Patient Database [PostgreSQL Wire Protocol / TLS 1.3]
- AI Symptom Checker Container -> AI Audit Log Store [Cloud Storage API / HTTPS]
- Shared Migration & Schema Manager -> EU/US Patient Databases [PostgreSQL Wire Protocol / TLS 1.3]

## Technology Stack
- PostgreSQL 15 on GCP Cloud SQL (`europe-west3`, `us-central1`): Regional structured data storage ensuring GDPR/HIPAA data residency.
- GCP Cloud Storage (`Audit`): Immutable bucket with Bucket Lock in compliance mode for MDR traceability.
- GCP Cloud KMS: Regional customer-managed encryption keys (CMEK) with enforced key rotation.
- Flyway: Version-controlled schema migrations executed via staggered regional Kubernetes jobs.

## Rationale
Segregating databases by region with strict IAM authentication, row-level security, and zero cross-region replication guarantees complete compliance with GDPR and HIPAA data residency constraints. Staggered, backward-compatible migrations and immutable audit logging ensure operational safety and regulatory traceability.