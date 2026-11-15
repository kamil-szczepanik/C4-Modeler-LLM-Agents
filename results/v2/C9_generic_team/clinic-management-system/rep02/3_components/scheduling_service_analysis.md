## Overview
The Scheduling Service is a core microservice within the Clinic Management System that handles appointment bookings and resource clash checks. It operates in a hybrid cloud infrastructure to support clinical workflows across medium-sized hospitals and clinics.

## Key Elements
- Scheduling Service (Microservice, Kubernetes, Database-per-service)
- Distributed Cache (Redis)
- Message Broker (Kafka / RabbitMQ)
- Secret Management (HashiCorp Vault)
- Downstream Consumers (Billing Service, EMR Service)

## Relationships
- API Gateway -> Scheduling Service: Routes incoming appointment and availability requests via [gRPC / REST]
- Scheduling Service -> Distributed Cache: Caches scheduling data and read models via [Redis Protocol]
- Scheduling Service -> Message Broker: Publishes asynchronous domain events via [Kafka / AMQP]
- Scheduling Service -> HashiCorp Vault: Retrieves encrypted configurations and secrets via [HTTPS / Vault API]

## Technology Stack
- Kubernetes: Orchestrates active-active deployment supporting 99.99% uptime constraint (R-06)
- Database-per-service with Optimistic Concurrency Control: Prevents double-booking race conditions during resource clash checks (R-02)
- CQRS Pattern: Separates high-throughput read operations using Redis from transactional write databases
- Transactional Outbox Pattern: Guarantees at-least-once asynchronous event delivery without dual-write inconsistencies
- OpenTelemetry: Provides distributed tracing propagation across hybrid cloud boundaries
- HashiCorp Vault: Manages externalized configuration and runtime secrets dynamically

## Rationale
This architecture uses CQRS, optimistic concurrency, and outbox patterns to ensure high-throughput appointment scheduling without resource clashes. The hybrid Kubernetes deployment with Redis caching and asynchronous messaging meets the strict 99.99% availability and data consistency requirements.