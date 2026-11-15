## Overview
Real-Time Payment Fraud Screening is an AWS-hosted cloud system that screens card-not-present payment authorizations for fraud and manages analyst review cases. It meets strict PCI-DSS Level 1 compliance while processing thousands of requests per second under tight latency constraints.

## Key Elements
* Fraud Analysts
* Payment Gateway / Acquirer
* Identity Provider (IdP)
* Audit Sink
* Secrets Manager
* AWS ALB (Ingress / API Gateway)
* Fraud Scoring Engine (Go container on Amazon ECS on EC2)
* Case Management API (Node.js/TypeScript container on Amazon ECS on EC2)
* Redis Feature Store (Amazon ElastiCache Multi-AZ)
* Transactional & Audit Data Store (Amazon RDS PostgreSQL)
* Asynchronous Messaging (Amazon SQS)

## Relationships
* Payment Gateway calls Fraud Scoring Engine via gRPC over mTLS (<40ms timeout)
* Fraud Analysts access Case Management API via HTTPS using OAuth 2.0 / OIDC
* Scoring Engine and Case Management API read/write to Amazon ElastiCache Redis and Amazon RDS PostgreSQL
* Scoring Engine and Case Management API publish tamper-evident audit logs to Amazon SQS

## Technology Stack
* AWS Cloud (eu-west-1): Target infrastructure provider
* Go: Used for Scoring Engine for sub-millisecond execution and predictable memory
* Node.js/TypeScript: Used for Case Management API to streamline analyst workflows
* Amazon ECS on EC2: Container orchestration for pinned CPU/memory to eliminate hypervisor jitter
* Amazon ElastiCache Redis: Low-latency feature store and rule caching with automatic failover
* Amazon RDS PostgreSQL: Transactional case storage and append-only audit logs with IAM auth
* Amazon SQS: Serverless, low-overhead asynchronous messaging for audit events
* AWS Secrets Manager: Secure runtime injection of database credentials and encryption keys

## Rationale
This architecture uses pinned EC2 instances with Go services and gRPC to guarantee sub-50ms P99 latency at high throughput within a €25k monthly budget. It ensures strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while remaining maintainable by a three-engineer team.