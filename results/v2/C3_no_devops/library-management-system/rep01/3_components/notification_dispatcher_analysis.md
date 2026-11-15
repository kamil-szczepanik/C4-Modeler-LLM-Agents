## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. Its Notification Dispatcher container handles asynchronous, multi-channel alerting for patrons while enforcing strict EU data residency and GDPR compliance.

## Key Elements
* **Notification Dispatcher Container**: Python/Celery worker managing asynchronous alerts.
* **Consumer Component**: Python/Celery worker processing raw events.
* **Routing & Preference Engine**: Python component selecting delivery channels (Email, SMS, Push).
* **Template Renderer**: Jinja2 component merging localized templates and sanitizing PII.
* **Channel Adapters**: Python/Requests components communicating with external services.
* **Message Broker**: RabbitMQ / AWS SQS supplying event payloads.
* **External Notification Service**: Third-party gateway delivering external notifications.
* **PostgreSQL State Store**: Database tracking notification state with AES-256 encryption.

## Relationships
* **Consumer Component -> Message Broker**: Consumes raw event payloads [AMQP].
* **Consumer Component -> Message Broker**: Validates HMAC authentication tokens [AMQP].
* **Channel Adapters -> External Notification Service**: Sends rendered payloads and receives delivery receipts [Outbound HTTPS via TLS 1.3/mTLS].
* **Routing & Preference Engine -> PostgreSQL State Store**: Tracks notification states and delivery attempts [SQL].

## Technology Stack
* **Python & Celery**: Selected for robust asynchronous task execution and native retry decorators.
* **Jinja2**: Chosen for flexible, localized notification templating.
* **PostgreSQL**: Used for state tracking, mandated by EU data residency and AES-256 encryption-at-rest constraints.
* **RabbitMQ / AWS SQS**: Deployed for decoupled, reliable message brokering via AMQP.
* **TLS 1.3 & mTLS**: Enforced for secure, encrypted outbound communication.

## Rationale
This architecture fits requirements by decoupling resource-intensive alerting tasks via a Python/Celery worker to maintain optimal system performance. It strictly enforces EU data residency and GDPR constraints through proactive PII sanitization and AES-256 encrypted state storage.