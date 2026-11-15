## Overview
The system provides real-time payment fraud screening for card-not-present authorizations and case management for analysts. It ensures PCI-DSS Level 1 compliance and 7-year auditability on a fixed AWS budget.

## Key Elements
- Fraud Analysts
- Payment Gateway / Acquirer
- Fallback Proxy Container
- Scoring Engine Container (AWS ECS on Fargate, Protocol Buffers)
- Case Management & Admin Container (AWS ECS on Fargate)
- Amazon Aurora Serverless (TLS)
- Amazon S3 (Object Lock)
- AWS Systems Manager Parameter Store (AWS Systems Manager)

## Relationships
- Fallback Proxy Container -> Scoring Engine Container: Forwards authorization requests [gRPC / TLS]
- Scoring Engine Container -> Amazon Aurora Serverless: Reads fraud rules and stores transaction decisions [TLS]
- Case Management & Admin Container -> Amazon Aurora Serverless: Manages review cases [TLS]
- Scoring Engine Container -> AWS Systems Manager Parameter Store: Reads runtime configuration and secrets [AWS API]
- Case Management & Admin Container -> AWS Systems Manager Parameter Store: Updates configuration and secrets [AWS API]

## Technology Stack
- AWS ECS on Fargate: Provides serverless container orchestration within the 25,000 EUR/month budget for a 3-engineer team.
- Amazon Aurora Serverless: Offers auto-scaling relational data storage with TLS encryption for PCI-DSS compliance.
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year audit storage for decision logs.
- AWS Systems Manager Parameter Store: Centralizes configuration and secrets management using SecureString and AWS KMS.

## Rationale
The architecture combines serverless containers and managed AWS services to minimize operational overhead for a three-engineer team while meeting strict P99 latency and PCI-DSS compliance goals. Immutable versioning and in-memory caching patterns guarantee sub-50ms fraud scoring performance and robust auditability.