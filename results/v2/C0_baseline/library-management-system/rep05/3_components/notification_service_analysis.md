## Overview
[The Notification Service is an asynchronous microservice responsible for multi-channel patron communications while strictly adhering to EU data residency and GDPR privacy regulations.]

## Key Elements
- Notification Service (Python FastAPI Container)
- Event Consumer Component (Background tasks)
- Template Engine Component (Jinja2)
- Dispatcher Component
- Channel Adapters Component
- Preference Cache Component (Redis)
- Status Tracker Component
- Internal API Component
- External Notification Gateway
- Event Bus (Apache Kafka / RabbitMQ)

## Relationships
- Event Bus -> Event Consumer: Consumes domain events [AMQP / Kafka]
- Channel Adapters -> External Notification Gateway: Delivers messages [REST / SMTP / HTTPS]
- External Notification Gateway -> Status Tracker: Sends delivery webhooks [HTTPS]
- Web Application -> Internal API: Retrieves notification logs [HTTP / JSON with JWT]
- Event Bus -> Preference Cache: Syncs user preferences [AMQP / Kafka]

## Technology Stack
- Python FastAPI: High speed and asynchronous capability for real-time dispatching
- Jinja2: Localized template rendering within EU cloud boundary
- Redis: Read-optimized preference caching with AOF persistence
- Apache Kafka: Reliable message transport with Dead-Letter Queues (DLQ)
- OpenTelemetry / Prometheus: Distributed tracing and metric exporting

## Rationale
[Asynchronous event consumption with local Redis caching guarantees low-latency notification delivery without violating microservice domain boundaries. Strict cryptographic controls, PII log scrubbing, and DLQ mechanisms ensure enterprise-grade security, operational resilience, and full EU data residency compliance.]