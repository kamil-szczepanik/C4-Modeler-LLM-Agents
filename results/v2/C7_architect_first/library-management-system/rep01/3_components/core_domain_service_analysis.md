## Overview
The Library Management System provides catalogue management, circulation controls, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
- **Circulation Controller**: NestJS Controller handling REST/gRPC endpoints, JWT validation, and RBAC.
- **Catalog Management Module**: NestJS Module managing item metadata, availability rules, and R-01 cataloguing.
- **Domain Event Publisher**: NestJS Service emitting encrypted AMQP events with W3C Trace Context.
- **Repository Adapters**: TypeORM/Prisma components with circuit breakers and RLS.
- **PostgreSQL**: Transactional database strictly hosted within EU partitions.
- **RabbitMQ**: Message broker handling asynchronous tasks and audit events.
- **Telemetry Sidecar (OTEL Collector)**: Observability platform for distributed tracing.

## Relationships
- **API Gateway -> Circulation Controller**: Routes requests [gRPC over mTLS].
- **Circulation Controller -> Catalog Management Module**: Coordinates item availability [TypeScript Method Calls].
- **Catalog Management & Circulation -> Repository Adapters**: Executes persistence operations [TLS-encrypted TCP with fail-closed circuit breakers].
- **Domain Event Publisher -> RabbitMQ**: Dispatches audit and domain events [AMQP over TLS with AES-GCM encryption and W3C headers].

## Technology Stack
- **NestJS (Node.js)**: Chosen for modular architecture and built-in dependency injection supporting Domain-Driven Design.
- **PostgreSQL**: Selected for robust transactional capabilities with Row-Level Security for EU data residency.
- **RabbitMQ**: Implemented with dead-letter exchanges and publisher confirms for reliable asynchronous messaging.
- **OpenTelemetry (OTEL)**: Mandated for end-to-end distributed tracing to meet latency SLAs.

## Rationale
This architecture uses a modular NestJS component structure to strictly isolate circulation and catalog logic while enforcing EU data residency. Resilient database adapters and secure message publishing ensure compliance, low latency, and fault tolerance for library patrons and staff.