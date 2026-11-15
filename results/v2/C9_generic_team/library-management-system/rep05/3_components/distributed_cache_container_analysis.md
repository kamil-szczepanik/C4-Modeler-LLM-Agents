## Overview
The system is a Library Management System providing cataloging, circulation, and self-service portals with strict EU data residency. The architecture utilizes a Distributed Cache Container to maintain stateless application tiers and meet sub-800ms search performance.

## Key Elements
- Distributed Cache Container: Redis
- Core Transactional Service Container
- Enterprise Logging and Monitoring Service
- Kubernetes Orchestrator

## Relationships
- Core Transactional Service Container -> Distributed Cache Container: Caches and retrieves fast data [Redis Protocol with TLS]
- Distributed Cache Container -> Enterprise Logging and Monitoring Service: Exports telemetry and metrics

## Technology Stack
- Redis: Chosen for high-throughput, low-latency caching to satisfy the <800ms performance requirement.
- AOF/RDB Persistence: Configured on EU-hosted storage volumes for data residency compliance.
- Resilience4j / Polly: Implemented for connection pooling and circuit breaking.
- Protocol Buffers / Compressed JSON: Used for efficient payload serialization.
- Testcontainers: Used for automated integration testing of caching logic.

## Rationale
This architecture ensures strict EU data residency while providing robust, high-performance caching mechanisms. Circuit breakers, cache stampede prevention, and failover strategies protect the system under high loads to maintain the 99th-percentile search response SLA.