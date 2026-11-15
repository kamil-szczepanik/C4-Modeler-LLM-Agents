## Overview
The Library Management System provides a solution for public and academic libraries to catalogue items and manage circulation. The architecture features a dedicated Search Service designed to meet strict EU data residency constraints and high-performance search requirements.

## Key Elements
- Search API Controller (Java, Spring Data Elasticsearch)
- Query Builder Component (Java, Spring Data Elasticsearch)
- Index Synchronizer Component (Java, Spring Data Elasticsearch)
- Elasticsearch Client Wrapper (Java, Spring Data Elasticsearch with Resilience4j)
- Elasticsearch Cluster (EU-hosted, encrypted-at-rest with CMK)

## Relationships
- API Gateway -> Search API Controller: Routes search queries via gRPC over mTLS
- Async Event Broker -> Index Synchronizer: Consumes item lifecycle events via Apache Kafka consumer protocol
- Search API Controller -> Query Builder Component: Passes validated DTOs via method calls
- Query Builder Component -> Elasticsearch Client Wrapper: Executes DSL queries via Java method calls
- Index Synchronizer Component -> Elasticsearch Client Wrapper: Executes bulk index operations via Java method calls

## Technology Stack
- Java / Spring Boot / Spring Data Elasticsearch: Selected for robust enterprise ecosystem and performance.
- Elasticsearch: Chosen to fulfill the sub-800ms 99th-percentile search requirement.
- Apache Kafka: Enables decoupled, asynchronous index synchronization.
- Resilience4j: Implements circuit breaking to protect availability and meet latency SLAs.
- TLS 1.3: Enforces secure data transmission and EU residency compliance.

## Rationale
This component-level architecture separates low-latency read paths from asynchronous ingestion, ensuring the system maintains high performance under load. Security controls, circuit breakers, and localized storage fulfill strict EU regulatory and performance constraints.