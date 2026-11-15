## Overview
The system is a Library Management System designed for public and academic libraries to catalogue items and manage circulation securely. It utilizes a hardened PostgreSQL 16 database architecture to meet strict EU data residency and high-performance search constraints.

## Key Elements
- Primary Database Instance (PostgreSQL 16)
- Read Replica Instances (PostgreSQL 16 Standbys)
- Connection Pooler (PgBouncer)
- Kubernetes Operator (CloudNativePG)
- Secrets Manager (HashiCorp Vault)
- Monitoring Tools (Prometheus, Grafana, PagerDuty)

## Relationships
- Core Domain Service -> PgBouncer: Routes SQL queries and transactions [TCP/TLS 1.3 with mTLS]
- Core Domain Service -> Primary Database Instance: Executes transactions and critical reads [JDBC/mTLS]
- Core Domain Service -> Read Replica Instances: Executes catalog search and read-heavy queries [JDBC/mTLS]
- PgBouncer -> Primary/Read Replicas: Forwards pooled connections [TCP/mTLS]

## Technology Stack
- PostgreSQL 16: Provides ACID compliance for circulation and JSONB support for catalog metadata (R-01).
- CloudNativePG: Automates high-availability, failover, and EU region multi-AZ deployments.
- HashiCorp Vault: Manages short-lived dynamic database credentials and AES-256 TDE encryption keys.
- pgaudit Extension: Enables rigorous audit logging for compliance.

## Rationale
This architecture ensures strict EU-only data residency and zero-trust security via end-to-end mTLS, TDE, and RLS. Explicit query routing and PgBouncer connection pooling guarantee high performance (sub-800ms searches) and eliminate read-after-write anomalies.