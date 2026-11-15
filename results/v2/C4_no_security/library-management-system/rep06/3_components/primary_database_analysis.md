## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
- Library Patrons, Library Staff and Circulation Clerks, Library Administrators
- Self-Service Portal & Staff Dashboard (React / TypeScript)
- API Gateway (Kong / NGINX)
- Core API Application (Spring Boot / Java)
- Managed PostgreSQL (Primary Database container with Catalog Module, Circulation Module, Identity & Access Module, Read Replica Component, and Archival & Partitioning Module)
- Search Engine (OpenSearch)
- Message Broker (Kafka / RabbitMQ)
- Async Workers (Spring Boot / Java)
- External Systems: Payment Gateway, Third-Party Identity Provider / LDAP, Third-Party Digital Content Providers, Notification Service, Centralized Log/Audit Aggregator, APM and Synthetic Monitoring Tool

## Relationships
- Core API Application -> Primary Database: Queries and updates transactional data [PostgreSQL wire protocol over TLS 1.3 via PgBouncer]
- Async Workers -> Archival & Partitioning Module: Executes scheduled batch cleanup jobs [PostgreSQL wire protocol over TLS 1.3]
- Core API Application -> Search Engine: Indexes and queries catalogue items [REST over TLS]
- Self-Service Portal & Staff Dashboard -> API Gateway: Routes user requests [HTTPS]
- API Gateway -> Core API Application: Forwards authenticated requests [gRPC/REST over TLS]

## Technology Stack
- Managed PostgreSQL: Relational data storage ensuring ACID compliance, GDPR readiness, and EU cloud region residency
- PgBouncer: Connection pooling to protect PostgreSQL from connection exhaustion
- Spring Boot / Java: Core business logic and asynchronous background workers
- OpenSearch: High-performance indexing and searching for catalogue items (<800ms 99th-percentile response)
- React / TypeScript: Responsive self-service portal and staff dashboard interface
- Kafka / RabbitMQ: Asynchronous message brokering for decoupled background processing

## Rationale
This architecture uses a robust, EU-restricted Managed PostgreSQL database with connection pooling and read-replications to guarantee ACID compliance, high availability, and strict GDPR data residency. Decoupled microservices and dedicated async workers ensure scalability and high-performance search responses under peak academic loads.