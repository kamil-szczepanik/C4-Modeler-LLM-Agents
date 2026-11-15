## Overview
[System: Library Management System / Core Domain Service]
[Purpose: Manages cataloging, circulation, and user profiles within a modular monolith architecture]

## Key Elements
- Catalog Component (Java, Spring Data JPA)
- Circulation Engine (Java, Spring)
- User Management Component (Java, Spring Security)
- Domain Event Publisher Component (Java, Spring ApplicationEventPublisher)
- Cache-Aside Component (Java, Spring Cache, Redis)
- Transaction Management Component (Java, Spring `@Transactional`)
- Security & GDPR Context Filter Component (Java, Spring Security Filter)
- Domain Model Validators (Java, JSR-380)
- Health & Metrics Actuator Component (Java, Spring Boot Actuator)

## Relationships
- API Gateway -> Security & GDPR Context Filter Component [gRPC over mTLS]
- Security & GDPR Context Filter Component -> Circulation Engine & Catalog Component [Java Method]
- Circulation Engine & Catalog Component -> Domain Model Validators [Java Method]
- Circulation Engine -> Transaction Management Component [Java Annotation]
- Transaction Management Component -> PostgreSQL [JDBC over TLS 1.3]
- Catalog Component -> Cache-Aside Component [Java Method]
- Cache-Aside Component -> Redis [RESP over TLS 1.3]
- Circulation Engine & Catalog Component -> Domain Event Publisher [Java Method]
- Domain Event Publisher -> RabbitMQ [AMQP over TLS]
- Core Domain Service -> Monitoring Infrastructure [HTTP over TLS]

## Technology Stack
- Java & Spring Boot: Core framework for modular monolith structure
- Spring Data JPA: Object-relational mapping and data persistence
- Spring Security: JWT validation and GDPR enforcement
- Redis: Caching layer for <800ms response time SLA
- PostgreSQL: ACID-compliant relational storage with EU-only data residency
- RabbitMQ: Asynchronous domain event distribution via AMQP

## Rationale
[A modular monolith design balances high cohesion for domain logic with strict ACID compliance for lending transactions.]
[Decoupled components and caching layers ensure performance SLAs (<800ms search) and EU data residency constraints are met.]