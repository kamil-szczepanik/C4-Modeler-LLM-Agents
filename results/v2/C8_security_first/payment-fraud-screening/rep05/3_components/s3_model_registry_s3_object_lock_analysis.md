## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect and block fraud while maintaining compliance. It evaluates transactions under 50 milliseconds and securely stores tamper-evident decision logs for 7 years.

## Key Elements
- Fraud Analysts & Risk Managers
- Payment Gateway & Identity Provider (AWS Cognito/Okta)
- AWS API Gateway & Internal Network Load Balancer (NLB)
- Scoring Engine Container (Rust/Go) on AWS ECS Fargate
- Case Management API Container (Node.js/Python)
- Fraud Analyst SPA (Single Page Application)
- S3 Model Registry & S3 Object Lock (AWS S3)
- Model Registry Metadata Index (Amazon DynamoDB)
- Validation & Ingestion Gatekeeper (AWS Lambda + Amazon SQS)
- Amazon QLDB & AWS KMS / Secrets Manager

## Relationships
- Fraud Analyst SPA -> API Gateway: HTTPS [REST/WSS]
- API Gateway -> Scoring Engine Container: gRPC / HTTP
- Scoring Engine Container -> Local Model Cache: POSIX file read
- Validation Lambda -> DynamoDB: HTTPS [AWS DynamoDB API]
- CI/CD Pipeline -> S3 Model Registry: HTTPS [AWS S3 API]
- Scoring Engine Container -> QLDB & KMS: HTTPS [AWS SDK]

## Technology Stack
- **Compute:** AWS ECS Fargate for serverless container orchestration
- **Storage & Audit:** Amazon S3 with Object Lock (Compliance Mode) for immutable 7-year model retention
- **Metadata Index:** Amazon DynamoDB for rapid model lineage and metrics lookup
- **Ingestion & Validation:** AWS Lambda and Amazon SQS for secure, cryptographically signed model verification
- **Security & Encryption:** AWS KMS and Secrets Manager for customer-managed keys and credential safety

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to meet strict P99 latency and high-throughput demands. Compliance controls such as S3 Object Lock, QLDB audit logs, and KMS encryption guarantee PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail within budget constraints.