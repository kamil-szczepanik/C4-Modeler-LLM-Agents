## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and provides case management for analysts. It ensures PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and 7-year auditable decision storage within a 25,000 EUR monthly budget on AWS.

## Key Elements
- Fraud Analyst (User)
- Payment Gateway / Core Processing Platform
- AWS API Gateway / ALB
- Fraud Scoring Engine (AWS ECS Fargate, Go/Rust)
- Case Management Service (AWS ECS Fargate, Node.js/TypeScript)
- Amazon ElastiCache Redis (Redis Engine, Multi-AZ Cluster Mode Enabled)
- Feature Store Component (In-Memory Hash/Sorted Sets)
- Rule Cache Component (In-Memory KV)
- Session State Component (In-Memory KV)
- Amazon Aurora PostgreSQL
- Amazon S3 Immutable Vault (Object Lock in Compliance Mode)
- AWS KMS / HSM

## Relationships
- Payment Gateway -> AWS API Gateway / ALB: Sends authorization requests [HTTPS/JSON]
- Fraud Analyst -> AWS API Gateway / ALB: Reviews suspicious payments [HTTPS/JSON]
- Fraud Scoring Engine -> Feature Store Component: Reads/writes sliding-window aggregates and velocity metrics [RESP/TCP]
- Fraud Scoring Engine -> Rule Cache Component: Reads active fraud rules and model thresholds [RESP/TCP]
- Case Management Service -> Session State Component: Reads/writes analyst session states and workspace locks [RESP/TCP]
- Fraud Scoring Engine -> Amazon Aurora PostgreSQL: Persists decision logs and metadata [PostgreSQL Wire Protocol/TLS]
- Fraud Scoring Engine -> Amazon S3 Immutable Vault: Stores tamper-evident decision inputs and explanations [HTTPS/AWS SigV4]

## Technology Stack
- AWS ECS Fargate: Container orchestration matching the 3-engineer operational capacity with zero server management overhead.
- Amazon ElastiCache Redis: Delivers sub-millisecond feature store and rule caching to achieve <50ms P99 latency.
- Amazon Aurora PostgreSQL: Provides scalable relational storage for case management and structured audit trails.
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year compliance audit storage.
- AWS KMS / HSM: Handles PCI-DSS compliant encryption and tokenization.

## Rationale
This architecture uses serverless containers and managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to 3,000 TPS. In-memory caching via Redis and strict data segregation ensure sub-50ms latency and strict PCI-DSS Level 1 compliance within the 25,000 EUR budget.