## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage reviews while ensuring strict compliance. It processes up to 3,000 requests per second with sub-50ms P99 latency while adhering to PCI-DSS Level 1 standards.

## Key Elements
- Fraud Analysts, ML Engineers / Data Scientists, Finance / Operations Managers
- AWS API Gateway / Network Load Balancer
- Fraud Scoring Engine (Go)
- Case Management Backend (Java / Spring Boot with React UI)
- Audit Logger (AWS Lambda / Worker)
- Feature Store (Amazon ElastiCache for Redis)
- Relational Store (Amazon RDS for PostgreSQL)
- Tamper-Evident Storage (Amazon S3 with Object Lock in Compliance Mode)
- Message Queue (Amazon SQS with AWS KMS encryption, comprising `fraud-decisions-queue` and `fraud-decisions-dlq`)

## Relationships
- Fraud Scoring Engine -> Message Queue: Asynchronously publishes decision payloads via HTTPS [Amazon SQS API, TLS 1.3]
- Message Queue -> Audit Logger: Consumes decision payloads for immutable logging [Event-driven consumption]
- Payment Gateway -> AWS API Gateway: Ingests payment authorization requests [HTTPS]
- Case Management Backend -> Amazon RDS for PostgreSQL: Persists review cases and analyst actions [SQL/TLS]

## Technology Stack
- AWS (eu-west-1): Cloud provider hosting the serverless and containerized infrastructure within a fixed budget of 25,000 EUR/month.
- Go & Java / Spring Boot: High-performance backend runtime environments for low-latency scoring and robust case management.
- Amazon SQS & AWS KMS: Serverless decoupling layer with customer-managed key encryption at rest to maintain PCI compliance.
- Amazon S3 (Object Lock Compliance Mode): Tamper-evident immutable storage ensuring 7-year audit retention.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while guaranteeing sub-50ms latency. Strict data minimization, IAM policies, and immutable storage ensure compliance with PCI-DSS Level 1 and 7-year audit constraints within the fixed infrastructure budget.