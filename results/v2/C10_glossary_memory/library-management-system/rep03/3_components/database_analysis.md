## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The system is designed with a PostgreSQL database container ensuring strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Relational Data Store (PostgreSQL Engine)
- Connection Pooler (PgBouncer)
- Audit Logging Module (pgAudit)
- HA Failover Manager (Patroni)
- Backup & Archival Agent (Barman / WAL-G)
- Circulation Service
- Catalog & Search Service

## Relationships
- Circulation Service -> Connection Pooler: Submits loan and fine transactions [SQL over mTLS]
- Catalog & Search Service -> Connection Pooler: Queries and updates item metadata [SQL over mTLS]
- Connection Pooler -> Relational Data Store: Forwards pooled queries [TCP/IP]
- Relational Data Store -> Audit Logging Module: Emits audit logs [Internal IPC]

## Technology Stack
- PostgreSQL: Provides robust ACID compliance and row-level security for transactional integrity.
- PgBouncer: Manages and optimizes incoming database connections under peak load.
- pgAudit: Captures security-relevant DDL/DML events for compliance.
- Patroni: Handles automated leader election and high availability across availability zones.
- Barman / WAL-G: Manages continuous WAL archiving and point-in-time recovery.

## Rationale
This architecture ensures strict EU-only data residency compliance and high availability for transactional workloads. The component layout protects system stability under heavy academic semester traffic while maintaining data security and PII isolation.