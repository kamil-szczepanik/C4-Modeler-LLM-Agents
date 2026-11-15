## Overview
The Case Management Backend is an AWS ECS Fargate-based container service that processes asynchronous flagged payment events and provides a secure portal for fraud analysts to review suspicious transactions. It ensures strict 7-year auditability and PCI-DSS compliance while supporting real-time decision workflows for a 3-engineer team.

## Key Elements
- **API Controller Component**: RESTful interface handling authentication, RBAC, input validation, and bulk case operations over HTTPS.
- **Case Workflow Engine Component**: Manages case states (Open, Under Review, Resolved) and bulk resolution logic.
- **Event Consumer Component**: Subscribes to Amazon SQS to ingest flagged transaction payloads and hydrate case records.
- **Audit Logger Component**: Streams immutable records to S3 Object Lock (Compliance Mode) and maintains an indexed metadata view in Amazon Aurora PostgreSQL.
- **SLA Metrics Component**: Calculates time-to-decision metrics for compliance and operational tracking.
- **RDS Proxy**: Manages database connection pooling between ECS Fargate tasks and Amazon Aurora PostgreSQL.

## Relationships
- Fraud Analyst / Merchant Risk Manager -> API Controller Component: Reviews cases and monitors metrics via [HTTPS] with [mTLS] and [OAuth2/OIDC]
- Event Consumer Component -> Amazon SQS: Consumes transaction messages via [AWS SDK / SQS API]
- Case Workflow Engine Component -> Amazon Aurora PostgreSQL: Persists case records and SLA metrics via [RDS Proxy] using [mTLS] and [AWS IAM]
- Audit Logger Component -> Amazon S3: Stores tamper-evident logs via [AWS SDK / S3 API] with [Object Lock]

## Technology Stack
- **Compute**: AWS ECS Fargate to minimize operational overhead for a 3-engineer team within the €25k/month budget.
- **Language**: TypeScript/Node.js or Go for rapid development and high concurrency.
- **Database**: Amazon Aurora PostgreSQL backed by RDS Proxy to handle connection pooling and failovers.
- **Storage**: Amazon S3 with Object Lock (Compliance Mode) for 7-year tamper-evident audit logging (R-06).
- **Messaging**: Amazon SQS with a Dead Letter Queue (DLQ) for asynchronous event ingestion.
- **Security**: AWS Secrets Manager, AWS KMS, AWS X-Ray, and OAuth2/OIDC with MFA.

## Rationale
This architecture balances strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability with a lean operational model suited for a 3-engineer team. Leveraging managed AWS services like ECS Fargate, S3 Object Lock, and RDS Proxy ensures high availability and resilience within the €25,000 monthly budget.