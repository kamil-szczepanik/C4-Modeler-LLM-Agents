## Overview
[Library Management System for public and academic libraries to catalogue items and manage circulation. Enforces strict EU data residency for all patron records.]

## Key Elements
* PostgreSQL 16 Primary Database
* PostgreSQL Read Replica
* PgBouncer Connection Pooler
* HashiCorp Vault External KMS
* Core Circulation & Cataloguing Service
* Reporting Service

## Relationships
* Core Circulation & Cataloguing Service -> PgBouncer: Executes transactional queries [JDBC over mTLS / TLS 1.3]
* Reporting Service -> PostgreSQL Read Replica: Executes aggregated analytical queries [JDBC over TLS 1.3]
* PostgreSQL Primary -> PostgreSQL Read Replica: Asynchronous replication [Encrypted Replication Stream]
* PostgreSQL -> HashiCorp Vault: Envelope encryption key management [HTTPS / REST]

## Technology Stack
* PostgreSQL 16: Primary database utilizing table partitioning, Row-Level Security, and `pgaudit` for compliance and auditability.
* PgBouncer: Connection pooling with TLS 1.3 termination to mitigate handshake latency.
* HashiCorp Vault: External Key Management Service for envelope encryption (DEKs).
* EU-Resident Object Store: Continuous Write-Ahead Log (WAL) archiving for Point-In-Time Recovery (PITR).

## Rationale
[PostgreSQL design satisfies the EU-only data residency constraint while ensuring GDPR compliance through cryptographic erasure of DEKs. Isolation of read workloads and envelope encryption maintain sub-800ms performance requirements.]