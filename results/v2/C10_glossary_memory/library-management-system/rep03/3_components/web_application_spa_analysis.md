## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets sub-800ms search performance requirements.

## Key Elements
- Library Member (Patron) [person]
- Librarian / Staff [person]
- Library Administrator [person]
- Web Application / SPA (React, TypeScript) [container]
- API Gateway (NGINX / Envoy) [container]
- Catalog & Search Service (Java, Spring Boot + Elasticsearch) [container]
- Circulation Service (Node.js / NestJS) [container]
- Database (PostgreSQL) [container]
- Message Broker (Apache Kafka / RabbitMQ) [container]
- Audit Service (Go) [container]
- Identity Provider [externalSystem]
- Payment Gateway [externalSystem]
- Notification Provider [externalSystem]

## Relationships
- Library Member (Patron) -> Web Application / SPA: HTTPS / TLS 1.3
- Librarian / Staff -> Web Application / SPA: HTTPS / TLS 1.3
- Library Administrator -> Web Application / SPA: HTTPS / TLS 1.3
- Web Application / SPA -> API Gateway: HTTPS / TLS 1.3
- API Gateway -> Catalog & Search Service: gRPC over mTLS
- API Gateway -> Circulation Service: gRPC over mTLS
- Circulation Service -> Database: SQL over mTLS
- Catalog & Search Service -> Database: SQL over mTLS
- Circulation Service -> Message Broker: AMQP/Kafka Protocol over mTLS
- Circulation Service -> Audit Service: REST over mTLS
- Circulation Service -> Payment Gateway: HTTPS/REST
- Circulation Service -> Notification Provider: HTTPS/REST
- API Gateway -> Identity Provider: OIDC/OAuth2 over HTTPS

## Technology Stack
- React, TypeScript: UI framework for Web Application / SPA ensuring modular component architecture and role-based feature toggling.
- NGINX / Envoy: Edge routing, TLS termination, and OIDC token validation.
- Java, Spring Boot + Elasticsearch: High-performance search and cataloging to satisfy sub-800ms search response SLOs.
- Node.js / NestJS: Business logic implementation for circulation and loan management workflows.
- PostgreSQL: Relational persistence for transactional library and user data.
- Apache Kafka / RabbitMQ: Asynchronous, event-driven inter-service communication.
- Go: High-throughput audit logging service for compliance and security.

## Rationale
The microservices architecture decouples high-performance search from transactional circulation workflows to strictly meet performance SLAs. EU-anchored deployment guarantees data residency compliance.