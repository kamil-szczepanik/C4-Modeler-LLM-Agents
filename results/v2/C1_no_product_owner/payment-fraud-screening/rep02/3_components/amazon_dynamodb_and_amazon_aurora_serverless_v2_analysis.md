## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud within sub-50ms latency while supporting case management reviews for analysts. It leverages a serverless AWS architecture designed for PCI-DSS Level 1 compliance and a 7-year auditability mandate.]

## Key Elements
- Fraud Scoring Engine (ECS Fargate, Go/Rust)
- Case Management Service (ECS Fargate, Node.js/Python)
- Amazon DynamoDB (Key-Value Store)
- Amazon Aurora Serverless v2 (Relational Store)
- Amazon RDS Proxy
- AWS KMS (Key Management Service)
- Amazon QLDB / S3 Object Lock buckets

## Relationships
- Fraud Scoring Engine -> Amazon DynamoDB: Query/Get Item [AWS SDK over TLS via VPC Endpoint]
- Case Management Service -> Amazon RDS Proxy: PostgreSQL Protocol over TLS
- Amazon RDS Proxy -> Amazon Aurora Serverless v2: PostgreSQL Protocol
- Fraud Scoring Engine & Case Management Service -> AWS KMS: Envelope Encryption [AWS SDK over TLS]

## Technology Stack
- AWS DynamoDB (On-Demand): Delivers sub-10ms operational lookups for velocity and rules within budget.
- Aurora PostgreSQL v15 (Serverless v2): Provides relational persistence for case management with a non-zero ACU floor for P99 latency.
- AWS RDS Proxy: Manages and pools database connections to prevent connection exhaustion.
- AWS KMS: Enforces customer-managed keys (CMKs) and annual rotation for data encryption.

## Rationale
[This architecture utilizes fully managed serverless AWS components to minimize operational toil for a three-engineer team while meeting strict sub-50ms P99 latency and PCI-DSS compliance limits. Security controls, private subnets, and immutable backups satisfy the 7-year auditability mandate within the 25,000 EUR monthly budget.]