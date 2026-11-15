## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Member (Patron) [person]
- Librarian / Staff [person]
- Library Administrator [person]
- Web Application / SPA (React, TypeScript) [container]
- API Gateway (NGINX / Envoy) [container]
- Catalog & Search Service (Java, Spring Boot + Elasticsearch) [container]
- Circulation Service (Node.js / NestJS) [container]
- Database (PostgreSQL) [container]
- Message Broker (Apache Kafka) [container]
- Audit Service (Go) [container]
- Payment Gateway [externalSystem]
- Notification Provider [externalSystem]
- Identity Provider [externalSystem]

## Relationships
- Library Member (Patron), Librarian / Staff, Library Administrator -> API Gateway [HTTPS / TLS 1.3]
- API Gateway -> Catalog & Search Service [gRPC over mTLS]
- API Gateway -> Circulation Service [gRPC over mTLS]
- Circulation Service -> Message Broker [AMQP/Kafka Protocol over mTLS]
- Catalog & Search Service -> Message Broker [Kafka Protocol over mTLS]
- Audit Service -> Message Broker [Kafka Protocol over mTLS]
- Circulation Service -> Database [SQL over mTLS]
- Catalog & Search Service -> Database [SQL over mTLS]
- Circulation Service -> Audit Service [REST over mTLS]
- Circulation Service -> Payment Gateway [HTTPS/REST]
- Circulation Service -> Notification Provider [HTTPS/REST]
- API Gateway -> Identity Provider [OIDC/OAuth2 over HTTPS]

## Technology Stack
- React, TypeScript: Responsive and type-safe user interface for patrons and staff.
- NGINX / Envoy: Edge routing, TLS termination, and OIDC token validation.
- Java, Spring Boot + Elasticsearch: High-performance cataloging and sub-800ms search fulfillment.
- Node.js / NestJS: Scalable business logic handling loans and fine management.
- PostgreSQL: Robust relational storage for transactional data integrity.
- Apache Kafka: Persistent, event-driven message broker supporting dead-letter queues and EU data residency.
- Go: High-performance audit logging for security compliance.

## Rationale
The architecture decouples high-frequency catalog searches from transactional circulation flows using asynchronous messaging. This ensures sub-800ms search response times and strict EU-only data residency compliance.