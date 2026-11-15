## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations in real time to prevent fraud. It processes payments securely while providing a case management platform for fraud analysts.

## Key Elements
- Transactional & Audit Data Store (Amazon RDS PostgreSQL)
- Case Management Repository (Relational tables with pgx driver)
- Audit Log Subsystem (PostgreSQL Append-Only Tables, RLS, and pgcrypto)
- Partition Manager (pg_partman for time-based partitioning)
- Cold Storage (WORM-configured Amazon S3 Glacier Vault via AWS Backup)
- Read Replica (Amazon RDS PostgreSQL Read Replica)

## Relationships
- Fraud Scoring Engine -> Case Management Repository: Writes evaluation results and initial case state [PostgreSQL Wire Protocol over TLS 1.3]
- Case Management API -> Case Management Repository: Reads and updates active review cases [PostgreSQL Wire Protocol over TLS 1.3]
- Case Management API -> Audit Log Subsystem: Appends immutable decision logs [PostgreSQL Wire Protocol, INSERT-only via RLS]
- Audit Log Subsystem -> S3 Glacier Vault: Delegates cold partition export [AWS SDK via IAM Role]

## Technology Stack
- Amazon RDS PostgreSQL: Balances ACID requirements with audit capabilities within budget
- pgcrypto & AWS KMS: Provides cryptographic hashing and column-level encryption for tamper-evidence and PCI-DSS compliance
- pg_partman: Automates time-based table partitioning for 7-year retention
- S3 Glacier Vault: Ensures WORM-configured immutable long-term storage
- AWS Secrets Manager: Manages automated database credential rotation every 30 days

## Rationale
This architecture uses proven managed AWS services and PostgreSQL extensions to meet strict PCI-DSS Level 1 compliance and 7-year auditability. It isolates analytics workloads and automates backups while remaining easily operable by a three-engineer team within a €25,000 monthly budget.