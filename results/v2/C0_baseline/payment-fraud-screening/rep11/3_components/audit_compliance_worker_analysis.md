## Overview
The Audit & Compliance Worker processes real-time decision payloads to generate tamper-evident, cryptographically signed audit logs stored in AWS. It ensures 7-year regulatory compliance for payment fraud screening without impacting sub-50ms transaction latency.

## Key Elements
- **Risk / Compliance Officer**: Internal persona auditing historical screening decisions independently.
- **Event Consumer Component**: Python process polling Amazon SQS.
- **Canonical Formatter Component**: Python module normalizing raw payloads into strict JSON schemas.
- **Cryptographic Signer Component**: Utility applying asymmetric AWS KMS signatures.
- **S3 Batch Writer Component**: Python module buffering and writing partitioned Apache Parquet files.
- **AWS S3 Object Lock**: Tamper-evident storage vault with Compliance Mode enabled.
- **Amazon Athena**: Query engine for compliance officers.

## Relationships
- Amazon SQS -> Event Consumer: Polls decision payloads [AWS SDK / SQS API]
- Event Consumer -> Canonical Formatter: In-memory method call [Python]
- Canonical Formatter -> Cryptographic Signer: In-memory method call [Python]
- Cryptographic Signer -> AWS KMS: Requests asymmetric signature [HTTPS / KMS API]
- Cryptographic Signer -> S3 Batch Writer: Internal method call [Python]
- S3 Batch Writer -> AWS S3 Object Lock: Multipart upload with SSE-KMS [HTTPS / S3 API]
- Risk / Compliance Officer -> Amazon Athena: Executes compliance verification queries [HTTPS / Athena Console or API]

## Technology Stack
- **Python**: Core runtime for asynchronous worker implementation due to team expertise.
- **Amazon SQS**: Decouples real-time payment ingestion from asynchronous logging to protect processing latency.
- **AWS KMS (`ECC_NIST_P256` or `RSA_2048`)**: Provides asymmetric cryptographic signing for non-repudiation.
- **Apache Parquet**: Columnar storage format optimizing query performance and reducing AWS Athena scan costs.
- **AWS S3 Object Lock (Compliance Mode)**: Enforces immutable 7-year data retention.
- **Amazon ECS on EC2**: Container orchestration managed by a 3-engineer team.

## Rationale
Asynchronous offloading via SQS isolates logging from real-time payment flows, guaranteeing decision latency remains below 50ms at P99. Apache Parquet partitioning and S3 Object Lock ensure immutable, cost-effective 7-year regulatory compliance within a 25,000 EUR monthly budget.