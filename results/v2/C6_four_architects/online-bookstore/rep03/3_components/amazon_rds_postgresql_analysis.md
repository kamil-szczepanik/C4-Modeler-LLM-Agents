## Overview
This architecture defines the relational database tier for an online bookstore supporting 1M MAU across multiple global regions. It ensures high performance, strict GDPR/CCPA compliance, and secure ACID transaction management.

## Key Elements
- PostgreSQL Relational Engine: Core RDBMS (PostgreSQL 15+) managing ACID transactions.
- PgBouncer: Connection pooler for handling high-concurrency requests.
- Partition Manager: Declarative table partitioning for performance and data purging.
- Extension Manager: Native extensions (`pg_trgm`, `pgcrypto`) for search and encryption.
- Row-Level Security (RLS) Policies: Tenant and regional data isolation mechanism.
- Audit & Logging Subsystem: Configured via `pgAudit` for compliance tracking.
- Migration Manager: Flyway/Liquibase schema version control integration.
- Read Replica Routing Logic: Offloads read queries to regional replicas.

## Relationships
- Order & Checkout Service -> Amazon RDS (PostgreSQL): Persists transactional data via [JDBC / TCP].
- Catalog & Search Service -> Amazon RDS (PostgreSQL): Reads catalogue data via [JDBC / SQL over TCP].
- Data Privacy & User Service -> Amazon RDS (PostgreSQL): Manages profiles and compliance deletions via [SQL over TCP].
- Payment & Currency Service -> Amazon RDS (PostgreSQL): Persists transaction records via [ADO.NET / SQL over TCP].
- Recommendation & Review Service -> Amazon RDS (PostgreSQL): Reads history for feature extraction via [Psycopg2 / TCP].
- Admin & Content Management Service -> Amazon RDS (PostgreSQL): Executes updates via [JDBC / SQL over TCP].
- Async Worker Service -> Amazon RDS (PostgreSQL): Updates job states via [JDBC / SQL over TCP].
- Amazon RDS Primary -> Amazon RDS Read Replicas: Replicates data via [PostgreSQL Streaming Replication / TCP].

## Technology Stack
- Amazon RDS (PostgreSQL): Managed relational database providing high availability and automated backups.
- PgBouncer: Lightweight connection pooling to prevent exhaustion under 1M MAU load.
- Amazon EBS (gp3/io2): High-performance persistent storage with Write-Ahead Logging.
- AWS DMS / PostgreSQL Logical Replication: Cross-region replication for global deployment in `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Rationale
The architecture combines connection pooling and partitioning to meet rigorous scalability and performance targets under high concurrent loads. Integrated encryption, RLS, and auditing natively satisfy strict GDPR/CCPA compliance and security mandates.