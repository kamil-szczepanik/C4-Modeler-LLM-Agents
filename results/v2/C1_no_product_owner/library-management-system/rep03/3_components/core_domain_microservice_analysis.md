## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for academic and public libraries. It ensures strict EU data residency and high performance with 99th-percentile search responses under 800 milliseconds.

## Key Elements
- **CirculationController**: Spring MVC component handling REST ingress, JWT claims verification, and Bean Validation.
- **CatalogDomainService**: Spring `@Service` managing core circulation rules and audit logging.
- **LoanRepository**: Spring Data JPA component managing relational persistence.
- **OutboxDispatcher**: Scheduled Spring component processing reliable event dispatching.
- **EventPublisher**: Spring AMQP component emitting messages to RabbitMQ.
- **PostgreSQL**: Relational database storing catalog data, loan states, and outbox tables with TLS 1.3 and column-level PII encryption.
- **RabbitMQ**: Message broker receiving asynchronous domain events via AMQPS.
- **HashiCorp Vault**: Secrets manager providing dynamic credentials and transit encryption keys.
- **OpenTelemetry Collector / Grafana**: Observability stack tracking W3C trace contexts and metrics.

## Relationships
- **API Gateway -> CirculationController**: Routes HTTP requests with RBAC [mTLS, REST/JSON]
- **CirculationController -> CatalogDomainService**: Invokes business rules [Java Method Call]
- **CatalogDomainService -> LoanRepository**: Persists domain entities and outbox records in a single database transaction [JPA/JDBC]
- **CatalogDomainService -> EventPublisher**: Triggers asynchronous event emission [Java Method Call]
- **OutboxDispatcher -> EventPublisher**: Relays pending outbox messages with Resilience4j circuit breaking [Java Method Call]
- **EventPublisher -> RabbitMQ Message Broker**: Publishes catalog and circulation state-change events [AMQPS]
- **Core Domain Microservice -> PostgreSQL**: Reads and writes relational data [JDBC, TLS 1.3]

## Technology Stack
- **Java 17 & Spring Boot**: Core container runtime ensuring robust enterprise domain logic.
- **Spring Data JPA & JDBC**: Relational data persistence layer.
- **Spring AMQP & RabbitMQ**: Asynchronous messaging infrastructure with outbox pattern.
- **Resilience4j**: Circuit breaking for fault tolerance against broker downtime.
- **HashiCorp Vault**: Dynamic secret bootstrapping and application-layer PII encryption.
- **OpenTelemetry & Prometheus**: Distributed tracing and telemetry collection.

## Rationale
The architecture guarantees zero data loss and fault tolerance during broker outages using the Transactional Outbox Pattern and Resilience4j circuit breakers. Strict security controls, including TLS 1.3, Vault-backed PII encryption, and method-level RBAC, satisfy EU data residency and security constraints.