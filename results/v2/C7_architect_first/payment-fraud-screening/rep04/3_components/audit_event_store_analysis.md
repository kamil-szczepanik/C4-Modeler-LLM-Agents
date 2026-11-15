## Overview
The Audit & Event Store provides tamper-evident, 7-year regulatory audit storage and cryptographic non-repudiation for all real-time payment fraud decisions. It ensures compliance with PCI-DSS Level 1 while maintaining sub-50ms system latency and strict budget constraints.

## Key Elements
* Ingest API / Router (Go)
* Ledger Writer (Go)
* Retention & Archival Worker (Go)
* Ingestion Buffer / WAL (Amazon SQS FIFO)
* Audit Query Adapter (Go)
* Amazon Aurora PostgreSQL (with Ledger/Table features)
* Amazon S3 with Object Lock (Compliance Mode)

## Relationships
* Fraud Scoring Engine -> Ingest API: gRPC over TLS [Internal RPC]
* Ingest API -> Ingestion Buffer: AWS SDK (HTTPS) [Message Queuing]
* Ledger Writer -> Ingestion Buffer: AWS SDK (HTTPS) [Stream Consumption]
* Ledger Writer -> Amazon Aurora: SQL/TCP [Data Persistence]
* Retention Worker -> Amazon S3: HTTPS [Object Lock API]
* Audit Query Adapter -> Amazon Aurora: SQL/TCP (Read Replica) [Query Isolation]

## Technology Stack
* Go: High-performance, low-latency microservice implementation
* Amazon SQS FIFO: Asynchronous buffering ensuring zero data loss and traffic spike absorption
* Amazon Aurora PostgreSQL: Relational persistence with tamper-evident ledger features
* Amazon S3 with Object Lock: Immutable, cost-effective 7-year cold tier storage
* AWS KMS: Dedicated Customer Managed Keys (CMKs) with automated rotation for encryption

## Rationale
This decoupled event-driven architecture prevents database I/O from breaching the 50ms latency constraint (R-04) while guaranteeing zero data loss. Cryptographic signing and S3 Object Lock fulfill the 7-year tamper-evident auditability mandate (R-06) within the 25,000 EUR monthly budget.