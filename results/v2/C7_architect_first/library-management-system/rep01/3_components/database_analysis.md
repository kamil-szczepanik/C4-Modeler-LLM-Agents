## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its database architecture ensures secure, high-performance, EU-compliant transactional storage and reporting isolation.

## Key Elements
- **Database Primary (PostgreSQL):** Manages transactional state with multi-AZ replication in the EU.
- **Database Read Replica (PostgreSQL Read Replica):** Isolates heavy reporting queries from transactional workloads.
- **PgBouncer:** Handles connection pooling to prevent connection exhaustion.
- **Catalog Schema:** Stores metadata for physical and digital items.
- **Circulation Schema:** Manages patron accounts, loans, and reservations.
- **Audit & Logging Schema:** Captures transactional state changes for observability.

## Relationships
- **Core Domain Service -> Database Primary:** Reads and writes transactional data via TLS-encrypted TCP.
- **Core Domain Service -> Database Read Replica:** Routes heavy analytics and reporting queries via SQL over TLS-encrypted TCP.
- **Database Primary -> Database Read Replica:** Synchronizes transactional data via Streaming Replication over TLS-encrypted TCP.
- **Search Service -> Database Primary (Catalog Schema):** Replicates catalog changes via Change Data Capture using Debezium over TLS-encrypted TCP.
- **Async Worker -> Database Primary:** Polls and writes background job states via SQL over TLS-encrypted TCP.

## Technology Stack
- **PostgreSQL:** Managed relational database chosen for robust transactional integrity and multi-AZ support.
- **PgBouncer:** Connection pooling middleware to protect against high load connection exhaustion.
- **Debezium:** Change Data Capture tool for feeding catalog updates to Elasticsearch.
- **Transparent Data Encryption (TDE):** Uses customer-managed keys (CMK) within the EU for data-at-rest protection.
- **mTLS:** Enforces strict client certificate verification for all database and replication connections.

## Rationale
This architecture satisfies EU data residency constraints through regional multi-AZ deployment while protecting self-service portal performance via read replicas and connection pooling. Schema-level least privilege and robust encryption ensure strict data protection for patron PII.