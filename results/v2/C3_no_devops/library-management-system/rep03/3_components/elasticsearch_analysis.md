## Overview
[The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures EU data residency while maintaining high-performance search capabilities.]

## Key Elements
- Library Patrons (Members), Librarians / Circulation Staff, Library Administrators
- External Identity Provider (IdP), Third-Party Payment Gateway, Digital Content Repositories
- Patron Portal (React.js SPA), Librarian Back-office (Next.js Web App), API Gateway (NGINX / Envoy)
- Catalogue Service (Java / Spring Boot), Circulation Service (Node.js / Express), Event Broker (Apache Kafka / RabbitMQ)
- PostgreSQL Database (EU-hosted), Elasticsearch (EU-hosted)
- Elasticsearch Components: Search Engine Core (Lucene), Inverted Index & Document Store, REST API / Query DSL Interface, Search Analytics & Logging Engine

## Relationships
- Catalogue Service -> REST API / Query DSL Interface (Elasticsearch): Executes search & indexing requests over HTTPS with mTLS (TLS 1.3)
- Search Analytics & Logging Engine -> Event Broker (Apache Kafka): Exports metrics via Filebeat / OpenTelemetry over TLS 1.3 with mTLS

## Technology Stack
- Java / Spring Boot & Node.js / Express: Core microservices implementation
- React.js & Next.js: Modern web UI frameworks for portals and back-office
- PostgreSQL & Elasticsearch: Persistent storage and EU-compliant high-performance search
- Apache Kafka / RabbitMQ: Asynchronous event-driven messaging
- TLS 1.3, mTLS, OAuth2/JWT, AES-256: Security and data protection protocols

## Rationale
[This architecture meets strict EU data residency constraints and performance SLAs by employing localized storage and secure, decoupled microservices. The design ensures scalable search operations and robust security without compromising system latency.]