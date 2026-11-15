## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance, and high-performance clinical workflows.

## Key Elements
- PostgreSQL Primary Instance (AWS RDS / On-Prem StatefulSet)
- Read Replica Cluster
- Connection Pooler (PgBouncer)
- Encryption & Backup Daemon
- Schema-Per-Service Isolation (Core Clinical, Scheduling, Billing schemas)
- Flyway/Liquibase Migration Engine

## Relationships
- Microservices to PgBouncer: PostgreSQL wire protocol over TLS 1.3
- PgBouncer to PostgreSQL Instances: TCP/SSL connection pooling
- Encryption & Backup Daemon to AWS S3 Object Lock: WAL streaming for immutable archival via HTTPS

## Technology Stack
- PostgreSQL: Relational database providing enterprise reliability and data integrity.
- PgBouncer: Connection pooler to manage high connection concurrency and prevent resource starvation.
- AWS RDS Multi-AZ: Cloud-managed primary database ensuring automated failover and 99.99% availability.
- pgaudit & pgcrypto: PostgreSQL extensions enforcing deep audit logging and column-level encryption for HIPAA/GDPR compliance.
- Flyway/Liquibase: Database migration engines ensuring idempotent schema updates via CI/CD pipelines.

## Rationale
This architecture uses schema isolation, connection pooling, and managed replication to meet strict sub-second performance and 99.99% availability requirements. Furthermore, native auditing and encryption safeguards satisfy mandatory healthcare data privacy regulations like HIPAA and GDPR.