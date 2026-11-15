## Overview
The Library Management System provides item cataloging, circulation, and self-service portals with strict EU data residency constraints. The PostgreSQL database container is decomposed into components ensuring high availability, performance, and compliance.

## Key Elements
- **Relation Engine (PostgreSQL 15):** Handles ACID transactions, B-Tree indexes, and foreign keys.
- **Connection Pooler (PgBouncer):** Manages client sessions from the Core Domain Service.
- **Read-Only Routing Proxy (HAProxy):** Routes read-heavy queries to streaming replicas.
- **Replication Manager (Patroni):** Manages EU-region synchronous replication.
- **Backup & Archival Agent (pgBackRest):** Handles point-in-time recovery and EU-bound storage.
- **Security & Audit Subsystem (pgAudit):** Logs DDL/DML operations for compliance.
- **Query Optimizer & Statistics Engine:** Evaluates execution plans with GIN/B-Tree indexes.
- **Extension Schema (pg_stat_statements):** Tracks execution metrics for performance tuning.

## Relationships
- Core Domain Service -> Connection Pooler: Manages database sessions [TCP / TLS 1.3]
- Core Domain Service -> Read-Only Routing Proxy: Submits read-only queries [TCP / TLS 1.3]
- Connection Pooler -> Relation Engine: Forwards write queries [TCP]
- Relation Engine -> Replication Manager: Streams WAL data [TCP / TLS 1.3]
- Backup & Archival Agent -> Relation Engine: Reads WAL archives [Local Disk / S3 EU-Central bucket]

## Technology Stack
- **PostgreSQL 15:** Core relational database for robust ACID transactions.
- **PgBouncer:** Efficient connection pooling to prevent exhaustion.
- **HAProxy:** Offloads read queries to replica nodes.
- **Patroni:** Ensures high availability and streaming replication.
- **pgBackRest:** Reliable backup and EU-compliant archival.
- **pgAudit:** Comprehensive security and operation auditing.

## Rationale
This architecture ensures strict EU-only data residency via isolated replica nodes and regional backups. Additionally, connection pooling and read-replication guarantee performance SLAs under 800ms.