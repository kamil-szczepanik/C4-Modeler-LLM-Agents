## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages analyst reviews. It ensures strict PCI-DSS compliance and sub-50ms decision latency for mid-size payment processors.

## Key Elements
- Fraud Analysts, Cardholder / Merchant
- Payment Gateway / Acquirer, Fallback Proxy
- Fallback Proxy Container (Container Proxy)
- Scoring Engine Container (AWS ECS on Fargate, Protocol Buffers)
- Case Management & Admin Container (AWS ECS on Fargate)
- Amazon S3 (AWS S3 with Object Lock, SSE-KMS, VPC Gateway Endpoints)
- Amazon Aurora Serverless (Amazon Aurora Serverless, TLS)
- AWS Systems Manager Parameter Store (AWS Systems Manager)
- AWS Lambda and Amazon EventBridge

## Relationships
- Payment Gateway / Acquirer -> Scoring Engine Container: Submits payment authorization requests [HTTPS / REST]
- Scoring Engine Container -> Amazon Aurora Serverless: Queries rules and merchant profiles [PostgreSQL / TLS]
- Scoring Engine Container -> Amazon S3: Loads model bundles and writes tamper-evident audit records [HTTPS / TLS]
- Fraud Analysts -> Case Management & Admin Container: Reviews flagged payments and manages cases [HTTPS / TLS]
- Case Management & Admin Container -> Amazon Aurora Serverless: Reads and writes case data [PostgreSQL / TLS]

## Technology Stack
- AWS ECS on Fargate: Runs containerized microservices without server management overhead.
- Amazon S3 with Object Lock: Provides WORM storage for immutable 7-year audit logs.
- AWS KMS: Enforces Server-Side Encryption (SSE-KMS) for data security.
- Amazon Aurora Serverless: Delivers scalable relational storage for rules and cases.
- Terraform / AWS CDK: Manages Infrastructure as Code to prevent configuration drift.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-person team while meeting strict PCI-DSS Level 1 and 7-year auditability constraints. Local caching and asynchronous batching ensure P99 latency remains below 50ms within the 25,000 EUR monthly budget.