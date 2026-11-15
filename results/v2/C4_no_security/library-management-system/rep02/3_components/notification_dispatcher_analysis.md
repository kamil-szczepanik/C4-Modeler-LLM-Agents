## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Notification Dispatcher container handles asynchronous, localized patron alerts and compliance logging.

## Key Elements
- Notification Dispatcher Container (Python / FastAPI)
- Kafka Event Consumer Component
- Preference Cache Component (Redis)
- Template Engine Component (Jinja2)
- Provider Adapter Component (HTTPX / SMTP Client)
- Audit Emitter Component
- External Systems: Apache Kafka, EU Notification Service, EU-Resident Log & Audit Sink, Observability Stack

## Relationships
- Kafka Event Consumer -> Preference Cache: Queries user settings [Redis Protocol / TLS]
- Preference Cache -> Template Engine: Supplies localization context [In-Process]
- Template Engine -> Provider Adapter: Forwards rendered payload [In-Process]
- Provider Adapter -> EU Notification Service: Delivers message [SMTP/HTTPS over TLS]
- Provider Adapter -> Audit Emitter: Logs delivery status [In-Process]
- Audit Emitter -> EU-Resident Log & Audit Sink: Forwards delivery events [HTTPS/TLS]
- Kafka Event Consumer -> Observability Stack: Traces propagation [OpenTelemetry]

## Technology Stack
- Python / FastAPI: High-throughput framework supporting asynchronous processing
- Apache Kafka: Asynchronous message broker preventing UI blocking
- Redis: Low-latency in-memory cache with persistence for user preferences
- Jinja2: Dynamic multi-language template rendering engine
- OpenTelemetry, Prometheus, Grafana: End-to-end distributed tracing and metric alerts
- Kubernetes / KEDA: Autoscaling tied to Kafka consumer lag

## Rationale
This architecture ensures high-throughput asynchronous processing to meet performance SLAs while maintaining strict EU-only data residency. It decouples core services from notification delivery using resilient patterns and reliable audit logging.