## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for public and academic libraries. The architecture ensures strict EU-only data residency and sub-800ms search responses.

## Key Elements
* Database Container: Regional PostgreSQL instance with encryption at rest
* Connection Pooler: PgBouncer
* Schema Migration Tool: Flyway or Liquibase
* Monitoring & Telemetry: Prometheus via `postgres_exporter` and native `pg_audit`
* Backup Storage: Disaster Recovery and Backup Storage container with WAL archiving

## Relationships
* Core Business Services -> Database Container: Reads and writes relational data via PostgreSQL protocol

## Technology Stack
* PostgreSQL: Provides ACID transactional integrity for circulation
* PgBouncer: Manages traffic spikes and connection limits
* Flyway/Liquibase: Automates safe schema evolution
* `postgres_exporter`: Exposes metrics for monitoring infrastructure

## Rationale
This architecture uses PostgreSQL with connection pooling and read replicas to meet the 800ms performance requirement. Automated PITR, encryption, and audit streaming ensure compliance with EU-only data residency.