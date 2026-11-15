## Overview
The Data Tier provides region-isolated, secure, and compliant storage infrastructure for the Cross-Border Telehealth Platform. It ensures strict data residency, auditability for AI diagnostics, and consent-driven access control across the EU and US regions.

## Key Elements
- **Region-Isolated PostgreSQL Instances**: Independent `Cloud SQL PostgreSQL` clusters in `europe-west3` and `us-central1`
- **Encrypted Object Store**: `Cloud Storage` buckets for media and AI artifacts
- **Key Management Service**: `Cloud KMS` for regional Customer-Managed Encryption Keys (CMEK)
- **Audit Ledger Subsystem**: Append-only PostgreSQL tables with cryptographic hashing
- **Connection Management**: PgBouncer sidecars for connection pooling

## Relationships
- **Core Telehealth Backend -> Data Tier**: Reads and writes clinical data, consent preferences, and sync queues via `TCP/PostgreSQL via mTLS`
- **Data Tier -> Cloud KMS**: Requests regional encryption keys and dynamic IAM authentication via `HTTPS/REST`

## Technology Stack
- **Cloud SQL PostgreSQL**: Provides region-isolated relational storage with Row-Level Security (RLS) for consent enforcement
- **Cloud KMS**: Enforces region-locked encryption to guarantee GDPR and HIPAA compliance
- **PgBouncer**: Manages intermittent rural reconnection spikes and prevents database exhaustion
- **Cloud Deploy**: Automates region-aware, backward-compatible schema migrations

## Rationale
This architecture guarantees strict regional data isolation to satisfy GDPR and HIPAA mandates while supporting rural offline sync capabilities. Furthermore, cryptographic audit logging ensures full traceability for EU MDR compliance.