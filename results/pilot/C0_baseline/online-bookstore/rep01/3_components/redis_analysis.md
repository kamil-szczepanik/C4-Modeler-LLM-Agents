## Overview
[The Online Bookstore caching layer utilizes Redis to provide ultra-fast, in-memory currency exchange rate lookups for international shoppers. It ensures rapid global checkout performance while shielding backend systems from third-party financial API rate limits.]

## Key Elements
- In-Memory Data Store Engine (Redis Hash data structures)
- Eviction Policy Manager (`volatile-lru` with TTL)
- Replication & Persistence Module (AOF persistence, asynchronous master-replica)
- Amazon ElastiCache (Multi-AZ with automatic failover)
- ECS Fargate Go Microservices

## Relationships
- ECS Fargate Go Microservices -> In-Memory Data Store Engine: Reads currency exchange rates via Redis Serialization Protocol (RESP) over TCP with TLS.
- In-Memory Data Store Engine -> AWS KMS: Encrypts data at rest using customer-managed keys.
- Amazon ElastiCache -> CloudWatch: Exports metrics including `DatabaseMemoryUsagePercentage` and `EngineCPUUtilization`.

## Technology Stack
- Redis: In-memory data store for sub-millisecond currency rate serialization and lookup.
- Amazon ElastiCache: Managed Redis service providing Multi-AZ high availability and automated failover.
- RESP (REdis Serialization Protocol): Lightweight TCP protocol for microservice communication.
- AWS KMS: Encryption at rest for data protection and compliance.

## Rationale
[In-memory caching via Redis satisfies strict performance requirements by delivering sub-millisecond currency conversions and keeping page loads under 2 seconds. Multi-AZ deployment through Amazon ElastiCache guarantees 99.95% uptime and reliable checkout availability across all target regions.]