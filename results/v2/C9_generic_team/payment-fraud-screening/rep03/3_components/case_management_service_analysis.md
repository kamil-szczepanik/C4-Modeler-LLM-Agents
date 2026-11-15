## Overview
[The system is a real-time payment fraud screening platform that screens card-not-present transactions and provides case management tools for fraud analysts. Its core purpose is to evaluate payment authorizations in under 50 ms while maintaining PCI-DSS compliance and 7-year tamper-evident auditability.]

## Key Elements
- Fraud Analysts
- Case Management Service (AWS ECS Fargate modular monolith)
- Read-Optimized Projection Database (AWS RDS Aurora Serverless v2)
- Event Store and Archival (AWS S3 Object Lock and S3 Glacier)
- Asynchronous Message Broker (Amazon SQS with Dead Letter Queue)
- Observability and Tracing (AWS Distro for OpenTelemetry Sidecar)

## Relationships
- Fraud Analysts -> Case Management Service: Reviews suspicious payments and manages fraud cases [HTTPS/TLS 1.3]
- Case Management Service -> Amazon SQS Message Bus: Consumes case review triggers and asynchronous events [Polling / SQS Protocol]
- Case Management Service -> AWS RDS Aurora Serverless v2: Queries and updates read-optimized case projections [PostgreSQL Protocol / TCP]
- Case Management Service -> AWS S3 Object Lock: Appends immutable domain events and event snapshots [AWS SDK / HTTPS]

## Technology Stack
- AWS ECS Fargate: Hosts the case management modular monolith with minimal operational overhead for a 3-person team.
- AWS RDS Aurora Serverless v2: Provides scalable, lightweight storage for read-optimized CQRS projections within the 25,000 EUR monthly budget.
- AWS S3 Object Lock: Guarantees tamper-evident, immutable 7-year event storage satisfying strict compliance mandates (R-06).
- Amazon SQS & Transactional Outbox: Ensures reliable asynchronous message delivery and prevents split-brain states between services.
- AWS Distro for OpenTelemetry: Delivers automated synthetic health checks and tracing without dedicated operations staff.

## Rationale
[This architecture combines an event-sourced CQRS modular monolith on AWS ECS Fargate with serverless storage to meet strict compliance, auditability, and performance constraints within budget. The design minimizes operational complexity, ensuring a three-engineer team can reliably maintain the system and scale securely.]