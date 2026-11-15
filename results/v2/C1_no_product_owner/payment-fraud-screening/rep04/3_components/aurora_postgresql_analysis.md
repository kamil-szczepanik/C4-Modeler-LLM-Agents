## Overview
The Aurora PostgreSQL database system securely persists encrypted audit logs, case management data, and transaction histories for real-time payment fraud screening. It ensures strict 7-year auditability and PCI-DSS compliance while operating within a fixed AWS budget and lean engineering team.

## Key Elements
- **Amazon Aurora PostgreSQL**: Managed relational database service deployed with Aurora Serverless v2.
- **Audit Ledger Table**: PostgreSQL relation with database triggers blocking updates/deletes for tamper-evidence.
- **Case Management Store**: Relational tables with PostgreSQL Row-Level Security (RLS) for analyst data segregation.
- **Audit Ingestion Worker**: Asynchronous consumer executing batch upserts.
- **PgBouncer**: Connection pooling proxy preventing thread exhaustion.
- **AWS KMS**: Key management service for Transparent Data Encryption (TDE).

## Relationships
- `Amazon MSK / Kafka` -> `Audit Ingestion Worker`: Streams batched audit records `[TCP / SSL]`
- `Audit Ingestion Worker` -> `Audit Ledger Table`: Appends immutable records `[Internal SQL]`
- `Case Management` -> `Case Management Store`: Reads and updates analyst review workflows `[TCP / SSL]`
- `Aurora PostgreSQL` -> `Amazon S3`: Archives detached monthly table partitions for long-term retention `[HTTPS]`

## Technology Stack
- **Amazon Aurora PostgreSQL (v15+)**: Relational storage providing enterprise reliability, declarative partitioning, and PL/pgSQL handlers.
- **pgcrypto Extension**: Provides cryptographic hashing and signatures for tamper-evident audit logs.
- **PgBouncer**: Lightweight connection pooler ensuring stability under high-concurrency loads (3,000 TPS).
- **AWS KMS**: Manages customer-managed keys (CMK) with automated rotation for strict PCI-DSS data encryption.

## Rationale
Decoupling synchronous database writes via Amazon MSK protects the hot path to guarantee <50ms P99 latency. Automated monthly partitioning, S3 archival, and Aurora Serverless v2 maintain strict 7-year auditability within the 25,000 EUR monthly budget for a 3-person team.