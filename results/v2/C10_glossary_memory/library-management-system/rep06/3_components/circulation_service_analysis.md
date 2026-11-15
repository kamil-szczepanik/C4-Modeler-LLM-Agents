## Overview
[The Circulation Service manages patron accounts, circulation workflows, and fine settlements for the Library Management System. It ensures secure, EU-compliant handling of borrowing history and instant self-service transaction feedback.]

## Key Elements
- Circulation Service (Java, Spring Boot)
- Loan Management Component (Spring Data JPA)
- Hold & Reservation Component
- Fine Management Component
- Audit Logging Component
- Primary Database & Read Replica (PostgreSQL)
- Payment Gateway (REST/JSON)
- Notification Service (Node.js, TypeScript, RabbitMQ/Kafka)
- Core API Gateway (Envoy, Spring Cloud Gateway)

## Relationships
- Core API Gateway -> Circulation Service [gRPC / HTTPS, mTLS]
- Fine Management Component -> Payment Gateway [REST/JSON, mTLS over HTTPS with Idempotency Keys]
- Loan Management Component -> Notification Service [AMQP / RabbitMQ]
- Loan Management Component & Fine Management Component -> Primary Database & Read Replica [PostgreSQL Protocol over TLS 1.3]
- Loan Management Component -> Hold & Reservation Component [In-process / Java Method Call]

## Technology Stack
- Java & Spring Boot: Powers the core container runtime to meet high-performance requirements
- Spring Security (@PreAuthorize): Enforces fine-grained method-level Role-Based Access Control (RBAC)
- HikariCP: Optimizes database connection pooling for high-concurrency check-out rushes
- OpenTelemetry: Provides distributed tracing for latency isolation
- HashiCorp Vault: Secures runtime injection of database credentials and API keys
- Kubernetes: Enforces strict EU-only node pools for data residency compliance

## Rationale
[Decomposing the Circulation Service into in-process Spring Boot components eliminates network overhead to meet performance SLAs while maintaining a unified runtime. Enforcing strict EU node pools, TLS 1.3, and transparent database encryption satisfies rigorous data residency and security mandates.]