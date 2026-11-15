## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It is architected as a distributed, event-driven container ecosystem constrained by strict EU data residency.

## Key Elements
- **Patron & Librarian / Staff**: End-users accessing the platform.
- **Web Application (SPA)**: React served via Nginx.
- **API Gateway**: Spring Cloud Gateway (Java).
- **Core Domain Service**: Spring Boot (Java).
- **Search Service**: OpenSearch.
- **Notification & Payment Worker / DRM Worker**: Python (Celery).
- **Message Broker**: Apache Kafka.
- **Caching Layer**: Redis.
- **Database**: PostgreSQL.
- **External Systems**: EU-Tenant Identity Provider (IdP), EU-Hosted Payment Gateway, Notification Service, Digital Content Repository / DRM Provider.

## Relationships
- Web Application -> HTTPS/REST -> API Gateway
- API Gateway -> REST/TLS -> Core Domain Service & Search Service
- API Gateway & Core Services -> TCP -> Redis
- Core Domain Service -> JDBC -> PostgreSQL
- Core Domain Service -> Apache Kafka -> Search Service & Workers
- Workers -> HTTPS -> EU-Hosted Payment Gateway, Notification Service, and DRM Provider

## Technology Stack
- **React / Nginx**: Provides responsive user interfaces for patrons and staff.
- **Spring Cloud Gateway**: Handles request routing, rate limiting, and JWT validation via EU-IdP.
- **Spring Boot**: Powers core cataloging and circulation logic.
- **OpenSearch**: Dedicated search index ensuring sub-800ms search responses (R-05).
- **Apache Kafka**: Manages decoupled, replayable domain event synchronization.
- **Python / Celery**: Isolates external third-party integrations (payments, notifications, DRM).
- **Redis**: Provides distributed rate limiting and hot item caching.
- **PostgreSQL**: Ensures transactional integrity within EU data residency constraints.

## Rationale
This architecture uses query-path isolation and an event-driven design with OpenSearch and Redis to effortlessly meet the sub-800ms search performance requirement. Furthermore, housing all persistent data stores, brokers, and application containers within an isolated EU-certified VPC strictly enforces the mandatory EU data residency constraints.