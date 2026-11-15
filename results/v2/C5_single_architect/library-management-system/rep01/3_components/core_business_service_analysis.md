## Overview
The Library Management System provides cataloguing, circulation, and self-service portal capabilities for public and academic libraries. It enforces strict EU-only data residency while ensuring high-performance search responses under 800 ms.

## Key Elements
- Patrons / Library Members and Librarians / Staff (Users)
- Web Application (React, TypeScript)
- API Gateway (Kong / Nginx)
- Core Business Service (Java, Spring Boot) containing:
  - Catalog Management Component (Spring Data JPA)
  - Circulation Component (Spring Transactions)
  - Payment Integration Component (Spring Cloud OpenFeign)
  - Search Integration Component (Spring WebClient)
- Search Service (Elasticsearch)
- Database (PostgreSQL)
- Redis Cache (Redis)
- Notification Worker (Node.js)
- External Payment Gateway, Digital Content Providers, Notification Service

## Relationships
- API Gateway -> Core Business Service: Routes business requests [gRPC/REST]
- Catalog Management Component -> Redis Cache: Caches hot catalog items [TCP/Lettuce]
- Circulation Component -> Database: Persists transaction states [TCP/JDBC]
- Payment Integration Component -> External Payment Gateway: Processes fines [HTTPS/JSON]
- Catalog Management Component -> Search Service: Synchronizes item metadata [HTTP/REST]
- Core Business Service -> Database: Reads and writes persistent data [TCP]

## Technology Stack
- Java and Spring Boot: Chosen for robust enterprise backend logic and modular domain-driven design.
- PostgreSQL: Provides reliable relational persistence within EU data residency constraints.
- Elasticsearch: Delivers sub-800ms 99th-percentile search performance for catalog items.
- Redis: Caches frequently accessed data to reduce database load.
- React and TypeScript: Powers the responsive front-end user interface.

## Rationale
This architecture uses a modular Spring Boot monolith backed by specialized caching and search technologies to meet strict performance targets. EU data residency is strictly maintained through localized PostgreSQL deployment and isolated container boundaries.