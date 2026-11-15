## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage manual analyst reviews. The architecture guarantees PCI-DSS compliance, 7-year auditability, and sub-50ms decision latency within a fixed infrastructure budget.

## Key Elements
- Scoring Engine (AWS ECS Fargate, Go)
- Audit Queue (Amazon SQS Standard/FIFO with DLQ)
- Audit Stream Processor (Amazon Kinesis Firehose)
- Audit Storage (Amazon S3 with S3 Object Lock)
- Feature Store (Redis Cluster)
- Case Management Portal (Node.js, TypeScript, PostgreSQL)
- Fraud Analysts

## Relationships
- Scoring Engine -> Audit Queue: Enqueue audit payload [HTTPS / AWS SDK with SigV4]
- Scoring Engine -> Feature Store: Read/Write features [Redis Protocol]
- Audit Queue -> Audit Stream Processor: Deliver audit batch [HTTPS Long Polling]
- Audit Stream Processor -> Audit Storage: Flush tamper-evident logs [S3 API]
- Fraud Analysts -> Case Management Portal: Review flagged transactions [HTTPS]

## Technology Stack
- AWS ECS Fargate: Container orchestration for cost efficiency and minimal operational overhead
- Amazon SQS: Asynchronous message queuing to decouple scoring from storage and prevent latency
- Amazon S3 with S3 Object Lock: WORM-compliant storage ensuring 7-year immutable audit logs
- Redis Cluster: Low-latency in-memory feature storage to satisfy the 50ms P99 SLA
- AWS KMS: Customer-managed keys enforcing encryption at rest for PCI-DSS compliance

## Rationale
Managed AWS services minimize operational burden, fitting the three-engineer team constraint and 25,000 EUR monthly budget. Asynchronous decoupling via SQS protects critical payment latency while ensuring 100% audit capture.