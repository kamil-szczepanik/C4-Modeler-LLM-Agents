## Overview
A Library Management System designed for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces EU-only data residency and meets strict performance and transactional integrity standards.

## Key Elements
- **Users**: Library Patrons, Library Staff
- **External Systems**: Payment Gateway, Identity Provider / SSO, Notification Service, Logging & APM
- **Containers**: Patron Web Application, Staff Administration Portal, API Gateway, Core Domain Services, Search Engine, Relational Database, Async Event Bus, Notification Worker
- **Core Components**: Catalog Component, Circulation Component, Billing Component, Search Integration Component, Audit & Compliance Component

## Relationships
- **API Gateway -> Core Domain Services**: Routes requests via [mTLS]
- **Core Domain Services -> Relational Database**: Reads/writes transactional data via [mTLS] and [PgBouncer]
- **Core Domain Services -> Search Engine**: Performs high-performance search queries via [mTLS]
- **Core Domain Services -> Async Event Bus**: Publishes domain events via [mTLS]
- **Core Domain Services -> Identity Provider / SSO**: Authenticates users via [SAML/OIDC]
- **Core Domain Services -> Payment Gateway**: Processes fee payments via [HTTPS/REST] with [Circuit Breaker]
- **Core Domain Services -> Logging & APM**: Sends telemetry, logs, and audit trails via [HTTPS]

## Technology Stack
- **Backend Core**: Node.js / NestJS (Modular Monolith) with TypeScript for structured component boundaries and dependency injection
- **Database & ORM**: PostgreSQL with TypeORM and PgBouncer connection pooling for transactional data and strict EU residency
- **Search & Caching**: Elasticsearch managed by Search Integration Component to achieve <800ms search NFRs
- **Messaging & Resilience**: RabbitMQ / Apache Kafka event bus; Opossum Circuit Breaker for payment degradation
- **Infrastructure & Security**: Kubernetes (HPA, cgroups, Secrets), Nginx / Spring Cloud Gateway, TLS 1.3 / mTLS, OAuth2/JWT

## Rationale
The modular monolith architecture balances rapid feature delivery for core cataloging and circulation with strict internal boundaries that allow future extraction into microservices if needed. Explicit decoupling via an async event bus, robust circuit breakers, and dedicated search integration protect transactional performance and meet EU data compliance constraints.