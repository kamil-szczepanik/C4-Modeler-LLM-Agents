## Overview
- The Core Domain Service manages cataloging, circulation, and financial rules for the Library Management System.
- It provides secure, scalable business logic processing for public and academic library patrons and staff.

## Key Elements
- API Gateway (NGINX / Spring Cloud Gateway)
- Core Domain Service (Java / Spring Boot container)
- Catalog Management Component (`Spring @Service`, Java)
- Circulation Engine Component (`Spring @Service`, Java)
- Fine & Fee Management Component (`Spring @Service`, Java)
- Domain Event Publisher (`Spring Component`, Java)
- Database (PostgreSQL with TDE, EU region)
- Asynchronous Broker (Redis with TLS, EU region)
- Background Worker (Python / Celery)

## Relationships
- API Gateway -> Catalog Management, Circulation Engine, & Fine/Fee Management: Routes requests via `gRPC` over HTTP/2 with mTLS
- Catalog Management, Circulation Engine, & Fine/Fee Management -> Database: Executes transactional reads and writes via `Spring Data JPA` and `JDBC over TLS`
- Circulation Engine & Fine/Fee Management -> Domain Event Publisher: Delegates domain state changes via Spring's `ApplicationEventPublisher`
- Domain Event Publisher -> Asynchronous Broker: Dispatches domain events via `Spring Data Redis` over TLS with application-layer encryption for financial payloads

## Technology Stack
- Java / Spring Boot: Chosen for robust enterprise business logic and dependency injection
- Spring Security: Enforces method-level `@PreAuthorize` authorization for granular access control
- PostgreSQL & Spring Data JPA: Provides ACID-compliant relational persistence with HikariCP connection pooling
- Redis & Spring Data Redis: Powers asynchronous event messaging with Dead Letter Queue handling
- Kubernetes: Hosts containerized OCI images with Horizontal Pod Autoscaling and resilience4j circuit breakers

## Rationale
- The Spring Boot micro-service architecture with strict component separation ensures high maintainability and isolated transactional boundaries for circulation and cataloging.
- Strict EU-region cloud deployment, mTLS, database encryption, and audit logging satisfy regional data residency and financial compliance mandates.