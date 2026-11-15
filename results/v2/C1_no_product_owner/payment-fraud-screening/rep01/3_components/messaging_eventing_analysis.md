## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst review workflows. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms latency at 3,000 TPS within a fixed 25,000 EUR monthly AWS budget.

## Key Elements
- Real-Time Scoring Service (Go container on Amazon ECS on EC2)
- Case Management Backend (Java Spring Boot container on Amazon ECS on Fargate)
- Audit Event Publisher (Lightweight Go client with asynchronous batching)
- Case Queue (Amazon SQS FIFO Queue with content-based deduplication and DLQ)
- Model Event Bus (Amazon EventBridge)
- Audit SNS Topic (Amazon SNS with fan-out pattern)

## Relationships
- Real-Time Scoring Service -> Audit Event Publisher: In-process function call, publishing asynchronously via AWS SDK over HTTPS [TLS 1.3]
- Audit Event Publisher -> Audit SNS Topic: Publishes audit logs [HTTPS, AWS KMS CMK encryption]
- Real-Time Scoring Service -> Case Queue: Sends review cases for suspicious transactions [Amazon SQS FIFO API, HTTPS, AWS KMS CMK encryption]
- Case Queue -> Case Management Backend: Long-polling for review workflows [AWS SDK, HTTPS]
- Model Event Bus -> Real-Time Scoring Service: Broadcasts model hot-reloading signals [HTTPS]

## Technology Stack
- Amazon SQS FIFO: Ensures strict message ordering per account to prevent analyst review race conditions.
- Amazon SNS & EventBridge: Provides reliable fan-out and event broadcasting with minimal operational overhead for a 3-engineer team.
- AWS KMS: Secures all queues, topics, and event buses with Customer Managed Keys for PCI-DSS compliance.
- Fluent Bit & LUKS: Encrypts ephemeral local disk-spill buffers for circuit breaker recovery.
- AWS X-Ray & CloudWatch: Enforces distributed tracing and metric alarms to meet the 1-minute fallback availability threshold.

## Rationale
This architecture leverages managed AWS messaging services to minimize operational overhead for a three-engineer team while meeting strict sub-50ms latency constraints. It enforces robust security, encryption, and FIFO ordering to satisfy PCI-DSS Level 1 compliance and 7-year auditability mandates within budget.