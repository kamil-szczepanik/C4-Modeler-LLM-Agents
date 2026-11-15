## Overview
The Search Service is a high-performance component of the Library Management System that catalogues items and delivers sub-800ms search responses for patrons and staff while enforcing strict EU data residency.

## Key Elements
- Search REST Controller
- Query Parser & Builder
- Resilience & Caching Proxy
- Indexing Worker
- OpenSearch Index
- Redis Cache
- Async Event Bus (Managed Kafka)

## Relationships
- API Gateway -> Search REST Controller [HTTP/REST]
- Async Event Bus -> Indexing Worker [Kafka Consumer Protocol]
- Search REST Controller -> Query Parser & Builder [In-memory]
- Query Parser & Builder -> Resilience & Caching Proxy [In-memory / RESP]
- Resilience & Caching Proxy -> OpenSearch [HTTPS / mTLS]
- Resilience & Caching Proxy -> Redis [RESP over TLS]

## Technology Stack
- OpenSearch: Underlying data store for scalable search queries and EU data residency compliance.
- Redis: Distributed cache to guarantee sub-800ms response SLAs under heavy load.
- Java: Core runtime language for implementing parsing, workers, and controllers.
- Apache Kafka: Asynchronous event bus for decoupled catalogue ingestion.
- mTLS & TLS 1.3: Protocol for secure inter-component communication and encryption-in-transit.

## Rationale
This architecture uses dedicated caching and search engines to easily satisfy the sub-800ms performance requirement. Strict encryption, isolation, and region-bound storage satisfy the EU data residency and security mandates.