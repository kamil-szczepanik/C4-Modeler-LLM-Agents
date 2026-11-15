## Overview
The Transactional Data Store provides secure, tamper-evident case management and audit logging for the Real-Time Payment Fraud Screening system on AWS. It ensures strict PCI-DSS compliance, 7-year auditability, and reliable persistence for fraud analyst workflows.

## Key Elements
- Transactional Data Store (Amazon Aurora PostgreSQL)
- RDS Proxy
- Case Repository Component
- Audit Ledger Component
- Database Migration Component

## Relationships
- Case Management Backend -> RDS Proxy: Routes database traffic [PostgreSQL Wire Protocol]
- RDS Proxy -> Case Repository & Audit Ledger: Forwards pooled queries [PostgreSQL Wire Protocol]
- Audit Ledger -> Audit Archival Storage: Streams append-only logs [HTTPS]
- CI/CD Pipeline -> Database Migration Component: Executes schema updates [HTTPS]

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for managed relational capabilities, high availability, and native feature support within budget.
- RDS Proxy: Selected for managed connection pooling and resilience against traffic spikes without operational overhead.
- PostgreSQL pgcrypto & Append-Only Tables: Implemented to guarantee tamper-evident audit logs satisfying R-06.
- Flyway: Utilized for automated, zero-downtime database migrations supporting continuous deployments.

## Rationale
This architecture uses fully managed AWS services to minimize operational burden for a three-engineer team while meeting strict security, auditability, and availability constraints. Native PostgreSQL extensions and proxy routing ensure high performance within the 25,000 EUR monthly budget.