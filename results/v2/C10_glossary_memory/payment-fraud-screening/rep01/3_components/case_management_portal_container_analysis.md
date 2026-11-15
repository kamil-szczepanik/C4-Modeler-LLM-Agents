## Overview
The Case Management Portal Container provides a secure, high-performance web interface for fraud analysts to review flagged transactions, execute bulk decisions, and inspect model explainability. It operates as part of the Real-Time Payment Fraud Screening System within strict PCI-DSS Level 1 compliance constraints.

## Key Elements
- Fraud Analyst (person)
- Case Management Portal Container (container, AWS Fargate)
- UI Presentation Component (component, React/TypeScript, Nginx)
- Case Management API Component (component, Node.js/TypeScript)
- Audit Logging Component (component)
- Identity Provider (IdP) (externalSystem)
- Amazon Aurora PostgreSQL (container)
- AWS Audit & Compliance Store (externalSystem)
- AWS CloudWatch / Observability Platform (externalSystem)

## Relationships
- Fraud Analyst -> UI Presentation Component: HTTPS (TLS 1.3)
- UI Presentation Component -> Case Management API Component: HTTPS (JSON/REST)
- Case Management API Component -> Amazon Aurora PostgreSQL: SQL / TLS
- Case Management API Component -> AWS Audit & Compliance Store: HTTPS / S3 API
- Case Management API Component -> AWS CloudWatch / Observability Platform: HTTPS / AWS SDK
- UI Presentation Component -> Identity Provider (IdP): OIDC / OAuth2

## Technology Stack
- AWS Fargate: Chosen for container orchestration to fit the 3-person team and 25,000 EUR monthly budget without Kubernetes overhead.
- React/TypeScript & Nginx: Powers the UI Presentation Component with strict CSP headers and client-side card data masking.
- Node.js/TypeScript: Powers the Case Management API Component for efficient asynchronous case workflow handling.
- AWS KMS (AES-256): Secures local disk buffers and encrypted storage for tamper-evident compliance audit trails.
- Amazon Aurora PostgreSQL: Stores transactional case data with read replicas.

## Rationale
This architecture leverages managed serverless containers on AWS to maintain a fixed low operational footprint suited for a three-engineer team. It embeds robust cryptographic audit logging and strict data masking to satisfy PCI-DSS Level 1 and 7-year auditability mandates without exceeding budget constraints.