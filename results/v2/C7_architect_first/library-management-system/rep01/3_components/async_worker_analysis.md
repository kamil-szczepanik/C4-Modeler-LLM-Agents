## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The Async Worker container processes background tasks and external integrations while protecting user-facing search performance.

## Key Elements
- **Async Worker (Python / Celery)**: Background task processing container.
- **Task Dispatcher Receiver**: Consumes messages via AMQP.
- **Celery Task Router Component**: Validates AMQP signatures, enforces JSON serialization, and routes tasks.
- **DLQ Handler Component**: Captures failed tasks and sanitizes PII payloads.
- **Sync Orchestrator Component**: Manages National Library Database synchronization.
- **Notification Processor Component**: Handles multi-language patron alerts.
- **Notification Templates Component**: Manages localized messaging policies.
- **External Systems**: RabbitMQ, National Library Database, Telemetry Sidecar / OTEL Collector.

## Relationships
- Core Domain Service -> Task Dispatcher Receiver [AMQP over TLS with RabbitMQ]
- Task Dispatcher Receiver -> Celery Task Router Component [In-memory function call]
- Celery Task Router Component -> DLQ Handler Component [In-memory on failure]
- Sync Orchestrator Component -> National Library Database [HTTPS/REST with TLS 1.3]
- Async Worker -> Telemetry Sidecar / OTEL Collector [OpenTelemetry context propagation]

## Technology Stack
- **Python / Celery**: Core runtime for background task processing and ecosystem integration.
- **RabbitMQ**: Message broker utilizing AMQP, TLS, and SASL/SCRAM-SHA-512 authentication.
- **JSON Serialization**: Enforced for secure payload handling instead of `pickle`.
- **AES-256**: Encrypts temporary states and cached data in Celery backends for EU data residency.
- **OpenTelemetry**: Ensures end-to-end distributed tracing across asynchronous boundaries.

## Rationale
This architecture offloads heavy data synchronization and notification tasks from user-facing paths, guaranteeing the 99th-percentile search response time remains under 800 ms. It enforces strict EU data residency, security, and fault tolerance via robust error handling and rate-limiting.