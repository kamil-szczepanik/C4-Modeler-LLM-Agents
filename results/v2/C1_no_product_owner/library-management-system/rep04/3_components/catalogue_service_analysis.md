## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
- **Users**: Library Patron, Librarian
- **External Systems**: Identity Provider (IdP), Payment Gateway, Notification Provider
- **Containers**: Web Frontend (React SPA, Nginx), API Gateway (Spring Cloud Gateway), Catalogue Service (Spring Boot, Java 21), Circulation Service, Notification Service, PostgreSQL, Elasticsearch, RabbitMQ
- **Catalogue Service Components**: Catalogue Controller, Catalogue Manager, Search Component, Repository Component, Outbox Publisher Component

## Relationships
- API Gateway -> Catalogue Controller: gRPC with mTLS and propagated JWTs
- Catalogue Manager -> Search Component: In-memory Java method calls
- Catalogue Manager -> Outbox Publisher Component: In-memory domain event dispatch
- Outbox Publisher Component -> RabbitMQ: AMQP over TLS 1.3
- RabbitMQ -> Search Component: Event consumer listener over TLS 1.3
- Search Component -> Elasticsearch: Bolt/REST over TLS 1.3
- Repository Component -> PostgreSQL: Encrypted database protocols (AES-256)
- Catalogue Service -> Identity Provider (IdP): TLS 1.3

## Technology Stack
- **Spring Boot / Java 21**: Core application framework for the Catalogue Service.
- **PostgreSQL**: Relational persistence managed via Spring Data JPA with Transparent Data Encryption (TDE).
- **Elasticsearch**: Indexing and search engine for high-performance catalog queries.
- **RabbitMQ**: Asynchronous messaging broker utilizing the outbox pattern.
- **Resilience4j**: Circuit breaking and fallback handling.
- **HashiCorp Vault**: Secret management for dynamic runtime credential injection.

## Rationale
This architecture decouples the write and read paths using an asynchronous outbox pattern over RabbitMQ, ensuring 99th-percentile search response times remain under the 800 ms SLA. Strict encryption, mTLS, and localized EU persistent volume claims satisfy compliance and data residency constraints.