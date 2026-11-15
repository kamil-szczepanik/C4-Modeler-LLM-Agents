## Overview
The Library Management System provides public and academic libraries with item cataloging, circulation management, and self-service portals. The architecture incorporates a dedicated Caching Container to ensure high-performance catalog browsing and meet strict latency requirements.

## Key Elements
- Caching Container: Redis in-memory data store
- Core Catalog/Circulation Service Container: Microservice managing library items
- Search Engine Container: Dedicated indexing engine for catalog searches
- API Gateway Container: Reverse proxy managing client requests
- EU-Hosted Observability Infrastructure: Centralized monitoring and alerting platform

## Relationships
- Core Catalog/Circulation Service Container -> Caching Container: Optimizes queries and performs write invalidations using the Redis Protocol
- Search Engine Container -> Caching Container: Optimizes queries using the Redis Protocol
- API Gateway Container -> Caching Container: Enforces distributed rate limiting using the Redis Protocol
- Caching Container -> EU-Hosted Observability Infrastructure: Forwards telemetry, traces, and memory alerts

## Technology Stack
- Redis: Chosen for in-memory data storage, low latency, and atomic operations
- Cache-Aside Pattern: Used with automated eviction (`allkeys-lru`) and TTLs to optimize read performance and satisfy R-05 (< 800 ms search response)
- Protocol Buffers / Compressed JSON: Mandated for lightweight payload sizing to prevent memory bloat
- Redis Protocol: Used for all inter-container caching and rate-limiting interactions

## Rationale
This architecture uses an isolated, highly optimized Redis caching layer to guarantee sub-800ms response times for heavy catalog searches. Strict data residency constraints, security isolation, and resiliency fallbacks ensure reliable, compliant operation under load.