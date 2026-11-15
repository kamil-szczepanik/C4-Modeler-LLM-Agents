## Overview
The Real-Time Payment Fraud Screening system processes card-not-present authorizations to prevent fraud and manage analyst reviews. It operates on AWS with strict compliance, auditability, and performance constraints.

## Key Elements
- Fraud Analyst
- Payment Gateway / Core Processing Platform
- AWS API Gateway / Application Load Balancer (ALB)
- Fraud Scoring Engine (Go/Rust on AWS ECS Fargate)
- Case Management Service (Node.js/TypeScript on AWS ECS Fargate)
- Amazon Aurora PostgreSQL with PgBouncer Connection Pooler
- Amazon ElastiCache Redis
- Amazon S3 Immutable Vault (Object Lock in Compliance Mode)
- Amazon SQS / SNS
- AWS Key Management Service (KMS)

## Relationships
- Payment Gateway -> AWS API Gateway / ALB: Sends authorization requests [HTTPS / TLS 1.3]
- AWS API Gateway / ALB -> Fraud Scoring Engine: Routes requests [gRPC / HTTP/2]
- Fraud Scoring Engine -> Amazon ElastiCache Redis: Low-latency rule and model lookups [Redis Protocol over TLS]
- Fraud Scoring Engine -> Connection Pooler (PgBouncer): Fetches context [PostgreSQL Wire Protocol over TLS 1.3]
- Case Management Service -> Connection Pooler (PgBouncer): Reads/writes case data [PostgreSQL Wire Protocol over TLS 1.3]
- Fraud Scoring Engine -> Amazon S3 Immutable Vault: Stores tamper-evident audit records [AWS SDK / HTTPS]
- Amazon Aurora PostgreSQL -> AWS KMS: Encrypts data at rest [Internal AWS API]

## Technology Stack
- AWS ECS Fargate: Provides scalable, serverless container execution fitting the 3-engineer team size.
- Amazon Aurora PostgreSQL 15: Manages ACID-compliant case data with multi-AZ replication.
- PgBouncer: Handles high concurrency and prevents database connection exhaustion.
- Amazon ElastiCache Redis: Delivers sub-50ms P99 decision latency for rule evaluations.
- Amazon S3 Object Lock: Implements Compliance Mode for 7-year tamper-evident audit storage.
- AWS KMS: Secures data encryption at rest for PCI-DSS Level 1 compliance.

## Rationale
This architecture uses serverless and managed AWS services to maintain high availability and PCI-DSS Level 1 compliance within a 25,000 EUR monthly budget. It meets the strict sub-50ms latency and 7-year auditability requirements while remaining operable by a three-engineer team.