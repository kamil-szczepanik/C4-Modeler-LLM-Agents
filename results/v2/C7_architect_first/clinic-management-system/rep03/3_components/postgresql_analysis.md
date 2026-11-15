## Overview
- A secure, high-availability Clinic Management System designed for medium-sized hospitals and clinics.
- Manages patient admissions, EMR, scheduling, and billing while enforcing strict HIPAA and GDPR compliance.

## Key Elements
- Database Engine (PostgreSQL v16 with `pgaudit`, Row-Level Security, and TDE)
- Connection Pooler (PgBouncer)
- Replication Agent (Patroni + etcd)
- Storage & Backup (AWS S3 Object Lock)
- Secret Management (HashiCorp Vault)

## Relationships
- Core Services to PgBouncer: `[TCP / mTLS, port 6432]` with X.509 client certificate authentication
- PgBouncer to Database Engine: `[TCP / mTLS, port 5432]` enforcing TLS 1.3
- Database Engine to AWS S3: `[HTTPS / TLS 1.3]` for continuous WAL archiving and backups
- Patroni to etcd: `[Internal IPC / TCP]` for cluster health checks and leader election

## Technology Stack
- PostgreSQL v16: Relational database providing robust storage and querying capabilities
- Patroni + etcd: Orchestrates automated failover for primary-standby deployment to hit 99.99% uptime
- PgBouncer: Manages incoming connections to maintain performance during peak clinic hours
- AWS S3 Object Lock: Ensures immutable 10-year data retention for backups and audit logs
- HashiCorp Vault: Automates short-lived X.509 certificate rotation and dynamic credential generation

## Rationale
- This architecture uses a cost-effective Patroni primary-standby model to meet 99.99% availability without complex multi-master scaling overhead.
- Comprehensive security controls like RLS, `pgaudit`, mTLS, and AES-256 encryption at rest directly satisfy healthcare compliance mandates.