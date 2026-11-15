## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The background workers container asynchronously processes decoupled system tasks.

## Key Elements
- Patrons and Library Staff (Users)
- Client-Side SPA/Mobile Container (Web/Mobile Technologies)
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container (Microservice API Runtime)
- Search Engine Container (Elasticsearch / OpenSearch)
- Data Access Layer / Persistence Container (PostgreSQL)
- Asynchronous Message Broker Container (RabbitMQ / Kafka)
- Background Workers Container (Background Worker Runtime)
- Configuration & Secrets Management Container (HashiCorp Vault)
- Centralized Observability Container (Observability Platform)

## Relationships
- Asynchronous Message Broker Container -> Background Workers Container: Consumes asynchronous events via subscription [Event Subscription]
- Background Workers Container -> Data Access Layer / Persistence Container: Reads and persists job states and domain data [SQL / TCP]
- Background Workers Container -> Configuration & Secrets Management Container: Fetches dynamic secrets and configuration [HTTPS]
- Background Workers Container -> Centralized Observability Container: Emits structured logs, traces, and metrics [OTLP / HTTPS]

## Technology Stack
- Background Worker Runtime: Stateless worker architecture supporting graceful shutdowns, concurrency limits, and backpressure
- Asynchronous Message Broker: RabbitMQ or Kafka for event distribution, Dead Letter Queues (DLQ), and payload versioning
- Persistence Layer: PostgreSQL with TTL-based pruning for job state tracking and idempotency records
- Secrets Management: HashiCorp Vault for dynamic credential injection and rotation
- Observability: Centralized monitoring with correlation ID propagation

## Rationale
This architecture ensures high performance, robust error handling, and horizontal scalability for asynchronous background tasks. It strictly maintains EU-only data residency while supporting fault tolerance and system resilience.