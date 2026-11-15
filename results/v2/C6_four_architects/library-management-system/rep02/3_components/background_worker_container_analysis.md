## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It utilizes a Python/Celery background worker container for asynchronous processing while enforcing strict EU-only data residency.

## Key Elements
- **Background Worker Container (Python/Celery)**: Core container hosting asynchronous processing logic.
- **Task Router (`Task Dispatcher`)**: Routes messages from the Event Broker.
- **Notification Processor**: Handles asynchronous dispatch of emails and push alerts.
- **Catalog Synchronization Engine**: Manages batch updates to search and database containers.
- **ILL & Registry Integrator**: Executes scheduled polling with external library systems.
- **Data Purge & Archival Worker**: Executes scheduled maintenance and lifecycle tasks.
- **Task Telemetry & DLQ Handler**: Manages failed jobs, Dead Letter Queues, and Prometheus metrics.

## Relationships
- **Core Services Container -> Task Router**: Dispatches async jobs [AMQP / Celery protocol via Apache Kafka EU-hosted].
- **Notification Processor -> SendGrid EU**: Dispatches notifications [HTTPS REST API].
- **Catalog Synchronization Engine -> OpenSearch & PostgreSQL EU**: Bulk indexing and state reconciliation [REST/Transport TCP and PostgreSQL wire protocol over TLS].
- **ILL & Registry Integrator -> National Library Registry & ILL Network**: Data synchronization [HTTPS].
- **Data Purge & Archival Worker -> Digital Asset Storage Container (MinIO/S3)**: Offloads expired media [S3 API over HTTPS].
- **Task Telemetry & DLQ Handler -> Redis Cache Container**: Persists retry states [Redis Protocol over TLS].

## Technology Stack
- **Python / Celery**: Core runtime and task queue framework for background processing.
- **Eventlet / Prefork**: Hybrid concurrency models for I/O-bound and CPU-bound workloads.
- **Apache Kafka EU-hosted**: Event broker for message transport.
- **Prometheus Python Client**: Observability and metrics collection.

## Rationale
This architecture efficiently separates heavy I/O and CPU-bound asynchronous workloads while guaranteeing strict EU data residency and robust error handling. The hybrid concurrency model maximizes resource utilization for scalable library operations.