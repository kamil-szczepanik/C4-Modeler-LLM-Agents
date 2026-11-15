## Overview
[The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations. Its core purpose is to deliver a reliable e-commerce experience scaled for 1M MAU while maintaining strict compliance.]

## Key Elements
- Checkout & Order Service
- Messaging Service (Amazon SQS: `OrderEventsQueue`, `ComplianceExportQueue`, and Dead-Letter Queues)
- Order & Fulfillment Workers
- Compliance Processor
- DLQ Redrive Lambda
- Event Archive (Amazon S3)

## Relationships
- Checkout & Order Service -> Messaging Service: Sends asynchronous events and data export requests [HTTPS, AWS SDK]
- Messaging Service -> Order & Fulfillment Workers: Dispatches asynchronous fulfillment tasks [SQS Long Polling]
- Messaging Service -> Compliance Processor: Triggers audit log and data export pipelines [SQS FIFO]
- Messaging Service (DLQ) -> DLQ Redrive Lambda: Invokes recovery workflow [AWS SDK]
- Messaging Service -> Event Archive: Persists processed event logs for auditing [Amazon S3 API]

## Technology Stack
- Amazon SQS: Decouples asynchronous workflows and ensures at-least-once delivery for orders and compliance.
- AWS KMS Customer Managed Keys (CMK): Encrypts messages at rest across all queues and the event archive.
- Amazon S3: Acts as a WORM-compliant Event Archive for long-term GDPR/CCPA audit logging.
- AWS Lambda: Executes automated DLQ message recovery and redrive operations.
- AWS IAM: Enforces strict least-privilege access control across services and workers.

## Rationale
[This architecture ensures 99.95% uptime and seamless handling of traffic spikes via decoupled message queues. It simultaneously satisfies strict GDPR/CCPA compliance and security mandates through encryption, audit trails, and strict IAM controls.]