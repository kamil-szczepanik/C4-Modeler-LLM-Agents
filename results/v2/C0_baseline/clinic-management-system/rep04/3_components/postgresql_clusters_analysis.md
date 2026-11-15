## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It provides highly available, secure, and interoperable clinical IT capabilities across hybrid infrastructure.]

## Key Elements
* Primary Database Instance (`PostgreSQL Engine`)
* Read Replica Instances (`PostgreSQL Read Replicas`)
* High Availability Manager (`Patroni / etcd`)
* Backup & Archival Agent (`Barman / pgBackRest`)
* Connection Pooler (`PgBouncer`)
* Audit Log Collector (`pgAudit`)

## Relationships
* Core Services -> Connection Pooler: SQL / TLS 1.3
* Core Services -> Read Replica Instances: SQL / TLS 1.3 (Read-only)
* Connection Pooler -> Primary Database Instance: Internal TCP
* Primary Database Instance -> Backup & Archival Agent: WAL streaming
* Primary Database Instance -> Audit Log Collector: Internal Hook

## Technology Stack
* PostgreSQL: Relational database engine chosen for ACID compliance and structured clinical data storage.
* Patroni / etcd: HA management for automated leader election and zero data loss failovers.
* pgBackRest / Barman: Backup agents for continuous WAL streaming to WORM object storage.
* PgBouncer: Connection pooler for handling high concurrency during peak clinical hours.
* pgAudit: Extension for capturing security-relevant DDL/DML events for HIPAA compliance.

## Rationale
[This architecture enforces stringent HIPAA and GDPR security controls alongside strict schema segregation for clinical and financial data. It leverages automated high availability and optimized connection pooling to guarantee 99.99% uptime and sub-second EMR performance.]