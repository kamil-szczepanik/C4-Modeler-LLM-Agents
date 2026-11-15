## Overview
An AWS-hosted online bookstore container architecture providing scalable product cataloging, secure checkout, and user reviews. Designed to handle 1M MAU with 99.95% uptime while ensuring GDPR compliance.

## Key Elements
- **Review API Controller**: Django REST Framework endpoint handling CRUD operations and filtering.
- **Event Consumer Component**: Celery worker processing `OrderCompleted` and `UserDeletionRequested` events.
- **Engagement Engine**: Python module calculating aggregate ratings and helpful votes.
- **Data Access Layer**: Django ORM interfacing with database storage.
- **Amazon Aurora PostgreSQL**: Relational database storing reviews, votes, and aggregates.
- **Amazon EventBridge & SQS**: Event bus and message queue handling asynchronous integrations.
- **Amazon ECS (Fargate)**: Container execution environment with Auto Scaling.

## Relationships
- **Edge & Ingress** -> **Review API Controller**: Forwards review requests via [gRPC over TLS].
- **Amazon EventBridge** -> **Event Consumer Component**: Delivers `OrderCompleted` and `UserDeletionRequested` events via [AWS SQS].
- **Review API Controller** -> **Amazon Aurora PostgreSQL**: Queries and persists review data via [TCP/PostgreSQL Protocol].

## Technology Stack
- **Python / Django**: Core framework chosen for rapid development of API and business logic.
- **Amazon Aurora PostgreSQL**: Relational database providing ACID compliance and JSON support for local read models.
- **Celery**: Asynchronous task queue for handling event consumers and GDPR anonymization.
- **Amazon ECS (Fargate)**: Serverless container orchestration ensuring zero-infrastructure management for 1M MAU scalability.
- **Amazon EventBridge**: Event bus decoupling cross-container communication for high availability.

## Rationale
Event-driven decoupling via Amazon EventBridge prevents blocking synchronous calls, ensuring 99.95% availability during checkout degradation. Local data projection and Amazon Aurora PostgreSQL indexes support sub-second query performance to meet the <2s page load SLA.