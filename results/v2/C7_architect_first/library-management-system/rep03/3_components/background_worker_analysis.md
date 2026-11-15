## Overview
The Library Management System background worker container processes asynchronous tasks, handles out-of-band communications, and synchronizes catalogue metadata. It ensures operational reliability, security, and EU data residency compliance.

## Key Elements
- Task Consumer (Celery Worker Core)
- Notification Dispatcher
- Data Sync Processor
- Task Router & DLQ Handler

## Relationships
- Task Consumer -> Asynchronous Broker (Redis): Consumes tasks via AMQP/Redis [TLS, mTLS]
- Notification Dispatcher -> Notification System: Sends alerts via REST/HTTPS
- Data Sync Processor -> National Library Registry: Syncs metadata via REST/HTTPS [TLS 1.3]
- Background Worker -> Database (PostgreSQL): Reads/writes job states via SQLAlchemy [TLS 1.3, PgBouncer]

## Technology Stack
- Python 5.x / Celery 5.x: Core background task processing framework
- Redis: Asynchronous message broker with TLS and AUTH enforcement
- PostgreSQL: Persistent storage for job states, audit logs, and patron preferences
- HashiCorp Vault: Secure run-time secret management for API credentials
- Prometheus / OpenTelemetry: Metrics monitoring, queue length tracking, and distributed tracing

## Rationale
Separating notification and data synchronization queues prevents task starvation while isolating long-running jobs. Strict data sanitization, encrypted storage, and regional broker deployment ensure EU-only data residency and patron privacy compliance.