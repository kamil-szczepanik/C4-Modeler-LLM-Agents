## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to deliver secure, highly available clinical workflows while maintaining strict compliance with healthcare regulations.

## Key Elements
- PostgreSQL Primary/Active-Active Nodes (Citus/Postgres-BDR)
- PgBouncer Connection Pooler
- Audit Trail Manager
- Backup & Archival Agent
- Logical Replication Manager
- Distributed Lock Manager (etcd/Redlock)
- Data Encryption & Key Handler
- Failover & Health Monitor (Patroni)
- Query Optimizer & Index Manager

## Relationships
- Core Services Container & EMR Service -> PgBouncer: Connection pooling [PostgreSQL wire protocol over TLS]
- PgBouncer -> Query Optimizer & Index Manager: Routes queries [PostgreSQL wire protocol]
- Query Optimizer & Index Manager -> PostgreSQL Primary/Active-Active Nodes: Executes query plans [Internal IPC]
- Data Encryption & Key Handler -> Key Management Service (HashiCorp Vault/AWS KMS): Fetches keys [HTTPS/REST with mTLS]
- Backup & Archival Agent -> Cloud Backup (AWS S3 Glacier): Streams WAL logs [HTTPS/TLS 1.3]
- Database Layer -> Observability & Monitoring Collector (OpenTelemetry/Prometheus): Exports telemetry [gRPC/OTLP over TLS]
- PostgreSQL Nodes <-> Logical Replication Manager: Cross-region sync [Encrypted replication protocol]

## Technology Stack
- PostgreSQL: Distributed multi-master relational storage for scalability
- Patroni: Automated leader election and failover to ensure 99.99% uptime
- PgBouncer: Connection pooling to support sub-second P95 performance
- HashiCorp Vault / AWS KMS: Envelope encryption for AES-256 data at rest
- AWS S3 Glacier: Long-term secure storage for 10-year data retention compliance
- Apache Citus / Postgres-BDR: Multi-master replication across hybrid regions

## Rationale
This architecture uses active-active multi-master replication and automated failover to achieve 99.99% availability across on-premise and AWS environments. Dedicated encryption handlers, audit trails, and connection pooling ensure strict HIPAA/GDPR compliance while meeting sub-second EMR performance requirements.