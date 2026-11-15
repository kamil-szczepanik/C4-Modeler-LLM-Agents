## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations and provides an interface for fraud analysts to review suspicious transactions. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms decision latency at 3,000 TPS within a strict €25,000 monthly budget.

## Key Elements
- Cardholder / End Customer
- Fraud Operations Analyst
- Risk Manager / Quant
- Fraud Ops Team Lead / Administrator
- AWS Application Load Balancer (ALB)
- Scoring Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- Amazon Aurora Serverless
- Amazon S3 with Object Lock
- AWS KMS
- AWS IAM Identity Center

## Relationships
- Application Load Balancer -> Scoring Container: Routes payment authorization requests [HTTPS / Internal TLS]
- Application Load Balancer -> Case Management Container: Routes case management traffic [Internal TLS / mTLS]
- Scoring Container -> Amazon Aurora Serverless: Reads rules and stores audit logs [TCP/TLS with PgBouncer]
- Case Management Container -> Amazon Aurora Serverless: Reads and writes case data [Internal TCP/TLS with PgBouncer]
- Case Management Container -> Amazon S3 with Object Lock: Emits signed audit logs [AWS SDK / HTTPS]
- Case Management Container -> AWS Secrets Manager: Fetches database credentials [AWS SDK / HTTPS]

## Technology Stack
- **Compute:** AWS ECS Fargate for serverless container orchestration with auto-scaling based on latency.
- **Database:** Amazon Aurora Serverless with PgBouncer connection pooling for cost-effective relational storage.
- **Audit Storage:** Amazon S3 with Object Lock for tamper-evident 7-year audit retention.
- **Security & IAM:** AWS KMS for encryption, AWS IAM Identity Center and RBAC for access control.
- **Observability:** AWS CloudWatch for centralized logging and metrics aggregation.

## Rationale
This architecture uses serverless AWS components to meet strict performance and auditability requirements while enforcing a fixed €25,000 monthly budget. Zero-trust networking, application-layer token masking, and immutable storage ensure full PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.