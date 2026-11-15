## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention.

## Key Elements
- PostgreSQL Database (Core transactional data storage)
- Database Schemas (`patient_schema`, `scheduling_schema`, `emr_schema`, `billing_schema`)
- Patroni Cluster with etcd (High availability consensus and management)
- PgBouncer (Connection pooling)
- Analytics Service Read Replica (Reporting workload offloading)
- External HSM / Vault (Key management for encryption)

## Relationships
- Patient Portal Service -> PostgreSQL Database: Reads/writes patient demographics [mTLS with AES-256 at rest]
- Scheduling Service -> PostgreSQL Database: Reads/writes scheduling data with clash checks [mTLS with AES-256 at rest]
- EMR Service -> PostgreSQL Database: Reads/writes electronic medical records and audit trails [mTLS with AES-256 at rest]
- Billing Service -> PostgreSQL Database: Reads/writes insurance claims and billing [mTLS with AES-256 at rest]
- Patroni Cluster -> Analytics Replica: Streams logical replication data [TLS]

## Technology Stack
- PostgreSQL: Core relational database with declarative range partitioning for 10-year retention
- Patroni & etcd: Automated failover and high-availability cluster management
- PgBouncer: Connection pooling to maintain sub-second P95 EMR performance
- `pgaudit` & `pg_partman`: Audit logging for HIPAA compliance and data partitioning
- SCRAM-SHA-256 & mTLS: Authentication and transport security
- External HSM / Vault: AES-256 encryption key management with 90-day rotation

## Rationale
This architecture uses dedicated database schemas and connection pooling to isolate workloads, ensuring fast EMR load times under high concurrency. Patroni and streaming replication provide the active-high availability and zero-data-loss failover required for 99.99% uptime.