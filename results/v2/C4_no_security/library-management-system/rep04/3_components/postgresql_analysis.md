## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It guarantees secure, high-performance operations while enforcing strict EU data residency and GDPR compliance.

## Key Elements
- PostgreSQL 16: Core relational engine for structured tables (`Patrons`, `Inventory`, `Circulation_Transactions`).
- PgBouncer: Connection pooler managing backend processes over TCP.
- pgaudit: Audit logging extension for DDL/DML security activity.
- Managed Multi-AZ Cluster: EU-central-1 deployment (AWS RDS/Azure Database) with automatic failover.
- pg_partman: Extension for time-based partitioning of `Circulation_Transactions`.

## Relationships
- Circulation Service -> PgBouncer: Connection pooling and queries [TCP / PostgreSQL Wire Protocol]
- PgBouncer -> PostgreSQL Engine: Forwards queries [TCP / PostgreSQL Wire Protocol]
- Circulation Service -> PostgreSQL Engine: Executes GDPR anonymization routines [TCP / PostgreSQL Wire Protocol]
- PostgreSQL Engine -> EU-hosted Log & Metrics Aggregator: Streams metrics via Prometheus exporter [HTTPS]

## Technology Stack
- PostgreSQL 16: Chosen for robust ACID compliance required for financial fines and inventory accuracy.
- PgBouncer: Selected to prevent connection thread exhaustion from Spring Boot services under peak load.
- Logical Schema Segregation & pg_partman: Utilized for efficient GDPR data purging via partition drop operations without table locks.
- PL/pgSQL Triggers & RLS: Implemented for automated PII anonymization and masking.

## Rationale
This architecture ensures strict legal compliance with EU data residency and GDPR right-to-be-forgotten mandates through regional hosting and automated purging. Furthermore, it guarantees high availability, rapid disaster recovery, and transactional integrity for critical library operations.