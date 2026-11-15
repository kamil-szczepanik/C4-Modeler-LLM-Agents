## Overview
- The Redis Cache Tier provides high-speed, low-latency data retrieval for catalogues, search queries, and session management.
- It is architected to meet EU data residency constraints and sub-second performance requirements for public and academic libraries.

## Key Elements
- Redis Cluster topology spanning three availability zones
- Redis OSS (v7.2) with Redis JSON and Search modules
- Consuming Services: Core Circulation & Catalog Service (Java/Spring Boot), Search Aggregator (Node.js/GraphQL), Authentication & Session Service (Node.js)
- Prometheus Redis exporter and OpenTelemetry collector
- Terraform modules and encrypted EBS volumes

## Relationships
- Core Circulation & Catalog Service -> Redis Cache Tier: Queries cache and triggers pub/sub invalidations [Redis Protocol over TCP port 6379]
- Search Aggregator -> Redis Cache Tier: Executes faceted queries and utilizes client-side caching [Redis Protocol over TCP port 6379]
- Authentication & Session Service -> Redis Cache Tier: Manages session tokens via Redis Hashes [Redis Protocol over TCP port 6379]
- Redis Exporter -> Prometheus: Scrapes metrics (memory fragmentation, eviction rates) [HTTP]

## Technology Stack
- Redis OSS v7.2: Selected for in-memory performance and advanced data structures
- Redis Cluster Topology: Ensures high availability, zero-data-loss failover, and horizontal write scalability
- Redis JSON & Search Modules: Enables complex faceted catalog queries directly in memory
- Mutual TLS (mTLS) & Redis 6+ ACLs: Secures wire protocol traffic and enforces strict cross-service access control
- AOF Persistence (`appendfsync everysec`) with encrypted EBS: Guarantees durability and satisfies EU data residency mandates

## Rationale
- The Redis Cluster configuration ensures 99th-percentile search responses remain below 800 ms during peak library circulation loads.
- Strict EU-compliant security controls, encryption, and automated memory management protect patron privacy while optimizing cloud infrastructure costs.