## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It utilizes a containerized microservices architecture backed by a robust PostgreSQL database component.

## Key Elements
* **PostgreSQL Database Container**: Core relational database management system.
* **Catalog Schema**: PostgreSQL schema managing physical and digital item metadata via relational tables and JSONB.
* **Circulation Schema**: PostgreSQL schema managing patron loans, holds, and ACID transactions.
* **Audit Schema**: PostgreSQL schema utilizing partitioned tables for GDPR compliance.
* **User Management Schema**: PostgreSQL schema managing patron profiles and staff roles with Row-Level Security (RLS).
* **PgBouncer**: Connection pooler and proxy component running in transaction pooling mode.
* **Backup & Replication Manager**: Barman and PostgreSQL Streaming Replication for high availability and point-in-time recovery.
* **Database Audit & Encryption Manager**: Enforces at-rest encryption and access logging via pgcrypto, pgaudit, and TLS 1.3.
* **Database Migration Component**: Flyway integrated into the Core Domain Service build pipeline.

## Relationships
* **Core Domain Service -> PgBouncer**: Client queries via [TCP/PostgreSQL Wire Protocol] over [TLS 1.3].
* **PgBouncer -> Schemas (Catalog, Circulation, Audit, User Management)**: Routed transactions via [TCP].
* **Core Domain Service -> Search Service (OpenSearch)**: Asynchronous index updates via [Apache Kafka] to meet the <800ms search response NFR.
* **Primary Node -> Standby Node**: Continuous WAL archiving via [TCP/PostgreSQL Streaming Replication].
* **Flyway -> Database Schemas**: Automated schema migrations via [JDBC].

## Technology Stack
* **PostgreSQL**: Relational database chosen for strict transactional integrity.
* **PgBouncer**: Manages connection spikes and prevents exhaustion under high traffic.
* **Barman & PostgreSQL Streaming Replication**: Ensures high availability and disaster recovery within EU borders.
* **pgcrypto & pgaudit**: Provides column/data encryption at rest and audit logging.
* **Flyway**: Automates database versioning and schema migrations.

## Rationale
This component architecture enforces strict EU-only data residency and regulatory compliance using isolated database schemas and RLS. It guarantees high availability and performance by offloading text search to OpenSearch and utilizing connection pooling and streaming replication.