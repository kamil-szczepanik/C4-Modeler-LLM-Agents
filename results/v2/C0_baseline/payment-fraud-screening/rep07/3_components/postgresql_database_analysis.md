## Overview
- Real-Time Payment Fraud Screening system evaluating card-not-present payment authorizations and managing fraud analyst reviews.
- Built for a mid-size payment processor under strict PCI-DSS Level 1 and 7-year auditability constraints.

## Key Elements
- **Case Repository Component**: Manages CRUD operations and state transitions for investigator reviews.
- **Audit & Compliance Log Component**: Handles append-only decision logs and analyst override histories using partitioned tables.
- **Database Security Manager**: Enforces AWS KMS-backed encryption and PostgreSQL Row-Level Security (RLS).
- **Primary RDS Instance**: Handles transactional case state updates.
- **Read Replica**: Dedicated to analyst reporting, audit queries, and read-heavy analytics.
- **PgBouncer**: Connection pooler hosted alongside the Case Management Backend.

## Relationships
- **Case Management Backend -> Primary RDS Instance**: Executes transactional writes and state updates via [PostgreSQL Protocol / TLS 1.3].
- **Case Management Backend -> Read Replica**: Routes read-heavy analytics and case history queries via [PostgreSQL Protocol / TLS 1.3].
- **PostgreSQL Database -> Amazon CloudWatch / S3 Object Lock**: Streams audit logs using `pgaudit` via [AWS API / HTTPS].

## Technology Stack
- **Amazon RDS (PostgreSQL)**: Core database chosen for native partitioning, RLS, and strict compliance support.
- **AWS KMS**: Provides customer-managed keys (CMK) for Transparent Data Encryption (TDE) to satisfy PCI-DSS Level 1.
- **PgBouncer**: Manages database connection spikes to prevent thread exhaustion during traffic surges.
- **`pgaudit` Extension**: Logs DDL, DCL, and role changes for tamper-evident 7-year audit trails.
- **AWS Secrets Manager**: Delivers automated 30-day rotation for short-lived database credentials.

## Rationale
- Partitioned tables and dedicated read replicas optimize performance for high-throughput transactional writes and 7-year historical audit scans.
- Native PostgreSQL security controls and managed AWS services minimize operational overhead for a three-engineer team while ensuring compliance.