## Overview
The architecture defines the Amazon Aurora PostgreSQL component for an online bookstore serving 1 million monthly active users globally. It ensures high availability, strict security compliance, and low-latency transactional performance across multiple AWS regions.

## Key Elements
- Connection Pooler Component (PgBouncer/AWS RDS Proxy)
- Catalog & Localization Schema Component
- Order & Transaction Schema Component
- Aurora Global Database Storage Engine Component
- Read-Replica Routing Component
- Materialized View / Indexing Component

## Relationships
- Order & Checkout Service -> Order & Transaction Schema Component: Executes ACID transactions [TCP/TLS via Proxy]
- Catalog & Search Service -> Read-Replica Routing Component: Directs read queries to local regional replicas [TCP/TLS via Proxy]
- Catalog & Search Service -> Catalog & Localization Schema Component: Queries book metadata [TCP/TLS via Proxy]

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for ACID compliance, global replication, and high availability.
- AWS Secrets Manager: Used for automated 30-day database credential rotation.
- AWS KMS: Implemented for encryption-at-rest with customer-managed keys.
- PostgreSQL Row-Level Security (RLS) & `pg_audit`: Enforces data isolation and compliance audit trails.
- PgBouncer / AWS RDS Proxy: Manages dynamic microservice connection limits.

## Rationale
This architecture meets GDPR/CCPA constraints and 99.95% uptime availability by utilizing global read-replicas, encryption, and strict RBAC controls. Multi-region routing and automated scaling ensure sub-second page loads and seamless performance under high traffic spikes.