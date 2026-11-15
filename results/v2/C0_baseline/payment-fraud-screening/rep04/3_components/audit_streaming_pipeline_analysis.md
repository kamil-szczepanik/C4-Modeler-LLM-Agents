## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud in real-time and provides case management for suspicious payments. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a €25,000 monthly budget.

## Key Elements
- Shopper / Cardholder, Merchant, Fraud Analyst, Risk / Compliance Officer
- AWS API Gateway
- Scoring Engine (Rust (Tokio), Amazon ECS Fargate)
- Case Management App (Node.js/Python, Amazon ECS Fargate)
- Feature Store & Cache (Amazon ElastiCache Redis, Amazon DynamoDB)
- Audit & Streaming Pipeline (Amazon Kinesis Data Streams, Amazon Kinesis Firehose, AWS Lambda)
- Audit Storage (Amazon S3 with Object Lock in Compliance Mode)
- Audit DLQ (Amazon SQS)

## Relationships
- Shopper / Cardholder -> Merchant: Initiates card-not-present payment [HTTPS]
- Merchant -> AWS API Gateway: Submits authorization requests [HTTPS/REST]
- AWS API Gateway -> Scoring Engine: Routes payment payloads [HTTP/2]
- Scoring Engine -> Feature Store & Cache: Queries user profiles and fraud rules [Redis RESP / DynamoDB API]
- Scoring Engine -> Audit & Streaming Pipeline: Streams pre-redacted audit events [AWS SDK / Kinesis PutRecords API]
- Audit & Streaming Pipeline -> Audit Storage: Persists immutable audit logs [AWS internal storage APIs]
- Audit & Streaming Pipeline -> Audit DLQ: Routes poisoned or failed records [AWS SQS SDK]
- Fraud Analyst -> Case Management App: Reviews flagged payments [HTTPS]

## Technology Stack
- AWS API Gateway: Low-overhead HTTP/2 ingress for processing 3,000 TPS.
- Rust (Tokio) & Amazon ECS Fargate: High-performance, low-latency execution for the Scoring Engine to meet the <50ms P99 SLA.
- Amazon Kinesis Data Streams & Firehose: Scalable ingestion and batching for streaming audit logs.
- Amazon S3 (Object Lock Compliance Mode): Ensures 7-year tamper-evident storage for regulatory compliance.
- AWS KMS: Customer-managed keys with automatic rotation for PCI-DSS data encryption.

## Rationale
The architecture combines low-latency containerized compute with fully managed AWS streaming and storage services to process 3,000 TPS under 50ms P99. It strictly enforces PCI-DSS compliance and 7-year tamper-evident auditability while operating within a €25,000 monthly budget for a three-person engineering team.