## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its database architecture ensures high performance, GDPR compliance, and strict EU-only data residency.

## Key Elements
* **PostgreSQL Container:** Core relational data store housing catalogue and circulation data.
* **PgBouncer:** Connection pooler managing client connections and statement timeouts.
* **PostgreSQL Core (Relational Data Engine):** Stores structured data and enforces row/column-level security (RLS/CLS).
* **pgaudit Extension:** Captures detailed statements and session audit logs for PII access.
* **pgcrypto Extension:** Handles transparent column-level encryption for sensitive patron data.
* **Redis Asynchronous Broker:** Decouples the Search Service from PostgreSQL via domain events.

## Relationships
* **Core Domain Service -> PgBouncer:** Relational reads/writes [JDBC/TLS with mutual TLS and SCRAM-SHA-256].
* **PgBouncer -> Relational Data Engine:** Routes and manages pooled connections [TCP].
* **Relational Data Engine -> pgaudit:** Emits database activity logs [Internal].
* **Core Domain Service -> Redis:** Publishes domain events for search index updates [Async Protocol].

## Technology Stack
* **PostgreSQL:** Primary relational database chosen for robust ACID compliance and security extensions.
* **PgBouncer:** Connection pooler selected to prevent thread exhaustion and enforce resource quotas.
* **pgaudit & pgcrypto:** Native extensions chosen to satisfy GDPR compliance and EU data residency constraints.
* **HashiCorp Vault:** Secret management tool utilized for dynamic database credentials and short-lived tokens.
* **Prometheus & Fluentbit:** Monitoring and log-shipping tools used for performance tracking and off-site audit log storage.

## Rationale
This architecture guarantees sub-800ms search responses and transactional performance by decoupling heavy indexing via Redis and utilizing analytics read-replicas. Strict encryption, audit logging, and EU-pinned backups ensure full GDPR compliance and data residency constraints.