## Overview
A secure, high-performance Search Container provides sub-second catalogue discovery for the Library Management System. It guarantees EU data residency while fulfilling strict latency requirements.

## Key Elements
- Search API Controller
- Index & Query Engine (Elasticsearch Core)
- Catalog Indexer Component
- Search Analytics Publisher

## Relationships
- Core Services Container -> Search API Controller: Synchronous queries [HTTP/REST, mTLS]
- Search API Controller -> Index & Query Engine: Executes queries [Internal HTTP]
- Catalog Indexer Component -> Index & Query Engine: Manages indexes and bulk updates [Internal HTTP]
- Search Analytics Publisher -> Centralized Log & Metrics Aggregator: Streams anonymized telemetry [HTTPS]

## Technology Stack
- Elasticsearch 8.x: Multi-node cluster for distributed inverted-index lookups and faceted search.
- Java / Spring Boot: Underlying framework for internal container components.
- Lucene indices: Optimized for read-heavy catalogue workloads and zero-downtime aliasing.

## Rationale
This architecture uses Elasticsearch to meet the sub-second search requirement (< 800 ms p99). Dedicated EU cloud infrastructure and strict security controls satisfy data residency and compliance mandates.