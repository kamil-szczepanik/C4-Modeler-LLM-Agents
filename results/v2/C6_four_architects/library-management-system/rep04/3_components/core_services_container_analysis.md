## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The Core Services Container acts as the modular monolithic domain engine executing within a Java Spring Boot runtime.

## Key Elements
- **Catalogue Component:** Manages physical and digital item metadata using Spring Data JPA.
- **Circulation Component:** Implements checkout, hold, and fine-processing domain logic using Spring Tx.
- **Integration Client Component:** Encapsulates outbound HTTPS calls via Spring Cloud OpenFeign/WebClient.
- **Compliance & Auditing Component:** Enforces regional anonymization and audit logs using Spring AOP.
- **Event Publisher Component:** Translates domain events using Spring AMQP.
- **Security Context & Session Component:** Handles request context and JWT validation using Spring Security.

## Relationships
- **API Gateway -> Security Context Component:** Forwards requests with JWT tokens [gRPC/HTTPS]
- **Catalogue & Circulation Components -> PostgreSQL Database:** Persists and retrieves relational data [TCP]
- **Catalogue Component -> Redis Caching Layer:** Reads and writes metadata cache [TCP]
- **Event Publisher Component -> Message Broker:** Publishes asynchronous events [AMQP]
- **Integration Client Component -> External Payment Gateway, National Library Registry, Notification Service, Digital Content Delivery Provider:** Executes external integrations [HTTPS]

## Technology Stack
- **Java & Spring Boot:** Core framework providing runtime environment and dependency injection.
- **Spring Data JPA & PostgreSQL:** Relational persistence layer ensuring transactional data integrity.
- **Redis:** High-performance caching layer to meet low-latency search goals.
- **Spring AMQP & Message Broker:** Asynchronous messaging for decoupled container communication.
- **Spring Security & Spring AOP:** Enforces security contexts and EU data residency constraints.

## Rationale
This modular monolith architecture ensures strict domain separation while maintaining high-performance transaction paths below the 800ms threshold. Spring AOP and targeted component boundaries natively enforce the strict EU-only data residency constraint.