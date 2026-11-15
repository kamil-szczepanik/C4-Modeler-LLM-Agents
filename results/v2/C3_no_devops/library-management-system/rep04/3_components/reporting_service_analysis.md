## Overview
The Reporting Service is a container within the Library Management System that generates operational and administrative reports and analytics for library staff. It ensures high performance by using read replicas and local asynchronous workers while maintaining strict EU data residency.

## Key Elements
- **Reporting Service (Container):** Python/FastAPI application for report orchestration and generation.
- **Report Generator Component:** Handles on-demand requests and API endpoints via Python/FastAPI.
- **Export Worker Component:** Processes asynchronous export jobs using Python/Celery, Pandas, and ReportLab.
- **Scheduler Component:** Manages timezone-aware automated reports via APScheduler.
- **RabbitMQ:** Message broker for asynchronous task distribution.
- **PostgreSQL Read Replica:** Dedicated database for heavy analytics queries.
- **MinIO:** Sovereign, local S3-compatible object storage for temporary file staging.

## Relationships
- **Staff Dashboard -> Report Generator:** Requests on-demand reports and schedules via REST/JSON over mTLS.
- **Report Generator -> Export Worker:** Dispatches background export tasks via RabbitMQ using AMQP over TLS.
- **Export Worker -> PostgreSQL Read Replica:** Fetches large datasets for aggregation via SQL over mTLS.
- **Export Worker -> MinIO:** Persists generated CSV/PDF files temporarily via HTTPS over TLS.
- **Staff Dashboard -> MinIO:** Downloads generated reports securely via time-limited cryptographically signed HTTPS URLs.

## Technology Stack
- **Python / FastAPI:** Core framework for the Reporting Service API and report generation due to rapid development and async support.
- **Python/Celery & RabbitMQ:** Asynchronous task queue for offloading heavy file generation without blocking synchronous REST requests.
- **APScheduler:** Timezone-aware scheduling backend to support precise regional library closing times.
- **Pandas & ReportLab:** Libraries for rendering structured CSV and PDF exports.
- **MinIO:** On-premise, S3-compatible object storage ensuring strict EU-only data residency constraints.

## Rationale
This architecture decouples heavy analytics and file export workloads from core circulation services by utilizing an isolated reporting container, dedicated read replicas, and asynchronous workers. Security controls, local S3 storage, and strict encryption enforce EU data residency and privacy compliance.