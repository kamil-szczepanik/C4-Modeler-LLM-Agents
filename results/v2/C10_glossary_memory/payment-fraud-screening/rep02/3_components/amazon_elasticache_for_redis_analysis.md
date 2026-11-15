## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations for a mid-size payment processor to detect fraud within a sub-50ms latency window while providing case management for analysts. It operates on AWS within a strict PCI-DSS Level 1 compliance boundary, balancing high performance with a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analyst & Risk Operations Manager [person]
- Payment Gateway / Acquiring System [externalSystem]
- External Fraud Intelligence Feeds [externalSystem]
- AWS API Gateway / Envoy Proxy [externalSystem]
- AWS Cognito [externalSystem]
- AWS S3 Object Lock [externalSystem]
- AWS KMS [externalSystem]
- Scoring Service Container (Go / AWS Fargate) [container]
- Case Management Container (Node.js / TypeScript / AWS Fargate) [container]
- Amazon ElastiCache for Redis (in-memory cache) [container]
- Amazon Aurora PostgreSQL Serverless v2 (relational database) [container]
- Feature Store Engine [component]
- Rules Cache Engine [component]

## Relationships
- Payment Gateway / Acquiring System -> AWS API Gateway / Envoy Proxy (gRPC over mTLS)
- Fraud Analyst & Risk Operations Manager -> AWS Cognito (OIDC/OAuth2 over HTTPS/REST)
- External Fraud Intelligence Feeds -> Real-Time Payment Fraud Screening System (HTTPS/REST webhooks)
- AWS API Gateway / Envoy Proxy -> Scoring Service Container (gRPC)
- Scoring Service Container -> Amazon ElastiCache for Redis (RESP over TLS)
- Scoring Service Container -> Feature Store Engine (RESP over TLS)
- Scoring Service Container -> Rules Cache Engine (RESP over TLS)
- Scoring Service Container -> AWS S3 Object Lock (AWS SDK / HTTPS)
- Case Management Container -> Amazon Aurora PostgreSQL Serverless v2 (PostgreSQL wire protocol over TLS)

## Technology Stack
- AWS Fargate: Executes containerized microservices with predictable low memory footprint and rapid scalability.
- Go: Powers the Scoring Service Container for predictable low memory usage and sub-50ms P99 latency.
- Node.js / TypeScript: Powers the Case Management Container for rapid analyst workflow development.
- Amazon ElastiCache for Redis (Redis OSS / Valkey): Delivers sub-millisecond lookups for feature storage and hot rules caching.
- Amazon Aurora PostgreSQL Serverless v2: Persists case management metadata and review actions securely.
- AWS S3 Object Lock: Provides immutable storage configured in Compliance Mode for 7-year audit logging.
- AWS KMS: Manages envelope encryption and hardware-isolated keys for PCI-DSS Level 1 data protection.
- AWS Cognito: Manages identity, OIDC/OAuth2 authentication, and role-based access control.

## Rationale
This architecture uses serverless container and database technologies on AWS to meet high throughput and low latency demands within a fixed budget and small team. Managed services reduce operational overhead while satisfying stringent PCI-DSS Level 1 compliance and 7-year auditability mandates.