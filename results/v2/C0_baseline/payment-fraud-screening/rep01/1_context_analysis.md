## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at 3,000 TPS while supporting analyst reviews. It ensures strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a €25k monthly AWS budget.

## Key Elements
- **Merchant / Payment Gateway**: External system submitting payment authorizations.
- **Fraud Analyst**: Human persona managing suspicious payments.
- **Real-Time Payment Fraud Screening System**: Core AWS-based system containing scoring engines and case management.
- **AWS KMS / S3 Object Lock**: Infrastructure providing WORM storage and encryption.
- **Identity Provider (IdP)**: External system managing OIDC/SAML authentication.

## Relationships
- Merchant/Gateway $\rightarrow$ Fraud System: Submits auth requests via gRPC over TLS 1.3 (<50ms P99).
- Fraud Analyst $\rightarrow$ Fraud System: Reviews flagged cases via HTTPS/TLS with OIDC/SAML MFA.
- Fraud System $\rightarrow$ AWS S3 Object Lock: Persists tamper-evident decisions using AWS SDK and IAM via AWS KMS.

## Technology Stack
- **AWS ECS Fargate**: Container orchestration chosen to minimize operational toil for a 3-person team.
- **gRPC / TLS 1.3**: Communication protocol ensuring ultra-low latency (<50ms P99).
- **AWS S3 Object Lock & KMS**: WORM storage and envelope encryption meeting 7-year audit requirements.
- **Terraform**: Infrastructure-as-Code for GitOps automated deployments.

## Rationale
Managed AWS services and containerization reduce operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 boundaries. gRPC and serverless scalability meet high-throughput, low-latency requirements within the fixed €25,000 monthly budget.