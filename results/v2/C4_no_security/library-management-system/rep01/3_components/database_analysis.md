## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system ensures strict EU-only data residency and sub-800ms transaction responsiveness.

## Key Elements
- PostgreSQL 16: Relational database storing transactional library data within the EU.
- PgBouncer: Sidecar connection pooler managing high concurrent connection spikes.
- pg_partman: Extension automating time-series data partitioning for historical logs.
- `secure_pii` Schema: Isolated database schema containing patron personal profiles.
- `postgres_exporter`: Sidecar exporting Prometheus metrics for query latency tracking.
- `pgaudit` Extension: Tool for streaming security and access logs to centralized SIEM.

## Relationships
- Core Services API -> PgBouncer: TCP/IP via PostgreSQL Wire Protocol with TLS 1.3
- PgBouncer -> PostgreSQL 16: Internal connection pooling via TCP/IP
- PostgreSQL 16 -> Centralized SIEM Platform: Log streaming via `pgaudit`

## Technology Stack
- PostgreSQL 16: Chosen for predictable data footprint control and EU data residency compliance.
- PgBouncer: Selected to handle high concurrent connection spikes from the Core Services API.
- pg_partman: Deployed for automated time-series partitioning to prevent index bloat and maintain query performance.
- Vault: Utilized for secret management and mandatory TLS 1.3 certificate injection.

## Rationale
This architecture satisfies strict EU data residency and GDPR privacy-by-design requirements through isolated PII vaults and automated pseudonymization. Furthermore, multi-AZ clustering, connection pooling, and table partitioning guarantee high availability and sub-800ms performance during peak academic periods.