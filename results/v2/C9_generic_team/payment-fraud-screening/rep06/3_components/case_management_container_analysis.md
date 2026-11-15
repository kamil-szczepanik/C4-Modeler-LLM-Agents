## Overview
[The Case Management Container manages suspicious payment reviews and review tasks for fraud analysts using AWS ECS with Fargate. It ensures secure, auditable, and resilient case resolution while adhering to strict compliance, budget, and team constraints.]

## Key Elements
- Case Management Container (AWS ECS with Fargate)
- Fraud Analysts
- Amazon Aurora
- Amazon SQS (with Dead Letter Queue)
- Model & Rule Registry Service Container
- Audit & Compliance Container

## Relationships
- Fraud Analysts -> Case Management Container: Interacts with review tasks and suspicious payment reviews [HTTPS/TLS 1.3, RESTful APIs with ETags]
- Case Management Container -> Amazon Aurora: Persists case and review data via logical CQRS [SQL]
- Model & Rule Registry Service Container -> Case Management Container: Supplies rules and models [Internal API]
- Case Management Container -> Audit & Compliance Container: Forwards domain event logs for state transitions [Internal API]
- Amazon SQS -> Case Management Container: Ingests asynchronous case creation events [AWS SDK / SQS Protocol]

## Technology Stack
- AWS ECS with Fargate: Serverless container management minimizing operational overhead for a three-engineer team.
- Amazon Aurora: Relational persistence layer utilizing logical CQRS views and Optimistic Concurrency Control (OCC).
- Amazon SQS: Asynchronous message queue with Dead Letter Queue (DLQ) for decoupled case ingestion.
- OpenAPI: Contract-first API design enforcing strict schema validation and RFC 7807 Problem Details.
- Hexagonal Architecture: Architectural pattern isolating core business logic from delivery and persistence adapters.

## Rationale
[This architecture respects the 25,000 EUR monthly budget and three-engineer limit by utilizing serverless managed services and logical separation over distributed infrastructure. It guarantees strict auditability (R-06) and security (R-05) through hexagonal design, idempotency keys, and explicit domain event logging.]