## Overview
- Architecture for the Library Management System's Dedicated Search Tier, designed to catalogue physical and digital items while guaranteeing high performance and strict data compliance.
- Achieves a 99th-percentile search response time under 800 ms through decoupled, resilient, and EU-compliant search infrastructure.

## Key Elements
- Library Patrons and Staff
- Self-Service Portals and Kiosks (Web/Mobile UI)
- API Gateway (HTTP/REST)
- API Composition / BFF Container (HTTP/REST, OpenAPI)
- Core Domain Services (Microservices / gRPC / REST)
- Dedicated Search Tier (Search Infrastructure)
- Primary Transactional Datastore (Relational Database / SQL)
- Asynchronous Event Bus / Message Broker (AMQP / Kafka) with Dead Letter Queue (DLQ)
- Caching Layer (Redis)
- EU-certified Secrets Management Vault & Object Storage

## Relationships
- Self-Service Portals and Kiosks -> API Gateway: Routes user traffic [HTTP/REST]
- API Gateway -> API Composition / BFF Container: Forwards requests [HTTP/REST]
- API Composition / BFF Container -> Dedicated Search Tier: Executes search queries via circuit breaker and bulkhead patterns [gRPC/HTTP]
- Asynchronous Event Bus -> Dedicated Search Tier: Consumes catalog events with idempotent handlers [Message Broker Protocol]
- Dedicated Search Tier -> EU-certified Object Storage: Stores backups and snapshots [HTTPS/S3 API]

## Technology Stack
- Search Infrastructure: Dedicated Search Tier with versioned indices and configuration-driven timeouts for < 800 ms p99 latency (*R-05*).
- Messaging: Asynchronous Event Bus (AMQP / Kafka) with Dead Letter Queue (DLQ) for asynchronous catalog updates (*R-01*).
- Resilience Patterns: Circuit breakers, bulkheads, and load shedding for thread pool isolation and graceful degradation.
- Observability: Structured telemetry with distributed correlation IDs.
- Compliance: EU-certified object storage for strictly localized index backups.

## Rationale
- Decouples write-heavy transactional operations from read-heavy search traffic using an asynchronous event-driven pattern, protecting p99 performance.
- Enforces strict EU data residency constraints through localized cloud region provisioning and EU-certified object storage backups.