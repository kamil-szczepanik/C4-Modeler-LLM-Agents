## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at 3,000 TPS, providing real-time approve/decline/review decisions and case management for analysts. It operates within AWS eu-west-1, adhering to PCI-DSS Level 1 compliance and a €25,000 monthly budget.

## Key Elements
- **Payment Gateway / Merchant Systems**: External actors sending authorization requests.
- **Fraud Operations Analysts & Risk Managers**: Human actors reviewing suspicious transactions and updating rules.
- **Real-Time Fraud Screening System**: Central AWS-hosted system processing requests.
- **API Gateway / ALB**: Entry point handling ingress traffic, mTLS, and circuit breaking.
- **ECS Fargate Containers**: Microservices executing fraud scoring and case management.
- **Model Registry / Feature Store**: Repository supplying ML models and features.
- **Amazon S3 / KMS**: Encrypted, tamper-evident WORM storage for 7-year audit logs.

## Relationships
- **Payment Gateway -> API Gateway / ALB**: gRPC / HTTPS with mTLS for authorization requests (R-01).
- **Fraud Analysts -> Web UI**: HTTPS (TLS 1.3) with OAuth2/OIDC and MFA for case management (R-02).
- **Risk Managers -> API Gateway**: HTTPS (REST) for zero-downtime rule/model updates (R-03).
- **ECS Fargate -> Model Registry**: HTTPS for hot-reloading scoring models.
- **ECS Fargate -> Amazon S3**: AWS SDK with KMS encryption for immutable audit logging.

## Technology Stack
- **AWS ECS Fargate**: Container orchestration chosen over AWS Lambda to maintain predictable costs under a €25,000/month budget at 3,000 TPS.
- **gRPC / REST**: Protocols ensuring P99 decision latency below 50 ms.
- **Terraform / AWS CDK**: Infrastructure-as-Code for a 3-person engineering team to achieve zero-ops deployment.
- **AWS KMS & S3 Object Lock**: Encryption and WORM storage ensuring PCI-DSS Level 1 and tamper-evident 7-year audit compliance.

## Rationale
This containerized AWS architecture guarantees sub-50ms latency and high availability via automated circuit breakers while respecting a fixed €25,000 budget and 3-person team limit. Strict zero-trust boundaries, encryption, and immutable audit logs satisfy PCI-DSS Level 1 and 7-year retention requirements without downtime.