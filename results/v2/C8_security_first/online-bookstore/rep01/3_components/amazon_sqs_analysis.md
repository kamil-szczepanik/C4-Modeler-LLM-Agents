## Overview
The Online Bookstore system uses Amazon SQS to asynchronously decouple order processing and ensure reliable, scalable checkout workflows. It guarantees message delivery, performance, and GDPR/CCPA compliance across multi-region deployments.

## Key Elements
- Order & Checkout Service (Java, Spring Boot, AWS ECS on Fargate)
- Queue Manager Engine (AWS SQS Managed)
- Access Control & Encryption Module (AWS IAM, AWS KMS)
- Dead Letter Queue (DLQ) Routing Component (Amazon SQS DLQ)
- Inventory & Fulfillment Service (AWS ECS on Fargate)
- Observability & Monitoring (Amazon CloudWatch, AWS X-Ray, AWS CloudTrail)

## Relationships
- Order & Checkout Service -> Queue Manager Engine: Enqueues order payloads [AWS SDK / HTTPS]
- Queue Manager Engine -> Access Control & Encryption Module: Validates policy and decrypts/encrypts [Internal AWS API]
- Queue Manager Engine -> DLQ Routing Component: Offloads failed messages [Internal AWS API]
- Queue Manager Engine -> Inventory & Fulfillment Service: Dispatches queued order events [AWS SDK / SQS Long Polling]

## Technology Stack
- Amazon SQS: Message queue for asynchronous decoupling and reliability
- AWS IAM & KMS: Least-privilege access control and encryption at rest (CMK with annual rotation)
- TLS 1.2+: Enforced encryption in transit (`aws:SecureTransport`)
- Amazon CloudWatch & AWS X-Ray: Scalability metrics, queue depth monitoring, and distributed tracing
- Terraform / AWS CDK: Infrastructure-as-code management for queues, DLQs, and alarms

## Rationale
This architecture ensures 99.95% uptime and handles 1M MAU by buffering checkout traffic against downstream outages. It maintains strict GDPR/CCPA data protection standards via IAM, KMS, and localized regional queues.