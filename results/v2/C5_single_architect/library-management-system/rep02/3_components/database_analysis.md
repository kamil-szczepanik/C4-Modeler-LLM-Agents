## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
*   Library Patrons and Library Staff (Users)
*   Web Application (React/TypeScript SPA)
*   API Gateway (Nginx / Spring Cloud Gateway)
*   Core Domain Service (Java/Spring Boot)
*   Search Service (Java with Elasticsearch)
*   Notification Worker (Node.js)
*   Database Container: Primary PostgreSQL Instance, PostgreSQL Read Replicas, PgBouncer Connection Pooler, Audit Logging Subsystem (`pgAudit`), and `pg_trgm` Extension
*   Message Broker (RabbitMQ / Apache Kafka)
*   External Systems: Payment Gateway, Notification Service, National Library Registry, Identity Provider

## Relationships
*   `Core Domain Service -> PgBouncer`: Acquires database connections [TCP/IP over TLS]
*   `Search Service -> PgBouncer`: Reads catalogue delta for indexing [TCP/IP over TLS]
*   `PgBouncer -> Primary PostgreSQL / Read Replicas`: Routes queries [PostgreSQL Native Protocol over TLS]

## Technology Stack
*   **PostgreSQL**: Selected for robust relational OLTP data management and strict compliance with EU-only data residency constraints.
*   **PgBouncer**: Deployed for efficient database connection pooling under high concurrency.
*   **pg_trgm Extension**: Enabled in PostgreSQL to support fast fuzzy-text searches, meeting performance requirements.
*   **pgAudit**: Utilized for native audit logging to ensure strict EU data governance compliance.

## Rationale
This architecture ensures low-latency performance with 99th-percentile search responses under 800 ms through optimized database read replicas and connection pooling. It strictly enforces EU data residency and governance requirements via localized deployment and native auditing tools.