## Overview
[System Processes real-time card-not-present payment authorizations in AWS for fraud screening and provides an analyst review interface.]
[Core purpose is to deliver sub-50ms fraud decisions while maintaining PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.]

## Key Elements
- **Payment Gateway / Acquirer**: External system sending transaction requests.
- **Tokenization Vault**: External system resolving card tokens for secure data handling.
- **Identity Provider (IdP)**: External system managing OIDC/SAML authentication and MFA.
- **Fraud Screening Engine (System-to-Be)**: AWS-hosted containerized system for scoring and case management.
- **WORM Compliance Storage**: External AWS S3 storage for 7-year audit logs.

## Relationships
- **Payment Gateway to Fraud Screening Engine**: Sends real-time payment events via HTTPS/gRPC with mTLS.
- **Fraud Screening Engine to Tokenization Vault**: Resolves tokens via HTTPS REST API.
- **Fraud Screening Engine to Identity Provider**: Authenticates analysts using OIDC/SAML.
- **Fraud Screening Engine to WORM Compliance Storage**: Sends cryptographically signed decision logs via AWS S3 APIs.

## Technology Stack
- **AWS ECS on Fargate**: Container orchestration chosen to avoid serverless cold starts and stay within the €25k budget.
- **AWS KMS**: Manages customer-managed keys (CMK) and asymmetric signing for tamper-evident R-06 audit logs and data encryption.
- **Terraform**: Infrastructure as Code tool used by the 3-engineer team to automate deployments via GitOps.
- **AWS Secrets Manager**: Eliminates hardcoded credentials to meet PCI-DSS Level 1 mandates.

## Rationale
[AWS managed services and containerization on Fargate provide high availability and meet the strict <50ms P99 latency within budget constraints.]
[A containerized GitOps approach and immutable storage enable a 3-engineer team to maintain PCI-DSS compliance and 7-year auditability effortlessly.]