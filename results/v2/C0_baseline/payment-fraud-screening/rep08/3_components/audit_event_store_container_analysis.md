## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst reviews. It ensures PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail within a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analysts & Risk Managers
- Compliance Officers & External Auditors
- API Gateway & Routing Layer (AWS API Gateway / ALB)
- Scoring Engine Container (Go or Rust on AWS Fargate Spot)
- Case Management Container (Node.js / React SPA backend with Amazon RDS PostgreSQL)
- Audit & Event Store Container (Amazon DynamoDB & S3 with Object Lock)
- Messaging Backbone (Amazon SQS / SNS)
- Model Storage & Management (Amazon S3 & AWS Secrets Manager)
- Identity Provider

## Relationships
- Case Management Container -> Audit & Event Store Container: Writes audit logs and events [AWS SDK (DynamoDB API)]
- Compliance Officers / External Auditors -> Audit Query API: Queries historical decisions and exports reports [REST API / HTTPS with OAuth2/OIDC, mTLS, IAM SigV4]
- Messaging Backbone (SQS) -> Ingestion Service: Processes audit events [AWS SDK]

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring localized data residency and compliance.
- Amazon DynamoDB: Provides low-overhead, highly available real-time event capture and queries.
- Amazon S3 with Object Lock (Compliance Mode): Guarantees 7-year tamper-evident immutability natively.
- AWS KMS: Manages Customer Managed Keys with automated rotation for encryption at rest.
- Terraform: Enforces infrastructure-as-code, S3 Lifecycle Policies, and automated backups.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while satisfying strict PCI-DSS compliance and 7-year auditability. Automated tiering and serverless components maintain high availability and performance within the 25,000 EUR monthly budget constraint.