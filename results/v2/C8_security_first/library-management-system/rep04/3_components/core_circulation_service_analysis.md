## Overview
[Core Circulation Service component of the Library Management System handling catalogue circulation, policy evaluation, and self-service portals.]

## Key Elements
- Circulation API Controller (Go)
- Transaction Manager (Go)
- Loan & Policy Engine (Go)
- Event Publisher Component (Go)
- PostgreSQL (Primary & Read-Replicas, AES-256 encrypted via EU Cloud HSM)
- Message Broker (Apache Kafka / RabbitMQ)

## Relationships
- API Gateway -> Circulation API Controller: Routes circulation requests [Internal mTLS and gRPC]
- Circulation API Controller -> Transaction Manager & Loan & Policy Engine: Internal function calls [Go interfaces]
- Transaction Manager -> PostgreSQL (Primary): Persists circulation states [SQL over TLS 1.3]
- Loan & Policy Engine -> PostgreSQL (Read-Replicas): Queries loan rules [SQL over TLS 1.3]
- Transaction Manager -> Event Publisher: Internal handoff [Go channels / interfaces]
- Event Publisher -> Message Broker: Publishes circulation events [AMQP / gRPC over TLS 1.3]

## Technology Stack
- Go: Selected for low memory footprints, fast execution (<50ms internal latency), and concurrency
- PostgreSQL: Provides ACID guarantees and read-replicas for scalable, stateless policy evaluations
- Protocol Buffers: Enforces strict schema validation at the API boundary
- OpenTelemetry: Captures distributed traces and RED metrics for SLA enforcement (<800ms search/response)

## Rationale
[Decomposing the service into Go-based components with explicit database separation ensures high-throughput patron self-service. Strict security controls, stateless read scaling, and asynchronous event publishing maintain EU data residency, zero-downtime reliability, and business policy flexibility.]