## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages case reviews for analysts. It ensures PCI-DSS Level 1 compliance while maintaining strict auditability and high availability.

## Key Elements
- Node.js Case Management Container (Node.js/TypeScript on AWS ECS Fargate)
- API Router / Controller (Express/Fastify)
- Case Workflow Service
- Audit & Compliance Logger
- Data Access Repository (Prisma/TypeORM)
- Decision Feedback Publisher
- Amazon Aurora PostgreSQL Serverless v2
- AWS QLDB
- Amazon SQS / EventBridge
- AWS Cognito & AWS Secrets Manager
- AWS KMS

## Relationships
- Fraud Analyst -> Node.js Case Management: Manages cases via HTTPS (OAuth2/OIDC via AWS Cognito)
- API Router -> Case Workflow Service: In-process function calls
- Case Workflow Service -> Data Access Repository: In-process calls
- Case Workflow Service -> Audit & Compliance Logger: Asynchronous event emission
- Audit & Compliance Logger -> AWS QLDB: Dispatches tamper-evident audit records via HTTPS/TLS (AWS SDK)
- Data Access Repository -> Amazon Aurora PostgreSQL Serverless v2: Reads/writes state via TLS with parameterization
- Case Workflow Service -> Decision Feedback Publisher: In-process event dispatch upon resolution
- Decision Feedback Publisher -> Amazon SQS / EventBridge: Publishes feedback messages via HTTPS/SigV4

## Technology Stack
- Node.js & TypeScript: Rapid development framework for case management APIs within engineering constraints.
- AWS ECS Fargate: Container orchestration avoiding server management for a 3-engineer team.
- Amazon Aurora PostgreSQL Serverless v2: Auto-scaling relational database fitting variable workloads within the budget.
- AWS QLDB: Tamper-evident ledger ensuring immutable, cryptographically verifiable 7-year audit trails.
- Amazon SQS / EventBridge: Decoupled asynchronous messaging for non-blocking feedback loops.
- AWS KMS: Field-level encryption and tokenization for PCI-DSS compliance.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while respecting a fixed budget. Strict boundary isolation, KMS encryption, and QLDB immutability satisfy rigorous PCI-DSS Level 1 compliance and 7-year auditability constraints.