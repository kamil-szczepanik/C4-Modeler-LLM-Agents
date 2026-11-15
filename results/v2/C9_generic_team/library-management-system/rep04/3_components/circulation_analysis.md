## Overview
- The Library Management System manages catalog items, circulation workflows, and self-service portals with strict EU data residency constraints.
- The Circulation component handles high-concurrency lending, returns, and inventory state transitions using robust distributed systems patterns.

## Key Elements
- Circulation Component (OCI-compliant Container, Spring Boot)
- Isolated Microservice Database (Relational/NoSQL Database)
- Asynchronous Message Broker Container (RabbitMQ / Kafka)
- Redis Distributed Cache Container (Redis)
- API Gateway Container (Envoy / NGINX)
- Notification / Messaging Service

## Relationships
- API Gateway Container -> Circulation: Routes traffic using gRPC/REST with correlation ID propagation
- Circulation -> Isolated Microservice Database: Reads and writes transactional data using SQL/TCP with Optimistic Locking (`@Version`)
- Circulation -> Asynchronous Message Broker Container: Publishes domain events (`ItemLent`, `ItemReturned`) via AMQP/TCP using the Transactional Outbox Pattern
- Circulation -> Redis Distributed Cache Container: Queries cached session data via TCP with strict TTLs and PII scrubbing
- Circulation -> Notification / Messaging Service: Triggers external notifications protected by Resilience4j circuit breakers

## Technology Stack
- Spring Boot: Selected for enterprise transactional workflow handling in the Circulation component
- Spring Data JPA: Utilized for entity management and `@Version`-based Optimistic Locking
- Resilience4j: Implemented for circuit breaker and fallback policies against non-critical downstream dependencies
- RFC 7807 Problem Details: Adopted for standardized, machine-readable API error payloads
- Testcontainers & Spring Cloud Contract: Deployed for automated integration and consumer-driven contract testing

## Rationale
- The architecture guarantees transactional atomicity and concurrency safety via the outbox pattern and optimistic locking under heavy workloads.
- Strict data scrubbing, correlation tracking, and isolated component design ensure compliance with EU-only data residency requirements.