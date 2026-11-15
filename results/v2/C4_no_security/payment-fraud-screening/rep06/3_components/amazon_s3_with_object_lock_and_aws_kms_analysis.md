## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations in real time to prevent fraud. It ensures sub-50ms decision latency, PCI-DSS compliance, and 7-year tamper-evident auditability within a fixed AWS infrastructure budget.

## Key Elements
- Shopper / Cardholder & Merchant / Payment Gateway
- Frontend Web App (React SPA)
- AWS ALB / API Gateway
- Real-Time Scoring Engine (Go, Amazon ECS Fargate)
- Case Management & Analytics API (Backend service)
- Amazon RDS PostgreSQL & Amazon ElastiCache (Redis)
- Amazon S3 with Object Lock and AWS KMS (WORM storage and encryption)
- AWS Kinesis Data Streams / Amazon SQS

## Relationships
- Shopper / Cardholder -> Merchant / Payment Gateway: Submits payment authorization [HTTPS]
- Merchant / Payment Gateway -> AWS ALB / API Gateway: Forwards authorization request [HTTPS]
- AWS ALB / API Gateway -> Real-Time Scoring Engine: Routes screening request [HTTP/2, gRPC]
- Real-Time Scoring Engine -> Amazon RDS PostgreSQL & Amazon ElastiCache (Redis): Fetches profiles and model data [TCP]
- Real-Time Scoring Engine -> Amazon S3 with Object Lock and AWS KMS: Writes tamper-evident audit logs [HTTPS, AWS SDK]
- Case Management & Analytics API -> Frontend Web App (React SPA): Serves case review UI [HTTPS]

## Technology Stack
- AWS ECS Fargate: Scalable container orchestration for the scoring engine, fitting a three-engineer team model.
- Go: High-performance language for low-latency scoring under 50 ms P99.
- Amazon ElastiCache (Redis): Low-latency caching for real-time feature stores.
- Amazon RDS PostgreSQL: Relational storage for case management and structured fraud data.
- Amazon S3 with Object Lock and AWS KMS: Immutable WORM storage ensuring 7-year tamper-evident compliance and security.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team. Immutable S3 storage paired with Redis and Go containers guarantees strict PCI-DSS compliance, auditability, and sub-50ms latency within the 25,000 EUR monthly budget.