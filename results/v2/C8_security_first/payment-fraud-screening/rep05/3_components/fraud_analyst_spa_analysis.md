## Overview
- A real-time payment fraud screening system evaluates card-not-present authorizations and provides case management tools for fraud analysts.
- The platform ensures PCI-DSS Level 1 compliance while maintaining sub-50 ms decision latencies and strict 7-year tamper-evident auditability.

## Key Elements
- Fraud Analysts & Risk Managers
- AWS API Gateway & Internal Network Load Balancer (NLB)
- Scoring Engine Container (Go/Rust)
- Case Management API Container (Node.js/Python)
- Fraud Analyst SPA (React SPA via AWS CloudFront & S3)
- S3 Model Registry & S3 Object Lock
- Amazon SQS & AWS QLDB
- AWS KMS & AWS Secrets Manager
- Identity Provider (AWS Cognito/Okta)

## Relationships
- Fraud Analysts & Risk Managers -> Fraud Analyst SPA: Accesses user interface [HTTPS / TLS 1.3]
- Fraud Analyst SPA -> Case Management API Container: Case workflows and batch actions [REST/JSON over HTTPS]
- Case Management API Container -> Scoring Engine Container: Internal scoring requests [gRPC / Internal VPC]
- Scoring Engine Container -> S3 Model Registry: Fetches scoring models [AWS SDK / TLS]
- Case Management API Container -> AWS QLDB & S3 Object Lock: Persists immutable audit logs [AWS SDK]

## Technology Stack
- AWS CloudFront & S3: Static hosting for React SPA with strict CSP and SRI for cost-effective global delivery.
- Node.js/Python & Go/Rust: Containerized microservices on AWS ECS Fargate for low latency and high concurrency.
- AWS QLDB & S3 Object Lock: Tamper-evident storage satisfying the 7-year audit retention requirement.
- AWS Cognito/Okta: OIDC/PKCE authentication using short-lived memory-only tokens.

## Rationale
- This AWS serverless and container architecture guarantees sub-50 ms P99 latency while strictly adhering to the 25,000 EUR monthly budget constraint.
- Managed services minimize operational overhead, allowing a lean team of three engineers to maintain PCI-DSS compliance and high availability.