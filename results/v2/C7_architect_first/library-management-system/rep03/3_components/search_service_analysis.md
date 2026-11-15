## Overview
The Search Service is a high-performance component of the Library Management System providing sub-second catalog discovery, faceted navigation, and secure access-controlled search for patrons and librarians. It operates entirely within an EU-restricted infrastructure to ensure data residency compliance.

## Key Elements
- **API Gateway**: NGINX / Spring Cloud Gateway routing incoming client traffic
- **Search Service Container**: Python FastAPI container executing asynchronous search queries
- **API Controller**: FastAPI routing and request validation handler
- **Search Orchestrator**: Core logic split into **Query Builder** (handling fuzzy matching, synonyms, and facets) and **Access Control Filter** (enforcing pre-query role-based filtering)
- **Elasticsearch Client**: `elasticsearch-py` async client
- **Index Sync Listener**: Background consumer keeping indices synchronized via Redis
- **Elasticsearch Cluster**: Primary read-model database storing catalog indices
- **Asynchronous Broker**: Redis for event distribution, DLQ management, and reconciliation

## Relationships
- API Gateway -> Search Service: Routes search requests via gRPC over HTTP/2 with mTLS (carrying pre-authenticated JWT/SPIFFE claims)
- Search Service -> Elasticsearch: Queries search index data and applies pre-query filters via HTTPS/REST with mTLS
- Redis -> Index Sync Listener: Consumes synchronization events and dead-letter queues via Redis RESP Protocol with TLS and AUTH
- Search Service -> PostgreSQL: Executes least-privilege backfill batch queries for daily reconciliation via JDBC/TLS

## Technology Stack
- **FastAPI / Pydantic**: Chosen for high-throughput asynchronous request handling and strict input validation
- **Elasticsearch**: Selected to satisfy the sub-800ms search NFR (R-05) and support fuzzy matching, synonyms, and faceted aggregations
- **Redis**: Utilized as an asynchronous event broker with DLQ support for index synchronization
- **OpenTelemetry / Prometheus**: Mandated for distributed tracing and metrics collection while scrubbing PII to maintain EU data residency

## Rationale
This architecture implements a robust CQRS read-model pattern that completely decouples the search domain from the core database, ensuring high availability and sub-800ms performance. Furthermore, enforcing pre-query access filtering directly within Elasticsearch securely protects restricted academic assets while adhering strictly to EU data residency constraints.