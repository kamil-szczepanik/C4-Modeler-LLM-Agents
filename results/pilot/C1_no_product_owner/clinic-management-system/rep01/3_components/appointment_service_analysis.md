## Overview
The Appointment Service manages clinical appointment scheduling, resource clash validation, and calendar synchronization within the Clinic Management System. It ensures high availability and regulatory compliance across hybrid Kubernetes and AWS cloud environments.

## Key Elements
- `AppointmentController`: Handles incoming HTTPS/mTLS REST endpoints and JWT-based authorization.
- `SchedulingEngine`: Enforces business logic, resource clash checks, and conflict-free slot allocation.
- `CalendarIntegration`: Synchronizes with external provider calendars using resilience4j circuit breakers.
- `AppointmentRepository`: Manages data persistence, PostgreSQL interactions, and Hibernate Envers audit trails.
- Redis Cluster: Provides distributed locking with TLS encryption and AES-256 at rest.
- Apache Kafka: Publishes encrypted `AppointmentScheduled` events using JWE and tokenized patient references.

## Relationships
- API Gateway -> `AppointmentController`: Routes scheduling requests [HTTPS / mTLS (Istio)]
- `AppointmentController` -> Identity Service: Validates JSON Web Tokens (JWT) locally
- `SchedulingEngine` -> Redis Cluster: Executes distributed lock checks before writes [TLS]
- `SchedulingEngine` -> `AppointmentRepository`: Queries and persists slot availability [JDBC / Spring Data JPA]
- `SchedulingEngine` -> Apache Kafka: Publishes asynchronous domain events [Spring Cloud Stream]

## Technology Stack
- Java / Spring Boot: Core container framework for robust enterprise clinical services.
- Spring Data JPA & Hibernate Envers: Handles relational data persistence and immutable audit trails.
- Redis (Redlock): Manages distributed locking to prevent booking slot collisions in active-active setups.
- Apache Kafka & JWE: Enables secure, asynchronous event-driven messaging with envelope encryption.
- Resilience4j: Protects external integrations with circuit breakers and exponential backoff.
- OpenTelemetry & Micrometer: Delivers distributed tracing and JVM performance metrics.

## Rationale
This architecture uses an active-active hybrid design with distributed locking and event-driven patterns to satisfy the 99.99% availability requirement. Strict encryption, JWT authorization, and immutable audit trails ensure full HIPAA and GDPR compliance for sensitive clinical data.