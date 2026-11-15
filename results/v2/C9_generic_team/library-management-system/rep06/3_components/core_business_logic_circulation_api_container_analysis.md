## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for public and academic libraries. The Core Business Logic / Circulation API Container manages core domain operations while adhering to strict EU data residency constraints.

## Key Elements
- Patrons and Library Staff (Users)
- Client-Side SPA/Mobile Container (Web/Mobile)
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container (Microservice / API Runtime)
- Search Engine Container (Elasticsearch / OpenSearch)
- Data Access Layer / Persistence Container (PostgreSQL)
- Asynchronous Message Broker Container (RabbitMQ / Kafka)
- Configuration & Secrets Management Container (HashiCorp Vault)
- Centralized Observability Container (Observability Platform)

## Relationships
- API Gateway Container -> Core Business Logic / Circulation API Container: Routes verified API requests via internal gRPC/HTTP
- Core Business Logic / Circulation API Container -> Search Engine Container: Queries and indexes catalog data via REST/gRPC
- Core Business Logic / Circulation API Container -> Data Access Layer / Persistence Container: Reads/writes relational data over TLS
- Core Business Logic / Circulation API Container -> Asynchronous Message Broker Container: Publishes domain events via AMQP/Kafka Protocol

## Technology Stack
- Repository Pattern & Dependency Injection: Decouples core domain logic from persistence and message transport mechanisms.
- Domain-Driven Design (DDD): Organizes code around Loan, Patron, and Item aggregates with explicit domain events.
- OpenAPI/Protobuf: Establishes a contract-first approach for gRPC/HTTP API boundaries.
- RFC 7807: Provides standardized problem details for global exception handling.
- Flyway/Liquibase: Manages atomic, version-controlled database migrations.

## Rationale
This architecture ensures high-performance search capabilities with sub-800ms responses while strictly isolating core circulation logic. Modular patterns and robust container probes guarantee reliability, maintainability, and EU data compliance.