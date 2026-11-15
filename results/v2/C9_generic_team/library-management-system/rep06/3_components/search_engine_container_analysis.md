## Overview
- The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries.
- The architecture ensures sub-800ms search performance and strict EU-only data residency compliance.

## Key Elements
- Client-Side SPA/Mobile Container (Web/Mobile Technologies)
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container (Microservice / API Runtime)
- Search Engine Container (Elasticsearch / OpenSearch)
- Data Access Layer / Persistence Container (PostgreSQL)
- Asynchronous Message Broker Container (RabbitMQ / Kafka) with Dead Letter Queue (DLQ)
- Background Workers Container (Background Worker Runtime)
- Configuration & Secrets Management Container (HashiCorp Vault)
- Centralized Observability Container (Observability Platform)

## Relationships
- Client-Side SPA/Mobile Container -> API Gateway Container: Sends user requests [HTTPS/REST]
- API Gateway Container -> Core Business Logic / Circulation API Container: Routes validated requests [gRPC/REST]
- Core Business Logic / Circulation API Container -> Data Access Layer / Persistence Container: Mutates and retrieves catalog data [JDBC/SQL]
- Core Business Logic / Circulation API Container -> Asynchronous Message Broker Container: Publishes domain events [AMQP/Kafka Protocol]
- Asynchronous Message Broker Container -> Search Engine Container: Synchronizes catalog events for indexing [AMQP/Kafka Protocol]
- Core Business Logic / Circulation API Container -> Search Engine Container: Queries catalog search index via Versioned Repository Abstraction Layer [REST/gRPC]
- Search Engine Container -> Centralized Observability Container: Ships query telemetry, latency percentiles, and slow-query logs [OTLP/HTTPS]

## Technology Stack
- Elasticsearch / OpenSearch: Selected for the Search Engine Container to guarantee sub-800ms search performance (R-05).
- PostgreSQL: Serves as the primary persistence store for reliable transactional data management.
- RabbitMQ / Kafka: Powers asynchronous event synchronization and Dead Letter Queue (DLQ) error isolation.
- NGINX / Kong: Implements API gateway routing, rate-limiting, and request boundary enforcement.

## Rationale
- The event-driven architecture decouples database mutations from search indexing, ensuring high resilience and eventual consistency.
- Strict infrastructure node pinning, automated EU-backed snapshots, and query boundary controls satisfy regional data residency and low-latency performance constraints.