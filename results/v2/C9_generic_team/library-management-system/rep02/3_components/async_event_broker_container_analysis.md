## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue items, manage circulation, and provide self-service portals within EU data residency constraints.

## Key Elements
- Self-Service Patrons & Library Staff (Users)
- Web Application (Frontend SPA served via CDN)
- API Gateway (with TLS termination and IAM token validation)
- Core Business Services (Decoupled microservices architecture)
- Search Engine Container (Elasticsearch/OpenSearch)
- Database Container (PostgreSQL)
- Async Event Broker Container (Apache Kafka or RabbitMQ)
- Shared Caching Container (Redis)
- File Storage Container (S3/HTTPS Compatible Storage)
- External Systems (IAM Provider, Centralized Audit and Logging System, External Notification Systems)

## Relationships
- Self-Service Patrons & Library Staff -> Web Application: Accesses features via HTTPS
- Web Application -> API Gateway: Routes requests via HTTPS/REST
- API Gateway -> Core Business Services: Forwards validated requests via gRPC/REST
- Core Business Services -> Database Container: Persists operational data via PostgreSQL protocol
- Core Business Services -> Search Engine Container: Queries catalogue and items via HTTP/REST
- Core Business Services -> Async Event Broker Container: Publishes and consumes asynchronous events via AMQP/Kafka protocol
- Core Business Services -> File Storage Container: Uploads and retrieves digital assets via S3 protocol using Claim Check pattern

## Technology Stack
- Apache Kafka or RabbitMQ: Powers the Async Event Broker Container with Avro/JSON Schema governance and IAM-backed ACLs.
- PostgreSQL: Manages transactional data and consumer idempotency deduplication tables.
- Elasticsearch/OpenSearch: Powers high-performance catalogue search with sub-800ms latency.
- Redis: Provides shared caching and local fallback event spooling.
- S3/HTTPS Compatible Storage: Stores large digital assets via the Claim Check pattern.

## Rationale
This architecture uses decoupled microservices and asynchronous event streaming to guarantee performance, scalability, and strict EU-only data residency. Robust resiliency patterns like consumer idempotency, circuit breakers, and Claim Check patterns ensure high availability for critical library operations.