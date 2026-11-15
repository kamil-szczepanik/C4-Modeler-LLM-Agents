## Overview
The Library Management System is a public and academic platform for cataloging items, managing circulation, and offering self-service portals. This architecture defines the component-level design of the Async Worker Container.

## Key Elements
* Task Router / Consumer (Celery Worker)
* Notification Processor
* Report & Batch Processor
* Data Purge & Compliance Worker
* Integration Sync Worker
* Message Broker (Managed RabbitMQ)
* Database (PostgreSQL Managed RDS EU-Central)
* File Storage Container (AWS S3 EU-Central)

## Relationships
* Task Router -> Message Broker: Consumes jobs [AMQP/TLS]
* Task Router -> Database: Persists job state and updates statuses [PostgreSQL/JDBC, EU-Central]
* Notification Processor -> Stripe EU: Triggers background payments and renewals [HTTPS/REST, TLS 1.3]
* Report & Batch Processor -> Database: Executes heavy analytical queries [PostgreSQL/JDBC, EU-Central]
* Report & Batch Processor -> File Storage Container: Uploads generated reports [HTTPS/REST, TLS 1.3]
* Data Purge & Compliance Worker -> Database: Executes GDPR data anonymisation [PostgreSQL/JDBC, EU-Central]
* Integration Sync Worker -> University SIS: Fetches student/faculty updates [HTTPS/REST, TLS 1.3]

## Technology Stack
* Python 3.11: Primary language for background task execution
* Celery: Distributed task queue framework
* Redis: Broker and result backend for Celery
* SQLAlchemy with asyncpg: Non-blocking ORM and PostgreSQL driver
* Alpine Docker: Hardened container base image for EU data residency compliance

## Rationale
The Python 3.11 and Celery stack with non-blocking `asyncpg` efficiently handles I/O-bound background tasks without blocking core APIs. Five dedicated components ensure robust third-party synchronization, reporting, and GDPR compliance while strictly enforcing EU-only data residency.