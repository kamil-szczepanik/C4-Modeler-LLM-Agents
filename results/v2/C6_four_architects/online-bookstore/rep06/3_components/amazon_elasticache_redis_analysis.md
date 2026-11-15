## Overview
The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations, supported by an internal caching layer. It utilizes Amazon ElastiCache for Redis to achieve sub-2-second page loads and 99.95% availability for 1 million monthly active users.

## Key Elements
- Amazon ElastiCache for Redis (Cluster Mode Enabled)
- Session Store Component
- Catalog Cache Component
- Rate Limiter / Token Bucket Component
- Distributed Lock Component
- Pub/Sub Broker Component
- Shopping Cart & Checkout Cache Component
- Metrics & Slow-Log Collector
- Redis Auth & ACL Enforcement
- Redis Eviction Engine

## Relationships
- Core E-Commerce Service -> Session Store Component, Catalog Cache Component, Shopping Cart & Checkout Cache Component, Distributed Lock Component, Pub/Sub Broker Component: Redis RESP protocol over TLS
- Recommendation Engine -> Catalog Cache Component: Redis RESP protocol over TLS
- Integration Service -> Rate Limiter / Token Bucket Component: Redis RESP protocol over TLS
- AWS CloudWatch -> Metrics & Slow-Log Collector: Amazon CloudWatch Agent / Redis `INFO` API
- Core E-Commerce Service & Recommendation Engine -> Redis Auth & ACL Enforcement: AUTH with user/password credentials over TLS

## Technology Stack
- Amazon ElastiCache for Redis (Cluster Mode Enabled): Managed Redis engine ensuring horizontal sharding and multi-AZ replication.
- Redis RESP over TLS: Secure binary protocol for high-performance client-cache communication.
- Lua scripting: Atomic execution for distributed locking and inventory management.
- `volatile-lru` eviction policy: Automated memory management preventing out-of-memory crashes.

## Rationale
This caching architecture delivers high throughput and low-latency data access to meet performance and scalability SLAs. Multi-AZ replication and automated failover guarantee high availability while strict ACLs and TLS encryption ensure security compliance.