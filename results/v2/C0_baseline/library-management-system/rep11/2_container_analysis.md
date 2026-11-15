## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures high performance and strict EU data residency compliance.

## Key Elements
- **Users:** Library Patrons, Librarians, Library Administrators
- **Containers:** Patron Self-Service Portal (React/TypeScript SPA), Librarian Workbench (Modular Monolith, .NET Core), Catalog API & Search Service (.NET Core), Asynchronous Processing Worker (.NET Core Worker Service), Integration Gateway (Kong/Envoy API Gateway), Database (PostgreSQL with GIN indexes), Message Broker (Redis/RabbitMQ)
- **External Systems:** EU Identity Provider, EU Payment Gateway, EU Notification Service, EU Cloud Region Provider, Central Logging & Monitoring SIEM, Web Application Firewall (WAF)

## Relationships
- **Patron Portal to Integration Gateway:** HTTPS / REST over TLS 1.3
- **Integration Gateway to Catalog API:** gRPC over mTLS with OAuth2/OIDC token validation
- **Catalog API to PostgreSQL:** SQL query over encrypted connections within EU availability zones
- **Librarian Workbench to Catalog API:** gRPC over mTLS
- **Asynchronous Processing Worker to Redis/RabbitMQ:** AMQP/TCP with message-level encryption
- **All Containers to SIEM:** Structured JSON logs and Prometheus metrics via OpenTelemetry (with PII sanitization)

## Technology Stack
- **Frontend:** React with TypeScript served via CDN for rapid patron engagement
- **Backend & Services:** .NET Core for high-performance APIs, modular monoliths, and worker services
- **Database & Search:** PostgreSQL utilizing built-in full-text search and GIN indexes, avoiding separate search clusters to reduce EU compliance overhead
- **Messaging:** Redis/RabbitMQ with Dead Letter Queues for decoupled asynchronous processing
- **Infrastructure & Security:** Kong/Envoy API Gateway, OAuth2/OIDC, mTLS, TLS 1.3, and AES-256 encryption-at-rest

## Rationale
This architecture eliminates standalone search clusters to streamline operations while utilizing PostgreSQL full-text search to reliably meet the sub-800ms search NFR. Strict container decomposition, mTLS, and localized cloud deployment enforce EU data residency and robust security standards.