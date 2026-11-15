## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for clinics and hospitals. It ensures high availability, strict HIPAA/GDPR compliance, and robust data retention.

## Key Elements
- PostgreSQL Primary Instance (PostgreSQL 16 on Kubernetes)
- PostgreSQL Standby Instances (Streaming Replication, Patroni on Kubernetes)
- Connection Pooler (PgBouncer)
- Audit Extension Module (`pg_audit`)
- Encryption Manager (`pgcrypto` / Transparent Data Encryption)
- Data Masking & Purging Component (PostgreSQL RLS & PL/pgSQL functions)
- Archiving Service (pgBackRest with cold object storage)

## Relationships
- Core Services Container -> Connection Pooler: Routes transactional queries [JDBC / TCP]
- Connection Pooler -> PostgreSQL Primary: Forwards operational queries [TCP]
- PostgreSQL Primary -> PostgreSQL Standby: Synchronous data replication [TCP]
- Core Services Container -> Data Masking & Purging Component: Executes GDPR compliance queries [JDBC / SQL]
- PostgreSQL Primary -> Archiving Service: Continuous WAL archiving [TCP / Object Storage API]

## Technology Stack
- PostgreSQL 16: Core relational database chosen for robust ACID compliance and transactional data integrity.
- Patroni with etcd: Manages automated leader election and high availability to achieve RPO=0 and prevent split-brain.
- PgBouncer: Connection pooler optimizing throughput to maintain sub-second EMR load times.
- `pg_audit` & `pgcrypto`: Implements tamper-proof audit trails and AES-256 encryption at rest to satisfy security mandates.
- pgBackRest: Manages continuous WAL archiving and automated backups for the 10-year retention policy.

## Rationale
This architecture guarantees 99.99% uptime and zero data loss through synchronous primary-standby failover, protecting critical clinical workflows. It integrates robust security controls like mTLS, AES-256, and immutable auditing to meet stringent HIPAA and GDPR requirements.