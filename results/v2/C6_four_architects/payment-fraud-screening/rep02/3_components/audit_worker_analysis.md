## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage analyst reviews. It ensures high performance, PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability on AWS.

## Key Elements
- **Audit Event Consumer**: Python (`boto3`) component polling streaming events.
- **Stream Offset Manager**: Python / AWS SDK tracking Kinesis shard iterator positions.
- **Tamper-Evident Signer**: Python (`cryptography`) component generating cryptographic hashes.
- **KMS Integration Wrapper**: Python (`boto3`) interface for AWS KMS envelope encryption.
- **Audit Persistence Adapter**: Python (`psycopg2`) component for database writes.
- **Dead Letter Queue (DLQ) Handler**: Python component capturing failed payloads.

## Relationships
- Audit Event Consumer -> Amazon Kinesis Data Streams: Polls and commits stream offsets [HTTPS]
- Audit Event Consumer -> Tamper-Evident Signer: Passes raw audit payload [In-memory]
- Audit Event Consumer -> Amazon SQS (DLQ): Forwards failed audit events [HTTPS]
- Tamper-Evident Signer -> AWS KMS: Requests signing keys/operations [HTTPS/TLS]
- Tamper-Evident Signer -> Audit Persistence Adapter: Passes signed record [In-memory]
- Audit Persistence Adapter -> Amazon Aurora PostgreSQL: Inserts audit log [TLS/TCP]

## Technology Stack
- **Python**: Chosen for rapid implementation by a three-engineer team.
- **`boto3` / AWS SDK**: Integrates natively with AWS services (Kinesis, SQS, KMS).
- **AWS KMS**: Secures signing keys via hardware isolation for PCI-DSS compliance.
- **Amazon Aurora PostgreSQL**: Provides durable, compliant storage for audit records.

## Rationale
This architecture decouples durable logging from real-time scoring to maintain P99 latency below 50 ms. It ensures tamper-evident auditability and PCI-DSS compliance within budget constraints.