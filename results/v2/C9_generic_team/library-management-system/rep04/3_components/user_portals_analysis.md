## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It meets the < 800 ms search performance SLA and enforces strict EU-only data residency constraints.

## Key Elements
- User Portals (OCI-compliant Container, Spring Boot)
- API Gateway Container (OCI-compliant Container, Envoy / NGINX)
- Redis Distributed Cache Container (Redis)
- Isolated Microservice Databases (Relational/NoSQL Database)
- Asynchronous Message Broker Container (RabbitMQ / Kafka)
- Web Frontend & Mobile App

## Relationships
- API Gateway Container -> User Portals: Routes traffic [gRPC]
- User Portals -> Redis Distributed Cache Container: Queries cache, idempotency, and rate limiting [TCP]
- User Portals -> Isolated Microservice Databases: Reads and writes EU-hosted data [SQL/TCP]
- User Portals -> Asynchronous Message Broker Container: Publishes/consumes events for notifications [AMQP/TCP]

## Technology Stack
- Spring Boot: Core framework for User Portals container, implementing Repository and Service Layer patterns.
- gRPC: Standardized internal service-to-service communication protocol for latency reduction.
- Redis: Distributed cache supporting circuit breaker fallbacks, idempotency keys, and rate limiting.
- Spring Boot Actuator: Liveness, readiness, and startup probes for OCI container orchestration.
- RFC 7807: Standardized Problem Details for global exception handling and error mapping.

## Rationale
The architecture uses gRPC, BFF patterns, and Redis-backed rate limiting to satisfy the < 800 ms search performance requirement. Startup configuration checks and geo-pinned connections strictly enforce the EU-only data residency constraint.