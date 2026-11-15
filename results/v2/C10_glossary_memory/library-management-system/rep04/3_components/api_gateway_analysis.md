## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures EU-only data residency, high-availability performance, and robust edge security.

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators
- API Gateway (NGINX / Kong) with WAF, JWT Validation, Rate Limiting, and Reverse Proxy components
- Catalog & Search Service (Spring Boot, Elasticsearch)
- Circulation & Loan Service (Node.js / Express)
- Reporting & Analytics Service (Python / FastAPI)
- Notification Dispatcher (Go)
- PostgreSQL Database (PostgreSQL 15), RabbitMQ (Message Broker)
- External Systems: Payment Gateway, Digital Content Providers, Notification Service, Identity Provider

## Relationships
- Library Patrons / Staff / Admins -> API Gateway: Accesses portals via HTTPS / WAF-protected
- API Gateway -> Identity Provider: Validates tokens via HTTPS
- API Gateway -> Catalog & Search Service, Circulation & Loan Service, Reporting & Analytics Service: Routes requests via HTTP/2 over TLS 1.3 (mTLS)
- Services -> PostgreSQL Database: Stores data via SQL / PostgreSQL protocol
- Services -> RabbitMQ: Publishes messages via AMQP over TLS 1.3
- Library Management System -> External Systems (Payment, Digital Content, Notification): Integrates via REST / HTTPS over TLS 1.3

## Technology Stack
- NGINX / Kong: API Gateway for edge routing, TLS termination, and WAF protection
- Spring Boot, Node.js / Express, Python / FastAPI, Go: Microservices runtime stacks
- Elasticsearch & PostgreSQL 15: Search indexing and transactional data storage
- RabbitMQ: Asynchronous event-driven messaging broker
- mTLS (TLS 1.3): Encrypted internal service-to-service communication

## Rationale
This architecture uses a secure API Gateway and microservices to isolate high-load reporting from patron searches, ensuring 99th-percentile search responses remain under 800 ms. Strict edge controls and mTLS guarantee EU data residency and compliance.