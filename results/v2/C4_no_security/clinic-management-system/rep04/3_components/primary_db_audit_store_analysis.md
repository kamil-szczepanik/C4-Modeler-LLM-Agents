## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers in a hybrid cloud architecture. It ensures HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention policy.

## Key Elements
- Transactional Data Store Component (PostgreSQL)
- Audit Logging Subsystem (`pg_audit` + WORM tables)
- High Availability Manager (Patroni + etcd)
- Partitioning & Archival Worker
- Security & Access Control Component (PostgreSQL Row-Level Security)
- GDPR Anonymization & Retention Worker
- Connection Pooler (PgBouncer)
- Log Shipper (Fluentbit / Vector)

## Relationships
- Clinical & EMR Core & Billing Containers -> Transactional Data Store Component [PostgreSQL Protocol]
- Transactional Data Store -> Audit Logging Subsystem [Asynchronous internal triggers]
- Audit Logging Subsystem -> SIEM / Object Storage [Fluentbit / Vector sidecars]
- Core Containers -> Security & Access Control Component [Database-level RLS interception]

## Technology Stack
- **PostgreSQL with Patroni & etcd:** Relational storage with active-active/passive failover to meet 99.99% uptime.
- **PostgreSQL Row-Level Security (RLS) & `pg_audit`:** Database-level security and immutable audit trails for HIPAA/GDPR.
- **PgBouncer:** Connection pooling to prevent CPU contention and protect the <1s P95 SLA.
- **Fluentbit / Vector:** Log forwarding for tamper-proof 10-year audit retention.

## Rationale
This component architecture enforces strict security and compliance controls at the database layer while isolating resource-intensive background tasks. This guarantees high availability, sub-second query performance, and long-term regulatory adherence across hybrid environments.