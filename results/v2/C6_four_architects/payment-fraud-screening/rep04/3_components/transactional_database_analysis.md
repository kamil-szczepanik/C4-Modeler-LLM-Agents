## Overview
The system provides real-time payment fraud screening for card-not-present transactions and a case management workflow for analysts. It is operated by a three-engineer team on AWS within a fixed budget while ensuring PCI-DSS compliance and sub-50ms P99 decision latency.

## Key Elements
- **Amazon Aurora PostgreSQL**: Primary relational database container utilizing multi-AZ deployment.
- **Case Management Store Schema**: Relational tables for analyst cases, review states, and workflow assignments.
- **Audit Ledger Schema**: Append-only tables using the `pgcrypto` extension for tamper-evident logs.
- **Database Connection Pooler (PgBouncer)**: Manages high-concurrency connection spikes from ECS Fargate tasks.
- **Row-Level Security (RLS) Policies**: Enforces data isolation and least-privilege access at the database engine level.
- **Database Migration Manager (Flyway/Liquibase)**: Manages automated schema evolution via CI/CD.
- **Transparent Data Encryption (TDE) / KMS Integration**: Secures storage volumes and audit schemas using AWS KMS-managed keys.
- **Aurora Read Replica**: Hot standby instance used to offload read-heavy case searches.
- **Backup and Retention Controller**: AWS Backup integration enforcing point-in-time recovery (PITR) and 7-year retention.

## Relationships
- **Case Management Service** -> **Database Connection Pooler**: Executes scoped CRUD operations and read-only queries via [TCP/TLS].
- **Audit Consumer Service** -> **Database Connection Pooler**: Batch-writes decision audit logs into the Audit Ledger Schema via [TCP/TLS].
- **Amazon Aurora PostgreSQL** -> **AWS Key Management Service (KMS)**: Encrypts storage volumes and audit records via [AWS API].
- **Amazon Aurora PostgreSQL** -> **AWS Backup**: Triggers automated snapshots and PITR logs via [AWS API].

## Technology Stack
- **Amazon Aurora PostgreSQL**: Chosen for ACID guarantees, reliability, and robust feature set suited for transactional case management.
- **PgBouncer**: Selected to prevent connection exhaustion from ECS Fargate tasks under high throughput (3,000 TPS).
- **AWS KMS**: Utilized for encryption at rest to satisfy PCI-DSS Level 1 compliance requirements.
- **AWS Backup**: Implemented for automated point-in-time recovery to meet the 7-year retention mandate without operational toil.

## Rationale
This component architecture balances strict compliance and auditability mandates with low-latency constraints. It minimizes operational overhead for a three-engineer team by leveraging managed AWS services and built-in database security controls.