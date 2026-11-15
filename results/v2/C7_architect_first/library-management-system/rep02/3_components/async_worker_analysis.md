## Overview
The Async Worker system manages background processing, search indexing, and third-party integrations for the Library Management System. It ensures asynchronous reliability and performance compliance under EU data residency constraints.

## Key Elements
* Task Consumer / Router (Python/Celery)
* Notification Dispatcher
* Index Synchronizer
* Integration Sync Engine
* Redis (Message Broker / Cluster with AOF+RDB)
* Relational Database (PostgreSQL with PgBouncer)
* Search Engine (OpenSearch)
* External Notification Service
* Digital Content Provider / DRM
* External Payment Gateway
* HashiCorp Vault

## Relationships
* Core Services API -> Task Consumer: Enqueues jobs [Redis, AMQP, TLS, mTLS]
* Notification Dispatcher -> External Notification Service: Sends alerts [HTTPS/REST]
* Index Synchronizer -> Search Engine: Updates search index [HTTP/REST]
* Integration Sync Engine -> Relational Database: Updates transaction/sync states [SQL/PostgreSQL, connection pooling]
* Integration Sync Engine -> HashiCorp Vault: Fetches API keys securely [HTTPS/REST]

## Technology Stack
* Python / Celery: Chosen for robust background task processing and ecosystem support
* Redis: Used as message broker with persistence (AOF+RDB) and TLS enabled
* PostgreSQL: Relational datastore utilizing PgBouncer for connection pooling
* OpenSearch: Search engine meeting sub-800ms search SLA via outbox pattern
* Prometheus & KEDA: Used for worker auto-scaling and queue depth monitoring
* OpenTelemetry: Provides structured JSON logging and distributed tracing

## Rationale
This architecture decouples heavy background tasks from core APIs to maintain sub-800ms search performance while guaranteeing EU data residency and idempotency. Strict PII sanitization and workload segregation protect patron privacy and ensure reliable notification delivery.