## Overview
- Event-driven messaging infrastructure for an Amazon-style online bookstore.
- Handles asynchronous order fulfillment, notifications, and microservice decoupling.

## Key Elements
- Amazon SNS Topics: Fan-out publishing for domain events (`OrderEvents`, `InventoryEvents`, `NotificationEvents`).
- Amazon SQS Queues: Point-to-point ingestion and buffering (Fulfillment Queue, Notification Queue, SQS FIFO queues).
- Dead-Letter Queues (DLQs): Poisoned payload isolation with a `maxReceiveCount` of 3.
- ECS Fargate Go Microservices: Event publishers and consumers.
- AWS KMS: Server-side and envelope encryption for PII protection.
- AWS VPC Endpoints (PrivateLink): Internal messaging traffic isolation.

## Relationships
- ECS Fargate Go Microservices -> Amazon SNS Topics: Publishes domain events [AWS SDK via HTTPS/MQTT].
- Amazon SNS Topics -> Amazon SQS Queues: Fans out asynchronous events [AWS SNS-SQS Subscriptions].
- ECS Fargate Go Microservices -> Amazon SQS Queues: Consumes and processes messages [AWS SDK long-polling].
- SQS Queues -> Dead-Letter Queues: Buffers failed messages [AWS SQS Redrive Policy].

## Technology Stack
- Amazon SQS & SNS: Decouples services for 99.95% uptime and asynchronous scalability.
- AWS KMS: Encrypts PII data at rest for GDPR/CCPA compliance.
- AWS PrivateLink: Secures internal communication by bypassing the public internet.
- Terraform: Provisions multi-region infrastructure across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- AWS X-Ray: Traces requests across asynchronous boundaries.

## Rationale
- Decouples microservices to handle 1M MAU and peak traffic without dropped transactions.
- Enforces strict security, encryption, and regional redundancy to meet compliance and uptime SLAs.