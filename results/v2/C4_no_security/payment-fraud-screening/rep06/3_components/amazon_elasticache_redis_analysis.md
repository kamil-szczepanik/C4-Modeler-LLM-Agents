## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations and manages fraud analyst reviews. It provides sub-50ms fraud decisions while maintaining strict PCI-DSS Level 1 compliance on AWS.

## Key Elements
- Shopper / Cardholder & Merchant / Payment Gateway (External Users and Systems)
- Frontend Web App (React SPA)
- Case Management & Analytics API (Backend service)
- Real-Time Scoring Engine (Go, Amazon ECS Fargate)
- Amazon ElastiCache (Redis) (Feature store and cache)
- Amazon RDS PostgreSQL (Primary relational database)
- Amazon S3 with Object Lock and AWS KMS (Tamper-evident audit logs and backups)
- AWS Kinesis Data Streams / Amazon SQS (Event streaming)
- AWS ALB / API Gateway (Ingress management)

## Relationships
- Shopper / Merchant -> AWS ALB / API Gateway: Submits payment authorizations over HTTPS / gRPC
- Real-Time Scoring Engine -> Amazon ElastiCache (Redis): Retrieves transient feature vectors via RESP (TLS 1.2+)
- Real-Time Scoring Engine -> Amazon RDS PostgreSQL: Reads fraud rules and writes audit logs via SQL/TLS
- Fraud Analyst -> Frontend Web App: Reviews suspicious payments over HTTPS
- Frontend Web App -> Case Management & Analytics API: Manages review cases over HTTPS / JSON

## Technology Stack
- Amazon ECS Fargate: Container orchestration chosen for zero-server-management overhead by a 3-engineer team.
- Amazon ElastiCache (Redis): In-memory feature store using Redis Hashes for O(1) lookups under 50ms P99 latency.
- Amazon RDS PostgreSQL: Relational store for rules and cases, supporting ACID compliance.
- Amazon S3 with Object Lock: Provides immutable 7-year audit retention required for compliance.
- AWS KMS: Encrypts data at rest across data stores for PCI-DSS Level 1 compliance.

## Rationale
This AWS-centric serverless and managed-service architecture keeps operational overhead minimal for a three-engineer team within a 25,000 EUR monthly budget. It leverages Redis for sub-50ms P99 decision latency and multi-AZ deployments with S3 Object Lock to guarantee PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.