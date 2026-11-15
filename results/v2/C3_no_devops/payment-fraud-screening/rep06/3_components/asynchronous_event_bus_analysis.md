## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides case management tools for analysts. It ensures high performance, PCI-DSS Level 1 compliance, and a 7-year tamper-evident audit trail within a fixed budget.

## Key Elements
- **Event Router**: Amazon EventBridge Bus
- **Event Archive**: Amazon EventBridge Archive with Amazon S3 Object Lock
- **Dead-Letter Queue (DLQ)**: Amazon SQS
- **Rule Dispatcher**: Amazon EventBridge Rule Subscriptions
- **Audit & Persistence Store**: Amazon Aurora PostgreSQL

## Relationships
- Scoring Engine -> Event Bus: Asynchronous event publishing via HTTPS using AWS SDK v2 and AWS Signature Version 4 (`PutEvents`)
- Event Bus -> Case Management SQS Queue: Event push delivery via HTTPS using AWS KMS CMK encryption
- Event Bus -> Audit Store Archive: Native SQS/S3 integration with Object Lock enabled for 7-year retention

## Technology Stack
- **Amazon EventBridge**: Fully managed serverless event bus selected to minimize operational overhead for a 3-engineer team and maintain strict P99 latency.
- **Amazon SQS**: Used for DLQ and downstream routing to guarantee zero data loss and at-least-once delivery.
- **Amazon S3 Object Lock**: Enforces tamper-evident 7-year audit retention to comply with PCI-DSS Level 1 constraints.
- **AWS KMS**: Provides customer-managed encryption keys with automated annual rotation for data at rest.
- **AWS PrivateLink**: Secures internal VPC endpoints to block public internet exposure.

## Rationale
This serverless event-driven architecture eliminates infrastructure maintenance overhead for a three-engineer team while staying well under the 25,000 EUR monthly budget. It guarantees sub-50 ms P99 decision latency and robust 7-year compliance via managed AWS services.