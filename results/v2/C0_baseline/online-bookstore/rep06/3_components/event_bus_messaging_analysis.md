## Overview
- Event-driven microservices architecture utilizing AWS serverless infrastructure to decouple services, ensure 99.95% uptime, and handle 1M MAU.
- Asynchronous messaging backbone for order processing, inventory syncing, and real-time recommendations while maintaining GDPR/CCPA compliance.

## Key Elements
- **Event Router (AWS EventBridge):** Central event bus using JSON-based rules.
- **Notification Dispatcher (AWS SNS):** Pub/sub topic for broadcast notifications.
- **Order Queue (AWS SQS):** Durable, at-least-once processing queue with Dead Letter Queues (DLQs).
- **Analytics Stream (AWS Kinesis):** High-throughput clickstream and review event ingestion.
- **EventBridge Schema Registry:** JSON schema validation and contract enforcement.
- **Producers & Consumers:** Order & Checkout Service, Catalog & Search Service, Recommendation Service, Marketing & Email Service.

## Relationships
- **Order & Checkout Service -> Event Router:** Publishes `OrderPlaced` [HTTPS / AWS SDK]
- **Event Router -> Order Queue:** Routes `OrderPlaced` for downstream fulfillment [AWS Native]
- **Event Router -> Notification Dispatcher:** Broadcasts async triggers for emails [AWS Native]
- **Catalog & Search Service -> Event Router:** Publishes `ItemViewed` and `ReviewSubmitted` [HTTPS / AWS SDK]
- **Event Router -> Recommendation Service:** Streams engagement data asynchronously [AWS SQS / Kinesis]

## Technology Stack
- **AWS EventBridge:** Core event routing and schema registry for serverless scale and validation.
- **AWS SQS & SNS:** Reliable queuing, decoupling, and fan-out notifications.
- **AWS Kinesis:** High-throughput streaming for analytics and recommendations.
- **AWS KMS:** Customer-managed keys (CMK) for end-to-end data encryption and PII protection.
- **AWS IAM (SigV4):** Role-based authentication and least-privilege authorization.
- **AWS CloudWatch & X-Ray:** Distributed tracing, backpressure monitoring, and DLQ alarms.

## Rationale
- Serverless event-driven design decouples critical paths like checkout and recommendations to guarantee sub-2-second page loads and high availability.
- Built-in DLQs, AWS KMS encryption, and IAM controls directly satisfy rigorous security, disaster recovery, and GDPR/CCPA compliance constraints.