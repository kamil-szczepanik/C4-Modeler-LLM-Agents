## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations within 50 milliseconds. It provides automated scoring, case management for analysts, and immutable 7-year audit logs for a mid-size payment processor.

## Key Elements
- **Merchant / Payment Gateway System**: External system submitting payment authorization requests via REST API.
- **Fraud Analyst**: Internal user reviewing suspicious transactions via case management UI.
- **Risk Manager / Data Scientist**: Internal user updating scoring models and rules with zero downtime.
- **Merchant Support**: Internal user accessing read-only audit logs for dispute resolution.
- **API Gateway**: AWS API Gateway enforcing TLS 1.3, mTLS, and AWS WAF rate-limiting.
- **Scoring Service**: AWS ECS on Fargate containers executing fraud detection logic.
- **Case Management App**: Containerized backend for analyst review workflows.
- **Audit Storage**: AWS S3 with Object Lock in Compliance Mode and AWS Glacier lifecycle policies.
- **Key Management**: AWS KMS / CloudHSM with automated key rotation.

## Relationships
- **Merchant System -> API Gateway**: Submits authorization requests via HTTPS using TLS 1.3, mTLS, and API keys.
- **API Gateway -> Scoring Service**: Forwards transaction payloads via internal VPC networking using gRPC.
- **Scoring Service -> Audit Storage**: Streams decision payloads, inputs, and model versions to S3 with Object Lock via AWS SDK.
- **Fraud Analyst -> Case Management App**: Reviews flagged transactions via HTTPS/OIDC with MFA.
- **Risk Manager -> Scoring Service**: Deploys updated models and rules with zero downtime via CI/CD pipelines.

## Technology Stack
- **Compute**: AWS ECS on Fargate with auto-scaling to maintain sub-50ms P99 latency within budget.
- **API & Protocol**: REST and gRPC for high-throughput, low-latency inter-service communication.
- **Security & Compliance**: AWS WAF, AWS KMS, CloudHSM, and TLS 1.3 for PCI-DSS Level 1 compliance.
- **Storage & Audit**: Amazon S3 with Compliance Mode Object Lock and S3 Glacier for 7-year retention.
- **Authentication**: OIDC/OAuth2 with hardware-token MFA for internal users.

## Rationale
This architecture uses managed AWS services to minimize operational toil for a three-engineer team while meeting strict sub-50ms latency and PCI-DSS compliance requirements. Serverless container scaling and S3 Glacier lifecycle policies ensure the system stays within the strict 25,000 EUR monthly budget.