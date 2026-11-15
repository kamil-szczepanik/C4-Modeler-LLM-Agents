## Overview
The Core Services Container is a Spring Boot microservice handling core business logic, cataloguing, and circulation for the Library Management System. It ensures high performance and EU data residency compliance.

## Key Elements
- Catalog Component: Manages physical and digital item metadata (Spring `@Service`, JPA)
- Circulation Component: Handles borrowing, returns, and holds logic (Spring `@Service`, JPA)
- Patron Account Component: Manages user profiles and EU-constrained PII (Spring `@Service`, JPA)
- Data Access Layer: Enforces EU-only data residency and AES-256 encryption (Spring Data JPA, Hibernate)
- External Dependencies: API Gateway, PostgreSQL Database, Elasticsearch Search Container, RabbitMQ

## Relationships
- API Gateway -> Catalog, Circulation, & Patron Components: Authenticated gRPC / internal REST with mTLS, W3C Trace Context, and Spring Security `@PreAuthorize`
- Catalog & Circulation Components -> Data Access Layer: JDBC over TLS 1.3 within private EU subnet
- Catalog Component -> Search Container: Asynchronous Change Data Capture (CDC) via Debezium and RabbitMQ DLQ

## Technology Stack
- Spring Boot & Spring Cloud: Framework for microservices and modular components ensuring rapid feature delivery
- Spring Data JPA & Hibernate: ORM and data access layer enforcing EU-only residency and AES-256 encryption
- Debezium & RabbitMQ: CDC pipeline and dead-letter queue for asynchronous Elasticsearch synchronization
- HashiCorp Vault & Kubernetes: Secret management and distroless container hardening for security compliance

## Rationale
This architecture uses a modular monolith pattern within the container to simplify transaction management while maintaining clean boundaries. It securely satisfies strict EU data residency constraints and sub-800ms search performance requirements (R-05).