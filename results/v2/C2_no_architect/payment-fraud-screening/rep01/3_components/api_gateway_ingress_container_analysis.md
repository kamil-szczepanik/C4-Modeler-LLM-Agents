## Overview
[System: Real-Time Payment Fraud Screening] screens card-not-present payment authorizations for fraud, processing up to 3,000 TPS within a strict <50ms P99 latency SLA.

## Key Elements
- External Payment Gateway
- API Gateway / Ingress Container (AWS ECS Fargate)
- Scoring Engine Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- AWS SageMaker Serverless Inference
- Amazon Aurora Serverless
- Amazon QLDB / Amazon S3 Object Lock

## Relationships
- External Payment Gateway -> API Gateway / Ingress Container: Sends payment authorizations [HTTPS with mTLS, TLS 1.3]
- API Gateway / Ingress Container -> Scoring Engine Container: Routes scoring requests [REST over internal VPC]
- Scoring Engine Container -> AWS SageMaker Serverless Inference: Invokes fraud models [HTTPS / AWS SDK]
- Case Management Container -> Amazon Aurora Serverless: Stores case data [PostgreSQL protocol]
- System -> Amazon QLDB / Amazon S3 Object Lock: Persists audit logs and decisions [AWS SDK]

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for low operational overhead suitable for a three-person team.
- Amazon QLDB & S3 Object Lock: Ensures tamper-evident storage for 7-year auditability (R-06).
- AWS WAF & Secrets Manager: Provides robust edge security and secret rotation supporting PCI-DSS Level 1.
- OpenTelemetry / AWS X-Ray: Distributed tracing to monitor P99 latency (<50ms).

## Rationale
This architecture uses serverless and managed AWS components to minimize operational complexity for a three-person team while enforcing PCI-DSS Level 1 compliance. It meets strict performance and availability SLAs within the 25,000 EUR monthly budget constraint.