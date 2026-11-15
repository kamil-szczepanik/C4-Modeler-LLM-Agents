## Overview
The Library Management System provides cataloging, circulation, and self-service portal capabilities for public and academic libraries. It ensures strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Self-Service Patrons and Library Staff (Users)
- Web Application (Frontend SPA served via CDN)
- API Gateway (TLS termination and IAM token validation)
- Core Business Services (Decoupled microservices architecture)
- Search Engine Container (Elasticsearch/OpenSearch)
- Database Container (PostgreSQL)
- Async Event Broker Container (Apache Kafka or RabbitMQ)
- Shared Caching Container (Redis)
- File Storage Container (S3/HTTPS Compatible Storage)
- Worker / Background Job Processing Container (Background Worker Service)
- Configuration Management Container/Service (Configuration Service)

## Relationships
- Web Application -> API Gateway: HTTPS requests
- API Gateway -> Core Business Services: gRPC/REST APIs
- Core Business Services -> Database Container: SQL queries via JDBC/ORM
- Core Business Services -> Search Engine Container: Search queries [HTTP/REST]
- Core Business Services -> Shared Caching Container: Cache read/write [RESP]
- Core Business Services -> File Storage Container: Uploads and retrieves files via pre-signed URLs [S3/HTTPS]
- Core Business Services -> Async Event Broker Container: Publishes domain events [AMQP/Kafka Protocol]
- Worker / Background Job Processing Container -> Async Event Broker Container: Consumes asynchronous tasks [AMQP/Kafka Protocol]

## Technology Stack
- S3/HTTPS Compatible Storage: File Storage Container ensuring secure asset persistence and EU data residency
- PostgreSQL: Primary relational database for transactional consistency
- Elasticsearch/OpenSearch: High-performance search index ensuring sub-800ms response times
- Apache Kafka or RabbitMQ: Asynchronous event broker for background processing pipelines
- Redis: Shared caching for session management and performance optimization

## Rationale
The decoupled microservices architecture with specialized data stores ensures high scalability, meeting the sub-800ms search performance requirement. Strict cloud configuration and S3-compatible storage policies successfully enforce the EU-only data residency constraint.