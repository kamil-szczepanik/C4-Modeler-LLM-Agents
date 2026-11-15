## Overview
The system screens card-not-present payment authorizations for fraud in real-time while providing case management for fraud analysts. It ensures sub-50ms decision latency and compliance with PCI-DSS Level 1 within a strict AWS budget.

## Key Elements
* Amazon ElastiCache (Redis Cluster): In-memory feature store for low-latency lookups.
* Scoring Engine Container: Go/Rust service running on AWS ECS Fargate.
* Model Registry / Feature Store: External system supplying scoring models and features.
* AWS CloudWatch & SNS: Monitoring and alerting infrastructure.
* AWS Secrets Manager: Credential management for Redis AUTH tokens.

## Relationships
* Scoring Engine Container -> Amazon ElastiCache: Performs feature lookups via TCP/Redis with TLS 1.3 and Redis AUTH tokens.
* Model Registry / Feature Store -> Amazon ElastiCache: Synchronizes features via asynchronous worker over TCP/Redis.
* Amazon ElastiCache -> AWS CloudWatch: Emits performance metrics and slow logs.

## Technology Stack
* AWS ElastiCache (Redis OSS, `cache.m6g.large` nodes): Chosen for sub-millisecond retrieval speeds to meet P99 latency requirements.
* Redis `volatile-lru` eviction policy: Prevents memory bloat and controls infrastructure costs.
* TLS 1.3 and Redis AUTH: Enforces strict data-in-transit security for PCI-DSS Level 1 compliance.
* AWS KMS: Encrypts data at rest within the cache cluster.

## Rationale
This architecture uses an in-memory Redis cluster to achieve sub-millisecond feature lookups, guaranteeing decision latencies below 50ms at scale. Stringent security controls and budget-conscious node sizing satisfy PCI-DSS Level 1 mandates and financial constraints without exceeding operational capacity.