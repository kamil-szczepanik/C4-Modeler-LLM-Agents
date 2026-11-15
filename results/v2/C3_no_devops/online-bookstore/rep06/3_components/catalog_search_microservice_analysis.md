## Overview
The Catalog & Search Microservice is a core revenue-driving Spring Boot application providing sub-2-second faceted search, real-time inventory visibility, and administrative catalog management. It utilizes a CQRS pattern to isolate high-throughput search traffic from write operations while maintaining GDPR and CCPA compliance.

## Key Elements
- `SearchController`: Spring MVC component exposing gRPC endpoints for keyword and faceted searches.
- `CatalogQueryService`: Spring Service orchestrating queries against AWS OpenSearch.
- `CatalogAdminController`: Spring MVC component handling administrative mutations with strict RBAC.
- `CatalogRepository`: Spring Data JPA component managing writes and reads against AWS Aurora PostgreSQL.
- `InventoryConsumer`: Spring Kafka consumer processing asynchronous inventory updates.
- `SearchAnalyticsService`: Component capturing anonymous search telemetry asynchronously.
- AWS OpenSearch: Managed search engine for typo-tolerant full-text search.
- AWS Aurora PostgreSQL: Relational database for canonical book metadata.
- AWS MSK (Kafka): Event streaming platform for domain events (`catalog.updated`).

## Relationships
- API Gateway -> `SearchController`: Routes search and catalog requests via gRPC over mTLS.
- API Gateway -> `CatalogAdminController`: Routes administrative mutations via gRPC over mTLS with JWT validation.
- `CatalogQueryService` -> AWS OpenSearch: Queries catalog data via REST over HTTPS with TLS.
- `CatalogRepository` -> AWS Aurora PostgreSQL: Reads and writes canonical data via JDBC with AWS KMS encryption at rest.
- `InventoryConsumer` -> AWS MSK (Kafka): Consumes inventory update events via AMQP/Kafka.
- `CatalogAdminController` -> `CatalogRepository`: Writes metadata via JDBC.
- `CatalogAdminController` -> AWS MSK (Kafka): Emits `catalog.updated` domain events secured with AWS KMS.
- `SearchAnalyticsService`: Publishes anonymous telemetry asynchronously.

## Technology Stack
- Java 17 / Spring Boot: Core framework chosen for enterprise robustness and robust dependency injection.
- Spring MVC / gRPC: Protocol chosen for high-performance inter-container communication.
- AWS OpenSearch: Selected for scalable, typo-tolerant full-text search and faceted filtering.
- AWS Aurora PostgreSQL: Chosen for reliable, transactional storage of canonical book metadata.
- AWS MSK (Kafka): Selected for asynchronous, decoupled event-driven communication and CQRS synchronization.
- AWS ECS Fargate: Chosen for serverless container orchestration meeting 99.95% availability targets.
- AWS KMS: Utilized for data encryption at rest and message integrity protection.

## Rationale
The CQRS pattern separates read-heavy search operations from administrative writes, ensuring sub-2-second performance on 3G networks and supporting 1M MAU. Zero-trust networking protocols (mTLS, TLS to OpenSearch, and AWS KMS) satisfy stringent GDPR, CCPA, and OWASP Top-10 security constraints.