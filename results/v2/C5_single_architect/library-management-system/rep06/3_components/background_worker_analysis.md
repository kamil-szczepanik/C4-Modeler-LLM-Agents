## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Background Worker container processes asynchronous tasks while maintaining EU-only data residency and supporting high-performance search SLAs.

## Key Elements
* Task Dispatcher / Consumer (Celery Worker Core)
* Notification Task Handler
* Payment Processor Worker
* Content Sync Worker
* Data Maintenance Worker
* Database Maintenance & Analytics Worker
* Redis (Celery task state and result backend)

## Relationships
* Async Event Broker (Apache Kafka) -> Task Dispatcher / Consumer (Secure TCP with TLS)
* Notification Task Handler -> Notification Provider (HTTPS)
* Payment Processor Worker -> Payment Gateway (HTTPS)
* Content Sync Worker -> Digital Content Provider (HTTPS)
* Data Maintenance Worker -> Search Service (Internal API / Database queries)
* Background Worker components -> PostgreSQL (Database)

## Technology Stack
* Python and Celery: Core framework for asynchronous background processing
* Redis: Task broker and state management with strict persistence for EU data residency
* Apache Kafka: Asynchronous event ingestion via secure TCP with TLS
* PostgreSQL: Primary persistent data store

## Rationale
Decomposing the Background Worker into specialized components isolates failure domains and protects core system performance. This architecture ensures strict adherence to EU data residency while meeting demanding search and processing response SLAs.