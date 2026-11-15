## Overview
- PostgreSQL relational database architecture built on Amazon Aurora to support the real-time fraud screening system.
- Provides tamper-evident audit logging, high-performance case management, and strict PCI-DSS Level 1 compliance.

## Key Elements
- AWS Aurora PostgreSQL (Database Container)
- Transaction & Case Repository (PostgreSQL relational tables)
- Audit Ledger (Append-only WORM tables with `pg_audit`)
- Partition Manager (`pg_partman` extension)
- Connection Pooler (PgBouncer / Aurora Proxy)
- Aurora Read Replica (Dedicated for case management and analytical queries)
- Amazon S3 Glacier Vaults (Cold storage for audit archives via AWS DMS)

## Relationships
- Real-Time Scoring Engine -> Connection Pooler: Persists decision metrics and audit logs [IAM-authenticated TLS 1.3]
- Case Management Backend -> Aurora Read Replica: Queries active fraud cases and analyst workloads [SQL/JDBC over TLS 1.3]
- Partition Manager -> Amazon S3: Offloads historical audit partitions older than 90 days [AWS KMS encrypted S3 API]
- Database Audit Ledger -> Amazon CloudWatch / SIEM: Streams `pgaudit` activity logs [Encrypted CloudWatch Log Stream]

## Technology Stack
- Amazon Aurora PostgreSQL (`db.r6g.large`): Selected for predictable baseline performance and cost control within the €25,000/month budget.
- AWS KMS (AES-256): Ensures encryption-at-rest and strict cryptographic integrity for S3 Glacier archives.
- PgBouncer / Aurora Proxy: Manages connection spikes and prevents connection exhaustion from ECS Fargate tasks.
- `pg_partman` & AWS DMS: Automates time-based partitioning and cold storage offloading to meet 7-year audit retention.

## Rationale
- The architecture guarantees sub-second analyst workflows and protects P99 scoring latency by isolating read replicas and implementing connection pooling.
- It satisfies PCI-DSS Level 1 and 7-year tamper-evident auditability constraints through IAM database authentication, column-level security, and KMS-encrypted WORM storage.