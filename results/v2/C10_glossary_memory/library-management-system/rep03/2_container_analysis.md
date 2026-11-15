## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Member (Patron) [person]
- Librarian / Staff [person]
- Library Administrator [person]
- Web Application / SPA [container, React, TypeScript]
- API Gateway [container, NGINX / Envoy]
- Catalog & Search Service [container, Java, Spring Boot + Elasticsearch]
- Circulation Service [container, Node.js / NestJS]
- Database [container, PostgreSQL]
- Message Broker [container, Apache Kafka / RabbitMQ]
- Audit Service [container, Go]
- Payment Gateway [externalSystem]
- Notification Provider [externalSystem]
- Identity Provider [externalSystem]

## Relationships
- Library Member (Patron) -> API Gateway (HTTPS / TLS 1.3)
- Librarian / Staff -> API Gateway (HTTPS / TLS 1.3)
- Library Administrator -> API Gateway (HTTPS / TLS 1.3)
- API Gateway -> Catalog & Search Service (gRPC over mTLS)
- API Gateway -> Circulation Service (gRPC over mTLS)
- Circulation Service -> Message Broker (AMQP/Kafka Protocol over mTLS)
- Circulation Service -> Database (SQL over mTLS)
- Catalog & Search Service -> Database (SQL over mTLS)
- Circulation Service -> Audit Service (REST over mTLS)
- Circulation Service -> Payment Gateway (HTTPS/REST)
- Circulation Service -> Notification Provider (HTTPS/REST)
- API Gateway -> Identity Provider (OIDC/OAuth2 over HTTPS)

## Technology Stack
- React, TypeScript: UI logic for patrons and staff
- NGINX / Envoy: Edge routing, TLS termination, and OIDC token validation
- Java, Spring Boot + Elasticsearch: Dedicated to meeting sub-800ms search and cataloging requirements
- Node.js / NestJS: Manages loans, fines, and business integrations
- PostgreSQL: Primary relational data store for transactional data
- Apache Kafka / RabbitMQ: Asynchronous, event-driven communication
- Go: High-performance audit logging service

## Rationale
Separating the Catalog & Search Service from the Circulation Service guarantees sub-800ms search performance for patrons without risking starvation from staff operations. Deploying all databases and Elasticsearch clusters in EU-only regions with strict mTLS and WORM audit logging ensures complete compliance with data residency and security constraints.