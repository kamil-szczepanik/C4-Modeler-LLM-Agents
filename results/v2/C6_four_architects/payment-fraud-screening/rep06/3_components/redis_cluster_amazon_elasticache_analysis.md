## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for suspicious payments. It ensures low-latency decision-making while maintaining PCI-DSS Level 1 compliance and a 7-year audit trail.

## Key Elements
- Fraud Analysts (Users)
- External Systems: Payment Gateway / Core Ledger, Identity Provider / IdP, Compliance Archive / AWS S3 Object Lock
- API Gateway / Envoy (Envoy / HTTPS / TLS)
- Fraud Scoring Engine (Go / gRPC)
- Case Management Backend (Java / Spring Boot)
- Model & Rule Registry Service (Python / FastAPI / S3)
- Analyst UI (React / AWS S3 / CloudFront)
- Asynchronous Audit Worker (Go / AWS Lambda)
- Redis Cluster / Amazon ElastiCache: Primary Shards, Replica Shards, Cluster Manager (Redis Sentinel), In-Memory Token / Feature Index, Sliding Window Rate Limiter (Amazon ElastiCache (Redis))
- PostgreSQL / Amazon Aurora (Amazon Aurora (PostgreSQL))
- Amazon SQS / SNS (Amazon SQS / SNS)
- AWS Secrets Manager / Parameter Store (AWS Secrets Manager)

## Relationships
- API Gateway / Envoy -> Fraud Scoring Engine: Forwards authorization requests [gRPC / mTLS]
- Fraud Scoring Engine -> Redis Cluster / Amazon ElastiCache: Queries feature data and executes velocity checks [Redis RESP / TCP/TLS]
- Case Management Backend -> PostgreSQL / Amazon Aurora: Reads and writes case data [JDBC / TCP/TLS]
- Asynchronous Audit Worker -> Compliance Archive / AWS S3 Object Lock: Stores tamper-evident audit logs [HTTPS / TLS 1.3]

## Technology Stack
- AWS: Target cloud provider in region eu-west-1
- Go & Java (Spring Boot): High-performance backend services for scoring and case management
- Amazon ElastiCache (Redis v7.x): In-memory feature store and rate limiter
- Amazon Aurora (PostgreSQL): Durable relational storage with ACID compliance
- AWS S3 Object Lock: Tamper-evident 7-year audit trail storage

## Rationale
This architecture uses managed AWS services to minimize operational overhead for a three-person engineering team within a 25,000 EUR monthly budget. In-memory caching and optimized microservices ensure P99 decision latency stays below 50 ms at 3,000 TPS.