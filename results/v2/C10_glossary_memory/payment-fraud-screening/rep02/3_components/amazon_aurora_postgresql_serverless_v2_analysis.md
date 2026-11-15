## Overview
The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud within a sub-50ms latency window while providing case management for analysts. It is operated by a three-person engineering team on AWS with PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analyst & Risk Operations Manager [person, context]
- Payment Gateway / Acquiring System [externalSystem, context]
- External Fraud Intelligence Feeds [externalSystem, context]
- AWS API Gateway / Envoy Proxy [externalSystem, context]
- AWS Fargate [externalSystem, context]
- AWS Cognito [externalSystem, context]
- AWS S3 Object Lock [externalSystem, context]
- AWS KMS [externalSystem, context]
- Scoring Service Container [container, container] (Go / AWS Fargate)
- Case Management Container [container, container] (Node.js / TypeScript / AWS Fargate)
- Amazon ElastiCache for Redis [container, container] (in-memory cache)
- Amazon Aurora PostgreSQL Serverless v2 [container, container] (relational database)

## Relationships
- Payment Gateway / Acquiring System -> AWS API Gateway / Envoy Proxy (gRPC over mTLS)
- Fraud Analyst & Risk Operations Manager -> AWS Cognito (OIDC/OAuth2 over HTTPS/REST)
- External Fraud Intelligence Feeds -> Real-Time Payment Fraud Screening System (HTTPS/REST webhooks)
- AWS API Gateway / Envoy Proxy -> Scoring Service Container (gRPC)
- Scoring Service Container -> Amazon ElastiCache for Redis (RESP over TLS)
- Scoring Service Container -> AWS S3 Object Lock (AWS SDK / HTTPS)
- Case Management Container -> Amazon Aurora PostgreSQL Serverless v2 (PostgreSQL wire protocol over TLS 1.3)
- AWS Fargate -> AWS S3 Object Lock (AWS SDK (HTTPS))

## Technology Stack
- AWS Fargate: Executes containerized microservices with minimal administrative overhead for a three-person team.
- Amazon Aurora PostgreSQL Serverless v2: Automatically scales compute to fit a 25,000 EUR monthly budget while persisting case data.
- Amazon ElastiCache for Redis: Delivers sub-millisecond lookups for hot rules and features to meet the sub-50ms P99 latency requirement.
- AWS S3 Object Lock: Provides tamper-evident, immutable storage in Compliance Mode for 7-year audit retention.
- AWS KMS: Manages envelope encryption and customer-managed keys for PCI-DSS Level 1 data protection.
- AWS Cognito: Handles OIDC/OAuth2 authentication and role-based access control.

## Rationale
This architecture meets the sub-50ms P99 latency and PCI-DSS Level 1 requirements by leveraging managed AWS services that minimize operational overhead for a three-person engineering team. Serverless and autoscaling components ensure compliance with the 25,000 EUR monthly infrastructure budget.