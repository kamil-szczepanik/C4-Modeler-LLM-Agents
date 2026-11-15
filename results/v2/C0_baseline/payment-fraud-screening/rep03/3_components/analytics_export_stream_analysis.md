## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for mid-size payment processors to detect and prevent fraud. It evaluates payment requests in real time and provides a case management interface for fraud analysts to review suspicious transactions.

## Key Elements
- Fraud Analyst / Risk Manager (User)
- Payment Gateway / Processing Engine, Identity Provider, Payment Card Network / Tokenization Vault, Secure Audit Archive (External Systems)
- API Gateway (Nginx / AWS ALB)
- Fraud Scoring Engine (Java/Quarkus or Go with embedded ONNX Runtime)
- Case Management Service (Node.js / TypeScript)
- Audit & Compliance Ledger (Rust or Go with AWS KMS-backed signing)
- Analytics Export Stream (Rust/Go Local Anonymizer sidecar & AWS Kinesis Firehose Client)
- Data Store (AWS Aurora PostgreSQL & Amazon Redis)
- Data Lake (Amazon S3)

## Relationships
- Fraud Gateway -> API Gateway: Forwards authorization requests [HTTPS / gRPC]
- API Gateway -> Fraud Scoring Engine: Routes payment payloads [gRPC]
- Fraud Scoring Engine -> Data Store: Reads risk profiles and historical data [TLS / JDBC]
- Fraud Scoring Engine -> Audit & Compliance Ledger: Writes immutable decision logs [gRPC]
- Case Management Service -> Data Store: Reads and updates review cases [TLS / SQL]
- Analytics Export Stream -> Data Lake (Amazon S3): Batch uploads anonymized metrics and schema payloads [HTTPS / AWS SigV4]

## Technology Stack
- AWS (Cloud Provider, eu-west-1 region) for infrastructure deployment
- Java/Quarkus or Go with embedded ONNX Runtime for high-performance fraud scoring
- Node.js / TypeScript for case management services
- AWS Aurora PostgreSQL and Amazon Redis for transactional and cached data storage
- Rust/Go for local anonymization sidecar to ensure zero-allocation PII scrubbing
- Amazon S3 with AWS KMS customer-managed keys for secure data lake storage

## Rationale
This architecture uses high-performance microservices and in-memory caching to achieve decision latencies below 50 ms at P99 under 3,000 requests per second. It ensures PCI-DSS Level 1 compliance and 7-year auditability through local PII scrubbing, cryptographic signing, and strict separation of analytics streams from live payment paths.