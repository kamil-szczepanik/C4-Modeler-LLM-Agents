## Overview
[The Library Management System is a comprehensive digital and physical cataloguing, circulation, and self-service platform designed for public and academic libraries. Its core purpose is to provide resilient, high-performance item management and patron services while strictly enforcing EU data residency mandates.]

## Key Elements
- Self-Service Patrons & Library Staff (Primary Users)
- Frontend SPA (Web Application served via CDN)
- API Gateway (TLS termination and IAM token validation)
- Core Business Services (Decoupled microservices architecture for Catalogue, Circulation, and User Management domains)
- Search Engine Container (Elasticsearch/OpenSearch)
- Database Container (PostgreSQL)
- Async Event Broker Container (Apache Kafka or RabbitMQ)
- Shared Caching Container (Redis)
- File Storage Container (S3/HTTPS Compatible Storage)
- Background Worker Service & Configuration Service
- External Systems (IAM Provider, Notification Systems, Digital Content Providers, Audit/Logging, etc.)

## Relationships
- API Gateway -> Core Business Services: Routes validated requests [gRPC/REST]
- Core Business Services -> PostgreSQL: Reads and writes domain data using a Database-per-Service pattern [PostgreSQL protocol]
- Core Business Services -> Elasticsearch/OpenSearch: Queries search index [HTTP/REST]
- Core Business Services -> Apache Kafka/RabbitMQ: Publishes and consumes asynchronous events [AMQP/Kafka protocol]
- Core Business Services -> Redis: Retrieves and stores cached data and idempotency keys [Redis protocol]
- Core Business Services -> S3/HTTPS Storage: Uploads and retrieves files [S3/HTTPS]
- Core Business Services -> External Notification Systems: Sends notifications [SMTP/SMPP]
- Core Business Services -> Third-Party Digital Content Providers: Integrates digital content with circuit breakers [HTTPS/REST]

## Technology Stack
- OpenAPI/Protobuf: Enforces strict API contract governance between the API Gateway and microservices
- Elasticsearch/OpenSearch: Powers high-performance catalogue searching to meet the <800 ms 99th-percentile SLA
- PostgreSQL: Stores relational domain data utilizing a Database-per-Service pattern and expand-and-contract migrations
- Apache Kafka/RabbitMQ: Handles asynchronous event-driven communication across isolated domain boundaries
- Redis: Manages shared caching, session data, and transaction idempotency keys
- RFC 7807: Standardizes Problem Details error handling across all microservices
- Geo-Pinned Infrastructure & IaC Linters: Enforces container-level environment isolation and EU-only data residency

## Rationale
- Decoupled microservices with a Database-per-Service pattern and Redis caching ensure independent scaling to meet the strict 800ms search performance requirement.
- Circuit breakers, Idempotency Keys, and strict API governance guarantee high availability, transactional integrity, and data compliance within EU borders.