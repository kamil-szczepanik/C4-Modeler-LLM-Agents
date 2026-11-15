## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture focuses on the Redis Cache Container component-level design to accelerate metadata retrieval and satisfy performance constraints.

## Key Elements
- In-Memory Data Store Engine (Redis Core): Manages key-value and sorted-set structures
- Cache Eviction & Expiry Manager: Enforces TTL policies and LRU eviction algorithms
- Persistence & Snapshot Manager (RDB/AOF): Handles point-in-time data durability
- TLS Termination & Security Manager: Secures transport-layer encryption and authentication
- Pub/Sub Messaging Module: Manages lightweight event channels for cache invalidation
- Replication & High Availability Manager: Handles master-replica synchronization and failover

## Relationships
- Core Services Container -> TLS Termination & Security Manager: Securely transmits cache queries [RESP over TLS/TCP]
- Core Services Container -> Pub/Sub Messaging Module: Publishes and subscribes to cache invalidation triggers [RESP over TLS/TCP]
- Cache Eviction Manager -> In-Memory Data Store Engine: Clears expired cache entries [Internal]
- Replication & High Availability Manager -> In-Memory Data Store Engine: Synchronizes state between instances [RESP replication stream]

## Technology Stack
- Redis: In-memory database chosen for low-latency catalogue metadata acceleration
- RESP (REdis Serialization Protocol): Standardized wire protocol for Redis communication
- TLS/TCP: Encrypted transport layer ensuring strict compliance with EU-only data residency
- Redis Sentinel/Clustering: Topology management for high availability and failover

## Rationale
This component decomposition ensures predictable in-memory execution times, directly supporting the 99th-percentile search response requirement under 800 ms. Enforcing TLS and strict replication boundaries guarantees full compliance with the EU-only data residency constraint.