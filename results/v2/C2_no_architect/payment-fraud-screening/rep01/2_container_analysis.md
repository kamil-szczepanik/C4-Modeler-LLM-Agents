## Overview
[Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst reviews. Core purpose is ensuring PCI-DSS Level 1 compliant, low-latency fraud decisions within budget.]

## Key Elements
- External Payment Gateway
- Fraud Analyst, Risk Operations Manager, Fraud Data Scientist
- API Gateway / Ingress Container
- Scoring Engine Container
- Case Management Container
- AWS SageMaker Serverless Inference
- Amazon Aurora Serverless / QLDB / S3 Object Lock
- AWS ECR, AWS Inspector, AWS Signer
- AWS Secrets Manager, AWS CloudWatch, AWS X-Ray

## Relationships
- External Payment Gateway interacts with API Gateway via HTTPS (TLS 1.3)
- API Gateway routes scoring requests to Scoring Engine Container via REST over internal VPC
- Scoring Engine invokes AWS SageMaker Serverless Inference via AWS SDK
- Scoring Engine writes tamper-evident decision logs to QLDB / S3 with Object Lock
- Fraud Analysts access Case Management Container via HTTPS with OIDC/OAuth2 MFA
- Case Management reads and writes review cases in Aurora Serverless

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen to minimize operational toil for a 3-engineer team
- AWS SageMaker Serverless Inference: Decouples model updates for zero-downtime scoring (R-03)
- Amazon S3 Object Lock & QLDB: Tamper-evident storage for 7-year audit retention (R-06)
- AWS Secrets Manager: Automatic rotation of database credentials and API keys
- AWS CloudWatch & X-Ray: Distributed tracing and metric alarms for <50ms P99 latency tracking (R-04)
- Native VPC Security Groups & IAM: Container isolation without App Mesh complexity

## Rationale
[This architecture leverages fully managed AWS services to fit the 25,000 EUR monthly budget and operational capacity of a three-engineer team. It ensures PCI-DSS compliance, tamper-evident 7-year auditability, and sub-50ms P99 latency while maintaining high availability and fail-safe controls.]