## Overview
The Event Bus & Integration container provides asynchronous event routing, messaging, and data streaming for the Online Bookstore. It decouples microservices, securely integrates with third-party APIs, and maintains GDPR/CCPA compliance.

## Key Elements
- Event Router (`AWS EventBridge`)
- Notification Queue (`Amazon SQS`)
- Integration Dispatcher (`AWS Lambda`)
- Audit Streamer (`Amazon Kinesis Data Firehose`)
- Notification Status Tracker (`Amazon DynamoDB / AWS Lambda`)
- Dead Letter Queues (DLQs) and S3 Audit Store

## Relationships
- Core E-Commerce Container -> Event Router: Publishes domain events [JSON over AWS SNS/EventBridge]
- Event Router -> Notification Queue: Forwards background tasks [AWS SQS]
- Notification Queue -> Integration Dispatcher: Triggers asynchronous processing [AWS Lambda Event Source Mapping]
- Event Router -> Audit Streamer: Streams order lifecycle events [AWS EventBridge Target / Kinesis]
- Audit Streamer -> Secure Analytics Store (S3): Persists immutable audit logs [HTTPS / AWS S3 API]

## Technology Stack
- AWS EventBridge: Selected for content-based event routing across microservices.
- Amazon SQS & DLQs: Chosen for asynchronous backpressure handling and isolation of poisoned messages.
- AWS Lambda: Used for secure third-party webhook dispatching and PII tokenization.
- Amazon Kinesis Data Firehose: Deployed for high-throughput, scalable audit logging.
- AWS KMS: Enforces encryption-at-rest with customer-managed keys (CMKs) for all message buses and stores.

## Rationale
This architecture guarantees 99.95% uptime and reliable message processing through decoupled queuing and idempotent execution. It satisfies strict GDPR/CCPA compliance mandates via TLS 1.3 encryption, KMS key management, and edge PII masking.