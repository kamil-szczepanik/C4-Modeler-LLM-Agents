## Overview
The Circulation & Payments Service manages library item borrowing, returns, holds, and fine payments. It ensures high performance, transactional consistency, and strict compliance with EU data residency regulations.

## Key Elements
- Circulation & Payments Service (Java 17 / Spring Boot container)
- Circulation REST Controller Component
- Circulation Engine Component
- Payment Processing Component
- Transactional Outbox Publisher Component
- PostgreSQL (EU-hosted)
- Apache Kafka (EU-hosted)
- EU Payment Gateway
- EU-hosted Log & Telemetry Aggregator

## Relationships
- API Gateway -> Circulation REST Controller: Routes requests via [gRPC / mTLS (Istio)]
- Circulation REST Controller -> Circulation Engine & Payment Processing: Invokes methods via [In-process / Java Method Calls]
- Payment Processing Component -> EU Payment Gateway: Processes transactions via [HTTPS/REST]
- Circulation Engine & Payment Processing -> PostgreSQL: Persists transactional state and outbox events via [JDBC]
- Transactional Outbox Publisher -> Apache Kafka: Publishes domain events via [Kafka Protocol / TLS]
- Circulation & Payments Service -> EU-hosted Log & Telemetry Aggregator: Ships Prometheus metrics and sanitized JSON logs via [TLS]

## Technology Stack
- Java 17 / Spring Boot: Core runtime and framework for robust enterprise service development.
- Spring Data JPA & PostgreSQL: Relational persistence supporting ACID transactions and the Transactional Outbox Pattern.
- Apache Kafka: Asynchronous event messaging for reliable notification publishing and zero-loss event propagation.
- Resilience4j: Circuit breaking to prevent cascading failures during payment gateway outages.
- Spring Security & JWT: Role-Based Access Control and authentication token validation.

## Rationale
The architecture uses the Transactional Outbox Pattern to guarantee eventual consistency between PostgreSQL and Kafka without distributed 2PC locks. Tokenization, strict RBAC, and EU-hosted infrastructure ensure full alignment with EU data residency mandates and PCI-DSS scope reduction.