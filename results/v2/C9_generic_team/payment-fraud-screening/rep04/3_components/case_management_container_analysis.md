## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages suspicious payment reviews for fraud analysts. Its core purpose is to screen transactions in under 50 ms while ensuring PCI-DSS compliance and 7-year auditability within a strict budget.]

## Key Elements
* Fraud Analysts
* Payment Gateway
* API Gateway / Ingress Container
* Real-Time Scoring Container
* Case Management Container
* Audit Logging Container
* Amazon S3 with S3 Object Lock
* AWS SQS / Kinesis
* AWS Secrets Manager / Parameter Store
* AWS RDS PostgreSQL

## Relationships
* Fraud Analysts -> Case Management Container: Reviews flagged transactions [HTTPS]
* API Gateway -> Real-Time Scoring Container: Forwards authorization requests [gRPC/REST]
* Case Management Container -> AWS RDS PostgreSQL: Persists case states and audit records [TCP/SQL]
* Case Management Container -> Audit Logging Container: Dispatches audit events [AWS SQS / Kinesis]

## Technology Stack
* AWS ECS with AWS Fargate: Chosen for container orchestration without Kubernetes management overhead, fitting the 3-engineer team and 25,000 EUR budget.
* AWS RDS PostgreSQL: Provides transactional integrity, relational storage, and support for Optimistic Concurrency Control (OCC).
* CQRS, Repository, and Service Layer Patterns: Separates read models, write operations, and business logic for high performance and maintainability.
* Finite State Machine & RFC 7807: Manages analyst case workflows and provides standardized problem details API error handling.
* Flyway / Liquibase & Pact: Ensures automated zero-downtime database migrations and contract testing.

## Rationale
[This architecture utilizes serverless container orchestration and managed relational storage to minimize operational overhead for a three-engineer team while strictly respecting the 25,000 EUR monthly infrastructure budget. Explicit state management, CQRS, and robust auditing patterns satisfy rigorous PCI-DSS compliance and 7-year auditability mandates without sacrificing sub-50ms transaction processing performance.]