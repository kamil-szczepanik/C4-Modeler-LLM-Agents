## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Search Service component ensures fast, secure, and compliant item discovery within strict EU data residency boundaries.

## Key Elements
- API Gateway (Spring Cloud Gateway, Java)
- Search Service Container (OpenSearch, Spring Boot, Redis)
- Query Parser & Router (Java)
- Tenant Security Context Filter (Java)
- Index Synchronization Worker (Java)
- Index Lifecycle Manager (OpenSearch ISM)
- Search Analytics & Caching Interceptor (Redis)
- Message Broker (Apache Kafka)

## Relationships
- API Gateway -> Query Parser & Router: Forwards search requests [REST/TLS]
- Message Broker -> Index Synchronization Worker: Consumes catalogue events [Apache Kafka]
- Query Parser & Router -> Search Analytics & Caching Interceptor: Checks cache [RESP/TCP]
- Query Parser & Router -> Tenant Security Context Filter: Validates tenant context [In-process]
- Tenant Security Context Filter -> Query Parser & Router: Passes validated context [In-process]
- Query Parser & Router -> OpenSearch Cluster: Executes queries [OpenSearch REST/HTTPs]
- Index Synchronization Worker -> OpenSearch Cluster: Applies index updates [OpenSearch REST/HTTPs]
- Index Lifecycle Manager -> OpenSearch Indices: Manages tiering and retention [OpenSearch REST API]

## Technology Stack
- Java & Spring Boot: Lightweight application boundary for routing, security filtering, and event synchronization.
- OpenSearch: Dedicated search engine and storage for sub-800ms catalogue queries and relevance ranking.
- Redis: High-performance caching layer for frequent searches and facets.
- Apache Kafka: Event broker for real-time catalogue mutation ingestion.
- OpenSearch ISM (Index State Management): Automated lifecycle management for EU-compliant backups and tiering.

## Rationale
This component architecture uses Redis caching and optimized OpenSearch indexing to consistently achieve the sub-800ms search latency requirement. Tenant-scoped routing and ISM snapshotting strictly enforce EU data residency and isolation constraints.