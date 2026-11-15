## Overview
The Data Storage Layer provides secure, highly available, and compliant persistent storage for structured transactional data and unstructured clinical records within the Clinic Management System. It guarantees strict HIPAA/GDPR compliance, a 10-year data retention mandate, and 99.99% system availability.

## Key Elements
- Relational Database Engine (PostgreSQL 15+ with Citus/Patroni)
- Object Storage Repository (MinIO on-prem / AWS S3 in eu-central-1)
- Database Audit & Encryption Proxy (HashiCorp Vault and PgAudit)
- Connection Pooling & Load Balancing (PgBouncer)
- Backup and Disaster Recovery (Velero and automated WAL archiving)

## Relationships
- EMR Core Service -> Relational Database Engine [TLS/SQL with RLS, TCP 5432]
- Billing Service -> Relational Database Engine [TLS/SQL with RLS, TCP 5432]
- EMR Core Service -> Object Storage Repository [HTTPS/S3 API, TLS 1.3]
- Relational Database Engine -> Object Storage Repository [Continuous WAL archiving, HTTPS]

## Technology Stack
- PostgreSQL 15+: Provides relational storage with Citus/Patroni for active-active high availability and Row-Level Security (RLS).
- MinIO / AWS S3: Supplies object storage with WORM policies and S3 Object Lock in Compliance mode for 10-year retention.
- HashiCorp Vault / AWS KMS: Manages envelope encryption keys and automatic 90-day key rotation.
- PgBouncer: Separates read-only queries from transactional writes to meet P95 performance targets.
- Velero: Executes Kubernetes-native continuous snapshotting of persistent volumes.

## Rationale
This architecture guarantees an RPO near zero and RTO under 15 minutes through synchronous replication and automated failover. Strict encryption, audit trails, and immutable storage policies satisfy healthcare regulations without disrupting clinical workflows.