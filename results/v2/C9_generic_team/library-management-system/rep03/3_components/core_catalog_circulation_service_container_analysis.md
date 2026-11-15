## Overview
The Library Management System provides a solution for public and academic libraries to catalogue items, manage circulation, and offer self-service portals. The architecture ensures strict EU data residency compliance and high performance.

## Key Elements
- Core Catalog/Circulation Service Container (Microservice)
- API Gateway Container (Reverse Proxy / API Gateway)
- Search Engine Container (Dedicated Indexing Engine)
- Caching Container (Redis)
- Message Broker Container
- Archival and Backup Storage Service
- Telemetry Sidecar/Agent Container

## Relationships
- API Gateway Container -> Core Catalog/Circulation Service Container: Routes synchronous internal calls [HTTP/gRPC]
- Core Catalog/Circulation Service Container -> Caching Container: Optimizes read-heavy queries [Redis Protocol]
- Core Catalog/Circulation Service Container -> Message Broker Container: Emits domain events for write transactions [AMQP/Kafka Protocol]
- Core Catalog/Circulation Service Container -> Archival and Backup Storage Service: Offloads encrypted backups [Secure Storage Protocol]

## Technology Stack
- Domain-Driven Design (DDD) layered architecture: Separates domain models, application services, and infrastructure adapters for maintainability.
- Repository Pattern with Write-Through/Cache-Aside strategy: Optimizes read performance and decouples state writes.
- OpenAPI/Protobuf: Enforces API contract versioning and contract-first development.
- Flyway/Liquibase: Manages embedded database migrations during container startup.

## Rationale
This architecture uses asynchronous event-driven synchronization and bulkhead isolation to meet the sub-800ms 99th-percentile search requirement. Local encryption and isolated logging enforce strict EU data residency and GDPR privacy compliance.