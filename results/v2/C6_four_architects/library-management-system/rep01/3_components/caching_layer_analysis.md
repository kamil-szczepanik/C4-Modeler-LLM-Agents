## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture ensures EU data residency and 99th-percentile search responses under 800 ms.

## Key Elements
- **Cache Manager (Redis Core):** Stores hot catalogue items and patron session states in-memory.
- **Rate Limiter (Redis Module):** Enforces distributed rate limits for the API Gateway.
- **Cache Invalidation Listener (Redis Pub/Sub Subscriber):** Purges stale catalogue entries upon receiving updates.
- **Distributed Lock Manager (Redis Redlock / SETNX):** Prevents cache stampedes during sudden traffic spikes.

## Relationships
- **API Gateway -> Rate Limiter:** Evaluates rate limits using Redis `EVAL` [TCP/RESP].
- **Core Domain Service -> Cache Manager:** Reads and writes hot items via cache-aside/write-through patterns [TCP/RESP].
- **Core Domain Service -> Distributed Lock Manager:** Acquires and releases locks during cache miss re-population using atomic commands [TCP/RESP].
- **Apache Kafka -> Cache Invalidation Listener:** Triggers cache eviction on data updates [TCP].
- **Cache Invalidation Listener -> Cache Manager:** Executes internal `DEL`/`UNLINK` commands [In-Memory Function Call].

## Technology Stack
- **Redis:** Core caching and data structure store for low-latency in-memory operations.
- **Redis Lua Scripting:** Ensures atomic rate-limiting checks without race conditions.
- **Redis SETNX / Redlock:** Provides distributed locking for cache stampede prevention.
- **Apache Kafka:** Transports asynchronous cache invalidation events.
- **TCP/RESP:** Protocol used for client-to-Redis communication within the EU perimeter.

## Rationale
This architecture uses Redis native primitives and in-memory operations over TCP/RESP to guarantee sub-800ms search latency under peak load while neutralizing cache stampedes. Furthermore, keeping all component states and event processing pipelines strictly within the EU perimeter satisfies core compliance constraints.