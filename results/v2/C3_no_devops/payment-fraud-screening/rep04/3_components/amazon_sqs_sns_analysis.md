## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud before approval and provides case management for human analysts. It operates on AWS to meet strict latency, security, and auditability requirements.

## Key Elements
- `FraudEventTopic` (Amazon SNS)
- `AuditLogQueue` (Amazon SQS)
- `CaseRoutingQueue` (Amazon SQS)
- Dead-Letter Queues (DLQ)
- `Scoring Engine` (ECS Container on AWS Fargate)
- `Case Management Backend` (ECS Container on AWS Fargate)

## Relationships
- `Scoring Engine` publishes authorization and decision events to `FraudEventTopic` via HTTPS (TLS 1.3)
- `FraudEventTopic` pushes payloads to `AuditLogQueue` and `CaseRoutingQueue` via SQS protocol over AWS PrivateLink
- `Case Management Backend` consumes review tasks from `CaseRoutingQueue` via HTTPS (TLS 1.3) using AWS SDK polling

## Technology Stack
- Amazon SNS & SQS: Provides asynchronous decoupled messaging within the AWS eu-west-1 region
- AWS PrivateLink (VPC Endpoints): Secures internal traffic to prevent public internet exposure
- AWS KMS: Encrypts data at rest with automatic annual key rotation and strict IAM least-privilege policies
- Dead-Letter Queues (DLQ): Prevents poison-pill message processing loops with a maximum receive count limit

## Rationale
This architecture uses managed AWS messaging services to maintain sub-50 ms P99 latency while adhering to a fixed 25,000 EUR monthly budget. It ensures PCI-DSS Level 1 compliance and 7-year auditability through strict encryption, tokenization, and decoupled audit logging.