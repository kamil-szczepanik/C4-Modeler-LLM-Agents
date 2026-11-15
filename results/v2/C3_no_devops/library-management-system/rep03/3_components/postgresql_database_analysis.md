## Overview
[The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and high availability while supporting rapid item searches and reliable transactions.]

## Key Elements
* Library Patrons (Members), Librarians / Circulation Staff, Library Administrators
* External Identity Provider (IdP), Third-Party Payment Gateway, Digital Content Repositories
* Patron Portal (React.js SPA), Librarian Back-office (Next.js Web App)
* API Gateway (NGINX / Envoy)
* Catalogue Service (Java / Spring Boot), Circulation Service (Node.js / Express), Event Broker (Apache Kafka / RabbitMQ)
* PostgreSQL Database (Primary Master, Read Replica, PgBouncer, `pg_audit`)
* Elasticsearch

## Relationships
* Patron Portal -> API Gateway: HTTPS/REST [TLS 1.3]
* Librarian Back-office -> API Gateway: HTTPS/REST [TLS 1.3]
* API Gateway -> Catalogue Service: HTTP/gRPC [Internal Network]
* API Gateway -> Circulation Service: HTTP/gRPC [Internal Network]
* Catalogue Service -> PostgreSQL Database (PgBouncer): JDBC/TCP [TLS 1.3, Read-only queries, AES-256]
* Circulation Service -> PostgreSQL Database (PgBouncer): pg driver/TCP [TLS 1.3, Read-write transactions, AES-256]
* Catalogue Service -> Elasticsearch: HTTP/REST [TLS 1.3]

## Technology Stack
* React.js: Powers the Patron Portal for responsive self-service interactions.
* Next.js: Enables server-side rendering for the Librarian Back-office.
* Java / Spring Boot: Chosen for the Catalogue Service to ensure enterprise robustness.
* Node.js / Express: Selected for the Circulation Service for high-concurrency handling.
* PostgreSQL: Manages ACID-compliant circulation and catalogue transactions with EU data residency.
* Elasticsearch: Delivers sub-800ms 99th-percentile search response times.
* PgBouncer & TLS 1.3: Provides connection pooling and secure transport encryption.

## Rationale
[This architecture satisfies EU data residency constraints through localized EU hosting and encrypted storage volumes. It guarantees high availability, ACID compliance, and sub-800ms search performance under peak loads.]