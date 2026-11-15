## Overview
The Database component provides secure, highly available, and EU-compliant relational data storage for the Library Management System. It handles transactional integrity, multi-tenant isolation, and encrypted persistence for catalogue and patron records.

## Key Elements
- Relational Storage Engine (PostgreSQL 15)
- Connection Pool Manager (HikariCP)
- Read Replica Engine
- Secrets Management Agent
- Security & Encryption Engine
- Automated Backup & PITR Engine
- Replica Sync Monitor
- Audit & Replication Log

## Relationships
- Core Domain Microservice -> Connection Pool Manager [JDBC / TCP with TLS 1.3 and mTLS]
- Connection Pool Manager -> Relational Storage Engine [Internal IPC]
- Secure Vault -> Secrets Management Agent [HTTPS / REST]
- Secrets Management Agent -> Relational Storage Engine [Internal IPC]
- Security & Encryption Engine -> OpenTelemetry Collector [OTLP]
- Automated Backup & PITR Engine -> EU-Only Object Storage Bucket [HTTPS]

## Technology Stack
- PostgreSQL 15: Selected for robust ACID compliance, Row-Level Security (RLS), and pgcrypto extension support.
- HikariCP: Chosen for high-performance connection pooling to meet concurrency and performance targets.
- HashiCorp Vault: Utilized for dynamic credential generation, key management, and automated rotation.
- pgaudit & OpenTelemetry: Deployed for comprehensive security auditing and centralized observability.

## Rationale
This architecture ensures strict EU data residency and high availability while meeting performance constraints. Security controls like mTLS, RLS, and encrypted PITR backups satisfy compliance mandates without degrading transaction speeds.