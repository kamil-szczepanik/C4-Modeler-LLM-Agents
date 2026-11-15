## Overview
The Library Management System is a comprehensive platform providing cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search capabilities with 99th-percentile response times under 800ms.

## Key Elements
- Library Member (Patron)
- Librarian / Staff
- Library Administrator
- Web Application / SPA (React, TypeScript)
- API Gateway (NGINX / Envoy)
- Catalog & Search Service (Java, Spring Boot + Elasticsearch)
- Circulation Service (Node.js / NestJS)
- Database (PostgreSQL)
- Message Broker (Apache Kafka / RabbitMQ)
- Audit Service (Go)
- Identity Provider
- Payment Gateway
- Notification Provider

## Relationships
- Library Member (Patron) -> API Gateway (HTTPS / TLS 1.3)
- Librarian / Staff -> API Gateway (HTTPS / TLS 1.3)
- Library Administrator -> API Gateway (HTTPS / TLS 1.3)
- API Gateway -> Catalog & Search Service (gRPC over mTLS)
- API Gateway -> Circulation Service (gRPC over mTLS)
- API Gateway -> Identity Provider (OIDC/OAuth2 over HTTPS)
- Circulation Service -> Message Broker (AMQP/Kafka Protocol over mTLS)
- Circulation Service -> Database (SQL over mTLS)
- Catalog & Search Service -> Database (SQL over mTLS)
- Circulation Service -> Audit Service (REST over mTLS)
- Circulation Service -> Payment Gateway (HTTPS/REST)
- Circulation Service -> Notification Provider (HTTPS/REST)

## Technology Stack
- React, TypeScript: Powers the modern, responsive user interface for patrons and staff.
- NGINX / Envoy: Provides high-performance edge routing, rate limiting, and mTLS termination at the API Gateway.
- Java, Spring Boot + Elasticsearch: Delivers sub-800ms search performance and robust catalog indexing.
- Node.js / NestJS: Manages modular business logic for circulation and fines.
- PostgreSQL: Serves as the reliable primary relational datastore enforcing data integrity.
- Apache Kafka / RabbitMQ: Enables asynchronous, event-driven communication across microservices.
- Go: Powers the high-performance audit logging service for compliance and security tracking.

## Rationale
This architecture uses a secure API Gateway paired with reactive microservices to isolate high-load search and circulation functions, guaranteeing performance SLAs. Strict protocol selection (gRPC over mTLS) and EU-hosted infrastructure fulfill all data residency and security constraints.