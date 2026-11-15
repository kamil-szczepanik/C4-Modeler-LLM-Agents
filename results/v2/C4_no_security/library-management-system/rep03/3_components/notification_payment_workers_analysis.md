## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU-only data residency constraints. It ensures resilient, asynchronous processing of financial transactions and notifications.

## Key Elements
* Library Patrons (Members), Librarians, Library Administrators
* Web Application (SPA) (React, TypeScript on EU CDN) & API Gateway (Nginx/Kong)
* Catalogue & Search Container (Elasticsearch, Java/Spring Boot)
* Circulation & Core Container (Node.js/Express)
* Notification & Payment Workers (Python/Celery) containing:
  - Payment Task Handler (Python/Celery + SQLAlchemy)
  - Notification Dispatcher (Python/Celery)
  - Queue Consumer & Router (Celery/RabbitMQ)
  - Audit & Ledger Component (Python/SQLAlchemy)
* External Systems: Payment Gateway, Notification Service, Digital Content Providers, Identity Provider (IdP)
* Infrastructure: PostgreSQL Database, RabbitMQ Message Broker

## Relationships
* Notification & Payment Workers -> Payment Gateway: Payment processing [HTTPS]
* Notification & Payment Workers -> Notification Service: Notification delivery [HTTPS]
* Queue Consumer & Router -> RabbitMQ Message Broker: Consumes messages with DLQ routing [AMQP]
* Payment Task Handler -> Notification Dispatcher: Internal failure event emission [AMQP]
* Payment Task Handler & Audit & Ledger -> PostgreSQL Database: Persists state and immutable logs [SQL]

## Technology Stack
* Python/Celery: Asynchronous background processing for non-blocking workflows
* RabbitMQ Message Broker: Queue management, DLQ routing, and queue-depth autoscaling
* PostgreSQL Database & SQLAlchemy: Relational storage and EU-resident audit logging
* Prometheus & OpenTelemetry: Real-time observability and 15-minute retry SLA monitoring
* Nginx/Kong & React: Secure entry points and EU-hosted frontend delivery

## Rationale
Asynchronous workers with idempotency and DLQs ensure 99.5% notification success and rapid fine-processing without UI latency. Strict EU-resident PostgreSQL storage and localized logging guarantee regulatory compliance and secure audit trails for administrators.