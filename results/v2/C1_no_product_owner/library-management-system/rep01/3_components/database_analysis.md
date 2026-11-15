## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The database container securely stores and manages relational data for inventory and user transactions.

## Key Elements
* Relational Data Store: PostgreSQL 15 engine for ACID-compliant storage
* Connection Pooler: PgBouncer for managing incoming TCP connections
* Catalogue & Search Service: Java Spring Boot and Elasticsearch service
* Circulation & User Service: Go and Spring Boot service

## Relationships
* Catalogue & Search Service -> Connection Pooler: Routes transactional queries [TLS 1.3, PostgreSQL Wire Protocol]
* Circulation & User Service -> Connection Pooler: Routes transactional queries [TLS 1.3, PostgreSQL Wire Protocol]
* Connection Pooler -> Relational Data Store: Forwards pooled queries [Encrypted Local TCP, Unix Domain Sockets]

## Technology Stack
* PostgreSQL 15: Relational database engine for robust data integrity
* PgBouncer: Connection pooling to prevent starvation and meet P99 latency <800ms
* AWS RDS (Frankfurt): Managed Multi-AZ instance for EU data residency
* Terraform / OpenTofu: Infrastructure as Code for configuration consistency
* Flyway / Liquibase: Automated schema migration pipelines
* AWS Secrets Manager: Dynamic runtime credential injection

## Rationale
This architecture ensures strict EU data residency via Frankfurt deployment while guaranteeing high performance and availability. Security controls like TLS 1.3, SCRAM-SHA-256, and principle-of-least-privilege database roles protect sensitive patron and catalog data.