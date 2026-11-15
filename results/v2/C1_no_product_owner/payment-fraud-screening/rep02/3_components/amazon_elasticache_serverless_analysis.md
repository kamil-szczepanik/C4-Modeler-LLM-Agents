## Overview
The system is a real-time payment fraud screening engine that evaluates card-not-present payment authorizations to protect against fraud while enabling analyst case reviews. It operates securely under PCI-DSS Level 1 compliance constraints on AWS in region eu-west-1.

## Key Elements
- Fraud Analysts and Payment Gateway / Acquirer Systems
- Fraud Scoring Engine (Go/Rust, ECS Fargate)
- Case Management Service (Node.js/Python, ECS Fargate)
- Amazon ElastiCache Serverless (Redis) with Rule & Model Cache Manager, Data Replication & Sharding Engine, and Encryption & Auth Gateway components
- Amazon Aurora Serverless v2 and Amazon DynamoDB
- AWS KMS (Key Management Service) and AWS Secrets Manager

## Relationships
- Fraud Scoring Engine -> Amazon ElastiCache Serverless (Encryption & Auth Gateway): In-memory reads/writes [RESP over TLS 1.3 with mTLS and Redis AUTH]
- Fraud Scoring Engine -> Amazon Aurora Serverless v2: Fallback scoring and state reads [PostgreSQL wire protocol over TLS 1.3]
- Case Management Service -> Amazon ElastiCache Serverless: Pushes dynamic rules and serialized models [RESP over TLS 1.3]

## Technology Stack
- Amazon ElastiCache Serverless (Redis): Provides sub-millisecond in-memory lookups for rules and models to meet strict latency goals.
- AWS KMS: Encrypts data at rest using customer-managed keys (CMKs) to satisfy PCI-DSS Level 1 compliance.
- AWS Secrets Manager: Manages automated rotation of Redis AUTH tokens for secure credential handling.
- Amazon CloudWatch: Tracks ElastiCache ECN consumption, CPU utilization, and latency for operational monitoring.

## Rationale
This architecture guarantees P99 decision latency under 50 ms at 3,000 TPS while respecting the €25,000 monthly budget limit. Ephemeral caching with robust failover ensures high availability and stringent PCI-DSS Level 1 security.