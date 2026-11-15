## Overview
The Real-Time Payment Fraud Screening System evaluates card-not-present payment authorizations for fraud, providing sub-50ms decisions and case management for analysts. It ensures compliance, auditability, and high availability while operating within strict budget and team constraints.

## Key Elements
- **Users**: Payers, Fraud Analysts, and Risk Managers/Quants.
- **External Systems**: Payment Gateway/Acquirer, Core Banking/Card Network Systems, Identity Provider (IdP).
- **Core Containers**: Edge Envoy Proxy on Amazon ECS Fargate, Real-Time Scoring Engine, Case Management Application, Audit and Storage Service.
- **Infrastructure**: Dedicated AWS VPC, Amazon S3 Glacier Vault Lock (WORM storage).

## Relationships
- **Payment Gateway to Edge Proxy**: HTTPS/gRPC via mTLS (TLS 1.3) for real-time transaction screening (R-01).
- **Users to IdP**: HTTPS using OAuth2/OIDC for authentication and RBAC.
- **Scoring Engine to Audit Storage**: AWS KMS encryption and Amazon S3 Object Lock for tamper-evident logs (R-06).

## Technology Stack
- **Compute/Edge**: Amazon ECS Fargate running Envoy proxy for perimeter mTLS termination, local caching, and fail-open timeout enforcement.
- **Security & Identity**: AWS IAM, Cognito, and AWS KMS customer-managed keys for tokenization and encryption.
- **Audit & Logging**: Amazon S3 Glacier Vault Lock for 7-year tamper-evident WORM storage.
- **Observability**: AWS Distro for OpenTelemetry with CloudWatch and X-Ray.
- **CI/CD**: GitHub Actions for automated blue/green deployments with cryptographically signed model artifacts.

## Rationale
AWS managed services and containerized Envoy proxies minimize operational toil for a three-person team while satisfying strict PCI-DSS Level 1 compliance. Tiered storage and efficient edge routing meet the 3,000 TPS performance and 7-year audit constraints within the €25,000 monthly budget.