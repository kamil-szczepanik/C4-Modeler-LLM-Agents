## Overview
The Library Management System is a comprehensive platform for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It ensures EU-only data residency while delivering high-performance search capabilities.

## Key Elements
- **Patron & Librarian/Staff**: End-users interacting with the system.
- **Web Application (SPA)**: React/TypeScript interface served via Nginx.
- **API Gateway**: Spring Cloud Gateway / Envoy handling routing and security.
- **Core Domain Service**: Java (Spring Boot) managing business logic and circulation.
- **Search Service**: Python (FastAPI) backed by Elasticsearch for high-performance querying.
- **Async Event Broker**: Apache Kafka managed EU instance for decoupled messaging.
- **Background Worker**: Python (Celery) processing asynchronous tasks.
- **Database**: PostgreSQL managed EU instance for relational persistence.
- **External Systems**: Payment Gateway, Notification Provider, Identity Provider, Digital Content Provider.

## Relationships
- Web Application -> API Gateway (HTTPS)
- API Gateway -> Core Domain Service & Search Service (gRPC/REST)
- Core Domain Service -> Database (JDBC)
- Core Domain Service -> Event Broker (TCP/Kafka Protocol)
- Event Broker -> Search Service (TCP/Kafka Protocol)
- Core Domain Service & Background Worker -> External Systems (HTTPS)

## Technology Stack
- **React/TypeScript & Nginx**: Provides a responsive, maintainable frontend user interface.
- **Spring Boot (Java)**: Powers reliable, enterprise-grade core domain business logic.
- **Elasticsearch & FastAPI (Python)**: Ensures 99th-percentile search responses under 800 ms (R-05).
- **Apache Kafka**: Decouples services and guarantees reliable asynchronous index updates.
- **PostgreSQL**: Stores relational data within strict EU data residency constraints.

## Rationale
This architecture successfully meets EU data residency constraints by hosting all databases and event brokers locally within the EU. Furthermore, isolating the dedicated Search Service with Elasticsearch ensures the 99th-percentile search response time remains under 800 ms.