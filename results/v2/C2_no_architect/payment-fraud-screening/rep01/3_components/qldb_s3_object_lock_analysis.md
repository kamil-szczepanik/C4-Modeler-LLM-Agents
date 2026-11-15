## Overview
The system is a real-time payment fraud screening platform for a mid-size payment processor. Its core purpose is to evaluate card-not-present payment authorizations and manage fraud reviews.

## Key Elements
- Fraud Analyst & Compliance Auditor
- External Payment Gateway & GitHub Actions
- AWS ECS Fargate Containers (API Gateway, Scoring Engine, Case Management)
- Amazon SageMaker Serverless Inference
- Amazon Aurora Serverless
- Amazon S3 with Object Lock (Compliance Mode) & AWS KMS

## Relationships
- External Payment Gateway -> API Gateway: Forwards payment authorizations [HTTPS/REST]
- API Gateway -> Scoring Engine Container: Routes authorization payloads [gRPC]
- Scoring Engine Container -> Amazon SageMaker: Invokes fraud models [AWS SDK]
- Scoring Engine Container -> Amazon S3: Writes tamper-evident decision logs [HTTPS/AWS SDK, TLS 1.3]
- Scoring Engine Container -> Amazon Aurora Serverless: Queries rules and persists cases [PostgreSQL Protocol]

## Technology Stack
- AWS ECS Fargate: Container orchestration to match the 3-engineer operational capacity limit.
- Amazon S3 Object Lock (Compliance Mode): Immutable storage guaranteeing 7-year audit retention.
- Amazon SageMaker Serverless Inference: Managed machine learning scaling for sub-50ms P99 latency.
- Amazon Aurora Serverless: Relational storage for rules and case management.
- AWS KMS: Customer-managed key encryption with locked policies for data protection.

## Rationale
This architecture leverages serverless and managed AWS services in eu-west-1 to achieve PCI-DSS Level 1 compliance and stringent auditability. It maintains high performance while respecting the strict 25,000 EUR monthly budget and three-engineer operational constraint.