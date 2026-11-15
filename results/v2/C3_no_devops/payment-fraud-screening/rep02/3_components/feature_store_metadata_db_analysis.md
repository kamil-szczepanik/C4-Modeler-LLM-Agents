## Overview
The Feature Store & Metadata DB provides ultra-low latency real-time features and secure metadata storage for the Real-Time Payment Fraud Screening system. It ensures tamper-evident auditability, PCI-DSS compliance, and rapid case review capabilities.

## Key Elements
* Redis Feature Cache Component
* PostgreSQL Transaction & Metadata Store Component
* Audit Ledger Component
* Feature Ingestion Worker Component

## Relationships
* Real-Time Scoring Engine -> Redis Feature Cache Component: Retrieves features via TCP/Redis Protocol
* Feature Ingestion Worker Component -> PostgreSQL Transaction & Metadata Store Component: Updates relational metadata via TCP/PostgreSQL Protocol
* Audit Ledger Component -> Amazon S3 Object Lock: Syncs immutable logs via AWS SDK
* Case Management Backend -> PostgreSQL Transaction & Metadata Store Component: Queries case-to-feature snapshots via TCP/PostgreSQL Protocol

## Technology Stack
* AWS ElastiCache Redis: Provides sub-millisecond in-memory feature retrieval for low-latency scoring
* PostgreSQL (RDS): Manages relational metadata, case mappings, and structured audit logs
* SHA-256 Cryptographic Chaining: Ensures tamper-evident audit logging for 7-year retention
* AWS KMS & pgcrypto: Enforces AES-256 storage encryption and column-level protection for PCI-DSS compliance
* AWS S3 Object Lock: Guarantees immutable, write-once-read-many (WORM) long-term storage

## Rationale
Decomposing the database into specialized caching, relational storage, and audit components isolates high-throughput scoring latency from heavy analytical queries. This architecture satisfies strict PCI-DSS compliance, 7-year auditability, and sub-50ms performance constraints within a limited budget and small engineering team.