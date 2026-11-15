## Overview
[Real-Time Payment Fraud Screening System] screens card-not-present payment authorizations for fraud in real time while providing case management for fraud analysts. It is operated by three engineers within a fixed €25,000/monthly AWS infrastructure budget while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Real-Time Payment Fraud Screening System (System)
- Fraud Analyst & Risk Operations Manager (Person)
- Payment Gateway / Acquiring System (External System)
- External Fraud Intelligence Feeds (External System)
- AWS API Gateway / Envoy Proxy (External System)
- AWS Fargate (External System)
- AWS Cognito (External System)
- AWS S3 Object Lock (External System)
- AWS KMS (External System)
- Scoring Service Container (Container - Go / AWS Fargate)
  - API Handler Component
  - Scoring Engine Component
  - Audit Dispatcher Component
  - Circuit Breaker & Fallback Manager Component
- Case Management Container (Container - Node.js / TypeScript / AWS Fargate)
- Amazon ElastiCache for Redis (Container - In-memory cache)
- Amazon Aurora PostgreSQL Serverless v2 (Container - Relational database)

## Relationships
- Payment Gateway / Acquiring System -> AWS API Gateway / Envoy Proxy (gRPC over mTLS)
- Fraud Analyst & Risk Operations Manager -> AWS Cognito (OIDC/OAuth2 over HTTPS/REST)
- External Fraud Intelligence Feeds -> Real-Time Payment Fraud Screening System (HTTPS/REST webhooks)
- AWS API Gateway / Envoy Proxy -> Scoring Service Container (gRPC over mTLS)
- Scoring Service Container -> Amazon ElastiCache for Redis (RESP over TLS)
- Scoring Service Container -> AWS S3 Object Lock (AWS SDK / HTTPS)
- Case Management Container -> Amazon Aurora PostgreSQL Serverless v2 (PostgreSQL wire protocol over TLS)

## Technology Stack
- Go on AWS Fargate: Selected for the Scoring Service Container to deliver predictable low memory footprint and sub-50ms P99 latency.
- Node.js / TypeScript on AWS Fargate: Powers the Case Management Container for rapid analyst UI and workflow iteration.
- Amazon ElastiCache for Redis: Provides in-memory feature storage and hot-rules caching for sub-millisecond lookups.
- Amazon Aurora PostgreSQL Serverless v2: Persists case management metadata and review actions securely with auto-scaling capabilities.
- AWS S3 Object Lock: Configured in Compliance Mode for tamper-evident, 7-year audit logging.
- AWS KMS: Manages envelope encryption and Fargate ephemeral storage encryption for PCI-DSS compliance.

## Rationale
This architecture utilizes containerized microservices on AWS Fargate paired with an in-memory Redis cache to meet the strict sub-50ms P99 latency requirement at 3,000 transactions per second. Immutable storage via AWS S3 Object Lock and AWS KMS encryption ensure PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a strict €25,000 monthly budget.