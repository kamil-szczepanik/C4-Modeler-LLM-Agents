## Overview
• Manages catalogue circulation and self-service portals for public and academic libraries.
• Enforces EU-only data residency while ensuring sub-800ms search performance.

## Key Elements
• Primary Database Instance (PostgreSQL with GIN indexes, pgAudit, pg_stat_statements)
• Read Replica (Asynchronous PostgreSQL replica)
• Schemas: Core Domain Schema, Audit Log Schema, Archival Schema
• Connection Pooling: PgBouncer
• Management: Cloud Native PG operator, EU Cloud Region Provider

## Relationships
• Catalog API & Search Service -> Core Domain Schema: Queries/updates relational data and GIN indices [TCP/SSL via Npgsql]
• Librarian Workbench -> Audit Log Schema: Writes immutable override transactions [TCP/SSL]
• Librarian Workbench -> Read Replica: Executes institutional reporting queries [TCP/SSL]
• Primary Database Instance -> Read Replica: Streams WAL data for asynchronous replication [TCP/SSL via mTLS]

## Technology Stack
• PostgreSQL: Relational storage and full-text search via GIN indexes supporting sub-800ms searches
• pgAudit & pg_stat_statements: Native extensions for compliance logging and performance monitoring
• PgBouncer: Connection pooling to prevent resource exhaustion
• Cloud Native PG: Automated multi-AZ high availability and failover management

## Rationale
• PostgreSQL with GIN indexes ensures sub-800ms search responses for patrons and fast lookups for librarians.
• Segregating read-heavy administrative reporting onto an asynchronous replica protects core transaction performance.