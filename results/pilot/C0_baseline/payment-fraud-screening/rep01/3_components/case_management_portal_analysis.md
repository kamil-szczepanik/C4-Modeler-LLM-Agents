## Overview
The Case Management Portal provides fraud analysts with an investigative interface to review suspicious payment transactions flagged by the real-time scoring engine. It ensures rapid triage and compliance with strict regulatory frameworks while protecting sensitive cardholder data.

## Key Elements
- Fraud Analysts
- React Web UI (TypeScript)
- NestJS API Controller
- Case Service (TypeScript)
- Prisma ORM (Data Access Layer)
- Amazon RDS for PostgreSQL
- External Identity Provider
- Audit Storage (Amazon S3 with S3 Object Lock)

## Relationships
- Fraud Analysts -> React Web UI: Investigate flagged transactions and manage cases [HTTPS/TLS 1.3]
- React Web UI -> NestJS API Controller: Invoke REST endpoints and fetch investigation data [HTTPS/TLS 1.3]
- NestJS API Controller -> Case Service: Execute business logic for case resolution [In-memory]
- Case Service -> Prisma ORM: Query and persist case metadata [Internal]
- Prisma ORM -> Amazon RDS for PostgreSQL: Persist relational case data [TCP/SSL, TLS 1.3, IAM authentication]
- NestJS API Controller -> External Identity Provider: Authenticate users and validate tokens [OIDC/JWT]
- NestJS API Controller -> Audit Storage: Retrieve historical decision explanations [Secure REST]

## Technology Stack
- React, TypeScript: Powers the analyst web UI for rapid, responsive case triage.
- NestJS, TypeScript: Provides a structured, scalable REST API controller architecture.
- Prisma ORM: Manages type-safe database access and parameterized queries to prevent injection vectors.
- Amazon RDS for PostgreSQL: Stores relational case data securely with automated Multi-AZ failover and AWS KMS encryption at rest.
- AWS ECS Fargate: Runs containerized services without manual server provisioning to fit the 3-engineer team constraint.

## Rationale
This architecture balances strict PCI-DSS Level 1 security and 7-year auditability requirements with a cost-effective, easily maintainable serverless cloud footprint. By utilizing managed AWS services, isolated private subnets, and strict data masking, it protects cardholder data while empowering a small engineering team to operate within budget.