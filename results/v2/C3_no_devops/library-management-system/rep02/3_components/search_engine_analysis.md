## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Search Engine container delivers high-performance, secure, and localized discovery of physical and digital items.

## Key Elements
*   API Gateway (NGINX / Spring Cloud Gateway)
*   Search Engine Container (OpenSearch/Elasticsearch cluster)
*   Query Router & Parser Component (Java/Spring)
*   Search Index Component (Apache Lucene underlying OpenSearch)
*   Analytics Emitter Component
*   Text Analysis Pipeline Component (OpenSearch Analysis Modules)
*   Analytics Worker (Python/Spring)

## Relationships
*   API Gateway -> Query Router: `gRPC` over `mTLS`
*   Query Router -> Text Analysis Pipeline: In-memory tokenization
*   Text Analysis Pipeline -> Search Index: Internal Lucene query execution
*   Analytics Emitter -> Analytics Worker: `Apache Kafka` event stream using `TLS 1.3` with `mTLS`

## Technology Stack
*   OpenSearch/Elasticsearch: Core search engine for scalable full-text and faceted search capabilities.
*   Apache Lucene: Underlying storage and indexing engine for sub-800ms retrieval.
*   Apache Kafka: Asynchronous telemetry event streaming to prevent query latency overhead.
*   AES-256 / EU-hosted KMS: Data-at-rest encryption ensuring EU data residency compliance.
*   Java/Spring: Query routing, validation, and security enforcement implementation.

## Rationale
This architecture guarantees sub-800ms search performance while enforcing strict EU data residency via local KMS encryption. The component decomposition separates parsing, security, text analysis, and telemetry to meet rigorous performance and compliance mandates.