## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and high-performance search and retrieval capabilities.

## Key Elements
- Library Members (Patrons), Librarians / Library Staff, Library Administrators
- Web Application (React/TypeScript SPA)
- API Gateway (NGINX / Spring Cloud Gateway)
- Core Business Services (Java with Spring Boot)
- Search Engine (Elasticsearch / OpenSearch cluster)
- Database (PostgreSQL managed service with EU hosting)
- Analytics Worker (Python/Spring + Apache Kafka/RabbitMQ)
- External Systems: Payment Gateway, Digital Content Providers, Notification System

## Relationships
- Web Application -> API Gateway: HTTPS / REST / GraphQL
- API Gateway -> Core Business Services: gRPC / REST with JWT
- Core Business Services -> Database: Secure PostgreSQL protocol via PgBouncer
- Core Business Services -> Search Engine: Transport Protocol (TCP/HTTP)
- Core Business Services -> Analytics Worker: Apache Kafka / RabbitMQ message publishing

## Technology Stack
- PostgreSQL: Managed SQL database with automated table partitioning for scalability
- PgBouncer: Connection pooling to prevent exhaustion under peak loads
- Flyway: Database schema versioning integrated into the CI/CD pipeline
- HashiCorp Vault: Dynamic secret management and credential rotation
- pgaudit: PostgreSQL extension for compliance auditing and PII tracking

## Rationale
This architecture ensures high transactional throughput, ACID compliance, and robust security through schema isolation and read replicas. It meets stringent EU data residency and performance SLAs (99th-percentile search response < 800 ms).