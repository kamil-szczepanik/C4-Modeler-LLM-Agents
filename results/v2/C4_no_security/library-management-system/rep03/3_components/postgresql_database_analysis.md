## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The PostgreSQL database tier ensures transactional persistence, strict EU data residency compliance, and zero data loss for library patrons.

## Key Elements
- PostgreSQL Database Container: Core relational data store
- Relational Schema / Core Tables: ACID-compliant normalization for Patrons, Items, and Loans
- PgBouncer: Connection pooler managing concurrent connections
- WAL (Write-Ahead Log) Archiver: Synchronous replication engine
- Patroni with etcd: Automated high-availability and consensus store
- pgaudit: Extension for GDPR-compliant audit logging
- Fluentbit: Sidecar for log and audit forwarding

## Relationships
- Circulation & Core Container -> PgBouncer: Acquires database sessions [TCP/PostgreSQL Wire Protocol]
- PgBouncer -> Relational Schema / Core Tables: Routes queries [TCP]
- Relational Schema / Core Tables -> WAL Archiver: Streams replication logs [TCP]
- Patroni / etcd -> Relational Schema / Core Tables: Orchestrates cluster state & failover [TCP]

## Technology Stack
- PostgreSQL: Core relational database engine for ACID transactional integrity
- PgBouncer: Connection pooling to prevent thread exhaustion during traffic spikes
- Patroni & etcd: Automated leader election and high availability clustering
- pgaudit: Native extension for tamper-evident GDPR audit logging
- Fluentbit: Secure log forwarding sidecar to centralized SIEM

## Rationale
This architecture guarantees strict EU data residency while maintaining high availability and zero data loss (RPO = 0) during peak academic semester traffic spikes. PgBouncer and cgroup resource pinning ensure predictable performance under heavy circulation loads.