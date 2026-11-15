## Overview
The Patient & Scheduling Service is a core Java/Spring Boot backend container of the Clinic Management System designed to handle patient registration, appointment scheduling, and resource clash detection. It ensures high availability, strict HIPAA/GDPR audit trails, and reliable event-driven decoupling for medium-sized hospitals and clinics.

## Key Elements
- **`PatientController`**: REST/gRPC endpoint handler for incoming API Gateway requests.
- **`SchedulingEngine`**: Domain component executing appointment booking and resource clash checks.
- **`PatientRepository`**: Data access component using Spring Data JPA/JDBC.
- **`CacheManager`**: Component interacting with Redis for schedule and availability caching.
- **`AuditLogger`**: Spring AOP component generating immutable, cryptographically signed audit logs.
- **`KafkaEventPublisher`**: Component using the transactional outbox pattern to emit events.

## Relationships
- `API Gateway / BFF` -> `PatientController`: Routes internal requests [gRPC]
- `PatientController` & `SchedulingEngine` -> `AuditLogger`: Intercepts calls for auditing [In-process / Aspect]
- `SchedulingEngine` -> `PatientRepository`: Persists data [JDBC/SQL]
- `SchedulingEngine` -> `CacheManager`: Retrieves cached slots [Redis Protocol]
- `KafkaEventPublisher` -> `Apache Kafka`: Publishes domain events [Kafka Protocol / TCP]

## Technology Stack
- **Spring Boot (Java)**: Core framework for robust, enterprise-grade service implementation.
- **Spring Data JPA & JDBC**: Data access layer for relational database operations.
- **Redis**: In-memory data store for high-performance schedule caching.
- **Spring AOP**: Aspect-oriented programming for transparent, centralized audit logging.
- **Apache Kafka**: Distributed event broker for asynchronous inter-service messaging.

## Rationale
This component architecture uses Spring Boot for mature enterprise patterns while isolating domain logic in the `SchedulingEngine` to satisfy complex scheduling requirements. Incorporating `AuditLogger` via AOP and `KafkaEventPublisher` via the transactional outbox pattern guarantees compliance, immutability, and 99.99% system availability.