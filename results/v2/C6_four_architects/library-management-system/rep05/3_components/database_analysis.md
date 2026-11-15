## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its database architecture ensures transactional consistency, EU data residency, and high-performance search support.

## Key Elements
* **Relational Data Store:** PostgreSQL Managed RDS engine storing core transactional entities.
* **Connection Pooler:** PgBouncer managing inbound database connections.
* **Read Replica:** PostgreSQL Replica handling read-heavy queries and reporting.
* **WAL Publisher:** Emits transaction logs for Change Data Capture (CDC).
* **Backup & Snapshot Manager:** AWS RDS Automated Backups enforcing region-locked recovery.
* **Audit & Security Monitor:** `pgaudit` capturing security events and query logs.
* **Database Schema Migration Engine:** Flyway or Liquibase for version-controlled schema evolution.

## Relationships
* **Core Services Container -> Connection Pooler:** `JDBC over TLS`
* **Core Services Container -> Read Replica:** `JDBC over TLS (Read-Only)`
* **Core Services Container -> Relational Data Store:** `JDBC over TLS (DDL execution)`
* **WAL Publisher -> Search Container:** `TCP/TLS stream (Debezium CDC)`
* **Primary Engine -> Read Replica:** `PostgreSQL Streaming Replication [TCP/TLS]`
* **Relational Data Store -> Backup & Snapshot Manager:** `Internal AWS Storage API over TLS`
* **Audit & Security Monitor -> File Storage Container:** `HTTPS / S3 API`

## Technology Stack
* **PostgreSQL Managed RDS:** Selected for ACID compliance, relational integrity, and robust extension support.
* **PgBouncer:** Utilized to prevent connection exhaustion under peak circulation loads.
* **Debezium:** Enables low-latency CDC to meet the <800ms search NFR.
* **AWS S3 EU-Central:** Secures encrypted backups and audit log archival within EU boundaries.
* **pgaudit:** Enforces enterprise-grade security and compliance logging.

## Rationale
This architecture uses read-replicas and WAL-based CDC to protect write performance and achieve sub-800ms search requirements. All components, backups, and logs remain strictly within the `eu-central-1` region to satisfy EU data residency mandates.