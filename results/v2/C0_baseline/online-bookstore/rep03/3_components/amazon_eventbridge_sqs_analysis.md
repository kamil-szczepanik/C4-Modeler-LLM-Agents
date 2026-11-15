## Overview
The Online Bookstore is a scaled-down, multi-region e-commerce platform designed to process book purchases, secure checkouts, and customer recommendations. It utilizes an asynchronous event-driven architecture to guarantee high availability and scale smoothly to 1M monthly active users.

## Key Elements
- **Event Bus (Amazon EventBridge):** Central JSON-based router for publishing and filtering domain events.
- **Order Processing Queue (Amazon SQS):** Decouples checkout services from downstream fulfillment and buffers order payloads.
- **Notification Queue (Amazon SQS):** Queues alerts and messages for customer notifications.
- **Dead-Letter Queue (Amazon SQS):** Captures poisoned or failed messages for administrative debugging.
- **Checkout Service, Recommendations Service, Notification Service:** Microservices producing and consuming asynchronous events.

## Relationships
- **Checkout Service -> Event Bus (Amazon EventBridge):** Publishes domain events like `OrderPlaced` [HTTPS / AWS SDK]
- **Event Bus -> Order Processing Queue (Amazon SQS):** Routes filtered domain events via EventBridge Rule targets [AWS SQS API]
- **Order Processing Queue -> Notification Service:** Delivers asynchronous events [AWS SQS Long Polling]
- **Recommendations Service -> Event Bus (Amazon EventBridge):** Publishes and consumes behavioral events [HTTPS / AWS SDK]

## Technology Stack
- **AWS EventBridge:** Serves as the content-based event router for scalable domain event propagation.
- **AWS SQS Standard/FIFO:** Provides message buffering, durability, and backpressure management.
- **AWS KMS (Customer Managed Keys):** Encrypts payloads at rest for compliance and security.
- **Terraform / AWS CDK:** Defines Infrastructure as Code with strict least-privilege IAM policies.

## Rationale
This architecture ensures 99.95% uptime and high scalability by decoupling core microservices through asynchronous message queues. It maintains robust security and data protection standards via strict IAM boundaries, KMS encryption, and centralized dead-letter queue monitoring.