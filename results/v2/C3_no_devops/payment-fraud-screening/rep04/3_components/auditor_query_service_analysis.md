## Overview
The Auditor Query Service provides a secure, serverless interface for compliance officers and auditors to query 7-year tamper-evident fraud screening decision logs. It ensures PCI-DSS compliance and explainability without exceeding operational constraints or infrastructure budgets.

## Key Elements
- Compliance / Auditor (User)
- API Controller (Node.js / TypeScript container on AWS Fargate)
- Query Translator (Stateless TypeScript component)
- Athena Client (AWS SDK)
- Amazon S3 (Audit log storage with S3 Object Lock and KMS CMKs)
- AWS Athena (Serverless query engine)
- Identity Provider (External System)

## Relationships
- Compliance / Auditor -> API Controller: Query reports via HTTPS / OAuth2 / mTLS (TLS 1.3)
- API Controller -> Query Translator: Invoke report generation via In-process calls
- Query Translator -> Athena Client: Execute parameterized SQL via AWS SDK / HTTPS
- Athena Client -> Amazon S3: Read immutable audit logs via S3 API / HTTPS
- API Controller -> Identity Provider: Validate JWTs via OpenID Connect (OIDC)

## Technology Stack
- Node.js / TypeScript on AWS Fargate: Chosen for lightweight containerized execution aligned with the 3-engineer team capacity.
- AWS Athena & Amazon S3: Chosen for serverless, pay-per-query scaling and immutable 7-year log retention within the 25,000 EUR/month budget.
- S3 Object Lock (Compliance Mode) & AWS KMS: Chosen to enforce tamper-evident data protection and PCI-DSS Level 1 mandates.

## Rationale
This architecture uses serverless components to maintain compliance and auditability requirements while respecting a strict financial budget and small operational team size. Security controls like mTLS, least-privilege IAM, and S3 Object Lock guarantee data protection and tamper resistance.