## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and sub-800ms search latency requirements.

## Key Elements
- Library Users and Administrators
- Client-Side Application Container (Single Page App / Mobile App)
- API Gateway Container (Reverse Proxy / API Gateway)
- Search Engine Container (Dedicated Indexing Engine)
- Caching Container (Redis)
- Message Broker Container (Message Broker)
- EU-Hosted Observability Infrastructure

## Relationships
- Client-Side Application Container -> API Gateway Container: Submits real-time search queries [HTTPS/REST]
- API Gateway Container -> Search Engine Container: Routes search queries [HTTP/gRPC]
- Search Engine Container -> Caching Container: Optimizes queries and caches facets [Redis Protocol]
- Message Broker Container -> Search Engine Container: Streams asynchronous catalogue update events
- Search Engine Container -> EU-Hosted Observability Infrastructure: Exports scrubbed query telemetry and W3C Trace Context

## Technology Stack
- Search Engine Container: Dedicated indexing engine utilizing Index Lifecycle Management (ILM) and alias swapping for zero-downtime schema migrations.
- Caching Container (Redis): Implements a cache-aside pattern with TTL strategies for high-frequency catalogue queries.
- Message Broker Container: Handles asynchronous event streaming to decouple write operations from indexing.
- Observability: W3C Trace Context and PII-scrubbed telemetry routed to regional EU-hosted infrastructure.

## Rationale
The asynchronous indexing pipeline and Redis caching layer insulate real-time searches from ingestion spikes to meet the strict 800ms p99 latency target. Enforcing regional storage policies guarantees compliance with EU-only data residency constraints.