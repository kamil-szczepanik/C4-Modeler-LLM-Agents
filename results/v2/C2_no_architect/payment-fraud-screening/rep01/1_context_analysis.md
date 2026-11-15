## Overview
[System Overview]
- Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS while routing suspicious cases to analysts.
- Core purpose is providing sub-50ms fraud decisions and case management while maintaining PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- External Payment Gateway
- API Gateway / ALB (Edge with Circuit Breaker)
- Fraud Scoring Engine (AWS ECS Fargate containers)
- Case Management UI (Fraud Analyst interface)
- Amazon SQS / Amazon Kinesis (Asynchronous event bus)
- Amazon S3 with Object Lock / Amazon QLDB (Tamper-evident audit storage)
- AWS KMS (Key Management Service)
- GitHub Actions (CI/CD deployment pipeline)

## Relationships
- External Payment Gateway to API Gateway/ALB via HTTPS / mTLS
- API Gateway/ALB to Fraud Scoring Engine via HTTP/2 and gRPC
- Fraud Scoring Engine to Amazon SQS/Kinesis via AWS SDK (TLS 1.3)
- Amazon SQS/Kinesis to S3 Object Lock / QLDB for asynchronous audit logs
- Fraud Analysts to Case Management UI via HTTPS (OAuth2/OIDC, WebAuthn MFA)
- GitHub Actions to AWS ECS Fargate via AWS API for zero-downtime blue/green deployments

## Technology Stack
- AWS ECS Fargate: Container orchestration to avoid memory-heavy ML overhead and cap idle infrastructure costs within budget.
- Amazon S3 Object Lock / QLDB: Tamper-evident storage implementing cryptographic hash chaining (Merkle trees) for 7-year auditability.
- AWS KMS: Envelope encryption with customer-managed keys (CMK) for data protection and strict separation of card and audit keys.
- AWS API Gateway / ALB: Edge routing providing circuit-breaker capabilities for high availability and fail-open handling.
- GitHub Actions & AWS Signer: Automated blue/green deployment pipelines with cryptographic container image and model verification.

## Rationale
- This architecture prioritizes managed AWS services to fit within a strict €25,000 monthly budget and a 3-person engineering team. 
- Asynchronous logging and lightweight containerization decouple high-throughput scoring from compliance requirements, guaranteeing sub-50ms latency and PCI-DSS Level 1 security.