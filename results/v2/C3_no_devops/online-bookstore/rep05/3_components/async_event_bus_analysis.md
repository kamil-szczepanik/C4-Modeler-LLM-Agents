## Overview
The Async Event Bus is a resilient asynchronous messaging infrastructure for the Online Bookstore, handling event distribution across microservices. It ensures decoupled, highly available, and scalable operations for retail workflows.

## Key Elements
- Event Router & Bus (Amazon EventBridge / SNS)
- Message Queues (Amazon SQS)
- DLQ Handler (Amazon SQS + AWS Lambda)
- Event Schema Registry (Amazon EventBridge Schema Registry)
- Core Microservices and Third-Party Shipping API

## Relationships
- Core Microservices -> Event Router: Publish domain events with AWS SigV4 [HTTPS]
- Event Router -> Event Schema Registry: Validate event payload structure [Internal AWS API]
- Event Router -> Message Queues: Fan-out valid events to subscriber queues [SQS Protocol]
- Message Queues -> Third-Party Shipping: Trigger fulfillment [HTTPS/REST]
- Message Queues -> DLQ Handler: Capture and scrub poisoned messages [SQS/Lambda]

## Technology Stack
- Amazon EventBridge & SNS: For high-throughput event routing and pub/sub messaging
- Amazon SQS: For buffering decoupled workloads to absorb traffic spikes and guarantee delivery
- AWS Lambda: For running serverless DLQ scrubbing and alerting logic
- Amazon EventBridge Schema Registry: For validating JSON event payloads and preventing malformed data propagation
- AWS KMS: For at-rest encryption of PII using customer-managed keys (CMK)

## Rationale
This architecture guarantees 99.95% uptime and high scalability by decoupling core checkout processes from external dependencies. Strict schema validation, IAM access controls, and KMS encryption ensure compliance with GDPR/CCPA and OWASP standards.