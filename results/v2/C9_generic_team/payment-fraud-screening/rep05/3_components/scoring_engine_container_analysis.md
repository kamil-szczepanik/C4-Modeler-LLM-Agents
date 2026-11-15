## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for analysts to review suspicious transactions. It ensures compliance, explainability, and high-throughput processing within strict performance and budget constraints.

## Key Elements
- Scoring Engine Container (AWS ECS on Fargate, Protocol Buffers)
- Fallback Proxy Container (Container Proxy)
- Case Management & Admin Container (AWS ECS on Fargate)
- Amazon S3 (AWS S3 with Object Lock)
- Amazon Aurora Serverless (Amazon Aurora Serverless, TLS)
- AWS Systems Manager Parameter Store (AWS Systems Manager)

## Relationships
- Fallback Proxy Container -> Scoring Engine Container: Invokes fraud evaluation [gRPC / HTTP]
- Scoring Engine Container -> Amazon S3: Loads model bundles and writes tamper-evident audit records [HTTPS / TLS]
- Scoring Engine Container -> AWS Systems Manager Parameter Store: Reads configuration [AWS API]

## Technology Stack
- AWS ECS on Fargate: Selected for minimal operational overhead and autoscaling support.
- Protocol Buffers: Ensures strict typing and low latency at the gRPC boundary.
- Amazon S3 with Object Lock: Provides tamper-evident storage for the 7-year audit requirement.
- Amazon Aurora Serverless: Manages relational case data securely with TLS encryption.
- AWS Systems Manager Parameter Store: Securely stores application configuration.

## Rationale
This architecture uses serverless and managed AWS services to meet sub-50 ms P99 latency at 3,000 TPS within a 25,000 EUR monthly budget. It limits operational overhead for a three-engineer team while satisfying strict PCI-DSS Level 1 compliance and 7-year auditability constraints.