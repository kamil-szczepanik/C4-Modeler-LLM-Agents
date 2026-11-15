## Overview
The Review Service is a containerized microservice within the Online Bookstore platform that manages customer reviews, ratings, and moderation workflows. It ensures high scalability, GDPR compliance, and event-driven integration with core e-commerce services.

## Key Elements
- Shopper / Reviewer (User)
- Store Administrator (User)
- Review Service (AWS ECS Fargate Container)
- Review Controller (Node.js/Express Component)
- Moderation & Sanitization Engine (Component)
- Review Repository (TypeORM Component)
- Rating Aggregator (Background Worker Component)
- Amazon Aurora PostgreSQL (Database)
- Amazon EventBridge (Event Bus)
- Notification Service (External System)
- Catalogue Service (External System)

## Relationships
- API Gateway & Security -> Review Controller: Routes gRPC traffic [gRPC with mTLS]
- Review Repository -> Amazon Aurora PostgreSQL: Executes SQL queries [TCP/5432 via VPC, TLS 1.3]
- Review Service -> Notification Service: Publishes review prompt events [Amazon SNS/SQS, JSON]
- Review Service -> Amazon EventBridge: Publishes `ReviewCreated` and `RatingUpdated` domain events [JSON via AWS SDK]
- Amazon EventBridge -> Catalogue Service: Dispatches rating updates [JSON over SQS/EventBridge]

## Technology Stack
- Node.js & Express: Runtime and framework for the Review Controller providing lightweight, asynchronous gRPC handling.
- TypeORM: Object-Relational Mapper for managing data models and secure queries against Amazon Aurora PostgreSQL.
- Amazon Aurora PostgreSQL: Relational database managed with AWS KMS (AES-256) encryption at rest for persistence.
- Amazon EventBridge: Serverless event bus utilized for asynchronous domain event distribution.
- AWS ECS Fargate: Container orchestration platform deployed behind an Internal Network Load Balancer (NLB) with rolling updates.
- OpenTelemetry: Observability framework utilized for distributed tracing and Prometheus-compatible metrics export.

## Rationale
This decoupled event-driven architecture isolates write-heavy review submissions from read-heavy catalogue browsing to maintain sub-2-second page loads and 99.95% uptime. Strict component isolation, role-based JWT validation, and automated GDPR deletion triggers satisfy stringent security and compliance requirements.