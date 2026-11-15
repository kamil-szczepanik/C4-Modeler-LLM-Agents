## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability and regulatory compliance.

## Key Elements
- Patients (Mobile/Web App users) and Licensed Clinicians (Portal users)
- Regional Cloud SQL PostgreSQL Databases (`europe-west3`, `us-central1`)
- Core Telehealth Schema, Consent & Audit Schema, FHIR Interoperability Schema
- PgBouncer Connection Poolers
- GCP GKE Regional Clusters

## Relationships
- Core Telehealth Service -> Core Telehealth Schema: SQL over TLS 1.3 with IAM authentication and PgBouncer
- Consent & Profile Management Service -> Consent & Audit Schema: SQL over TLS 1.3 with least-privilege accounts
- Pharmacy Integration Gateway -> FHIR Interoperability Schema: SQL over TLS 1.3 using dedicated credentials

## Technology Stack
- Cloud SQL PostgreSQL 15: Regional databases ensuring GDPR and HIPAA compliance
- JSONB: Optimized data types for indexing US FHIR resources
- PgBouncer: Connection pooling to handle telehealth traffic spikes
- Terraform: Automated infrastructure deployment with point-in-time recovery
- GCP Cloud Monitoring: Performance tracking, slow query logging, and alerting

## Rationale
Regional database isolation guarantees that EU and US patient data strictly remain within their respective compliance jurisdictions. Schema segregation, connection pooling, and high-availability configurations ensure sub-second query performance and uninterrupted telehealth services during peak loads.