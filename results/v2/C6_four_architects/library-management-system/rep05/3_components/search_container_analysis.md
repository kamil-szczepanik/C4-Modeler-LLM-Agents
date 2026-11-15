## Overview
The Search Container component of the Library Management System delivers ultra-fast, secure catalogue searching for physical and digital items. It provides resilient, high-performance querying while strictly adhering to EU data residency requirements.

## Key Elements
- **Query Service Component**: Java / Spring Boot service handling incoming search requests.
- **Schema Validation & Sanitization Component**: Java / OWASP Validator protecting against query injection.
- **Encryption & Compliance Component**: Java / Spring Security enforcing TLS 1.3 and data masking.
- **Circuit Breaker & Fallback Component**: Resilience4j handling latency spikes and fallback results.
- **Indexing Worker Component**: Java / custom consumer processing asynchronous updates.
- **Index Lifecycle Management (ILM) Component**: Elasticsearch ILM managing index rollover and purging.
- **Search Engine Core**: Elasticsearch 8.x distributed cluster deployed across 3 availability zones.

## Relationships
- API Gateway -> Query Service Component [gRPC]
- Message Broker -> Indexing Worker Component [AMQP via Debezium CDC]
- Query Service Component -> Cache / Session Store [Redis Protocol]
- Query Service Component -> Search Engine Core [Transport Protocol / HTTP over TLS 1.3]
- Indexing Worker Component -> Search Engine Core [HTTP/REST over TLS 1.3]
- Search Engine Core nodes <-> Search Engine Core nodes [Transport Protocol / TCP 9300]

## Technology Stack
- **Java / Spring Boot**: High-performance backend foundation for query processing and validation.
- **Elasticsearch 8.x**: Distributed search engine delivering sub-second queries and built-in ILM.
- **Resilience4j**: Lightweight fault tolerance for circuit breaking and fallback execution.
- **Managed AWS Redis**: Low-latency caching layer for fast fallback search snippets.
- **AWS EU-Central (`eu-central-1`)**: Cloud infrastructure region enforcing mandatory EU-only data residency.

## Rationale
This architecture uses event-driven asynchronous indexing to remove write contention from the critical query path, ensuring the 99th-percentile search response stays below 800 ms. Pinning the Elasticsearch cluster and storage strictly to `eu-central-1` fulfills all EU data residency constraints.