## Overview
The Library Management System provides physical and digital item cataloging, circulation management, and self-service portals. It employs a containerized architecture optimized for sub-800ms search performance and strict EU data residency compliance.

## Key Elements
- Library Patrons & Staff
- Web Application (SPA)
- API Gateway
- Core Domain Service
- Search Service
- Database
- Async Worker
- Telemetry Sidecar / OTEL Collector
- External Systems (Identity Provider, Payment Gateway, National Library Database, Centralized Observability Platform)

## Relationships
- SPA -> API Gateway (HTTPS/REST with TLS 1.3)
- API Gateway -> Core Domain & Search Services (gRPC over mTLS)
- Core Domain -> Database (TLS-encrypted TCP)
- Core Domain -> Async Worker (AMQP over TLS with RabbitMQ)
- Containers -> Centralized Observability Platform (via OTEL Collector)

## Technology Stack
- React: Powers the frontend SPA for fast patron and staff self-service.
- Nginx / Kong: Acts as API Gateway for ingress, rate-limiting, and JWT validation.
- Node.js / NestJS: Implements the Core Domain Service for circulation and catalog logic.
- Java / Elasticsearch: Powers the dedicated Search Service to guarantee sub-800ms query performance.
- PostgreSQL: Stores transactional data with multi-AZ replication in the EU.
- Python / Celery: Manages asynchronous background tasks and external integrations.

## Rationale
The micro-services design isolates heavy search queries to meet strict performance requirements while ensuring all data and processing remain strictly within the EU. Robust security, encryption, and operational resilience protect patron privacy and maintain high availability.