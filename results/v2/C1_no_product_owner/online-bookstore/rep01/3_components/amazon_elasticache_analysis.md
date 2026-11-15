## Overview
The Online Bookstore uses Amazon ElastiCache (Redis) as an in-memory data store to manage transient shopping cart states, user sessions, and low-latency product recommendations. It is architected for high availability, sub-millisecond retrieval times, and strict GDPR/CCPA compliance across multi-AZ AWS deployments.

## Key Elements
- Cache Router / Cluster Manager (Redis Cluster)
- In-Memory Recommendation Store (Redis Hash & Sorted Set)
- Session & Token Cache (Redis String / Key-Value Store)
- Catalog Service (Go, AWS ECS Fargate)
- Order & Checkout Service (Node.js, AWS ECS Fargate)
- Recommendation Service (Python FastAPI, AWS ECS Fargate)
- AWS Secrets Manager & AWS KMS
- Amazon CloudWatch Logs

## Relationships
- Catalog Service -> In-Memory Recommendation Store: Reads pre-computed collaborative filtering data [Redis Protocol]
- Order & Checkout Service -> Session & Token Cache: Stores transient shopping cart items and checkout locks [Redis Protocol]
- Catalog Service -> Amazon ElastiCache: Invalidates and reads product detail cache [Redis Protocol]
- Recommendation Service -> Amazon ElastiCache: Reads recommendation cache [Redis Protocol]
- Cache Router / Cluster Manager -> Redis Shards: Routes data across multi-AZ topology [Redis Protocol]

## Technology Stack
- Amazon ElastiCache (Redis): In-memory caching for high performance (<2s page load) and session management.
- Redis Cluster: Sharding and multi-AZ replication for 99.95% uptime and high availability.
- AWS Secrets Manager: Secure runtime injection and automated rotation of Redis AUTH tokens.
- AWS KMS & TLS: Encryption at rest and in-transit for data protection and GDPR/CCPA compliance.
- Amazon CloudWatch: Monitoring of `EngineCPUUtilization`, `SwapUsage`, and Redis Slow Logs for security audits.

## Rationale
This architecture guarantees sub-millisecond data retrieval to meet rigorous performance constraints under 1M MAU traffic. Furthermore, encryption, strict TTLs, and private subnet isolation ensure compliance with security and privacy mandates.