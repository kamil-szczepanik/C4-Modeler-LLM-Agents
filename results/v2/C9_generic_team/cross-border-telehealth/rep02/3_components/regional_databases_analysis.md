## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Regional Databases (GCP Managed Database in `europe-west3` and `us-central1`)
- Data Localization Router
- API Gateway and Offline Sync/Queue Container
- Asynchronous Task Worker
- Cloud KMS (Key Management Service)

## Relationships
- Data Localization Router -> Regional Databases: Persists localized data securely [TLS]
- API Gateway -> Regional Databases: Executes read/write operations with idempotency keys [HTTPS]
- Asynchronous Task Worker -> Regional Databases: Processes outbox events and handles retry queues [Internal RPC]

## Technology Stack
- GCP Managed Databases: Ensures strict regional data isolation for GDPR and HIPAA compliance.
- Cloud KMS: Provides database-level encryption-at-rest for PII and PHI protection.
- Transactional Outbox Pattern: Guarantees atomic writes and reliable event publishing during network partitions.
- Database-Level Audit Triggers: Generates tamper-resistant, immutable audit logs for regulatory accountability.

## Rationale
This architecture guarantees strict regional compliance by isolating data within `europe-west3` and `us-central1` using managed cloud services. It maintains high availability and data integrity for rural users through local idempotency, outbox patterns, and robust connection management.