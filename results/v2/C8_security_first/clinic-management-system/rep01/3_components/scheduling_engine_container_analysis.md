## Overview
The Scheduling Engine Container manages appointment bookings, clinician calendars, resource optimization, and automated waitlist backfilling for the Clinic Management System. It ensures high-availability clinical operations while maintaining HIPAA and GDPR compliance across hybrid Kubernetes clusters.

## Key Elements
* Booking API Controller (Java / Spring Boot)
* Conflict Resolution Service (Java / Spring Boot)
* Calendar & Slot Manager (Java / Spring Boot)
* Resource Allocation Coordinator (Java / Spring Boot)
* Notification Publisher (Java / Spring Boot)
* Envoy / NGINX API Gateway
* Primary Database (PostgreSQL with Citus)
* Event Broker (Redpanda)
* Observability Stack (OpenTelemetry, Grafana Mimir/Tempo, Falco)

## Relationships
* Envoy / NGINX API Gateway -> Booking API Controller: Routes HTTP/2 and gRPC requests over mTLS
* Booking API Controller -> Primary Database: Executes transactional reads and writes over encrypted internal TCP
* Notification Publisher -> Redpanda: Publishes encrypted domain events using Kafka/Redpanda Spring Boot starter over encrypted internal TCP
* Conflict Resolution Service -> Redpanda: Consumes cancellation events for waitlist backfilling over encrypted internal TCP
* Resource Allocation Coordinator -> Primary Database: Manages atomic multi-resource locking using database-level advisory locks over encrypted internal TCP

## Technology Stack
* Java with Spring Boot: Core framework providing robust dependency injection, Spring Security, and enterprise ecosystem integration.
* PostgreSQL with Citus: Relational data storage supporting horizontal scaling and secure data persistence.
* Redpanda: Event streaming platform enabling reliable, asynchronous domain event publishing and waitlist queueing.
* Resilience4j: Fault-tolerance library providing circuit breakers and bulkhead patterns to prevent cascading failures.
* OpenTelemetry & Grafana: Observability tools ensuring distributed tracing, custom metrics tracking, and compliance monitoring.

## Rationale
This architecture uses Spring Boot micro-components combined with robust resilience patterns and transactional outbox mechanisms to guarantee 99.99% uptime and high throughput. Column-level encryption, field-level pseudonymization, and stateless auto-scaling container deployments ensure strict HIPAA/GDPR compliance under peak clinical workloads.