## Overview
[The system is a Library Management System providing cataloguing, circulation, and self-service portals for public and academic libraries. It relies on a hardened PostgreSQL persistence tier designed for EU data residency compliance and strict performance SLAs.]

## Key Elements
- **PostgreSQL 16 Primary & Standby:** Relational storage engine managing ACID-compliant circulation, loans, and structured catalogue metadata.
- **PgBouncer:** Connection pooler managing client connections from Spring Boot microservices.
- **Patroni / etcd:** Replication manager providing automated leader election and streaming replication.
- **CloudNativePG Operator:** Kubernetes-based deployment manager for PostgreSQL.
- **pgaudit Extension:** Module generating structured audit logs for patron PII access.

## Relationships
- **Circulation & Loan Service Container -> PgBouncer:** Transactional queries and updates via [JDBC / TLS 1.3].
- **PgBouncer -> PostgreSQL Primary:** Backend database connections via [TLS 1.3].
- **PostgreSQL Primary -> PostgreSQL Standby:** Asynchronous/Synchronous streaming replication via [TCP].
- **PostgreSQL Standby -> Centralized SIEM:** Out-of-band audit log streaming via [Syslog / TLS].

## Technology Stack
- **PostgreSQL 16:** Relational database chosen for robust ACID compliance and robust extension support.
- **PgBouncer:** Connection pooler selected to prevent thread exhaustion under high concurrent load.
- **Patroni and etcd:** High availability stack chosen for automated failover and leader election.
- **pgaudit:** Extension selected for granular, tamper-evident audit logging of PII.
- **CloudNativePG:** Kubernetes operator chosen for automated operational lifecycle management.

## Rationale
[This architecture ensures 99.9% availability and meets the <800ms performance SLA through connection pooling, automated failover, and table partitioning. It guarantees strict EU GDPR compliance via TDE, TLS 1.3, and isolated subnets.]