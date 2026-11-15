## Overview
[System screens card-not-present payment authorizations for fraud in real-time and provides case management for analysts. Built for a mid-size payment processor in AWS eu-west-1.]

## Key Elements
- Merchant / Payment Gateway (API Client)
- Fraud Analyst and Risk Operations Manager
- Compliance Auditor / Regulators
- Real-Time Payment Fraud Screening System (AWS Boundary)
- External Identity Provider (IdP)
- AWS S3 / Glacier (Cold Storage)

## Relationships
- Merchant to System: gRPC/REST over TLS for sub-50ms authorization scoring
- Analysts to System: HTTPS via Web UI for case management
- System to IdP: OAuth2/OIDC for multi-factor authentication
- System to S3/Glacier: AWS SDK/IAM for 7-year tamper-evident audit logs

## Technology Stack
- AWS API Gateway & Route 53: Ingress routing and health checks for <50ms P99 latency and fail-open availability
- AWS CloudWatch & CloudTrail: Native observability and PCI-DSS Level 1 compliant log monitoring
- AWS S3 / Glacier: Immutable storage for 7-year audit retention within budget
- AWS CodePipeline: Blue/green deployments for zero-downtime model updates

## Rationale
[Native AWS managed services minimize operational overhead for a three-engineer team while ensuring PCI-DSS Level 1 compliance. Using serverless and cloud-native primitives guarantees performance targets within the strict 25,000 EUR monthly budget.]