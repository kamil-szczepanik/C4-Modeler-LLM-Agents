## Overview
The Library Management System is a comprehensive digital solution designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture prioritizes strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Library Patron and Librarian / Staff (Users)
- Web Application Container (React/TypeScript via Nginx)
- API Gateway Container (Kong/Envoy)
- Core Services Container (Java/Spring Boot)
- Search Service Container (Elasticsearch/OpenSearch)
- Database Container (PostgreSQL EU region)
- Redis Cache Container
- Background Worker Container (Python/Celery)
- Event Broker Container (Apache Kafka EU-hosted)
- Digital Asset Storage Container (MinIO / S3-compatible Object Storage, EU-hosted)
- External Systems: Stripe EU, SendGrid EU, EU Identity Provider, National Library Registry, Interlibrary Loan Network

## Relationships
- Web App to API Gateway: HTTPS/REST and WebSockets
- API Gateway to internal containers: gRPC for low-latency communication
- Core Services to Search Service: Apache Kafka TCP protocol over TLS (event-driven index updates)
- Core Services to PostgreSQL: SQL over TCP (EU-bound)
- Core Services to Redis Cache: RESP over TCP
- Core Services to Event Broker: Kafka Protocol over TLS
- Core Services to Background Worker: AMQP via RabbitMQ
- Core Services to Digital Asset Storage: HTTPS/REST (S3 API) with pre-signed URLs
- External integrations (Stripe EU, SendGrid EU, EU IdP, National Library Registry, ILL): HTTPS/REST

## Technology Stack
- React/TypeScript & Nginx: Frontend Single Page Application
- Kong/Envoy: Edge routing, SSL termination, and JWT auth validation
- Java/Spring Boot: Core business logic container for cataloguing and circulation
- OpenSearch: Dedicated search index ensuring R-05 sub-800ms performance
- PostgreSQL: Primary transactional store with strict EU data residency enforcement
- Redis: In-memory cache for catalogue metadata acceleration
- Apache Kafka: Event streaming platform with TLS for decoupled, asynchronous messaging
- MinIO / S3-compatible Object Storage: EU-hosted binary storage for digital assets (PDFs, e-books)

## Rationale
This container architecture uses dedicated search and caching services to reliably achieve the 99th-percentile search response time under 800ms. Furthermore, it strictly enforces EU-only data residency constraints across all primary databases, event brokers, and object storage containers.