## Overview
The Search Aggregator is a microservices container within the Library Management System that provides federated search and discovery capabilities. It aggregates local inventories and external digital providers to serve lightning-fast responses meeting strict performance SLAs.

## Key Elements
- **Search Aggregator Container**: Node.js and GraphQL service handling search aggregation.
- **GraphQL Resolver Layer**: Apollo Server component for query parsing, schema federation, rate-limiting, and RBAC.
- **Query Planner & Fan-Out Engine**: Component for parallel execution and circuit-breaking.
- **Search Result Cacher**: Redis Cache Tier component for rapid retrieval of frequent queries.
- **Facet & Weighting Engine**: Component for dynamic multi-segment filtering.
- **Telemetry Streamer**: Component for offloading search interaction metrics.

## Relationships
- Mobile API Gateway -> Search Aggregator: gRPC over TLS
- Search Aggregator -> Core Circulation & Catalog Service: gRPC over TLS [gRPC over TLS]
- Search Aggregator -> Elasticsearch / OpenSearch Cluster: Queries catalog search index [REST APIs, HTTPS]
- Search Aggregator -> Redis Cache Tier: Caches search results [Redis protocol, mTLS, AES-256]
- Search Aggregator -> Asynchronous Notification Worker: Offloads telemetry [Internal message queues]

## Technology Stack
- Node.js and Apollo Server: Chosen for flexible GraphQL data fetching and query complexity control.
- Redis Cache Tier: Selected for sub-800ms search result caching with AES-256 encryption.
- Elasticsearch / OpenSearch: Utilized for high-performance catalog indexing and multi-segment filtering.
- OpenTelemetry and Prometheus: Deployed for distributed tracing and p99 latency monitoring.
- Terraform: Enforces EU-only data residency and region-pinned cluster configurations.

## Rationale
This architecture uses concurrent fan-out, intelligent caching, and strict query complexity controls to satisfy the sub-800ms 99th-percentile performance requirement. Simultaneously, it enforces EU data residency constraints and robust security protocols across all federated library assets.