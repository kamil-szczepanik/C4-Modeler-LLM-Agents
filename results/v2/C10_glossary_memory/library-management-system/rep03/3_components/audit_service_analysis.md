## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search performance requirements.

## Key Elements
- Library Member (Patron) [person]
- Librarian / Staff [person]
- Library Administrator [person]
- Web Application / SPA (React, TypeScript) [container]
- API Gateway (NGINX / Envoy) [container]
- Catalog & Search Service (Java, Spring Boot + Elasticsearch) [container]
- Circulation Service (Node.js / NestJS) [container]
- Message Broker (Apache Kafka / RabbitMQ) [container]
- Audit Service (Go) [container]
  - Audit Consumer [component, Go]
  - Audit API Handler [component, Go]
  - Audit Database (PostgreSQL) [component]
- Identity Provider, Payment Gateway, Notification Provider [externalSystem]

## Relationships
- Library Member (Patron), Librarian / Staff, Library Administrator -> API Gateway (HTTPS / TLS 1.3)
- API Gateway -> Catalog & Search Service (gRPC over mTLS)
- API Gateway -> Circulation Service (gRPC over mTLS)
- API Gateway -> Audit API Handler (gRPC over mTLS)
- Circulation Service, Catalog & Search Service -> Message Broker (AMQP/Kafka Protocol over mTLS)
- Message Broker -> Audit Consumer (AMQP/Kafka Protocol over mTLS)
- Audit Consumer, Audit API Handler -> Audit Database (SQL over mTLS)
- API Gateway -> Identity Provider (OIDC/OAuth2 over HTTPS)

## Technology Stack
- Go: Chosen for the Audit Service to deliver high-performance, low-latency event processing.
- Java & Elasticsearch: Powers the Catalog & Search Service to meet sub-800ms performance constraints.
- PostgreSQL: Serves as the primary transactional database and immutable audit data store with EU data residency.
- Apache Kafka / RabbitMQ: Enables asynchronous, decoupled event-driven communication and dead-letter queue reliability.
- React & TypeScript: Delivers modern, responsive UI logic for the Web Application SPA.

## Rationale
This architecture decouples core transactions from logging via a message broker to protect patron-facing performance. It enforces regulatory compliance, GDPR adherence, and security via strict EU data residency, mTLS transport, and RBAC-secured audit exports.