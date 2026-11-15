## Overview
- The Library Management System provides self-service portals, circulation management, and cataloging for academic and public libraries.
- The system is designed to meet strict EU data residency constraints and sub-800ms search performance SLAs.

## Key Elements
- **Database Container**: PostgreSQL primary-replica cluster hosted in an EU region (Frankfurt).
- **Connection Pooler**: PgBouncer managing incoming database connections.
- **Relational Storage Engine**: PostgreSQL core with `pg_trgm` extension for fuzzy matching.
- **Logical Replication Slot**: PostgreSQL internal mechanism for Change Data Capture (CDC).
- **Core Services Container**: Java Spring Boot application handling business logic.
- **Search Worker Container**: Debezium-based CDC consumer syncing data to Elasticsearch.

## Relationships
- **Core Services Container -> Connection Pooler (PgBouncer)**: Routes transactional queries via TCP using the PgBouncer protocol.
- **Connection Pooler (PgBouncer) -> Relational Storage Engine**: Forwards queued client connections via TCP and Unix Domain Sockets.
- **Relational Storage Engine -> Logical Replication Slot**: Streams Write-Ahead Log (WAL) data.
- **Logical Replication Slot -> Search Worker Container**: Streams database changes via PostgreSQL CDC over TCP.

## Technology Stack
- **PostgreSQL**: Chosen for robust relational storage and EU data residency compliance.
- **PgBouncer**: Selected to prevent connection exhaustion from heavy self-service portal traffic.
- **pg_trgm Extension**: Implemented for fast trigram-based fuzzy matching to meet performance SLAs.
- **Logical Replication / Debezium**: Utilized for real-time CDC without polling overhead.

## Rationale
- The PostgreSQL-based architecture ensures strict EU data residency while supporting high-throughput transactions.
- Internal components like PgBouncer and `pg_trgm` directly support the required performance SLAs and connection scaling.