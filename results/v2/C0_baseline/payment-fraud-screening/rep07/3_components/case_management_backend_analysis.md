## Overview
[The Case Management Backend is a Node.js and TypeScript container running on AWS ECS Fargate that processes fraud analyst reviews and audit logs for the Real-Time Payment Fraud Screening system. It enforces strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while staying within a 25,000 EUR monthly budget.]

## Key Elements
- API Router / Controller (TypeScript, Express/Fastify)
- Case Workflow Service (TypeScript)
- Audit & Compliance Logger (TypeScript)
- Messaging Consumer/Publisher (TypeScript)
- Masking & Sanitization Middleware (TypeScript)
- PostgreSQL Database (Amazon RDS PostgreSQL)
- Audit Storage (Amazon S3 with Object Lock)
- Messaging Bus (Amazon SQS / EventBridge)

## Relationships
- API Router -> Case Workflow Service: Invokes business logic [Internal Function Call]
- API Router -> Masking & Sanitization Middleware: Sanitizes payloads [Internal Function Call]
- Case Workflow Service -> Audit & Compliance Logger: Triggers immutable logging [Internal Function Call]
- Case Workflow Service -> PostgreSQL Database: Persists case state [TypeORM/Prisma via PostgreSQL Protocol]
- Audit & Compliance Logger -> Audit Storage (Amazon S3): Writes cryptographically signed audit logs [HTTPS/S3 API]

## Technology Stack
- Node.js & TypeScript: Enables rapid iteration and workflow logic within a three-engineer team constraint
- AWS ECS Fargate: Provides container orchestration while maintaining a single tightly controlled security perimeter
- Amazon RDS PostgreSQL: Persists transactional case data securely with AWS KMS-managed encryption at rest
- Amazon S3 Object Lock: Stores tamper-evident, cryptographically signed audit logs for 7-year regulatory compliance
- AWS Secrets Manager: Manages database credentials with automated rotation directly in ECS task definitions

## Rationale
[This architecture unifies core backend logic within AWS ECS Fargate to satisfy PCI-DSS Level 1 boundaries and simplify IAM enforcement. Asynchronous audit logging and in-memory buffering ensure sub-second analyst UX while meeting strict auditability requirements.]