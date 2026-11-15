## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud, and enables fraud analysts to review suspicious transactions. It ensures PCI-DSS Level 1 compliance and 7-year auditability while operating within a 25,000 EUR monthly budget on AWS.

## Key Elements
- **Users**: Fraud Analysts, Compliance Officers, Auditors / Regulators
- **External Systems**: Payment Gateway / Merchants, AWS S3 with Object Lock and Glacier Deep Archive
- **Containers**: AWS API Gateway, Fraud Scoring Engine (Go / Rust), Case Management & Rules Service (Node.js / Go), Audit & Evidence Worker (Go), AWS ElastiCache (Redis), Amazon SQS, Amazon ECS on AWS Fargate
- **Worker Components**: SQS Consumer, Canonicalizer & Sanitizer, S3 Batch Writer, SQS DLQ

## Relationships
- Payment Gateway / Merchants -> AWS API Gateway: Submits authorization requests [HTTPS / REST]
- AWS API Gateway -> Fraud Scoring Engine: Evaluates scoring rules [gRPC / Internal VPC]
- Fraud Scoring Engine -> Amazon SQS: Publishes async audit events [SQS SendMessage]
- Amazon SQS -> Audit & Evidence Worker: Delivers async audit events [SQS Poll]
- Audit & Evidence Worker -> AWS S3 with Object Lock: Writes immutable audit logs with metadata [HTTPS / AWS SDK v2]
- Audit & Evidence Worker -> SQS DLQ: Routes failed writes on persistent errors [SQS SendMessage]

## Technology Stack
- **Compute**: Amazon ECS on AWS Fargate for serverless container deployment with minimal operational overhead
- **Language**: Go for high-performance, low-memory worker implementation and scoring engines
- **Storage**: AWS S3 with Object Lock and Glacier Deep Archive for immutable, cost-effective 7-year audit retention
- **Messaging**: Amazon SQS with Dead Letter Queues for reliable, decoupled asynchronous event processing
- **Caching**: AWS ElastiCache (Redis) for low-latency rule and case state management

## Rationale
This architecture uses serverless containers and managed AWS services to minimize operational overhead for a three-engineer team. Immutable S3 storage with metadata indexing guarantees PCI-DSS compliance and 7-year auditability within the strict budget.