## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for academic and public libraries. It uses an event-driven microservices architecture hosted strictly within the EU.

## Key Elements
- Users: Patron, Librarian / Staff
- External Systems: Authentication Provider, External Payment Gateway, National Library Registry, Notification Service
- Containers: Web App (React/TypeScript, Nginx), API Gateway (Kong/Spring Cloud Gateway), Core Domain Service (Java/Spring Boot), Search Service (Elasticsearch), Database (PostgreSQL), Async Event Broker (Apache Kafka/RabbitMQ), Background Worker (Python/Celery or Node.js)

## Relationships
- Web App $\rightarrow$ API Gateway (HTTPS/JSON)
- API Gateway $\rightarrow$ Core Domain & Search Services (gRPC/Internal REST over mTLS)
- Core Domain Service $\rightarrow$ PostgreSQL (JDBC/TLS 1.3 with mTLS)
- Core Domain Service $\rightarrow$ Async Event Broker (AMQP/Kafka Protocol + TLS 1.3)
- Async Event Broker $\rightarrow$ Search Service & Background Worker (Consumer subscription over mTLS)

## Technology Stack
- React/TypeScript & Nginx: Frontend UI delivery
- Kong/Spring Cloud Gateway: Single entry point, routing, and JWT validation
- Java/Spring Boot: Core circulation and cataloguing logic
- Elasticsearch: Fulfills search performance requirements (<800ms 99th-percentile)
- PostgreSQL: Relational data storage with read replicas and automated failover
- Apache Kafka/RabbitMQ: Asynchronous event publishing and decoupling with DLQs
- OpenTelemetry: Distributed tracing across all service hops and message contexts
- AES-256 & EU-hosted KMS: At-rest encryption for database and broker volumes

## Rationale
This architecture decouples heavy search indexing from core transactions using an event broker, ensuring the 800ms search SLA is met. Strict mTLS, TLS 1.3, and EU-hosted infrastructure enforce mandatory data residency and security constraints.