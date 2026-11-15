## Overview
This system screens card-not-present payment authorizations for fraud in real-time and provides a case management interface for human analysts. It balances strict compliance, high throughput, and low operational overhead for a small engineering team.

## Key Elements
- Case Repository Component: Manages analyst decisions and investigation notes using PostgreSQL relational tables with JSONB.
- Rule & Model Metadata Component: Stores active rule definitions and version pointers in PostgreSQL.
- Audit Ledger Component: Implements append-only tables with Row-Level Security (RLS) and pgcrypto SHA-256 hashing.
- Connection Pooling & Routing Component: Managed via PgBouncer / RDS Proxy to control connection limits.
- Database Backup & PITR Component: Handles automated snapshot lifecycles and WAL archiving.
- Read Replica Routing Component: Offloads analytical queries using Aurora PostgreSQL Read Replica endpoints.

## Relationships
- Case Management Backend -> Case Repository: Read/Write case states via SQL / PostgreSQL Wire Protocol over TLS.
- Model & Rule Registry Service -> Read Replica Routing: Queries rule metadata and metrics via SQL over TLS.
- Audit Ledger Component -> Compliance Archive (AWS S3): Exports daily encrypted snapshots via AWS Internal Storage APIs over TLS.

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for managed scalability, high availability, and native AWS ecosystem integration.
- pgcrypto & PostgreSQL RLS: Used for lightweight cryptographic hashing and tamper-evident audit logs without external KMS latency.
- RDS Proxy / PgBouncer: Implemented to multiplex connections and protect database performance under high load.
- Amazon S3: Utilized for cost-effective 7-year compliance audit storage.

## Rationale
The architecture ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while maintaining P99 decision latency below 50 ms at 3,000 req/sec. It operates within a 25,000 EUR monthly budget and is maintainable by a three-engineer team through managed AWS services.