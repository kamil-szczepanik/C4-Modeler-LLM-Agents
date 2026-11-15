## Overview
The Online Bookstore uses Amazon SQS to provide reliable, asynchronous message buffering and task distribution across scalable backend microservices. It ensures resilient transaction processing, order fulfillment, and notification workflows under high user loads.

## Key Elements
- **OrderQueue**: SQS FIFO queue for buffering checkout events and preventing duplicate fulfillment.
- **NotificationQueue**: SQS Standard queue for asynchronous email and alert dispatches.
- **AnalyticsQueue**: SQS Standard queue for buffering clickstream and inventory events.
- **Dead-Letter Queues (DLQs)**: `OrderDLQ`, `NotificationDLQ`, and `AnalyticsDLQ` for capturing poisoned messages.
- **ECS Workers**: `Core Services`, `Notification Worker`, and `Analytics Ingestion Container` consuming queue messages.

## Relationships
- `Core Services` sends messages to `OrderQueue` via AWS SDK (HTTPS/TLS 1.3).
- `Notification Worker` polls `NotificationQueue` via Long Polling (HTTPS/TLS 1.3).
- `Analytics Ingestion Container` polls `AnalyticsQueue` via Long Polling (HTTPS/TLS 1.3).
- Primary queues route failed messages exceeding `maxReceiveCount` (3) to their respective DLQs.

## Technology Stack
- **Amazon SQS (FIFO & Standard)**: Chosen for ordered transaction processing and scalable task buffering.
- **AWS KMS**: Utilized with customer-managed keys for Server-Side Encryption (SSE) to meet GDPR/CCPA data protection requirements.
- **Amazon CloudWatch**: Used for monitoring queue metrics (`ApproximateNumberOfMessagesVisible`, `OldestMessageAge`).
- **AWS IAM**: Enforces least-privilege access and explicit transport security (`aws:SecureTransport` set to `true`).

## Rationale
This asynchronous queue architecture isolates peak checkout traffic to protect core transactional integrity while meeting strict scalability and 99.95% uptime requirements. Integrating KMS encryption and IAM least-privilege ensures compliance with GDPR and CCPA security constraints.