## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and meets performance requirements like 99th-percentile search under 800 ms.

## Key Elements
- Library Patron and Librarian / Staff (Users)
- Web Application (React, TypeScript, Nginx)
- API Gateway (Spring Cloud Gateway / Kong)
- Core Domain Service (Java, Spring Boot)
- Search Service (Python, FastAPI, Elasticsearch)
- Background Worker Service (Python/Celery or Java/Spring Batch)
- PostgreSQL Database (PostgreSQL container with Relational Storage Engine, PgBouncer Connection Pooler, and Flyway/Liquibase Database Migration Manager)
- Redis Cache (Redis)
- Payment Gateway, Notification Service, DRM Provider (External Systems)

## Relationships
- Library Patron / Librarian -> Web Application [HTTPS]
- Web Application -> API Gateway [HTTPS]
- API Gateway -> Core Domain Service & Search Service [gRPC / REST]
- Core Domain Service -> PostgreSQL Database / Connection Pooler [TCP / PostgreSQL Wire Protocol]
- Core Domain Service -> Redis Cache [RESP]
- Core Domain Service -> Search Service [REST / gRPC]
- Core Domain Service -> External Systems [HTTPS / REST]

## Technology Stack
- Frontend: React, TypeScript, Nginx for self-service portals
- Backend: Java (Spring Boot) for Core Domain Service; Python (FastAPI) for Search Service
- Data & Caching: PostgreSQL for transactional data; Elasticsearch for <800ms search performance; Redis for caching
- Database Management: PgBouncer for connection pooling; Flyway / Liquibase for schema migrations
- Infrastructure/Gateway: Spring Cloud Gateway / Kong

## Rationale
This architecture isolates connection management and enforces EU-only data residency requirements within the PostgreSQL database container. Dedicated search and caching technologies ensure high performance and low latency under peak operational loads.