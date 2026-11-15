## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages fraud review cases. It uses a serverless AWS architecture to deliver low-latency decisions while ensuring strict compliance and auditability.

## Key Elements
- **Users**: Fraud Analyst
- **External Systems**: Payment Gateway / Core Ledger, Card Schemes / Tokenization Provider, Identity Provider (IdP), Notification Service
- **Containers**: AWS ALB, Fraud Scoring Service, Case Management API, CloudFront / React SPA, API Gateway, Amazon ElastiCache (Redis), Amazon S3 Model Registry, Amazon SQS, AWS Lambda (Audit Processor), Amazon S3 Object Lock, Amazon Aurora PostgreSQL, AWS Cloud Map
- **Components (AWS Lambda)**: SQS Event Consumer, Audit Normalizer, Cryptographic Signer, KMS Signer Client, S3 Storage Client, DLQ Error Handler

## Relationships
- **SQS Event Consumer** -> **Audit Normalizer**: In-memory function call
- **Audit Normalizer** -> **Cryptographic Signer**: In-memory function call
- **Cryptographic Signer** -> **KMS Signer Client**: In-memory function call
- **KMS Signer Client** -> **AWS KMS**: Requests cryptographic signature via HTTPS / AWS SigV4
- **Cryptographic Signer** -> **S3 Storage Client**: In-memory function call
- **S3 Storage Client** -> **Amazon S3 Object Lock**: Persists audit logs via HTTPS / AWS SigV4
- **SQS Event Consumer** -> **Amazon SQS (DLQ)**: Sends failed audit payloads via HTTPS / AWS SigV4

## Technology Stack
- **Node.js (TypeScript)**: Chosen for Lambda execution to minimize cold-start latency and optimize AWS SDK v3 performance.
- **AWS KMS**: Provides hardware-backed key protection for tamper-evident audit log signing.
- **Amazon S3 Object Lock**: Secures audit records in compliance mode for 7-year retention.
- **Amazon SQS & DLQ**: Ensures reliable asynchronous event processing and error isolation.

## Rationale
This architecture leverages serverless AWS components to minimize operational overhead for a three-engineer team within a fixed budget. It satisfies strict PCI-DSS Level 1 compliance and 7-year tamper-evident audit requirements using managed encryption and storage services.