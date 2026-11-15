## Overview
The Data Storage component provides transactional persistence for the Library Management System, prioritizing strict EU data residency and high-concurrency performance for cataloging and checkouts. It supports low-latency operations while enforcing rigorous security and audit compliance standards.

## Key Elements
- PostgreSQL 16 (Primary & Read-Replicas)
- PgBouncer (Connection Pooling)
- Patroni (Automated High Availability Failover)
- Debezium / Kafka Connect (Asynchronous WAL Streaming)
- EU-Resident Object Storage (Encrypted Backups & PITR)
- Prometheus & OpenTelemetry (Observability Stack)

## Relationships
- Core Domain Services -> PostgreSQL (Primary): Persists relational aggregates [SQL / JDBC over TLS 1.3]
- Staff Dashboard / Reporting -> PostgreSQL (Read-Replicas): Offloads non-critical read queries [SQL / JDBC over TLS 1.3]
- PostgreSQL -> EU-Resident Log & Audit Sink: Streams Write-Ahead Logs asynchronously [Debezium / Apache Kafka]
- Core Domain Services -> PgBouncer: Manages high-concurrency client connections [TCP / TLS 1.3]

## Technology Stack
- PostgreSQL 16: Selected for native JSONB metadata support (R-01) and robust transactional integrity
- PgBouncer: Implemented to prevent thread exhaustion under high concurrency from self-service kiosks
- Patroni: Deployed for automated multi-AZ primary-replica failover in the EU region
- Transparent Data Encryption (TDE): Enforced with customer-managed keys (CMK) for data-at-rest security

## Rationale
This architecture ensures strict compliance with EU-only data residency constraints via regional hosting and encrypted backups. Furthermore, read-replication, connection pooling, and asynchronous auditing protect core performance SLAs (R-05) during peak library operational periods.