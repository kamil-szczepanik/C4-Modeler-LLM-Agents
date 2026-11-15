## Overview
- Screens card-not-present payment authorizations for fraud in real-time while providing case management for analysts.
- Ensures PCI-DSS Level 1 compliance, sub-50ms P99 decision latency, and 7-year tamper-evident auditability within a strict budget.

## Key Elements
- Real-Time Payment Fraud Screening System [system, context]
- Fraud Analyst & Risk Operations Manager [person, context]
- Payment Gateway / Acquiring System [externalSystem, context]
- External Fraud Intelligence Feeds [externalSystem, context]
- AWS API Gateway / Envoy Proxy [externalSystem, context]
- Scoring Service Container [container, Go / AWS Fargate]
- Case Management Container [container, Node.js / TypeScript / AWS Fargate]
- Amazon ElastiCache for Redis [container, in-memory cache]
- Amazon Aurora PostgreSQL Serverless v2 [container, relational database]
- AWS S3 Object Lock [externalSystem, storage]
- AWS Cognito [externalSystem, auth]
- AWS KMS [externalSystem, security]

## Relationships
- Payment Gateway / Acquiring System -> AWS API Gateway / Envoy Proxy (gRPC over mTLS)
- Fraud Analyst & Risk Operations Manager -> AWS Cognito (OIDC/OAuth2 over HTTPS/REST)
- AWS API Gateway / Envoy Proxy -> Scoring Service Container (gRPC)
- Scoring Service Container -> Amazon ElastiCache for Redis (RESP over TLS)
- Scoring Service Container -> AWS S3 Object Lock (AWS SDK / HTTPS)
- Case Management Container -> Amazon Aurora PostgreSQL Serverless v2 (PostgreSQL wire protocol over TLS)
- External Fraud Intelligence Feeds -> Real-Time Payment Fraud Screening System (HTTPS/REST webhooks)

## Technology Stack
- **Go (Golang)** on **AWS Fargate**: Selected for the Scoring Service Container to guarantee predictable low memory footprint and sub-50ms P99 latency.
- **Node.js / TypeScript** on **AWS Fargate**: Powers the Case Management Container for analyst workflows and UI rendering.
- **Amazon ElastiCache for Redis**: Provides in-memory feature storage and hot rules caching for sub-millisecond lookups.
- **Amazon Aurora PostgreSQL Serverless v2**: Persists case management metadata and review actions securely.
- **AWS S3 Object Lock**: Enforces Compliance Mode for immutable, tamper-evident 7-year audit logging.
- **AWS KMS**: Manages envelope encryption, database column encryption, and customer-managed keys (CMKs).
- **AWS Cognito & AWS Secrets Manager**: Handle OIDC/OAuth2 authentication, RBAC, and dynamic secret rotation.

## Rationale
- Container isolation separates the high-throughput scoring hot path from analyst workflows, protecting performance and PCI-DSS boundaries.
- Managed AWS services and lean microservices architectures enable a 3-engineer team to operate reliably under the €25,000 monthly budget.