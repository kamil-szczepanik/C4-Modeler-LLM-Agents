## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations and provides case management for fraud analysts. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms latency and 7-year auditability.

## Key Elements
* Fraud Analyst, Merchant Risk Manager, Compliance / Auditor Officer
* AWS API Gateway
* Real-Time Scoring Engine (Go / Java, AWS ECS Fargate)
* Case Management Backend (AWS ECS Fargate)
* Amazon Aurora PostgreSQL (Amazon Aurora PostgreSQL)
* Amazon S3 (Amazon S3)
* Amazon ElastiCache (Redis) (Amazon ElastiCache (Redis))
* Amazon SQS (AWS SQS)
* Amazon RDS Proxy

## Relationships
* Real-Time Scoring Engine -> Amazon SQS: Pushes decision audit payloads [HTTPS / AWS SDK]
* Case Management Backend -> Amazon RDS Proxy: Reads and writes case data and transaction records [PostgreSQL wire protocol over TLS 1.3]
* Amazon RDS Proxy -> Amazon Aurora PostgreSQL: Manages connection pooling and routes queries [PostgreSQL wire protocol over TLS 1.3]
* Real-Time Scoring Engine -> Amazon ElastiCache (Redis): Queries real-time feature stores [RESP over TCP with TLS]

## Technology Stack
* AWS ECS Fargate: Provides serverless container orchestration within a 3-engineer team limit.
* Amazon Aurora PostgreSQL: Relational storage for active case management and transaction history.
* Amazon RDS Proxy: Handles connection pooling and prevents thread exhaustion under high load.
* Amazon S3 with WORM storage: Provides immutable, tamper-evident 7-year audit log retention.
* AWS KMS & Secrets Manager: Enforces encryption-at-rest and eliminates static credentials.

## Rationale
This architecture decouples high-volume audit logging via Amazon SQS and utilizes RDS Proxy to protect Aurora PostgreSQL, ensuring P99 latency remains below 50 ms. It strictly enforces PCI-DSS Level 1 compliance and 7-year auditability while operating within a 25,000 EUR monthly budget.