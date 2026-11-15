## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It strictly adheres to EU-only data residency constraints while ensuring high-performance search capabilities.

## Key Elements
- **Library Patron & Librarian**: End-users interacting via self-service portals.
- **Web Application**: React and TypeScript frontend container.
- **API Gateway**: Kong or NGINX routing layer.
- **Core Domain**: Java and Spring Boot backend container.
- **Search Engine**: Elasticsearch container for complex queries.
- **PostgreSQL Database**: EU-hosted relational database container housing the Relational Schema Engine, Full-Text Search Index (`pg_trgm`), Audit & Data Residency Enforcement Module, and Connection Pooler (PgBouncer).
- **Integration Worker**: Node.js or Python background worker.
- **Message Broker**: RabbitMQ container.

## Relationships
- **Core Domain** -> **Connection Pooler**: Manages pooled SQL transactions via JDBC over TLS 1.3.
- **Integration Worker** -> **Relational Schema Engine**: Performs asynchronous bulk updates via native PostgreSQL wire protocol.
- **Core Domain** -> **PostgreSQL Database**: Reads and writes transactional data using native TCP drivers over TLS.

## Technology Stack
- **React & TypeScript**: Powers the Web Application for type-safe UI development.
- **Java & Spring Boot**: Implements the Core Domain for robust business logic execution.
- **PostgreSQL**: Stores transactional data with strict geographic compliance and fast exact-match lookups.
- **PgBouncer**: Manages database connection limits to sustain peak transactional throughput.
- **Elasticsearch**: Handles high-performance search queries to meet the < 800 ms response requirement.

## Rationale
This architecture ensures strict compliance with EU data residency laws while delivering sub-800ms search responses through optimized indexing and connection pooling. Decoupled containers and robust protocols guarantee high scalability and transactional integrity.