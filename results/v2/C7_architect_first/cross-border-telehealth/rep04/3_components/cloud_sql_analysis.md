## Overview
This architecture summary defines the Cloud SQL database component for a cross-border telehealth platform serving EU and US patients. Its core purpose is providing regionally isolated, secure, and compliant data storage for video consultations, e-prescriptions, and AI symptom checker logs.

## Key Elements
- PostgreSQL Database Engine (PostgreSQL 15)
- Row-Level Security (RLS) Policy Enforcer
- Audit Logging Extension (pgAudit)
- Consent Indexing & Verification Engine
- PgBouncer Connection Pooler

## Relationships
- Core Telehealth Backend -> PostgreSQL Database Engine: Executes SQL queries over TLS using the `pg` Node.js driver [TCP/PostgreSQL Protocol via mTLS]
- Core Telehealth Backend -> Consent Indexing & Verification Engine: Validates patient data-sharing scope before transactional writes [TCP/PostgreSQL Protocol]
- PostgreSQL Database Engine -> pgAudit: Intercepts and logs transactional events to Cloud Logging [Internal IPC]
- PostgreSQL Database Engine -> Cloud KMS: Encrypts data-at-rest using regional Customer-Managed Encryption Keys [Google Cloud API]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for strict physical data residency.
- Cloud SQL (PostgreSQL 15): Managed relational database service configured with physically isolated instances per region to satisfy GDPR and HIPAA.
- Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) with distinct regional keys to secure data at rest.
- PgBouncer: Connection pooling service at container ingress to manage rural internet reconnection surges.

## Rationale
This architecture ensures strict regulatory compliance through physical data segregation and regional CMEK encryption. Additionally, it guarantees high availability and low-latency performance for users with unstable internet connections.