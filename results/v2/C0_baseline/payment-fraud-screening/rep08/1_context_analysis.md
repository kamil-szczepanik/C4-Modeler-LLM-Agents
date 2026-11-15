## Overview
Real-Time Payment Fraud Screening system providing instant sub-50ms risk scoring for card-not-present transactions and case management for fraud analysts. Built to ensure PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a strict budget and small engineering team.

## Key Elements
- **Payment Gateway / Merchants**: External API clients submitting authorization requests.
- **Fraud Analysts & Risk Managers**: Internal users reviewing suspicious payments and updating models.
- **Identity Provider**: AWS Cognito / Okta for OIDC/OAuth2 authentication.
- **API Gateway & Fargate Services**: AWS API Gateway and AWS ECS on Fargate containers for low-latency request handling and scoring.
- **WORM Audit Storage**: AWS S3 Object Lock with compliance mode and SHA-256 cryptographic hashing.
- **BI / Analytics Tool**: Amazon QuickSight for aggregated metric reporting via isolated data pipelines.

## Relationships
- **Payment Gateway to API Gateway**: Synchronous gRPC/REST over mTLS for real-time scoring requests.
- **Analysts to Case Management UI**: HTTPS (TLS 1.3) with MFA and RBAC/ABAC enforcement.
- **Scoring Engine to WORM Storage**: Asynchronous event logging storing inputs, model versions, and explanations.
- **WORM Storage to BI Tool**: Asynchronous data pipeline (AWS DMS / S3 triggers) using pseudonymized data.

## Technology Stack
- **Compute**: AWS ECS on Fargate for predictable sub-50ms P99 latency without serverless cold starts.
- **Security & Encryption**: AWS KMS with customer-managed keys (CMK), TLS 1.3, and mTLS for data in transit and at rest.
- **Auditability**: AWS S3 Object Lock with SHA-256 Merkle trees for tamper-evident 7-year log retention.
- **CI/CD & Deployments**: AWS CodePipeline using GitOps for zero-downtime model updates.
- **Identity**: AWS Cognito or Okta for OIDC/OAuth2 authentication and authorization.

## Rationale
AWS managed services minimize operational overhead for a 3-engineer team while satisfying strict PCI-DSS Level 1 and auditability mandates. ECS Fargate and dedicated data pipelines ensure high performance and strict data isolation within the fixed €25k monthly budget.