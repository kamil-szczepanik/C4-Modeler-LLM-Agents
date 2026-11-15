## Overview
[The Customer Review Service manages customer reviews, 5-star ratings, and content moderation for the Online Bookstore platform. It provides high-throughput, low-latency review operations while ensuring GDPR/CCPA compliance and OWASP security mitigations.]

## Key Elements
*   Review Controller (Express Router)
*   Review Validation & Sanitization Engine (Joi / DOMPurify)
*   Moderation & Compliance Manager
*   Review Data Access Layer (AWS SDK)
*   Event Publisher (AWS SDK)
*   Amazon DynamoDB
*   Amazon EventBridge with SQS Dead Letter Queues (DLQs)
*   AWS ECS Fargate & Application Load Balancer
*   Redis (ElastiCache)

## Relationships
*   AWS API Gateway -> Review Controller: Routes review REST/HTTPS requests [HTTPS / JSON]
*   Review Controller -> Validation Engine & Moderation Manager: Invokes internal workflows [In-memory]
*   Moderation Manager & Review Controller -> Review Data Access Layer -> Amazon DynamoDB: Reads and writes review records [AWS SDK]
*   Event Publisher -> Amazon EventBridge: Emits `ReviewSubmitted`, `ReviewDeleted`, and `UserAnonymized` events [AWS SDK]
*   Amazon EventBridge -> Amazon SQS DLQs: Handles failed asynchronous event deliveries [AWS SQS]

## Technology Stack
*   Node.js / Express: Core runtime for lightweight, scalable service endpoints.
*   Amazon DynamoDB: NoSQL database selected for single-digit millisecond latency to handle 1M MAU.
*   Joi & DOMPurify: Sanitization and validation libraries for OWASP Top-10 XSS mitigations.
*   Amazon EventBridge & SQS: Event bus and DLQs for decoupled, reliable asynchronous event-driven workflows.
*   Redis (ElastiCache): Distributed cache for API rate limiting against bot spam.

## Rationale
[This architecture uses decoupled asynchronous event publishing to maintain single-digit millisecond response times without blocking review submissions. It guarantees high availability and regulatory compliance through managed AWS infrastructure and isolated moderation components.]