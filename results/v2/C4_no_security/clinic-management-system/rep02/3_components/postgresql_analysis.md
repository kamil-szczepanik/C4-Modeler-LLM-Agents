## Overview
The Clinic Management System is a hybrid-cloud clinical IT platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides high-availability, HIPAA/GDPR-compliant healthcare operations across medium-sized hospitals and clinics.

## Key Elements
- PostgreSQL 16 (Operational Database Engine)
- Row-Level Security (RLS) Enforcer
- Partition Manager
- CDC Outreach Publisher (Debezium)
- Encryption & Masking Module
- PgBouncer (Connection Pooling)
- Tiered Storage (S3-compatible)
- Apache Kafka

## Relationships
- Clinical Services -> PostgreSQL (Encryption & Masking Module): Queries encrypted/masked PHI [JDBC / TLS 1.3]
- Billing Services -> PostgreSQL: Reads and writes billing data [JDBC / TLS]
- PostgreSQL (Partition Manager) -> Tiered Storage: Offloads cold historical records [S3 API / HTTPS]
- PostgreSQL (CDC Publisher) -> Apache Kafka: Publishes audit logs and event streams [TCP / Kafka Wire Protocol]

## Technology Stack
- PostgreSQL 16: Relational database engine chosen for robust ACID compliance and advanced partitioning features.
- Debezium: Change Data Capture tool selected for reliable streaming of audit logs and events.
- PgBouncer: Connection pooling utility implemented to protect database resources under heavy clinical loads.
- pgBackRest: Backup framework utilized for automated Point-in-Time Recovery and disaster recovery drills.
- S3-compatible Tiered Storage: Cost-effective storage backend chosen to meet the ≥ 10 years data retention mandate.

## Rationale
This component architecture ensures sub-second EMR performance by decoupling hot operational data from cold archival records via partitioning and S3 offloading. Furthermore, native PostgreSQL encryption, RLS, and CDC mechanisms fulfill stringent HIPAA, GDPR, and 99.99% availability requirements.