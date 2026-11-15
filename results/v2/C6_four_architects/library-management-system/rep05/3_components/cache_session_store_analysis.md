## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The architecture utilizes an in-memory cache and session store to achieve sub-millisecond latency and meet high-performance search requirements.

## Key Elements
*   **Cache / Session Store Container:** Managed AWS ElastiCache for Redis 7.x Cluster Mode in `eu-central-1`.
*   **Session Store Component:** Manages active user authentication tokens and TTL-expiring keys.
*   **Hot Data Cache Component:** Caches frequent catalogue queries using a `volatile-lru` eviction policy.
*   **Distributed Lock Component:** Coordinates concurrency for circulation checkouts.
*   **API Gateway & Core Services Container:** External callers interacting with the cache container.

## Relationships
*   **API Gateway -> Session Store Component:** Validates active user sessions using RESP3 over TLS 1.3 with IAM authentication.
*   **Core Services Container -> Hot Data Cache Component:** Queries and invalidates cached catalogue data using RESP3 over TLS 1.3.
*   **Core Services Container -> Distributed Lock Component:** Acquires and releases concurrency locks using RESP3 over TLS 1.3.

## Technology Stack
*   **AWS ElastiCache for Redis 7.x (Cluster Mode):** Selected for in-memory data structures, native multi-AZ replication, and EU-Central-1 data residency.
*   **RESP3 over TLS 1.3:** Enforces secure encryption in transit for all container interactions.
*   **Redis ACLs & IAM Database Authentication:** Secures service-level access boundaries.

## Rationale
This architecture ensures sub-millisecond session validation and hot data caching to satisfy the 99th-percentile search response time under 800 ms. Strict adherence to AWS EU-Central-1 deployment and TLS 1.3 guarantees compliance with EU-only data residency constraints.