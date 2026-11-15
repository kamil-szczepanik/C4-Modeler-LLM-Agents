## Overview
[The Distributed Cache container provides in-memory session management, fast catalog lookups, and cache consistency for the Library Management System. Its core purpose is to guarantee high-performance search responses and secure EU-only volatile data storage.]

## Key Elements
- Session Store Component
- Catalog L2 Cache Component
- Eviction & Expiry Manager
- Cluster Topology Manager Component
- Pub/Sub Broker Component
- Health & Metrics Exporter Component
- Circuit Breaker & Rate Limiter Component

## Relationships
- Core Domain Service -> Distributed Cache: Manages sessions, executes cache invalidation, and acquires distributed locks via RESP3/TCP (TLS 1.3)
- Search Service -> Distributed Cache: Queries pre-serialized search facets and hot item metadata via RESP3/TCP (TLS 1.3)
- Prometheus -> Health & Metrics Exporter: Scrapes system and memory metrics via HTTP/TLS on port 9121

## Technology Stack
- Redis 7.x Open Source: Selected for robust in-memory data structures and master-replica replication.
- RESP3 over TCP: Protocol for low-latency internal container communications.
- Lettuce / Jedis: Cluster-aware client connections ensuring proper slot-based redirection.
- Redis Lua Engine: Executes atomic check-and-set operations for distributed locking and rate limiting.
- Redis Exporter Sidecar: Exposes Prometheus-compatible metrics for monitoring memory fragmentation.

## Rationale
[Disabling RDB/AOF persistence while enforcing volatile-lru eviction strictly satisfies the EU-only data residency constraint for transient patron data. Furthermore, utilizing Redis Cluster mode with Lua-based distributed locking prevents cache stampedes, ensuring 99th-percentile search responses remain under the required 800 ms threshold.]