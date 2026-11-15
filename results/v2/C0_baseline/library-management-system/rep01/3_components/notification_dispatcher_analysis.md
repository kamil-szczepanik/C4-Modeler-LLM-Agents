## Overview
[The Notification Dispatcher is an asynchronous message distribution container within the Library Management System responsible for routing, rendering, and delivering multi-channel alerts to patrons and operational notifications to librarians while maintaining strict GDPR compliance.]

## Key Elements
- Ingress Controller (Python, FastAPI)
- Preference & Policy Engine (Python)
- Template Renderer (Jinja2)
- Dispatch Worker (Celery, Python)
- Message Broker (RabbitMQ / Kafka)
- External Systems: Notification Service, Audit Logging Container, HashiCorp Vault

## Relationships
- API Gateway -> Ingress Controller: Routes notification tasks [gRPC over mTLS]
- Ingress Controller -> Preference & Policy Engine: Passes validated tasks [Internal Async]
- Dispatch Worker -> Notification Service: Forwards formatted alerts [TLS-secured AMQP]
- Dispatch Worker -> Audit Logging Container: Forwards unrecoverable DLQ failures [Async via RabbitMQ]
- Dispatch Worker -> HashiCorp Vault: Retrieves API keys and mTLS certificates [REST/HTTPS]

## Technology Stack
- Python / FastAPI: High-performance async framework for API ingestion
- Pydantic: Strict schema validation for transient payloads and payload minimization
- Jinja2: Localized message rendering with auto-escaping enabled for SSTI prevention
- Celery: Background task management for resilient, retry-enabled message delivery
- RabbitMQ/Kafka: Message broker featuring Dead Letter Queues (DLQ) and queue-depth HPA metrics
- HashiCorp Vault: Secure, dynamic retrieval of external service credentials

## Rationale
- Asynchronous queuing and token-bucket rate limiting prevent system lag and protect against upstream throttling during bulk operational notices.
- Zero persistent PII storage and embedded preference evaluation satisfy EU data residency and strict GDPR privacy constraints.