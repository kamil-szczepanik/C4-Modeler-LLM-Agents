## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare clinics. It uses a hybrid cloud architecture to ensure high availability and HIPAA/GDPR compliance.

## Key Elements
- PostgreSQL 16 Engine: Core relational database with RLS and `pgaudit`.
- PgBouncer Sidecar: Connection pooler for throughput optimization.
- WAL-G Sidecar: Backup manager for object storage archiving.
- CloudNativePG Operator: Kubernetes controller for replication and failover.

## Relationships
- EMR & Patient Service -> PostgreSQL: Queries and updates clinical data via TCP with TLS 1.3
- Billing & Claims Service -> PostgreSQL: Reads/writes billing data via TCP with TLS 1.3
- PostgreSQL -> S3-compatible Object Storage: Streams encrypted WAL logs for backups via HTTPS

## Technology Stack
- PostgreSQL 16: Selected for robust relational integrity and extensions.
- CloudNativePG: Chosen for automated Kubernetes failover and active-active/standby management.
- PgBouncer: Utilized to prevent thread exhaustion and maintain sub-second response times.
- WAL-G: Deployed for efficient object storage archiving supporting 10-year retention.

## Rationale
This architecture guarantees 99.99% availability and HIPAA compliance using resilient Kubernetes-native replication. It meets sub-second P95 performance targets by isolating workloads through read replicas and connection pooling.