## Overview
The Catalogue Service manages physical and digital library item inventories and metadata. It delivers high-performance discovery while enforcing EU data residency constraints.

## Key Elements
*   Catalogue API Controller (Java/Spring Boot)
*   Item Domain Model & Business Logic Component
*   Data Access Repository (PostgreSQL with JPA)
*   Search Synchronizer Component
*   Search Engine (ElasticSearch)
*   Usage Analytics & Telemetry Hook
*   Cache Layer (Redis)

## Relationships
*   API Gateway -> Catalogue API Controller: REST/JSON over HTTPS with JWT validation
*   Catalogue API Controller -> Item Domain Model: Direct Java method invocation
*   Search Synchronizer -> Search Engine (ElasticSearch): gRPC/TCP
*   Item Domain Model -> Data Access Repository (PostgreSQL): JDBC/JPA over mTLS
*   Search Synchronizer & Telemetry Hook -> Audit Logging/Kafka: Asynchronous event publishing
*   Item Domain Model -> Redis Cache: Encrypted caching with strict TTLs

## Technology Stack
*   **Java / Spring Boot**: Chosen for robust domain modeling and enterprise integration.
*   **PostgreSQL**: Ensures ACID compliance for transactional inventory updates.
*   **ElasticSearch**: Provides high-performance search to meet the <800ms SLA.
*   **Apache Kafka**: Decouples write operations from indexing and telemetry to protect search performance.
*   **Redis**: Caches frequently accessed metadata with strict memory encryption.
*   **Kubernetes**: Manages independently autoscaling pods with strict CPU/memory limits in EU sovereign regions.

## Rationale
This architecture decouples heavy search indexing and telemetry via Kafka to consistently achieve the required sub-800ms search response time. Strict zero-trust security controls, mTLS, and EU-localized data stores ensure full compliance with regional regulations and data protection standards.