## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud and provides case management for human analysts. It operates within strict regulatory, performance, and budgetary constraints using managed cloud infrastructure.

## Key Elements
* Payment Gateway / Acquirer
* Fraud Analysts
* Card Networks & Tokenization Vault
* Regulatory & Audit Authorities
* Core Banking / Ledger System
* ML Model Training Environment
* Identity Provider (IdP)
* API Ingestion & Routing Container
* Real-Time Scoring Engine Container
* Case Management Backend Container
* Audit & Compliance Worker
* Fail-Open Circuit Breaker Proxy
* Model & Rule Sync Service
* Amazon ElastiCache (Redis)
* Amazon Aurora PostgreSQL
* Amazon S3 Object Lock

## Relationships
* Payment Gateway to API Ingestion: Synchronous gRPC over TLS 1.3
* Fraud Analysts to Case Management Backend: HTTPS over TLS 1.3 via AWS Client VPN or IAM-authenticated Web UI
* Real-Time Scoring Engine to Amazon ElastiCache: Redis TCP protocol over TLS
* Audit & Compliance Worker to Amazon S3 Object Lock: Asynchronous event export via AWS SDK
* Real-Time Scoring Engine to Audit SQS: AWS SDK async event dispatch

## Technology Stack
* AWS ECS on Fargate: Runs core stateless containers within the 25k EUR budget and 3-engineer constraint
* Go or Rust: High-performance runtime for the Real-Time Scoring Engine to meet <50ms P99 latency
* Amazon ElastiCache (Redis): In-memory cache for sub-millisecond feature lookups and zero-downtime model hot-swapping
* Amazon Aurora PostgreSQL: Relational database for persistent case management workflows
* Amazon S3 Object Lock: WORM storage ensuring tamper-evident 7-year audit log retention
* Envoy: Circuit breaker proxy ensuring automated fail-open availability under high latency

## Rationale
This architecture uses managed AWS services to minimize operational overhead for a three-engineer team while respecting a 25,000 EUR monthly budget. High-performance containers and caching guarantee sub-50ms P99 latency and high availability to satisfy strict payment processing SLAs.