## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system ensures EU-only data residency and sub-800ms search response times.

## Key Elements
- Core Domain Service (Java, Spring Boot)
- Search Service Components (Spring Boot): Search REST Controller, Query Builder Component, Search Circuit Breaker (Resilience4j), Elasticsearch Client Wrapper, Search Result Ranker / Post-Processor, Index Synchronizer Consumer
- Elasticsearch Engine (Elasticsearch)
- Notification & Event Bus (Apache Kafka)

## Relationships
- Core Domain Service -> Search REST Controller: `[HTTP/REST over TLS]`
- Notification & Event Bus (Kafka) -> Index Synchronizer Consumer: `[Kafka Protocol over TLS]`
- Index Synchronizer Consumer -> Elasticsearch Client Wrapper: `[In-process Method Call]`
- Search REST Controller -> Query Builder: `[In-process Method Call]`
- Query Builder -> Search Circuit Breaker: `[In-process Method Call]`
- Search Circuit Breaker -> Elasticsearch Client Wrapper: `[In-process Method Call]`
- Elasticsearch Client Wrapper -> Search Result Ranker: `[In-process Method Call]`
- Search Result Ranker -> Search REST Controller: `[In-process Method Call]`
- Elasticsearch Client Wrapper -> Elasticsearch Engine: `[Elasticsearch Native TCP / Transport over TLS]`

## Technology Stack
- Java & Spring Boot: Rapid routing and integration with the existing ecosystem
- Elasticsearch & Elasticsearch Client Wrapper: Dedicated search engine and client ensuring sub-800ms responses with EU boundary node pinning
- Apache Kafka: Asynchronous event streaming for non-blocking index synchronization
- Resilience4j: Circuit breaking for graceful degradation under heavy load
- Python: FastAPI for reporting and Celery for async workers

## Rationale
Decoupling the write path via Kafka and maintaining a localized Elasticsearch cluster ensures sub-800ms search latency without blocking read paths. Strict EU node pinning and in-memory isolation components satisfy data residency and resilience requirements.