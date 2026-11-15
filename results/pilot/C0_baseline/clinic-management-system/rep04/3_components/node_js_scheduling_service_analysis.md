## Overview
The Node.js Scheduling Service manages appointment scheduling, resource clash validation, and event publishing within a hybrid Kubernetes and AWS environment for the Clinic Management System. It ensures high-availability, conflict-free booking for patients and staff while maintaining HIPAA and GDPR compliance.

## Key Elements
*   **REST API Controller (Express.js):** Handles incoming HTTP routes, JWT validation, Zod schema validation, and rate limiting.
*   **Scheduling Engine:** Encapsulates slot-allocation business logic, resource metadata, sanitation windows, and constraint calculations.
*   **Resource Clash Detector:** Utilizes Redis distributed locks via `ioredis` to prevent double-booking.
*   **Persistence Repository:** Manages transactional writes, PgBouncer connection pooling, and the transactional outbox pattern to the PostgreSQL Cluster.
*   **Kafka Event Publisher:** Emits `AppointmentScheduled` domain events asynchronously using `kafkajs` to Apache Kafka.

## Relationships
*   **API Gateway -> REST API Controller:** Routes authenticated HTTP/REST requests over mTLS.
*   **Scheduling Engine -> Resource Clash Detector:** Acquires locks using `ioredis` over TLS 1.3.
*   **Persistence Repository -> PostgreSQL Cluster:** Executes SQL transactions using the `pg` client over TLS 1.3.
*   **Kafka Event Publisher -> Apache Kafka Event Bus:** Publishes domain events over TLS.

## Technology Stack
*   **Node.js & Express.js:** Core runtime and framework for lightweight, high-performance API routing.
*   **Redis Cluster & Redis Sentinel:** Provides distributed locking for real-time resource clash detection.
*   **PostgreSQL Cluster:** Relational data store for durable bookings and transactional outbox persistence.
*   **Apache Kafka:** Event bus for reliable, decoupled asynchronous messaging.
*   **Zod / Joi:** Runtime schema validation for security and input sanitization.
*   **OpenTelemetry & Prometheus:** Distributed tracing and metrics monitoring.

## Rationale
This architecture uses an asynchronous event-driven design backed by Redis distributed locks to meet the stringent sub-millisecond clash detection and 99.99% availability requirements. Decoupling the booking engine from downstream systems via Kafka and the outbox pattern ensures reliable clinic operations under heavy concurrent load.