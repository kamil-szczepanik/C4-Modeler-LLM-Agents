## Overview
The system is a scalable online bookstore providing browsing, secure checkout, reviews, and recommendations for 1M MAU. It utilizes an in-memory caching architecture via Amazon ElastiCache (Redis) to ensure high performance and low latency.

## Key Elements
* **Catalog Cache Component**: Stores serialized book metadata, search facets, and cached third-party recommendations.
* **Session & Cart Cache Component**: Stores ephemeral user session tokens and active shopping cart hashes with strict non-eviction policies.
* **Inventory Counter Component**: Stores atomic integer counters for real-time stock levels during flash sales.

## Relationships
* **Catalog Service -> Catalog Cache Component**: Retrieves book metadata and recommendations via Redis Protocol (`rediss://`).
* **Order & Checkout Service -> Session & Cart Cache Component**: Manages session state and active carts via Redis Protocol (`rediss://`).
* **Order & Checkout Service -> Inventory Counter Component**: Executes atomic inventory decrements via Redis Protocol (`rediss://`).

## Technology Stack
* **Amazon ElastiCache for Redis (Cluster Mode Enabled)**: Chosen for sub-millisecond retrieval and multi-AZ high availability.
* **Redis AOF (Append-Only File) Persistence**: Enabled to prevent state loss of active carts and inventory during failovers.
* **Lettuce / Jedis Connection Pooling**: Mandated across ECS/Fargate services to prevent connection exhaustion.
* **AWS Secrets Manager & IAM Authentication**: Enforces secure Redis AUTH token rotation for OWASP compliance.

## Rationale
This architecture ensures 99.95% uptime and sub-2-second page loads by isolating volatile cache data from critical session and inventory state. Segregating memory eviction policies (`volatile-lru` versus `noeviction`) guarantees performance scaling while preserving transactional data integrity.