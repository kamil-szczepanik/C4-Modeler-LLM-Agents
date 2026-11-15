## Overview
[Library Management System provides catalogue management, circulation tracking, and self-service portals for public and academic libraries. The Circulation & Catalogue Microservice powers core inventory and checkout operations while enforcing strict EU data residency.]

## Key Elements
*   Patron Self-Service Portal & Librarian Management Portal (React/TypeScript SPAs)
*   API Gateway (Kong / Envoy)
*   Circulation & Catalogue Microservice (Java / Spring Boot)
*   Search Microservice (Java / Spring Boot)
*   Message Broker (RabbitMQ / Kafka)
*   Database Layer (PostgreSQL with TDE and HikariCP)
*   Elasticsearch (EU-hosted)

## Relationships
*   API Gateway -> Circulation & Catalogue Microservice: Routes ingress via OAuth 2.0 / OIDC and mTLS
*   Search Microservice -> Circulation & Catalogue Microservice: Inter-service communication via gRPC over mTLS
*   Circulation & Catalogue Microservice -> Message Broker: Publishes signed asynchronous events via AMQP / Kafka Protocol
*   Circulation & Catalogue Microservice -> Database Layer: Persists data via JDBC over TLS 1.3

## Technology Stack
*   Java / Spring Boot: Core container framework providing robust enterprise capabilities and dependency injection.
*   Spring MVC & Spring Security: Handles REST endpoints and method-level `@PreAuthorize` RBAC.
*   Spring Data JPA: Manages database persistence and optimistic locking via `@Version`.
*   PostgreSQL & HikariCP: Relational storage with optimized, secure connection pooling.
*   Spring Cloud Stream & Apache Kafka: Asynchronous event messaging with HMAC payload signing.
*   Resilience4j: Implements circuit breakers and rate limiters for fault tolerance.
*   OpenTelemetry: Provides distributed tracing with agent-level PII scrubbing.
*   Kubernetes: Manages horizontal autoscaling (min 3 replicas) across EU zones.

## Rationale
[This architecture uses a horizontally autoscaled Spring Boot microservice with circuit breakers and connection pooling to easily achieve the 99.9% availability target and <800ms search SLA. Furthermore, EU-pinned databases, TLS 1.3, and PII-scrubbed telemetry strictly satisfy regional data residency and GDPR compliance mandates.]