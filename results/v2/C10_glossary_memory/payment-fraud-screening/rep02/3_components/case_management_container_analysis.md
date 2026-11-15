## Overview
[Real-Time Payment Fraud Screening System] screens card-not-present payment authorizations of a mid-size payment processor for fraud before approval. It provides a case management container for fraud analysts to review suspicious payments while meeting strict PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analyst & Risk Operations Manager [person, context]
- Case Management Container [container] (Node.js / TypeScript / AWS Fargate)
- Case Management API Component [component] (Node.js / TypeScript)
- Audit & Compliance Writer Component [component] (Node.js / TypeScript)
- Authentication & Authorization Middleware Component [component] (Node.js / TypeScript)
- Amazon Aurora PostgreSQL Serverless v2 [container] (relational database)
- Amazon CloudWatch [externalSystem]
- AWS Cognito [externalSystem]
- AWS S3 Object Lock [externalSystem]
- AWS KMS [externalSystem]

## Relationships
- Fraud Analyst & Risk Operations Manager -> Case Management API Component (HTTPS/REST over TLS)
- Authentication & Authorization Middleware Component -> AWS Cognito (OIDC/OAuth2 verification)
- Case Management API Component -> Amazon Aurora PostgreSQL Serverless v2 (PostgreSQL wire protocol over TLS with AWS KMS encryption)
- Audit & Compliance Writer Component -> Amazon CloudWatch (Structured JSON over HTTPS)

## Technology Stack
- Node.js / TypeScript: Core runtime and language for the Case Management Container ensuring rapid development for a 3-engineer team.
- AWS Fargate: Serverless container execution providing automated scaling based on active analyst concurrency within budget.
- Amazon Aurora PostgreSQL Serverless v2: Relational database providing column-level encryption via AWS KMS for zero PAN footprint compliance.
- AWS Cognito: Managed Identity Provider handling JWT validation, OIDC/OAuth2, and strict RBAC.
- Amazon CloudWatch: Centralized logging service capturing structured audit logs and metrics.

## Rationale
This architecture uses serverless AWS services to minimize operational overhead for a three-engineer team while staying within the 25,000 EUR monthly budget. Strict data-masking, zero-PAN footprints, and immutable audit logging ensure full PCI-DSS Level 1 compliance and 7-year auditability.