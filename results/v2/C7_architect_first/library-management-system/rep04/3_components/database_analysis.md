## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. Its database architecture ensures secure, high-performance transactional processing while maintaining strict EU data residency compliance.

## Key Elements
- Database Container (PostgreSQL)
- Connection Pooler (PgBouncer)
- Relational Storage Engine (PostgreSQL Core)
- Read-Replica Routing Layer
- Row-Level Security (RLS) Policy Engine
- Audit Logging Module (pgaudit)
- Patroni Primary-Replica Cluster with etcd
- HashiCorp Vault

## Relationships
- Core Services Container -> Connection Pooler: Manages persistent connections [JDBC/TCP, TLS 1.3]
- Connection Pooler -> Relational Storage Engine: Routes write and transactional queries [TCP]
- Connection Pooler -> Read-Replica Routing Layer: Routes read-only queries [TCP]
- Read-Replica Routing Layer -> PostgreSQL Replicas: Distributes read queries [TCP, mTLS]
- Telemetry Container -> Database: Scrapes metrics and replication lag [Prometheus exporter]

## Technology Stack
- PostgreSQL: Core relational data storage enforcing ACID compliance
- PgBouncer: Inbound connection management to prevent exhaustion under load
- Patroni & etcd: Automated high-availability failover and consensus management
- HashiCorp Vault: Dynamic, short-lived database credential provisioning
- pgaudit: Security and administrative event capture for compliance reporting
- AES-256 and TDE: Column-level and storage volume encryption for EU data residency

## Rationale
This architecture uses a primary-replica PostgreSQL cluster with read routing to achieve 99th-percentile search response times under 800 ms. Strict EU-only encryption, RLS policies, and dynamic credentials ensure robust data protection and regulatory compliance.