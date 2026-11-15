## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries within the EU. The PostgreSQL Read Replica offloads analytical queries to protect core transactional performance.

## Key Elements
- PostgreSQL Read Replica (PostgreSQL 15+)
- PostgreSQL Engine (Read-Only)
- Streaming Replication Receiver
- Connection Pooler (PgBouncer)
- Write-Ahead Log (WAL) Replayer
- Prometheus PostgreSQL Exporter
- Reporting Service (Python/FastAPI)

## Relationships
- Primary PostgreSQL -> PostgreSQL Read Replica: Asynchronous replication [Binary Streaming via TCP with mTLS]
- Reporting Service -> PostgreSQL Read Replica (via PgBouncer): Queries analytics data [SQL over mTLS]
- Prometheus -> Prometheus PostgreSQL Exporter: Scrapes metrics [HTTP with mTLS/Basic Auth]

## Technology Stack
- PostgreSQL 15+: Native streaming replication and robust read replica capabilities
- PgBouncer: Manages analytical connection spikes and prevents connection exhaustion
- Prometheus PostgreSQL Exporter: Exposes database performance and replication lag metrics
- pgaudit: Tracks analytical query patterns for security compliance
- Transparent Data Encryption (TDE): Secures data at rest using EU-hosted KMS keys

## Rationale
This architecture offloads heavy analytical queries to protect core circulation response times under 800ms. It enforces strict EU-only data residency and security compliance while maintaining a sub-5-second replication lag SLA.