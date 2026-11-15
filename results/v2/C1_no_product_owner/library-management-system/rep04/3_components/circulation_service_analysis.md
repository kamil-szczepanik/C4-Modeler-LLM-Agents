## Overview
The Circulation Service is a core container of the Library Management System responsible for managing borrowing, returns, and fine workflows. It ensures high performance, strict EU data residency, and reliable transaction processing for academic and public libraries.

## Key Elements
- **Circulation Controller / GrpcHandler**: Exposes gRPC endpoints [Java/gRPC].
- **Borrowing Engine**: Manages loan logic including the **Loan Rule Engine (Specification Pattern)** [Spring Service / Java 21].
- **Fine Management Component**: Handles fee calculations with **Resilience4j** circuit breaking.
- **Circulation Data Access Object (DAO)**: Manages persistence via **Spring Data JPA / Hibernate**.
- **Outbox Pattern Component**: Guarantees reliable messaging via local transactions.
- **Event Publisher**: Publishes domain events [Spring AMQP].

## Relationships
- API Gateway -> Circulation Controller: Routes requests [gRPC with mTLS, JWT]
- Circulation DAO -> PostgreSQL: Persists data [Encrypted database protocols, AES-256]
- Event Publisher -> RabbitMQ: Publishes messages [AMQP over TLS]
- Fine Management Component -> Payment Gateway: Processes fees [TLS 1.3]

## Technology Stack
- **Spring Boot / Java 21**: Core application framework for modular architecture and robust concurrency.
- **PostgreSQL**: Primary transactional data store ensuring EU-only data residency compliance.
- **RabbitMQ**: Message broker for asynchronous, decoupled event distribution.
- **gRPC with mTLS**: High-performance internal service-to-service communication protocol.
- **Resilience4j**: Fault tolerance library preventing downstream cascading failures.
- **OpenTelemetry**: Distributed tracing standard for system observability.

## Rationale
This architecture uses modular Spring Boot services with gRPC communication to meet strict performance requirements like sub-800ms searches. The Outbox pattern and robust security controls ensure data integrity, transactional reliability, and EU data residency compliance.