## Overview
The Library Management System is a EU-hosted platform for public and academic libraries to catalogue items and manage circulation. The Database component provides secure, highly available transactional storage with strict compliance and performance guarantees.

## Key Elements
- Relational Engine - Primary (PostgreSQL)
- Relational Engine - Read Replica (PostgreSQL)
- Connection Pooler (PgBouncer)
- Replication Manager (Patroni/Stolon)
- Audit Container (Go)

## Relationships
- Core Services Container -> PgBouncer: Read queries [TCP/mTLS] routed to Read Replica
- Core Services Container -> PgBouncer: Writes and transactions [TCP/mTLS] routed to Primary
- PostgreSQL -> Audit Container: Stream audit logs (`pgaudit`) [mTLS sidecar]

## Technology Stack
- PostgreSQL: Provides relational storage with Write-Ahead Logging (WAL) for durability and point-in-time recovery.
- PgBouncer: Manages connection pools and routing targets to prevent thread exhaustion.
- Patroni/Stolon: Automates High Availability and failover across EU availability zones.
- Prometheus/Grafana: Monitors replication lag, connection saturation, and query latency.
- AES-256 TDE & EU KMS: Secures data at rest per EU residency constraints.

## Rationale
This architecture ensures strict EU data residency compliance, GDPR adherence via Row-Level Security and audit logging, and sub-800ms performance by separating read and write workloads. High availability mechanisms and backup strategies prevent data loss during peak academic periods.