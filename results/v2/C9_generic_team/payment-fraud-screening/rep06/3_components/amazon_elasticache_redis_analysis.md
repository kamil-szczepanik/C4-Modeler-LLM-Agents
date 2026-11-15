## Overview
Amazon ElastiCache (Redis) provides high-performance, in-memory caching for feature vectors and rule states to meet sub-50ms latency targets. It is optimized for read-heavy transactional scoring while ensuring strict security and zero-downtime model updates.

## Key Elements
- Amazon ElastiCache (Redis) Cluster (Multi-AZ with replication group)
- Real-Time Scoring Engine Container (AWS ECS with Fargate)
- Amazon Aurora (Primary Database)
- Amazon CloudWatch / AWS KMS

## Relationships
- Real-Time Scoring Engine Container -> Amazon ElastiCache (Redis): Queries cached feature vectors using Redis Protocol over TLS 1.3
- Amazon ElastiCache (Redis) -> Amazon Aurora: Fallback data source on cache misses

## Technology Stack
- Amazon ElastiCache (Redis): In-memory store for sub-50ms P99 latency at 3,000 TPS
- AWS KMS: Encrypts cached data at rest for PCI-DSS compliance
- Protocol Buffers / Optimized JSON: Compact serialization to minimize memory footprint
- CloudWatch & SNS: Automated telemetry and alerting for 3-person ops team

## Rationale
This architecture uses an in-memory caching tier with automated failover and read-replica routing to guarantee sub-50ms decision latency under heavy load. Security controls and zero-downtime deployment strategies satisfy compliance and operational constraints for a small engineering team.