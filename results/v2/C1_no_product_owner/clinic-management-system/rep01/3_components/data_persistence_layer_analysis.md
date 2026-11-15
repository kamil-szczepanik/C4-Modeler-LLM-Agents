## Overview
The Data Persistence Layer securely stores and manages patient demographics, medical records, schedules, and billing data for the Clinic Management System. It guarantees high availability, 10-year data retention, and strict HIPAA/GDPR compliance across hybrid cloud infrastructure.

## Key Elements
- **Patient Data Store**: PostgreSQL 15 with Citus Extension and pg_partman for partitioned patient demographics
- **EMR Audit Repository**: PostgreSQL 15 with immutable append-only tables and pgaudit for tamper-proof audit trails
- **Transaction Coordinator**: PgBouncer for high-concurrency connection pooling
- **Failover Orchestrator**: Patroni for automated leader election and active-passive failover
- **Replication & Backup Manager**: Barman with PostgreSQL streaming replication
- **Observability & Archival Agents**: Prometheus PostgreSQL Exporter, pg_stat_statements, and Automated Compliance Archival Daemon

## Relationships
- **Patient, Scheduling, EMR, & Billing Services -> Transaction Coordinator**: Transmits queries and transactions via [TLS 1.3 / JDBC with SCRAM-SHA-256]
- **Transaction Coordinator -> Patient Data Store & EMR Audit Repository**: Routes read/write operations via [Internal mTLS / TCP]
- **Replication & Backup Manager -> Multi-Region Infrastructure**: Synchronizes primary databases in `on-prem-k8s` with `eu-central-1`
- **Database Observability Agent -> External SIEM**: Streams security and audit logs via [HTTPS / TLS]

## Technology Stack
- **PostgreSQL 15**: Relational database engine chosen for robust ACID compliance and advanced partitioning support
- **Patroni**: Automated failover and consensus manager ensuring 99.99% availability (R-06)
- **PgBouncer**: Connection pooling layer ensuring EMR screen load performance <1 s P95 (R-07)
- **Barman**: Backup and recovery manager supporting 10-year data retention compliance
- **Citus Extension & pg_partman**: Distributed scaling and automated partition management for large clinical datasets
- **AES-256 & HSM**: Cryptographic standard ensuring data-at-rest security and GDPR crypto-shredding

## Rationale
This architecture eliminates hybrid cloud split-brain risks using an active-passive Patroni-managed topology while scaling efficiently with pg_partman. Strict PostgreSQL Row-Level Security, mTLS, and immutable audit logs ensure full HIPAA and GDPR compliance.