## Overview
The Case Management Backend processes fraud review workflows for payment analysts using an isolated, scalable microservice architecture. It provides high-performance REST/GraphQL APIs and asynchronous bulk processing while maintaining strict PCI-DSS compliance and auditability.

## Key Elements
- Case API Controller (AWS ECS Fargate, Node.js/Express/Fastify)
- Workflow Engine Component (Node.js/TypeScript)
- Batch Processing Worker Component (AWS ECS Fargate)
- Notification & Telemetry Component (Node.js/TypeScript)
- Audit Dispatcher Component (Node.js/TypeScript)
- PostgreSQL Database (AWS RDS with AWS KMS encryption)
- Asynchronous Job Queue (Amazon SQS / Redis on Amazon ElastiCache with DLQ)

## Relationships
- Analyst & Rules Portal -> Case API Controller: Submits REST/GraphQL requests [HTTPS/REST/GraphQL]
- Case API Controller -> Asynchronous Job Queue: Enqueues bulk requests [AWS SQS / Redis protocol]
- Batch Processing Worker Component -> Workflow Engine Component: Executes state transitions [In-process function calls]
- Workflow Engine Component -> PostgreSQL Database: Persists case state [PostgreSQL wire protocol over TLS 1.3]
- Audit Dispatcher Component -> Audit & Event Stream: Streams immutable audit events [Amazon EventBridge]
- Notification & Telemetry Component -> Analyst & Rules Portal: Pushes job status updates [WebSockets]

## Technology Stack
- AWS ECS Fargate: Container orchestration ensuring serverless operational simplicity for a 3-engineer team.
- Node.js & TypeScript: Runtime and language for rapid API development with strict schema validation (Zod/Joi).
- AWS RDS PostgreSQL: Relational storage for transactional case states, protected via AWS KMS and AWS Secrets Manager.
- Amazon SQS / Redis: Asynchronous job queuing preventing gateway timeouts during bulk decisioning.
- AWS X-Ray & CloudWatch: Distributed tracing and monitoring enforcing system observability.

## Rationale
This architecture balances strict 7-year auditability and PCI-DSS Level 1 compliance with a fixed €25k monthly budget through serverless scaling and managed AWS services. Separating real-time APIs from batch workers protects database performance, ensuring rapid analyst workflows under heavy transaction loads.