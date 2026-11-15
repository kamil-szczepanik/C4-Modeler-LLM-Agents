## Overview
[The Library Management System is a cloud-native enterprise solution that enables public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals with EU-only data residency and security compliance.]

## Key Elements
- Library Patrons [person]
- Librarians / Circulation Staff [person]
- Library Administrators [person]
- Patron Self-Service Portal [container, Web/Mobile App]
- Circulation Management Dashboard [container]
- Administration Console [container]
- API Gateway [container, NGINX / Kong]
- Catalog & Search Service [container, Spring Boot, Elasticsearch]
- Circulation & Loan Service [container, Node.js / Express]
- Reporting & Analytics Service [container, Python / FastAPI]
- Notification Dispatcher [container, Go]
- PostgreSQL Database [container, PostgreSQL 15]
- RabbitMQ [container, message broker]
- Payment Gateway, Digital Content Providers, Notification Service, Identity Provider [external systems]

## Relationships
- Library Patrons / Staff / Administrators -> API Gateway (HTTPS / WAF-protected)
- API Gateway -> Backends (HTTP/2 reverse proxy)
- Front-ends -> Identity Provider (OIDC / OAuth 2.0 over HTTPS with PKCE)
- Microservices -> Microservices (gRPC over TLS 1.3 / mTLS)
- Microservices -> RabbitMQ (AMQP over TLS 1.3)
- Library Management System -> Payment Gateway, Digital Content Providers, Notification Service (REST / HTTPS over TLS 1.3)

## Technology Stack
- API Gateway: NGINX / Kong for TLS termination, WAF policies, and routing
- Search: Elasticsearch for sub-800ms catalogue queries (R-05 compliance)
- Backend Services: Spring Boot, Node.js, Python/FastAPI, and Go for modular microservice capabilities
- Storage: PostgreSQL 15 with read-replicas for transactional state and analytics
- Messaging: RabbitMQ for asynchronous event-driven notifications
- Security: Keycloak/Auth0 EU for IAM; AES-256 encryption with EU-only keys for data at rest

## Rationale
[This architecture cleanly segregates user personas into dedicated front-ends while routing all traffic through a secure, EU-hosted API Gateway to satisfy strict regional data residency constraints. Decoupling high-performance search, stateless circulation, and asynchronous notifications ensures the system meets the demanding sub-800ms search threshold (R-05) and maintains high availability.]