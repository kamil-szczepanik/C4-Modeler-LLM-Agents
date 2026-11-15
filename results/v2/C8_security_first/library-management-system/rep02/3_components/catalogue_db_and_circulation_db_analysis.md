## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. The architecture ensures EU-only data residency and meets 99th-percentile search performance under 800 ms.

## Key Elements
- PostgreSQL (Primary and Replica instances)
- Patroni (High availability and automated failover)
- PgBouncer (Connection pooling sidecar)
- Flyway/Liquibase (Migration runner container)
- Prometheus (Observability and monitoring)

## Relationships
- Catalogue Service -> PostgreSQL: Reads catalogue data via TCP/Postgres wire protocol over mTLS and PgBouncer
- Circulation & Loan Service -> PostgreSQL: Reads/writes circulation data via TCP/Postgres wire protocol over mTLS and PgBouncer
- Prometheus -> PostgreSQL and PgBouncer: Scrapes metrics via Prometheus exporters

## Technology Stack
- PostgreSQL: Relational database with AES-256 encrypted EU persistent volumes for secure storage
- Patroni: High-availability template for PostgreSQL automated failover across availability zones
- PgBouncer: Connection pooler to manage persistent database connections and prevent saturation
- Flyway/Liquibase: CI/CD-driven migration runners for zero-downtime, backward-compatible schema changes
- SCRAM-SHA-256: Database authentication protocol integrated with dynamic secrets management

## Rationale
Separating the database into independent physical PostgreSQL instances isolates transactional circulation writes from read-heavy catalogue queries, preventing resource contention. Enforcing mTLS, PgBouncer pooling, and read-replica routing ensures strict security, EU data residency compliance, and rapid search response times.