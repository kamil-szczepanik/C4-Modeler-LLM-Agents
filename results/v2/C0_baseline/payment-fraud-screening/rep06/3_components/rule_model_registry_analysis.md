## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud to protect transactions while ensuring sub-50ms decision latency. It provides a secure, auditable, and highly available platform for payment processors, operating under PCI-DSS Level 1 compliance constraints.

## Key Elements
- Fraud Analysts / Data Scientists / Fraud Managers (Users)
- AWS API Gateway / Application Load Balancer (ALB)
- Scoring Engine (AWS ECS Fargate / Go or Rust)
- Case Management API (AWS ECS Fargate)
- Rule & Model Registry (Registry API, Amazon S3, Amazon DynamoDB)
- External Systems: Payment Gateway/Acquirer, Tokenization Vault, Identity Provider (IdP), WORM Compliance Storage

## Relationships
- Scoring Engine -> Rule & Model Registry: Fetches versioned models and rules via HTTPS / AWS SigV4 with local in-memory caching.
- Registry API -> Amazon S3: Persists immutable binary model files and rule definitions (.onnx / .json) via AWS SDK.
- Registry API -> Amazon DynamoDB: Reads and writes version tags, access controls, and audit logs via AWS SDK.
- Fraud Analysts -> Case Management API: Reviews suspicious payments and manages cases via HTTPS.

## Technology Stack
- AWS ECS Fargate: Container orchestration for microservices, chosen for low operational overhead suitable for a three-engineer team.
- Amazon S3: Immutable binary artifact storage, selected for cost-efficiency within the 25k EUR/month budget.
- Amazon DynamoDB: Metadata and audit log storage with KMS encryption, providing low-latency tamper-evident tracking.
- AWS Lambda / Python FastAPI: Administrative REST interface for model uploads, schema validation, and RBAC.
- AWS KMS: Customer-managed encryption keys ensuring data protection at rest for PCI-DSS compliance.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational complexity for a three-engineer team within a strict budget. Local caching and immutable storage patterns ensure high availability, deterministic <50ms P99 latency, and robust 7-year auditability.