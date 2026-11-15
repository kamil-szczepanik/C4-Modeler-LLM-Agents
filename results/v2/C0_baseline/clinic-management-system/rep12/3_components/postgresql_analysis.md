## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers.]
[It provides high availability, stringent compliance, and low-latency clinical data access.]

## Key Elements
- PostgreSQL Primary Instance (`PostgreSQL 16`)
- PostgreSQL Read-Replica Cluster (`PostgreSQL 16`)
- Connection Pooler (`PgBouncer`)
- Backup Daemon (`pgBackRest`)
- HA Orchestration (`Patroni` with `etcd`)
- Audit & Monitoring (`pgaudit`, `postgres_exporter`)

## Relationships
- Spring Boot Core Services -> Connection Pooler: Writes transactional data [JDBC/TLS 1.3]
- Apache Superset -> PostgreSQL Read-Replica Cluster: Queries analytics data [JDBC/TLS 1.3]
- PostgreSQL Primary Instance -> PostgreSQL Read-Replica Cluster: Streams WAL replication [TCP/mTLS]
- PostgreSQL -> Go Audit Logging Container: Sends audit events [pgaudit/Async]

## Technology Stack
- PostgreSQL 16: ACID compliance, RLS, and Row-Level Security for multi-tenant data isolation.
- PgBouncer: Connection pooling with session mode for safe context propagation.
- Patroni & etcd: Automated leader election and high availability.
- pgBackRest: AES-256 encrypted backups and WAL archiving for 10-year retention.
- pgaudit: Database activity monitoring for HIPAA and GDPR compliance.

## Rationale
[This architecture ensures 99.99% uptime and strict compliance using automated failover, encryption, and audit controls.]
[It guarantees sub-second EMR performance by isolating heavy analytical queries onto read-replicas.]