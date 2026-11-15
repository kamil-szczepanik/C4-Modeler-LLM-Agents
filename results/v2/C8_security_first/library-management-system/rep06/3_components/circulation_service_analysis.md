## Overview
The Circulation Service is a high-throughput microservice managing library loans, renewals, and returns within the Library Management System. It ensures zero-downtime transactions and strict EU data residency compliance.

## Key Elements
- **Loan API Controller**: REST/gRPC endpoints validating incoming JWTs from the API Gateway and enforcing RBAC.
- **Loan Domain Engine**: Core business logic handling checkouts, renewals, returns, and grace periods.
- **Circulation Repository & Outbox Store**: Data access layer managing transactional state and reliable event publishing.
- **Event Publisher/Subscriber**: Asynchronous message handler interfacing with the message broker.
- **PostgreSQL Database**: Persistent transactional store utilizing read replicas.
- **HashiCorp Vault**: Dynamic secrets and encryption key manager.

## Relationships
- **API Gateway -> Loan API Controller**: Forwards authenticated requests via JWT/OAuth 2.0.
- **Loan Domain Engine -> Circulation Repository**: Executes transactional reads/writes.
- **Circulation Repository -> PostgreSQL Database**: Persists data securely via TLS 1.3 and mTLS.
- **Event Publisher -> Message Broker**: Publishes domain events using AMQP with the Outbox Pattern.
- **Circulation Service -> HashiCorp Vault**: Fetches dynamic secrets via Kubernetes Service Account token exchange.

## Technology Stack
- **Go (Golang)**: Chosen for high throughput, concurrency model, and low memory footprint.
- **pgx Driver**: PostgreSQL driver enforcing TLS 1.3, connection pooling, and resilient data access.
- **Kubernetes**: Container orchestration platform for horizontal scaling, probes, and resource governance.
- **OpenTelemetry & Prometheus**: Observability stacks for distributed tracing, metrics, and outbox lag monitoring.

## Rationale
Decomposing the Circulation Service into strict internal components using Go guarantees high-performance self-service availability. The Outbox Pattern and decoupled event publishing ensure transactional resilience during peak workloads while maintaining EU compliance.