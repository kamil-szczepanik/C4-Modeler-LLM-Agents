## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages suspicious transaction reviews. It provides automated scoring and analyst case management while enforcing strict security and auditability.

## Key Elements
- **Fraud Analyst**: Human user reviewing suspicious payments via case management UI.
- **AWS ALB (Ingress / API Gateway)**: Application Load Balancer terminating TLS 1.3 and routing HTTPS traffic.
- **Case Management API**: Node.js/TypeScript container running on Amazon ECS on AWS Fargate.
- **HTTP Router / Controller (Express.js)**: Handles ingress routing and request validation.
- **Auth & RBAC Middleware**: Validates JWTs from the IdP and enforces least-privilege roles.
- **Case Service**: Core business logic orchestrating case assignment and status transitions.
- **Audit & Compliance Logger**: Generates HMAC-SHA256 signed, tamper-evident audit trails.
- **Redis Feature Store**: Amazon ElastiCache Multi-AZ Redis caching state and token revocation lists.
- **Transactional & Audit Data Store**: Amazon RDS PostgreSQL storing case states and audit logs.
- **Asynchronous Messaging**: Amazon SQS handling dead-letter queues and audit events.
- **Secrets Manager**: AWS Secrets Manager storing database credentials and keys via AWS PrivateLink.
- **Identity Provider (IdP)**: Authenticates analyst sessions using OAuth 2.0 / OIDC.

## Relationships
- **Fraud Analyst -> AWS ALB**: Accesses case management dashboard [HTTPS / TLS 1.3]
- **AWS ALB -> Case Management API**: Forwards case management requests [HTTPS / mTLS]
- **Case Management API -> Redis Feature Store**: Reads/writes cache and state data [Redis Protocol with TLS]
- **Case Management API -> Transactional & Audit Data Store**: Reads/writes case storage using IAM Database Authentication [PostgreSQL Wire Protocol]
- **Case Management API -> Asynchronous Messaging**: Publishes audit events and messages [SQS API]
- **Case Management API -> Secrets Manager**: Retrieves credentials and keys [AWS SDK / PrivateLink]
- **Case Management API -> Identity Provider (IdP)**: Authenticates analyst sessions [OAuth 2.0 / OIDC]

## Technology Stack
- **Node.js/TypeScript**: Core runtime for the Case Management API, matching team skill set and async I/O needs.
- **Amazon ECS on AWS Fargate**: Serverless container orchestration eliminating EC2 OS patching and right-sizing resources within budget.
- **Amazon RDS PostgreSQL**: Managed relational database for ACID-compliant case state storage and audit logs.
- **Amazon ElastiCache Redis**: In-memory data store for caching and token revocation lists.
- **AWS Secrets Manager & IAM**: Secures credentials via ephemeral tokens and IAM Database Authentication.

## Rationale
This architecture fits the requirements by combining serverless AWS Fargate containers with managed data stores to maintain PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail within a €25,000 monthly budget. The 3-engineer team leverages familiar Node.js and TypeScript technologies while ensuring low operational overhead and high availability.