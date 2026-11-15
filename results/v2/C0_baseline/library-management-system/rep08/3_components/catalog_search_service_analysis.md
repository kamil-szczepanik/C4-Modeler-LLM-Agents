## Overview
The Catalog & Search Service delivers high-performance discovery, faceted search, and typo-tolerant queries for the Library Management System. It ensures lightning-fast search responses under 800 ms while strictly enforcing EU data residency.

## Key Elements
*   API Gateway (NGINX / Envoy)
*   Catalog & Search Service (Kotlin / Spring Boot)
    *   Search Controller (`@RestController`)
    *   Catalog Management Controller (`@RestController`)
    *   Search Service (`@Service`) with Typo Tolerance & Scoring Engine
    *   Catalog Data Synchronizer (`@Component`)
    *   Elasticsearch Client (`RestHighLevelClient` / `ElasticsearchRestTemplate`)
*   Elasticsearch (StatefulSet, EU-hosted)
*   PostgreSQL (PostgreSQL (EU-hosted))
*   EU-hosted Log & Telemetry Aggregator

## Relationships
*   API Gateway -> Search Controller: Routes search and catalog requests via gRPC / mTLS (Istio)
*   Search Controller -> Search Service: In-process validation and query handling
*   Search Service -> Elasticsearch Client: In-process query building and aggregation
*   Elasticsearch Client -> Elasticsearch: Executes queries and indexes data via TCP with mTLS
*   Catalog Management Controller -> PostgreSQL: Mutates item records via JDBC
*   Catalog Data Synchronizer -> Elasticsearch Client: Asynchronously indexes data via CDC
*   Catalog & Search Service -> EU-hosted Log & Telemetry Aggregator: Ships Prometheus metrics and sanitized JSON logs via TLS

## Technology Stack
*   Kotlin / Spring Boot: Core container runtime providing robust enterprise foundations
*   Elasticsearch: Search engine backend providing sub-800ms P99 queries and fuzzy matching
*   PostgreSQL: Relational datastore for persistent catalog mutation storage
*   Kubernetes StatefulSet: Orchestration for stateful Elasticsearch instances ensuring data residency
*   Prometheus: Metrics instrumentation for query latency, CDC lag, and resource monitoring
*   Istio: Service mesh providing mTLS, Envoy rate limiting, and traffic routing

## Rationale
Decomposing the Catalog & Search Service into dedicated controllers, asynchronous CDC synchronization, and Elasticsearch guarantees sub-800ms P99 search latencies while protecting write paths. Enforcing strict JVM heap limits, StatefulSets, and EU-only hosting fully satisfies regional data residency and high availability requirements.