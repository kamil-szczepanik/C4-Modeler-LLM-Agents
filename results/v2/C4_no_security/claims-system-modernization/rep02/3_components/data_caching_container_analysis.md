## Overview
[A hybrid cloud data and caching architecture designed to support the gradual migration of regional insurance claims from a legacy mainframe to Azure. It ensures zero data loss, sub-2s screen loads, and rapid 1-day rollbacks.]

## Key Elements
- Transactional Store Component: Azure Cosmos DB (SQL API)
- Read Model Cache Component: Azure Cache for Redis
- Audit & Reconciliation Log Component: Cosmos DB Change Feed
- Data Lifecycle & Compliance Worker: Background processor for TTLs and archiving
- External Consumers: Claims Core Service Container

## Relationships
- Claims Core Service Container -> Transactional Store Component: Persists primary CRUD operations [TCP/TLS via Azure SDK]
- Claims Core Service Container -> Read Model Cache Component: Fetches read projections for sub-2s loads [TCP/TLS via Jedis]
- Transactional Store Component -> Audit & Reconciliation Log Component: Tracks state mutations for rollbacks [Internal async via Change Feed]

## Technology Stack
- Azure Cosmos DB: Chosen for strong session consistency and polymorphic schemas supporting incremental migration (R-03, R-04).
- Azure Cache for Redis: Selected to cache pre-aggregated claim views ensuring sub-2s latency (R-05).
- Cosmos DB Change Feed: Utilized for automated state tracking, event-driven cache invalidation, and bi-directional mainframe reconciliation (R-06).

## Rationale
[This architecture fits the requirements by combining robust consistency controls with high-performance caching to safely bridge the modern Azure platform and the legacy mainframe. It provides automated safeguards and rollback mechanisms tailored for a team with low cloud experience.]