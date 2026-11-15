## Overview
Real-Time Payment Fraud Screening is a low-latency financial system that screens card-not-present payment authorizations for fraud and manages analyst review workflows. It ensures PCI-DSS compliance and 7-year auditability on AWS with a 3-engineer team.

## Key Elements
- Fraud Analyst & Risk/Compliance Officer
- Case Management App (Node.js/TypeScript on Amazon ECS Fargate)
- API Controller Component, Case Service Component, Audit Client Component, Data Repository Component, Dashboard & Metrics Component
- Amazon API Gateway
- Amazon Aurora PostgreSQL Serverless v2
- Immutable Audit Sink (Amazon S3 with Object Lock)
- Identity Provider

## Relationships
- Fraud Analyst & Risk/Compliance Officer -> Amazon API Gateway: Accesses case management UI [HTTPS / TLS 1.3]
- Amazon API Gateway -> API Controller Component: Routes authenticated API requests [HTTP / JSON]
- Case Service Component -> Data Repository Component: Reads and writes relational case state [TypeORM / Prisma]
- Data Repository Component -> Amazon Aurora PostgreSQL Serverless v2: Persists case data [IAM DB Auth / TLS]
- Audit Client Component -> Immutable Audit Sink: Emits cryptographically signed case resolution events [AWS SDK / HTTPS]
- Case Management App -> Identity Provider: Validates OIDC/OAuth2 tokens and RBAC claims [HTTPS]

## Technology Stack
- Runtime: Node.js and TypeScript on Amazon ECS Fargate for lightweight, ephemeral, and stateless container management.
- Backend Framework: Express.js/Fastify for simple routing without heavy CQRS overhead.
- Database ORM: TypeORM/Prisma for type-safe relational data mapping.
- Storage & Audit: Amazon Aurora PostgreSQL Serverless v2 and Amazon S3 with Object Lock for immutable 7-year audit logging.
- Security & Auth: AWS KMS, AWS IAM, and OIDC/OAuth2 via Identity Provider for secretless infrastructure and strict RBAC.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team within a 25,000 EUR monthly budget. Modular component boundaries in Node.js ensure maintainability while meeting strict PCI-DSS Level 1 security and tamper-evident audit requirements.