## Overview
[The system is a Real-Time Payment Fraud Screening System designed to screen card-not-present payment authorizations for fraud and provide case management for fraud analysts. Its core purpose is to block fraudulent transactions while maintaining strict PCI-DSS Level 1 compliance and a sub-50ms P99 latency.]

## Key Elements
- Decision API Container [container]
- Scoring Engine Container [container]
- Case Management Portal Container [container]
- Amazon Aurora PostgreSQL [container]
- CI/CD & Model Registry Pipeline [externalSystem, context]
- Identity Provider (IdP) [externalSystem, context]
- AWS Audit & Compliance Store [externalSystem, context]

## Relationships
- Merchant / Payment Gateway -> Decision API Container (gRPC / HTTPS)
- Decision API Container -> Scoring Engine Container (Internal VPC gRPC / mTLS)
- Fraud Analyst -> Case Management Portal Container (HTTPS (TLS 1.3))
- Case Management Portal Container -> Identity Provider (IdP) (OIDC / OAuth2)
- Scoring Engine Container -> AWS Audit & Compliance Store (HTTPS / S3 API)

## Technology Stack
- AWS Fargate [infrastructure]: Standardizes compute for Decision and Scoring containers to eliminate Lambda cold starts and meet latency SLAs.
- Go [language]: Powers the Decision API for high-performance and low-latency authorization checks.
- Python / FastAPI [language / framework]: Powers the Scoring Engine for ML model inference.
- Amazon Aurora PostgreSQL [database]: Stores transactional case data with read replicas.
- Amazon S3 Object Lock [storage]: Implements WORM storage for the 7-year tamper-evident audit requirement.

## Rationale
[Standardizing on AWS Fargate ensures predictable sub-50ms P99 latency while avoiding Kubernetes complexity for a three-engineer team. Edge tokenization and strict VPC isolation satisfy PCI-DSS Level 1 compliance and robust auditability within the 25,000 EUR monthly budget.]