## Overview
The Case Management Container provides a secure review interface and API backend for fraud analysts and managers to investigate suspicious transactions. It ensures PCI-DSS Level 1 compliance while maintaining immutable audit trails and SLA-driven case queues.

## Key Elements
- Fraud Analyst (Person)
- Risk/Fraud Operations Manager (Person)
- API Gateway (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- AWS Cognito
- Amazon ElastiCache Serverless (Redis)
- Amazon CloudWatch
- AWS S3 Glacier with Object Lock

## Relationships
- Fraud Analyst -> API Gateway: Accesses review UI and submits decisions [HTTPS, OAuth2/OIDC, AWS Cognito]
- Risk/Fraud Operations Manager -> API Gateway: Accesses operational metrics and queues [HTTPS, OAuth2/OIDC, AWS Cognito]
- API Gateway -> Case Management Container: Forwards authenticated review requests [mTLS / AWS IAM SigV4, HTTPS]
- Case Management Container -> Amazon ElastiCache Serverless: Caches session state and queue data [Redis Protocol, TLS 1.3, AWS KMS]
- Case Management Container -> AWS S3 Glacier: Stores tamper-evident audit logs and decisions [HTTPS, AWS KMS, Object Lock]

## Technology Stack
- AWS ECS Fargate (Spot): Runs containerized backend workloads efficiently within the budget.
- AWS Cognito: Manages authentication, short-lived JWTs (15 min), and RBAC segregation.
- Amazon ElastiCache Serverless (Redis): Caches session data with encryption at rest via AWS KMS.
- Amazon CloudWatch: Monitors container insights and metrics with automated log scrubbing.
- AWS S3 Glacier with Object Lock: Enforces tamper-evident 7-year audit retention (R-06).

## Rationale
This architecture balances strict PCI-DSS Level 1 security controls and 7-year auditability with the operational constraints of a three-engineer team. Serverless and managed AWS services minimize operational overhead while fitting within the 25,000 EUR monthly budget.