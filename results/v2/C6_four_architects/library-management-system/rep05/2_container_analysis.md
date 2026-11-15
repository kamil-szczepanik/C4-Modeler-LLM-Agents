## Overview
The Library Management System provides a public and academic portal for cataloguing physical and digital items, managing circulation, and offering self-service features. It utilizes a decoupled container architecture strictly pinned to the `eu-central-1` region to satisfy EU data residency and performance constraints.

## Key Elements
- Library Patrons and Staff (Users)
- Web Application (SPA) (React/TypeScript)
- API Gateway (Nginx / Envoy)
- Core Services Container (Spring Boot / Java)
- Search Container (Elasticsearch Cluster)
- Integration Service (Node.js / Python)
- Async Worker Container (Python / Celery or Java / Spring Batch)
- Message Broker (Managed RabbitMQ)
- Database (PostgreSQL Managed RDS)
- Cache / Session Store (Managed AWS Redis)
- File Storage Container (AWS S3 EU-Central)

## Relationships
- Patrons/Staff to Web Application: HTTPS via browser
- Web Application to API Gateway: HTTPS/REST
- API Gateway to Core & Search Containers: gRPC / internal REST
- API Gateway & Core Services to Redis Container: RESP over TLS
- Core Services to PostgreSQL: JDBC over TLS
- Core Services to Message Broker: AMQP/TLS
- Message Broker to Async Worker Container: AMQP/TLS
- Integration Service & Async Worker to AWS S3 & Stripe EU: HTTPS/REST
- PostgreSQL to Search Container: Debezium CDC via internal TCP/TLS

## Technology Stack
- React/TypeScript: Powers the frontend SPA hosted on an EU-Central CDN
- Spring Boot (Java): Provides scalable business logic for core catalogue and circulation
- Elasticsearch: Optimizes indexing and queries to meet the < 800ms 99th-percentile search SLA
- PostgreSQL (Managed RDS): Ensures transactional consistency for core records
- Managed RabbitMQ: Enables decoupled asynchronous event handling and webhooks
- Redis (AWS ElastiCache): Delivers sub-millisecond session validation and hot caching
- AWS S3 EU-Central: Secures digital assets and documents within the EU boundary

## Rationale
This containerized architecture decouples synchronous user requests from heavy background processing, protecting the system against cascading failures from external integrations like Stripe and SIS. Strict isolation of read models, caching layers, and region-locked managed services guarantees compliance with EU data residency while easily achieving the sub-800ms search performance requirement.