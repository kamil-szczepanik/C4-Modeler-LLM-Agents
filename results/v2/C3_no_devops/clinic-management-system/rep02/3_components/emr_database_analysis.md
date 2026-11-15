## Overview
The EMR Database is a secure, highly available data storage system managing electronic medical records for the Clinic Management System. It ensures strict HIPAA and GDPR compliance while supporting sub-second clinical queries.

## Key Elements
- Relational Storage Engine (PostgreSQL Cluster with synchronous streaming replication)
- Audit Logging Subsystem (PostgreSQL `pgAudit`)
- Connection Pooler & Read Scaler (PgBouncer)
- Encryption & Key Manager Integration (HashiCorp Vault with AES-256 TDE)
- EMR Backend Container
- Audit & Compliance Daemon Container
- Cold Storage

## Relationships
- EMR Backend Container -> PgBouncer: Queries and updates patient records via TLS 1.3 mTLS with dynamic credentials
- PgBouncer -> Relational Storage Engine: Routes read-only queries to replicas and writes to primary PostgreSQL node
- Relational Storage Engine -> Audit Logging Subsystem: Captures DDL/DML activity via `pgAudit`
- Audit Logging Subsystem -> Cold Storage: Exports WORM-protected audit logs for 10-year retention
- EMR Backend Container -> HashiCorp Vault: Provisions dynamic, short-lived database credentials

## Technology Stack
- PostgreSQL Cluster: Primary relational database providing Row-Level Security (RLS) and declarative table partitioning for multi-tenancy and fast archiving
- PgBouncer: Connection pooler handling high connection spikes and routing read-heavy diagnostic traffic
- `pgAudit`: Native database auditing extension for comprehensive compliance logging
- HashiCorp Vault: Secrets management engine providing AES-256 Transparent Data Encryption (TDE) keys and dynamic credentials
- TLS 1.3: Enforces strict secure transport protocols across all database connections

## Rationale
This architecture guarantees 99.99% availability via synchronous replication and connection pooling while meeting stringent HIPAA and GDPR requirements through RLS, `pgAudit`, and Vault-backed AES-256 encryption.