## Overview
The Notification Worker is an asynchronous background task processing container for the Library Management System, delivering reliable alerts to patrons and staff. It ensures EU data residency compliance, secure PII handling, and resilient message delivery.

## Key Elements
* Task Consumer Component (Celery Worker Core)
* Notification Dispatcher Component
* Delivery Audit Component
* RabbitMQ Message Broker
* PostgreSQL Database
* External Notification Services (Email/SMS gateways)

## Relationships
* Task Consumer -> RabbitMQ: Consumes background tasks [AMQP over TLS 1.3 with mTLS/SASL-SCRAM]
* Task Consumer -> Notification Dispatcher: Invokes processing logic [In-memory function call]
* Notification Dispatcher -> Delivery Audit: Persists delivery state [SQL over TLS]
* Delivery Audit -> PostgreSQL: Persists audit trails with least-privilege roles [SQL over TLS 1.3]
* Notification Dispatcher -> External Notification Services: Dispatches alerts [TLS 1.3 with certificate pinning]

## Technology Stack
* Python & Celery: Asynchronous background task processing and consumer management
* Pydantic: Strict schema validation and payload sanitization
* SQLAlchemy: Database ORM and client connectivity
* HashiCorp Vault: Secure injection of external provider API keys

## Rationale
This architecture isolates background notification processing to protect sensitive patron PII and maintain strict EU data residency compliance. Utilizing a dedicated worker with least-privilege database access and encrypted channels ensures high security and system reliability.