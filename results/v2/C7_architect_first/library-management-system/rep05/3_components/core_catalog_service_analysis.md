## Overview
- The Core Catalog Service manages physical and digital item cataloging, bibliographic validation, and metadata storage for the Library Management System.
- It ensures high-performance operations, strict EU data residency compliance, and secure data handling for public and academic libraries.

## Key Elements
- **CatalogController**: Spring MVC/REST adapter exposing gRPC endpoints with SPIFFE/SPIRE SVID authentication.
- **CatalogService**: Domain component containing metadata validation (MARC21/Dublin Core), dynamic schema adapters, and facet generation.
- **CatalogRepository**: Spring Data JPA/Hibernate data access component with HikariCP connection pooling and PostgreSQL JDBC drivers.
- **Outbox Poller**: Asynchronous event drainer implementing the transactional outbox pattern.
- **SearchSyncPublisher**: Event emitter generating cryptographically signed (HMAC-SHA256) outbox messages.
- **PostgreSQL Database**: Primary-replica relational database with EU data residency, Row-Level Security (RLS), and AES-256 encryption-at-rest.
- **RabbitMQ**: Message broker secured with mTLS and dead-letter exchanges (DLX) for asynchronous search synchronization.

## Relationships
- **API Gateway / Circulation Service** -> **CatalogController**: Routes gRPC requests over Istio service mesh using mTLS.
- **CatalogController** -> **CatalogService**: Direct in-process method invocation.
- **CatalogService** -> **CatalogRepository**: Spring Data JPA / JDBC calls with Hibernate Envers auditing.
- **CatalogRepository** -> **PostgreSQL Database**: TLS 1.3 encrypted JDBC queries, utilizing `JSONB` columns for flexible metadata.
- **Outbox Poller** -> **RabbitMQ**: Publishes HMAC-SHA256 signed transactional outbox events for downstream search indexing.

## Technology Stack
- **Java / Spring Boot**: Foundation for building enterprise-grade, robust backend microservices.
- **Spring Data JPA / Hibernate**: Provides ORM capabilities with Hibernate Envers for immutable audit logs.
- **PostgreSQL**: Relational database supporting read-replicas, RLS, and `JSONB` for schema-agnostic attributes.
- **gRPC / Istio**: Enables high-performance internal communication with mTLS security.
- **RabbitMQ**: Asynchronous message broker with DLX for decoupling service synchronization.
- **OpenTelemetry**: Standardized tracing framework for monitoring latency and connection pools.

## Rationale
- The architecture isolates domain logic, transport, and persistence while using PostgreSQL read-replicas and `JSONB` to meet the <800ms search latency requirement (R-05).
- Security controls like EU-hosted KMS, AES-256 encryption, RLS, and signed outbox messaging strictly enforce EU data residency and tenant isolation constraints.