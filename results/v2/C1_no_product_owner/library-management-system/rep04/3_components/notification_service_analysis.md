## Overview
[Library Management System] is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals.

## Key Elements
* Notification Controller (Spring Web/gRPC)
* Event Consumer / Listener (Spring AMQP)
* Template Engine (Thymeleaf)
* Dispatch Engine (Java 21 Service Layer)
* Provider Integration Client (Spring WebClient with Resilience4j)
* Outbox Table (PostgreSQL with JPA/Hibernate)
* RabbitMQ (Message Broker)
* Notification Provider (External API)
* HashiCorp Vault (Secret Management)

## Relationships
* API Gateway -> Notification Controller: gRPC with mTLS and propagated JWTs
* Event Consumer -> RabbitMQ: AMQP over TLS
* Notification Controller / Event Consumer -> Outbox Table: JDBC over TLS
* Dispatch Engine -> Provider Integration Client: In-process Java method calls
* Provider Integration Client -> Notification Provider: Outbound REST over TLS 1.3
* Provider Integration Client -> HashiCorp Vault: Secure secret retrieval

## Technology Stack
* Java 21 & Spring Boot: Core runtime and framework for robust service implementation
* PostgreSQL: Relational database utilizing the Outbox Pattern for reliable transactional messaging
* RabbitMQ: Asynchronous message broker for handling event-driven alerts
* Resilience4j: Circuit breaker implementation to protect external provider calls and fail fast
* Thymeleaf: Secure template engine enforcing strict escaping to prevent SSTI
* OpenTelemetry: Distributed tracing across gRPC boundaries, RabbitMQ headers, and TLS requests

## Rationale
This component architecture implements strict EU-only data residency constraints through regional provider mandates, PII redaction, and encrypted outbox storage. It guarantees high performance, transactional reliability, and security using resilience patterns and token-bucket rate limiting.