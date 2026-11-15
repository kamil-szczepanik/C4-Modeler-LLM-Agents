## Overview
An AWS-hosted online bookstore utilizing an asynchronous background worker container architecture to process events, notifications, and third-party integrations. It ensures reliable, scalable, and observable e-commerce operations.

## Key Elements
- Background Worker Container: AWS ECS/EKS tasks handling asynchronous processing
- Message Broker: AWS SQS and AWS SNS for pub/sub pipelines and queue segmentation (`high-priority`, `default`, `bulk`)
- Dead-Letter Queues (DLQ): SQS DLQs with isolation and triage/replay mechanisms
- External Integrations: Third-Party Shipping Providers, Payment Gateways, and Notification Services via HTTPS
- Observability: AWS X-Ray and OpenTelemetry for distributed tracing

## Relationships
- Checkout & Order Container -> AWS SQS/SNS: Publishes asynchronous domain events [AWS SQS]
- Background Worker Container -> Notification Services: Sends asynchronous email/SMS notifications [HTTPS]
- Background Worker Container -> Third-Party Shipping Providers: Communicates fulfillment and tracking requests [HTTPS]
- Background Worker Container -> AWS SQS DLQ: Isolates poisoned messages after max-receive count is exceeded [AWS SQS]

## Technology Stack
- AWS ECS/EKS: Container orchestration ensuring zero-data-loss graceful shutdowns via `SIGTERM` signals
- AWS SQS/SNS: Message transport utilizing payload envelopes, W3C Trace Context headers, and idempotency keys
- Resilience4j/Polly: Circuit breaker and exponential backoff libraries for external API protection
- Redis / DynamoDB: Distributed locking for atomic state management during message redelivery
- OpenTelemetry & AWS X-Ray: Distributed tracing across asynchronous boundaries

## Rationale
Queue segmentation and priority routing protect critical transactional workloads from heavy batch jobs, safeguarding the 99.95% availability target. Circuit breakers, idempotency keys, and DLQs ensure resilience and data integrity against third-party API failures.