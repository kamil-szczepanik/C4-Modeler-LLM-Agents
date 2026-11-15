## Overview
- Scaled-down Amazon-style e-commerce site for purchasing books, reviews, and recommendations.
- Built to handle 1M MAU globally with high availability and strict GDPR/CCPA compliance.

## Key Elements
- **Users**: Book Buyer, Registered Reviewer, Store Administrator
- **External Systems**: Stripe/PayPal, FedEx/UPS, Auth0/AWS Cognito, AWS SES, Currency Exchange Rate Service
- **Containers**: React/TypeScript SPA, AWS API Gateway, Order & Checkout Service, Catalog & Search Service, Recommendations Service, Review Service, Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), AWS EventBridge
- **Components (Amazon RDS PostgreSQL)**: PostgreSQL Relational Engine (v15+), PgBouncer Connection Pooler, AWS Backup & PITR Manager, Cross-Region Read Replicas, PostgreSQL Row-Level Security (RLS) Policies, pgaudit Extension

## Relationships
- `Order & Checkout Service` -> `PgBouncer Connection Pooler`: Queries and transactions [Encrypted TCP, TLS 1.3]
- `PgBouncer Connection Pooler` -> `PostgreSQL Relational Engine`: Multiplexed backend connections [TCP, UNIX domain socket]
- `Catalog & Search Service` -> `PostgreSQL Relational Engine`: CDC write/sync operations [Encrypted TCP]
- `AWS Backup & PITR Manager` -> `Cross-Region Read Replicas`: Synchronizes encrypted snapshots [AWS internal backbone, KMS]

## Technology Stack
- **Amazon RDS PostgreSQL**: Provides ACID-compliant transactional storage for orders and payments.
- **PgBouncer**: Manages connection pooling to prevent exhaustion under high traffic.
- **AWS KMS**: Enforces data-at-rest encryption using customer-managed keys.
- **Debezium**: Executes Change Data Capture (CDC) to synchronize catalogue data with search services.

## Rationale
- Isolating transactional workloads in RDS PostgreSQL ensures secure, ACID-compliant checkouts and strict GDPR/CCPA data residency compliance.
- PgBouncer and Multi-AZ replication sustain 99.95% uptime and performance targets for 1M MAU.