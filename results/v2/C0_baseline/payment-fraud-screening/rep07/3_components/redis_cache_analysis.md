## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations and manages reviews for fraud analysts. The architecture uses low-latency caching to meet rigorous performance and security constraints.

## Key Elements
- In-Memory Data Store (Redis Engine)
- Persistence/Backup Worker (AWS ElastiCache Managed Snapshot)
- Real-Time Scoring Engine
- Amazon ElastiCache (Redis)

## Relationships
- Real-Time Scoring Engine -> Redis Cache: Performs sub-millisecond feature lookups using RESP over TCP with mTLS and TLS 1.3
- Redis Cache -> Amazon S3: Stores daily automated backups with a 7-day retention period

## Technology Stack
- Amazon ElastiCache for Redis (Cluster Mode Disabled, Multi-AZ): Selected for sub-millisecond performance to meet the P99 < 50ms latency requirement.
- Graviton2 cache.m6g.large instances: Chosen for optimal price-performance to adhere to the €25,000/month infrastructure budget.
- Redis 7.x native ACLs and AWS IAM Database Authentication: Implemented to enforce least-privilege access and PCI-DSS compliance.
- AWS KMS: Used for at-rest encryption of cached cryptographic tokens and feature sets.

## Rationale
This architecture achieves sub-millisecond state lookups required for high-throughput fraud scoring while strictly containing costs for a three-person engineering team. It maintains PCI-DSS compliance through robust encryption, strict data minimization, and isolated private subnet deployment.