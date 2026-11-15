## Overview
The Model Management Service enables zero-downtime updates and governance for fraud scoring models. It provides risk managers with self-service model promotion, explainability previews, and performance dashboards while maintaining PCI-DSS compliance.

## Key Elements
- Fraud Analysts and Risk Managers (Users)
- Model Management Service (AWS ECS Fargate Container)
- Real-Time Scoring Engine (ECS Fargate Container)
- Audit & Cryptographic Signer Sidecar (AWS ECS Fargate Container)
- AWS S3 & AWS KMS (Storage and Encryption)
- AWS Cognito (Identity Provider)

## Relationships
- Fraud Analysts to Model Management Service via HTTPS/TLS 1.3 (OAuth2/OIDC via AWS Cognito)
- Model Management Service to AWS S3 via HTTPS (Model artifact storage and version manifests)
- Model Management Service to Audit & Cryptographic Signer via gRPC/Internal Network (Model promotion and rollback audit logs)
- Real-Time Scoring Engine to AWS S3 via HTTPS (Model hot-reloading and signature verification)

## Technology Stack
- AWS ECS Fargate: Container orchestration aligned with the 3-engineer team constraint and €25k/month budget.
- AWS S3 with Object Lock: Storage for model artifacts and 7-year audit retention compliance.
- AWS KMS: Customer-managed encryption keys for at-rest model security.
- AWS Cognito: OIDC/OAuth2 authentication and RBAC for risk managers.
- AWS CloudWatch: Metrics and performance dashboard integration.

## Rationale
This architecture ensures zero-downtime model updates and strict 7-year auditability while respecting operational limits. Leveraging managed AWS services minimizes maintenance overhead for the three-engineer team.