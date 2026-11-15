## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It relies on a high-availability PostgreSQL Database Cluster to securely store stateful transactional data within EU cloud regions.

## Key Elements
- PostgreSQL Database Cluster (PostgreSQL container)
- Primary transactional write engine
- Dedicated read replica nodes
- PgBouncer (connection proxy component)
- Patroni consensus agent component
- Core Circulation & Catalog Service, Authentication & Session Service, and Integration Service

## Relationships
- Core Circulation & Catalog Service -> PostgreSQL Database Cluster: Queries stateful transactional data via PostgreSQL Protocol over mutual TLS (mTLS)
- Upstream services -> PgBouncer -> PostgreSQL instances: Connection pooling and request queuing using PostgreSQL wire protocol

## Technology Stack
- PostgreSQL: Core transactional storage ensuring strict ACID compliance
- PgBouncer: Connection pooling to prevent connection exhaustion and handle client queuing
- Patroni: Automated failover orchestration and distributed consensus for high availability
- Flyway: Zero-downtime database schema migrations
- HashiCorp Vault: Dynamic secret management for distinct SCRAM-SHA-256 credentials
- Prometheus (`postgres_exporter`) & OpenTelemetry: Metrics collection, tracing, and monitoring
- `pgaudit`: Database audit logging for compliance and tracking patron PII access

## Rationale
This architecture uses primary-replica replication and Patroni automated failover to meet strict sub-second performance requirements and zero-downtime demands during peak academic periods. Enforcing strict EU-only data residency, encryption at rest, and mTLS guarantees full compliance with regional privacy regulations.