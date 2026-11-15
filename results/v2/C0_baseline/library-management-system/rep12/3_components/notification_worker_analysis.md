## Overview
The Notification Worker is a background container within the Library Management System that asynchronously processes and dispatches multi-channel alerts to patrons. It ensures compliance with EU data residency while maintaining high availability and observability.

## Key Elements
- Notification Worker (Node.js / NestJS)
- Event Consumer Component (AMQP)
- Template Engine Component (ICU message syntax)
- Dispatch Router & Adapter Components (Circuit breaker, mTLS)
- Delivery Status Tracker Component
- Notification Query Service Component (RBAC, tenant isolation)
- RabbitMQ / Apache Kafka (Async Event Bus)
- PostgreSQL (Relational Database with read-replica)
- External Notification Service

## Relationships
- Async Event Bus -> Notification Worker: Consumes notification triggers via AMQP with TLS and HMAC signature validation
- Notification Worker -> External Notification Service: Dispatches alerts via HTTPS using mTLS and short-lived vault credentials
- Notification Worker -> PostgreSQL: Records delivery outcomes and metrics
- Staff Administration Portal -> Notification Query Service: Queries aggregated notification histories via API Gateway using read-replicas

## Technology Stack
- Node.js / NestJS: Chosen for asynchronous I/O and architectural consistency across backend services
- RabbitMQ: Selected with dead-letter exchanges (DLX) and exponential backoff for resilient event consumption
- PostgreSQL: Provides durable storage with row-level security and read-replicas for high-throughput tracking
- Kubernetes (HPA): Enables auto-scaling based on queue length metrics

## Rationale
This architecture guarantees strict EU data residency, GDPR-compliant PII redaction, and multi-language support while maintaining resilience against external service outages via circuit breakers. It isolates background write workloads from staff-facing analytical queries to ensure optimal performance.