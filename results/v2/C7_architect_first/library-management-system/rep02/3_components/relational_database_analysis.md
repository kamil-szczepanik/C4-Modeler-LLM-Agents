## Overview
The system is a Library Management System designed for public and academic libraries to catalogue items, manage circulation, and provide secure self-service portals. It enforces strict EU-only data residency and high-performance transactional capabilities.

## Key Elements
*   Core Services API: Node.js / NestJS backend service
*   Connection Pooling Subsystem: PgBouncer
*   Relational Storage Engine: PostgreSQL database with `pg_trgm` extension
*   Audit & Telemetry Component: `pgaudit`, `postgres_exporter`, and Prometheus
*   High Availability Manager: Patroni across multi-availability zones
*   Secrets Management: HashiCorp Vault

## Relationships
*   Core Services API -> PgBouncer: Synchronous communication over TCP / PostgreSQL protocol with TLS 1.3 and mandatory mTLS
*   PgBouncer -> PostgreSQL: Internal connection routing and throttling
*   Prometheus -> postgres_exporter: Telemetry scraping for metrics and slow queries
*   Core Services API -> HashiCorp Vault: Dynamic secret generation and rotation

## Technology Stack
*   PostgreSQL: Primary EU-hosted datastore with Transparent Data Encryption (TDE) via Customer-Managed Keys (CMK) and column-level AES-256 PII encryption for data security and GDPR compliance
*   PgBouncer: Connection pooling to protect PostgreSQL under peak loads
*   Patroni: Automated failover and multi-AZ deployment for zero-downtime maintenance
*   pgaudit: Captures DDL/DML statements for compliance SIEM ingestion

## Rationale
This architecture ensures strict compliance with EU data residency and privacy regulations through isolated regional deployments and robust encryption. It guarantees high performance, transactional integrity, and fault tolerance during peak library circulation loads.