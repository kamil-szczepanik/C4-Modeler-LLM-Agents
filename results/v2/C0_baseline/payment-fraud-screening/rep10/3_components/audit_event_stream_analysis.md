## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect and prevent fraud before approval, while providing case management for manual reviews. It ensures strict PCI-DSS Level 1 compliance and 7-year immutable auditability within a strict infrastructure budget and small engineering team.

## Key Elements
- **Manual Analyst**: Human user reviewing suspicious payments via the frontend portal.
- **Real-Time Scoring Engine**: Container executing fraud models via AWS ECS Fargate and ONNX Runtime.
- **Audit & Event Stream**: Container ingesting, buffering, and dispatching compliance and decision events.
- **Event Ingestion Router**: Amazon EventBridge component routing schema-validated events.
- **Buffer & Batcher**: Amazon Kinesis Data Firehose component aggregating events into Parquet batches.
- **Decision Audit Store**: External system using AWS S3 Object Lock and AWS KMS for 7-year tamper-evident storage.

## Relationships
- **Real-Time Scoring Engine -> Event Ingestion Router**: Streams scoring decisions and explainability metadata via HTTPS / EventBridge `PutEvents` API.
- **Case Management Backend -> Event Ingestion Router**: Streams case workflow events via HTTPS / EventBridge `PutEvents` API.
- **Event Ingestion Router -> Buffer & Batcher**: Forwards filtered events via Kinesis Firehose direct integration over HTTPS.
- **Buffer & Batcher -> Decision Audit Store**: Delivers encrypted Parquet batches via S3 API over TLS 1.3.

## Technology Stack
- **AWS EventBridge**: Used for serverless, decoupled event ingestion and routing with Dead Letter Queues to minimize operational overhead.
- **AWS Kinesis Data Firehose**: Used to batch and compress high-throughput events into Parquet format within budget.
- **AWS S3 Object Lock & KMS**: Used for 7-year tamper-evident audit log retention and encryption in Compliance Mode.
- **AWS CDK**: Used for infrastructure-as-code definition by a three-person engineering team.

## Rationale
Serverless AWS components eliminate self-hosted infrastructure management, fitting the three-engineer team limit and 25,000 EUR monthly budget. Asynchronous event streaming ensures sub-50ms P99 scoring latency while satisfying strict PCI-DSS and 7-year auditability requirements.