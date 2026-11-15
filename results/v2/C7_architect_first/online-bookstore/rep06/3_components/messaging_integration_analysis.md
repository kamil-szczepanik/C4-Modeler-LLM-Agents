## Overview
- The Messaging & Integration container handles asynchronous decoupling for shipping, notifications, and analytics in the Online Bookstore.
- It utilizes AWS managed serverless services to ensure scalability, GDPR/CCPA compliance, and high availability.

## Key Elements
- **Event Router**: Amazon EventBridge serverless event bus.
- **Notification Dispatcher Queue**: Amazon SQS standard queue.
- **Shipping Fulfillment Topic**: Amazon SNS pub/sub topic.
- **Dead Letter Queue (DLQ) Handlers**: Paired Amazon SQS DLQs.
- **Schema Registry**: AWS Glue Schema Registry.
- **State Store**: Amazon ElastiCache Redis.

## Relationships
- Core API Application -> Event Router: Publishes domain events [HTTPS / AWS SDK]
- Event Router -> Notification Dispatcher Queue: Forwards notification events [AWS SQS integration]
- Event Router -> Shipping Fulfillment Topic: Forwards checkout events [AWS SNS integration]
- Event Router -> DLQ Handler: Routes failed messages after max retries [AWS SQS]
- DLQ Handler -> Event Router: Publishes *OrderProcessingFailed* event [AWS SDK]

## Technology Stack
- **Amazon EventBridge**: Provides serverless event routing with schema validation for domain events.
- **Amazon SQS / SNS**: Delivers managed asynchronous queuing and pub/sub capabilities.
- **AWS KMS**: Secures payloads at rest using customer-managed keys for GDPR/CCPA compliance.
- **AWS Glue Schema Registry**: Enforces strict payload validation and secrets redaction.
- **Amazon ElastiCache Redis**: Manages deduplication and idempotency tracking.

## Rationale
- Serverless AWS components guarantee 99.95% uptime and seamless scaling to 1M MAU.
- Strict regional IAM controls and encryption ensure robust GDPR and CCPA compliance.