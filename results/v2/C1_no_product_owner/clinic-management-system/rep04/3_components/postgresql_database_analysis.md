## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It features a hybrid cloud architecture designed for high availability, security, and strict regulatory compliance.]

## Key Elements
- PostgreSQL v15+ Primary Database Engine
- Read Replica Instances
- PgBouncer Connection Pooler
- Patroni / CloudNativePG Automated Failover Orchestrator
- pgBackRest Backup & PITR Agent
- postgres-exporter Observability Exporter
- Vault Agent / Sidecar (HashiCorp Vault)
- pgaudit Extension

## Relationships
- Microservices -> PgBouncer: TCP/IP with TLS 1.3
- PgBouncer -> Primary Database Engine: TCP/IP via Internal Mesh
- Primary Database Engine -> Read Replica Instances: Streaming Replication with mTLS / IPsec
- Primary Database Engine -> pgBackRest: Encrypted WAL streams to WORM Storage [AES-256]
- Vault Agent -> PgBouncer: Supplies dynamic credentials via TLS 1.3 [SCRAM-SHA-256]

## Technology Stack
- PostgreSQL v15+: Core transactional engine for strong consistency and relational data integrity
- PgBouncer: Connection pooling to prevent thread exhaustion under high concurrency
- Patroni / CloudNativePG: Consensus-based leader election and automated failover for 99.99% availability
- HashiCorp Vault: Dynamic secrets management to eliminate hardcoded database credentials
- pgBackRest & WORM Storage: Secure backups satisfying 10-year data retention and compliance mandates
- pgaudit & Row-Level Security: Detailed audit logging and data masking for HIPAA and GDPR compliance

## Rationale
[The architecture employs active-active hybrid patterns, automated consensus-driven failover, and rigorous encryption to meet 99.99% availability and strict healthcare compliance mandates. Component-level segregation ensures optimal P95 read performance while securing patient health information.]