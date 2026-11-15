## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud, and provides case management for human analysts. It operates on AWS to meet strict PCI-DSS Level 1 compliance, sub-50ms latency, and 7-year auditability constraints.

## Key Elements
- Fraud Analyst
- Payment Gateway / Core Processing Platform
- AWS API Gateway / Application Load Balancer
- Fraud Scoring Engine (AWS ECS Fargate)
- Case Management Service (AWS ECS Fargate)
- Amazon ElastiCache Redis
- Amazon Aurora PostgreSQL
- Amazon S3 Immutable Vault
- Fraud Event Topic (Amazon SNS)
- Review Queue (Amazon SQS Standard)
- Audit Event Queue (Amazon SQS FIFO)
- Audit Dead-Letter Queue (Amazon SQS FIFO)

## Relationships
- Fraud Analyst -> AWS API Gateway / ALB: Manages suspicious payment reviews [HTTPS]
- Payment Gateway -> AWS API Gateway / ALB: Submits payment authorization requests [HTTPS, REST]
- Fraud Scoring Engine -> Amazon Aurora PostgreSQL: Reads scoring rules and model metadata [PostgreSQL Wire Protocol]
- Fraud Scoring Engine -> Amazon ElastiCache Redis: Caches tokenized card velocity and profile data [Redis Protocol]
- Fraud Scoring Engine -> Fraud Event Topic (Amazon SNS): Publishes scoring outcomes [AWS SDK, HTTPS]
- Fraud Event Topic -> Review Queue (Amazon SQS): Filters and fans out review cases [SNS Subscription]
- Case Management Service -> Review Queue (Amazon SQS): Polls review tasks [AWS SDK, Long Polling]
- Fraud Scoring Engine -> Audit Event Queue (Amazon SQS FIFO): Publishes decision payloads asynchronously [AWS SDK, SSE-KMS]
- Audit Event Queue -> Amazon S3 Immutable Vault: Commits audit logs with Object Lock [AWS SDK]

## Technology Stack
- AWS ECS Fargate: Runs containerized microservices without server management overhead.
- Amazon SQS FIFO: Guarantees strict ordering for audit logs and zero data loss.
- Amazon SNS: Enables scalable fan-out of domain events.
- Amazon S3 Object Lock: Enforces tamper-evident compliance mode for 7-year audit retention.
- Amazon ElastiCache Redis: Delivers sub-millisecond data retrieval to satisfy P99 latency limits.
- Amazon Aurora PostgreSQL: Provides reliable, ACID-compliant relational storage for case management.

## Rationale
This architecture decouples real-time scoring from asynchronous auditing and case management to easily achieve the sub-50ms P99 latency requirement. Utilizing managed AWS serverless and container services keeps infrastructure costs well within the 25,000 EUR monthly budget while maintaining a lean three-engineer operations team.