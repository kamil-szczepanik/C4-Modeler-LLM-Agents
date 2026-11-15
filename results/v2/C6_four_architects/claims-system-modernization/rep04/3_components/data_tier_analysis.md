## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern hybrid cloud architecture. Its core purpose is to ensure continuous, reliable claims processing, online submission, and adjuster workflows while maintaining strict data consistency and a 3-year migration path.

## Key Elements
* Azure Database for PostgreSQL: Central relational database instance.
* Transactional Store (OLTP): Manages incoming claims and migrated states in the `core_oltp` schema.
* CQRS Read Model Store: Optimized denormalized tables in the `read_models` schema for fast UI queries.
* Migration Sync State Ledger: Tracks dual-write/sync status and sequence IDs in the `core_oltp` schema.
* Archival & Purge Worker: Background service utilizing PostgreSQL `pg_cron` and native table partitioning.

## Relationships
* Application Tier -> Data Tier: Read/write operations and connection pooling [PostgreSQL Protocol / JDBC]
* Application Tier -> Transactional Store: Reads and writes claims data [PostgreSQL Protocol / JDBC]
* Application Tier -> Read Model Store: Fast queries for UI display [PostgreSQL Protocol / JDBC]
* Application Tier -> Migration Sync State Ledger: Validates claim migration status and prevents double-processing [PostgreSQL Protocol / JDBC]
* Integration Tier -> Data Tier / Migration Sync State Ledger: Asynchronous state synchronization and updates from mainframe batch events [PostgreSQL Protocol / JDBC]
* Transactional Store -> Archival Worker: Triggers data partitioning and archiving routines [Internal SQL / PostgreSQL `pg_cron`]

## Technology Stack
* Azure Database for PostgreSQL: Chosen for robustness, relational consistency, and alignment with the team's limited cloud experience.
* PostgreSQL Schemas (`core_oltp` and `read_models`): Simplifies connection management and isolates transactional data from read models.
* PostgreSQL `pg_cron` and Native Table Partitioning: Automates historical claim data retention for sustained performance.

## Rationale
This architecture fits the requirements by decoupling fast UI reads from slow legacy dependencies to guarantee sub-2-second response times. Additionally, the dedicated migration ledger and relational schema design ensure strict zero-data-loss consistency and rapid rollback capabilities during the phased 3-year mainframe migration.