## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It guarantees EU-only data residency and sub-800ms search performance.

## Key Elements
* Web Application (SPA): React/TypeScript served via CDN
* API Gateway: Nginx / Kong
* Core Services API: Node.js/NestJS
* Search Engine: Elasticsearch / OpenSearch
* Relational Database: PostgreSQL
* Async Worker: Python/Celery
* Analytics Event Collector & Datastore: Kafka/Fluentd and ClickHouse/TimescaleDB
* External Systems: Payment Gateway, DRM Provider, Notification Service

## Relationships
* Web App -> API Gateway (HTTPS / JSON)
* API Gateway -> Core Services API (gRPC / mTLS)
* Core Services API -> Relational Database (TCP / PostgreSQL protocol)
* Core Services API -> Search Engine (HTTP / REST)
* Core Services API -> Async Worker (Redis / Message Broker)
* API Gateway -> Analytics Event Collector (HTTP / TLS 1.3)
* Analytics Event Collector -> Analytics Datastore (TCP)

## Technology Stack
* React/TypeScript: Client-side UI and administrative reporting
* Nginx / Kong: Reverse proxy, TLS termination, OAuth 2.0 / OIDC JWT validation
* Node.js/NestJS: Business logic and role-based access control (RBAC)
* PostgreSQL: Primary EU-hosted datastore with CMK encryption at rest
* Elasticsearch / OpenSearch: Dedicated search container for <800ms NFR
* Python/Celery & Redis: Asynchronous background jobs
* ClickHouse / TimescaleDB: EU-hosted telemetry and usage analytics datastore

## Rationale
The microservices-based container architecture isolates high-impact analytical and search workloads from core circulation transactions to meet performance SLAs. Strict EU data residency controls, encryption, and PII pseudonymization ensure full compliance with regional regulations.