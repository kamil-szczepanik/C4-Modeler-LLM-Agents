## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under strict latency and compliance constraints. It enables rapid transaction scoring alongside case management and rule updates for fraud analysts.

## Key Elements
- Fraud Analysts, Risk / Compliance Officers
- Merchant / Payment Gateway, Tokenization Provider, Audit Archive (AWS S3 Object Lock)
- AWS API Gateway, AWS ACM Private CA, Amazon CloudFront, Amazon S3
- Fraud Screening Engine (Go/Rust, AWS Fargate), Case Management & Reporting Frontend (React SPA)
- Case Management & Reporting Backend (Python FastAPI)
- Supporting Services: Amazon ElastiCache for Redis, Amazon SQS, Amazon Athena, AWS Secrets Manager, AWS KMS, Amazon ECR

## Relationships
- Merchant / Payment Gateway -> AWS API Gateway: Invokes real-time payment authorization [HTTPS / mTLS]
- AWS API Gateway -> Fraud Screening Engine: Forwards scoring requests [mTLS over private VPC subnets]
- Fraud Screening Engine -> Amazon ElastiCache for Redis: Queries and updates cached features [Redis Protocol]
- Fraud Screening Engine -> Amazon SQS: Publishes decision and audit events asynchronously [AWS SDK / SQS API]
- Fraud Analysts -> Amazon CloudFront: Accesses case management dashboard [HTTPS]
- Case Management Backend -> Amazon S3 / Athena: Queries historical audit records and reports [AWS SDK]

## Technology Stack
- Compute: AWS Fargate on Amazon ECS (chosen to minimize infrastructure operational toil for a 3-person team while meeting security requirements)
- Language/Runtime: Go and Rust (selected for high-throughput, low-latency execution and memory safety)
- Caching/State: Amazon ElastiCache for Redis (enables sub-50ms P99 feature retrieval)
- Messaging: Amazon SQS (decouples async audit logging and telemetry emission)
- Compliance/Security: AWS KMS, S3 Object Lock, AWS Secrets Manager (guarantees tamper-evident 7-year auditability and PCI-DSS compliance)

## Rationale
This architecture uses serverless containers and managed AWS services to keep operational overhead minimal for a three-person engineering team within a fixed €25,000 monthly budget. Decoupled asynchronous components and in-memory caching guarantee sub-50ms P99 latency and high availability under peak transaction loads.