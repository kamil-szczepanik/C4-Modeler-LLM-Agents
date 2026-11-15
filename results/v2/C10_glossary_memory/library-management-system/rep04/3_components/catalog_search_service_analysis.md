## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The Catalog & Search Service delivers high-performance discovery, meeting the <800ms search SLA via optimized caching and indexing.

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators
- API Gateway (NGINX / Kong)
- Catalog & Search Service (Spring Boot, Elasticsearch)
- Circulation & Loan Service (Node.js / Express)
- Reporting & Analytics Service (Python / FastAPI)
- Notification Dispatcher (Go)
- PostgreSQL Database (PostgreSQL 15)
- RabbitMQ (Message Broker)
- Identity Provider (Keycloak/Auth0 EU), Payment Gateway, Digital Content Providers, Notification Service

## Relationships
- API Gateway -> Catalog & Search Service: HTTP/2 reverse proxy
- Catalog & Search Service -> Circulation & Loan Service: gRPC over TLS 1.3 / mTLS
- Catalog & Search Service -> RabbitMQ: AMQP over TLS 1.3
- Catalog & Search Service -> Digital Content Providers: REST / HTTPS over TLS 1.3
- Circulation & Loan Service -> PostgreSQL Database: SQL / PostgreSQL protocol

## Technology Stack
- Spring Boot & Elasticsearch: Powers fast faceted search and catalog management within the <800ms SLA
- Node.js / Express: Handles transactional circulation and loan workflows
- PostgreSQL 15: Stores persistent transactional state and analytics data securely in the EU
- RabbitMQ: Facilitates asynchronous event-driven messaging across microservices
- NGINX / Kong: Manages ingress routing, TLS termination, and WAF policies

## Rationale
The microservices architecture isolates high-throughput search and circulation workloads to guarantee performance. Strict adherence to EU-hosted infrastructure and TLS 1.3 encryption ensures compliance with data residency and security mandates.