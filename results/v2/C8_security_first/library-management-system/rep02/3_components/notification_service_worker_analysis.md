## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It uses a Notification Service Worker to process asynchronous alerts while strictly adhering to EU data residency constraints.

## Key Elements
- **Notification Service Worker (Python FastAPI)**: Container handling asynchronous notification processing.
- **RabbitMQ Message Consumer**: Internal component listening to the message broker over AMQP with TLS.
- **Notification Dispatcher Engine**: Internal component coordinating payload validation and routing.
- **Preference & Localization Filter**: Internal component verifying patron notification preferences, localization, and quiet-hours.
- **External API Client (Httpx)**: Internal component managing outbound HTTPS requests with circuit breakers and exponential backoff.
- **Dead-Letter Handler**: Internal component routing permanently failed messages to RabbitMQ DLQ.
- **External Notification Service**: External system receiving dispatched notifications.

## Relationships
- RabbitMQ Message Consumer -> Notification Dispatcher Engine: Internal function call [AMQP with TLS]
- Notification Dispatcher Engine -> Preference & Localization Filter: Internal async call
- Preference & Localization Filter -> External API Client: Internal payload passing
- External API Client -> External Notification Service: Sends messages [HTTPS (REST/JSON) with TLS 1.3 and mTLS]

## Technology Stack
- **Python FastAPI**: Core framework for the Notification Service Worker providing high-performance async processing.
- **RabbitMQ**: Message broker utilizing AMQP with TLS and dead-letter queues for reliable asynchronous messaging.
- **Httpx**: Python HTTP client configured with circuit breakers and exponential backoff for external API calls.
- **Kubernetes**: Deployment platform utilizing Horizontal Pod Autoscalers driven by RabbitMQ queue length metrics.
- **OpenTelemetry & Prometheus**: Observability stack for distributed tracing, structured JSON logging with PII masking, and metric tracking.

## Rationale
This architecture isolates asynchronous background processing behind a strict trust boundary to protect patron PII and meet EU-only data residency requirements. Internal component decomposition ensures high reliability, fault tolerance, and precise preference filtering for library patrons.