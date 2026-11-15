## Overview
The Search Container is a high-performance catalogue search subsystem for the Library Management System, designed to deliver fast, secure item discovery for patrons and staff. It processes complex search queries, facets, and spelling suggestions while maintaining strict EU-only data residency.

## Key Elements
- Search Router / API Handler (Java/Spring Boot)
- Facet & Aggregation Processor (Java/Spring Boot)
- Search Engine Index (Elasticsearch 8.x, 3-node Kubernetes StatefulSet)
- CDC Ingestion Listener (Logstash / Kafka Connect)
- Caching Layer (Redis)

## Relationships
- `API Gateway -> Search Router`: REST/HTTPS (JSON payload) with JWT validation
- `Search Router -> Search Engine Index`: REST/Transport protocol using optimized Query DSL
- `CDC Ingestion Listener -> Search Engine Index`: Internal TCP/Transport protocol for low-latency index updates
- `Search Router -> Redis`: In-memory caching for frequent search queries and facet counts

## Technology Stack
- Java / Spring Boot: Chosen for robust enterprise API routing and query construction
- Elasticsearch 8.x: Utilized for inverted indices, multi-match queries, and aggregations to meet < 800 ms performance (R-05)
- Redis: Implements short-TTL caching and rate limiting to prevent abuse
- Kubernetes / NVMe: Ensures high availability and low disk I/O latency on local persistent volumes
- TLS 1.3 / AES-256: Enforced for transport security and data-at-rest protection

## Rationale
This architecture decouples heavy indexing writes from user-facing search queries to satisfy the stringent 99th-percentile < 800 ms performance requirement. Enforcing local Kubernetes clustering, Redis caching, and strict TLS encryption ensures both high-availability scalability and compliance with EU data residency mandates.