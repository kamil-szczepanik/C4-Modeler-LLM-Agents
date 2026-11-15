## Overview
The Async Worker Container processes background circulation tasks, asynchronous inventory updates, and patron notifications for the Library Management System. It operates in an isolated private subnet to ensure secure, event-driven processing while maintaining strict EU data residency compliance.

## Key Elements
- Task Dispatcher / Consumer (Python, Celery with Redis/RabbitMQ client)
- Notification Handler Component (Python)
- Circulation Processor Component (Python)
- DLQ Publisher Component (Python, Celery retry hooks)
- Message Broker (RabbitMQ / Redis)
- Centralized Log & Metrics Aggregator (Prometheus, OpenTelemetry)

## Relationships
- Core Services Container -> Message Broker: Publishes asynchronous circulation and notification events [AMQP, mTLS]
- Task Dispatcher -> Notification Handler / Circulation Processor: Routes tasks internally [In-memory]
- Notification Handler -> EU Notification Service: Dispatches alerts and reminders [HTTPS]
- Circulation Processor -> Database Container: Manages background loan and inventory states [TCP/Postgres, PgBouncer]
- DLQ Publisher -> Core Services Container (via Message Broker): Emits failure events for librarian review [AMQP]

## Technology Stack
- Python / Celery: Chosen for robust asynchronous task queue management and background worker execution.
- RabbitMQ / Redis: Selected as the message broker for reliable event publishing and consumer queue management.
- PgBouncer: Implemented for database connection pooling to prevent connection exhaustion during peak loads.
- Prometheus / OpenTelemetry: Deployed for distributed tracing, task execution latency tracking, and metric aggregation.

## Rationale
This architecture ensures high performance and strict security by isolating asynchronous workloads, utilizing queue-depth autoscaling, and enforcing PII sanitization. It guarantees reliable non-blocking event processing while meeting EU data residency constraints.