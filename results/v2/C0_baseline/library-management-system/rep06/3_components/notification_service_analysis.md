## Overview
- Notification Service for the Library Management System handling asynchronous patron alerts via email and SMS.
- Ensures EU-only data residency, high deliverability, and strict adherence to patron privacy and accessibility standards.

## Key Elements
- Notification Consumer (Python/Celery Worker)
- Preference Manager (Python / FastAPI or Django)
- Dispatch Adapter (Sendinblue/Brevo EU API Client)
- Template Engine (Jinja2)
- Audit & Metrics Publisher (OpenTelemetry SDK)
- Redis (State Store & Deduplication Cache)
- Event Broker (Apache Kafka / AWS EventBridge EU)

## Relationships
- Event Broker -> Notification Consumer: Consumes notification events [Kafka/AMQP protocol]
- Notification Consumer -> Template Engine: Renders localized messages [Internal Function Call]
- Template Engine -> Dispatch Adapter: Sends formatted payload [Internal Function Call]
- Dispatch Adapter -> Sendinblue/Brevo EU: Sends outbound notifications [HTTPS API, TLS 1.3]
- Audit & Metrics Publisher -> OpenTelemetry Collector: Emits structured logs and traces [OTLP over gRPC]

## Technology Stack
- Python / Celery: Backend processing and asynchronous task orchestration for high throughput.
- Sendinblue/Brevo EU: External messaging provider ensuring strict EU-only data residency.
- Jinja2: Sandboxed template engine for localized, multi-language rendering and unsubscribe headers.
- Redis: Caching and idempotency tracking with encryption at rest for PII protection.
- OpenTelemetry SDK: Standardized telemetry for audit logging and delivery tracking.

## Rationale
- Decoupled asynchronous workers with KEDA autoscaling ensure reliable performance during bulk notification runs.
- Comprehensive security controls—including PII masking, TLS 1.3, and strict egress filtering—satisfy EU compliance and data protection mandates.