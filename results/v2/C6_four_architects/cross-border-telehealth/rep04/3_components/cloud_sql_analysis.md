## Overview
- Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US.
- Engineered for strict regulatory compliance, region-locked data residency, and high availability in low-bandwidth environments.

## Key Elements
- Region-Specific Database Instances (Cloud SQL EU in `europe-west3`, Cloud SQL US in `us-central1`)
- Database Connection Pooler (PgBouncer)
- Row-Level Security (RLS) Engine
- Audit Logging & Encryption Module (`pgAudit` + Cloud KMS CMEK)
- FHIR Storage Schemas (JSONB tables)
- Partitioned Consent & Audit Tables
- Read Replicas (Regional)
- Schema Migration & Versioning Engine (Flyway/Liquibase)
- Database Backup & Point-in-Time Recovery (PITR) Agent
- Automated Data Purging Daemon (`pg_cron`)
- In-Database Cryptographic Erasure Engine (`pgcrypto`)
- Database Telemetry & Metrics Exporter

## Relationships
- Core Telehealth, Video Consultation, AI Symptom Checker, Consent Management, and E-Prescription services -> Region-Specific Database Instances & Read Replicas [PostgreSQL Wire Protocol with TLS 1.3]
- Audit & Compliance Logging Service -> Audit Logging & Encryption Module [PostgreSQL Wire Protocol with TLS 1.3]
- E-Prescription & Interoperability Gateway -> FHIR Storage Schemas [PostgreSQL Wire Protocol with TLS 1.3]
- Cloud SQL Instance -> Cloud Storage Regional Bucket [GCP Internal APIs with TLS 1.3]
- Google Cloud Monitoring -> Database Telemetry & Metrics Exporter [HTTPS / Prometheus Scrape Protocol with TLS 1.3]

## Technology Stack
- Google Cloud SQL for PostgreSQL: Managed relational storage ensuring robust multi-region isolation.
- PgBouncer: Sidecar connection pooling for efficient handling of stateless microservices.
- PostgreSQL Extensions (`pgAudit`, `pg_cron`, `pgcrypto`): Built-in tools for immutable auditing, automated purging, and cryptographic erasure.
- Cloud KMS: Customer-managed encryption keys enforcing strict data-at-rest compliance per region.

## Rationale
- Multi-instance regional partitioning guarantees that EU health data remains in `europe-west3` and US data in `us-central1` to satisfy GDPR and HIPAA.
- Native database extensions and partitioning ensure strict accountability, high availability, and automated compliance management without external data leakage.