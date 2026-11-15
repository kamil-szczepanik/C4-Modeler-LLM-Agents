## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing books, managing orders, and providing recommendations. The asynchronous messaging backbone utilizes AWS EventBridge and Amazon SQS to handle event-driven communication across microservices.

## Key Elements
- **Event Bus (AWS EventBridge)**: Central event router utilizing JSON-based rules.
- **Event Archive**: Retains historical domain events for 30 days for disaster recovery.
- **Order Processing Queue (Amazon SQS)**: Buffers order-related events.
- **Recommendation Queue (Amazon SQS)**: Decouples the Recommendation Service from traffic spikes.
- **Catalog Update Queue (Amazon SQS)**: Decouples inventory and product updates.
- **Dead-Letter Queues (DLQs)**: Attached to SQS queues for isolating failed messages.

## Relationships
- **Order & Checkout Service -> AWS EventBridge**: Publishes domain events [HTTPS]
- **AWS EventBridge -> Amazon SQS (Recommendation Queue)**: Forwards filtered events [AWS API / IAM]
- **AWS EventBridge -> Amazon SQS (Catalog Update Queue)**: Routes inventory events [AWS API]
- **Recommendation Service -> Amazon SQS (Recommendation Queue)**: Polls for asynchronous events [HTTPS/Long Polling]
- **Catalog Service -> Amazon SQS (Catalog Update Queue)**: Consumes inventory events [HTTPS/Long Polling]

## Technology Stack
- **AWS EventBridge & Amazon SQS**: Core event-driven messaging backbone for reliable asynchronous communication.
- **AWS KMS & Secrets Manager**: Encrypts event bus payloads and SQS messages at rest using customer-managed keys (CMKs).
- **Terraform / AWS CDK**: Manages infrastructure as code for multi-region deployments.
- **Amazon CloudWatch & AWS X-Ray**: Tracks queue metrics and asynchronous request latency.

## Rationale
This asynchronous architecture isolates microservices to absorb traffic spikes, ensuring 99.95% uptime and performance under 2 seconds. Furthermore, strict encryption, IAM policies, and retention limits satisfy GDPR and CCPA compliance requirements.