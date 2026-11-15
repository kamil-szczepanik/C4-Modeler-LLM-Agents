## Overview
A scalable Node.js notification worker container processes asynchronous library events and handles external communication retries. It guarantees EU-only data residency and reliable messaging through native dead-letter queues and persistent audit storage.

## Key Elements
* **Notification Worker Container**: Node.js container for asynchronous message processing.
* **Event Consumer Component**: Consumes messages securely using `amqplib`.
* **Retry & Circuit Breaker Component**: Manages transient failures using Opossum logic with exponential backoff.
* **DLQ Producer & Native Exchanges**: Handles permanently failed messages for administrative visibility.
* **Notification History Store Component**: EU-hosted managed PostgreSQL instance for audit trails and delivery states.
* **Preference Cache Component**: Replicated Redis cluster caching patron communication preferences.
* **Telemetry Logger Component**: Ships structured logs via OpenTelemetry SDK.

## Relationships
* **Event Consumer -> RabbitMQ**: Consumes async events [AMQP over TLS].
* **Retry & Circuit Breaker -> Notification Service**: Calls external provider for delivery [HTTPS].
* **DLQ Producer -> RabbitMQ DLQ**: Routes failed messages for administrative monitoring.
* **Telemetry Logger -> Centralized Observability Platform**: Ships metrics and logs [gRPC].
* **Notification Worker -> PostgreSQL**: Persists audit logs and history [TCP/TLS].
* **Notification Worker -> Redis**: Queries communication preferences [Redis Protocol/TLS].

## Technology Stack
* **Node.js**: Runtime environment for the stateless notification worker.
* **`amqplib`**: Library for secure message consumption from RabbitMQ.
* **Opossum**: Circuit breaker implementation for resilient external API calls.
* **OpenTelemetry SDK**: Standardized instrumentation for telemetry and log shipping.
* **PostgreSQL (EU-Hosted Managed)**: Durable storage for compliance, history, and audit logs.
* **Redis (Replicated Cluster)**: Low-latency caching for patron communication preferences.
* **Kubernetes HPA**: Orchestrates horizontal scalability based on RabbitMQ queue metrics.

## Rationale
This architecture ensures robust asynchronous message delivery and high availability through resilient circuit-breaking, automated scaling, and native dead-letter handling. It strictly enforces EU-only data residency via compliant managed storage and localized caching.