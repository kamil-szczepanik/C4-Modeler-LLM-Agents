## Overview
The Review & Moderation Service manages compliance-heavy customer reviews, ratings, and moderation workflows for the Online Bookstore. It balances community engagement with strict regulatory compliance via automated toxicity detection and role-based access control.

## Key Elements
- **Review API Controller**: Handles incoming REST/GraphQL traffic and JWT-validated RBAC.
- **Moderation Engine**: Executes automated NLP/toxicity checks and quarantines abusive content.
- **Compliance Manager**: Handles GDPR/CCPA data deletions, anonymization, and Right of Access exports.
- **Event Publisher**: Dispatches domain events asynchronously to the messaging bus.
- **Export Aggregator**: Streams user review history securely to cloud storage.
- **Review Data Access Layer**: Interfaces with the primary database.

## Relationships
- **Review API Controller -> Moderation Engine**: Passes submitted reviews [In-process function call]
- **Moderation Engine -> Review Data Access Layer**: Persists approved and quarantined statuses [TCP via TLS 1.3]
- **Compliance Manager -> Messaging Bus**: Consumes user-deletion events and publishes exports [Amazon SQS/SNS]
- **Event Publisher -> Messaging Bus**: Publishes moderation and export events [Amazon SNS/SQS via outbox pattern]
- **Export Aggregator -> Amazon S3**: Streams export payloads for secure presigned-url generation [HTTPS]

## Technology Stack
- **Node.js / Express**: Core runtime and framework for all service components.
- **Amazon DocumentDB (MongoDB-compatible)**: Stores semi-structured review schemas with encryption at rest via AWS KMS.
- **Amazon ECS with Fargate**: Container orchestration providing auto-scaling based on CPU, memory, and SQS queue depth.
- **Amazon SQS / SNS with DLQ**: Asynchronous messaging bus ensuring event delivery resilience and error isolation.
- **AWS X-Ray & OpenTelemetry**: Distributed tracing and observability instrumentation.
- **Joi / Zod**: Input schema validation preventing NoSQL injection and XSS.

## Rationale
Decomposing the service into specialized internal components isolates compliance, moderation, and data access logic to maintain high availability and performance. Leveraging managed AWS services like Fargate and DocumentDB ensures scalable, secure handling of peak retail traffic while strictly enforcing GDPR and CCPA requirements.