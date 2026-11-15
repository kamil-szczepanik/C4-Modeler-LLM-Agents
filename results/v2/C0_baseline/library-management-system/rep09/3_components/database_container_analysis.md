## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The architecture ensures strict data residency, high performance, and GDPR compliance.

## Key Elements
- Relational Storage Engine (PostgreSQL Primary)
- Read-Replica Instance (PostgreSQL Read-Only Engine)
- Connection Pooler (PgBouncer)
- Audit Logging Extension (`pg_audit`)
- Replication Manager (Patroni / PostgreSQL Streaming Replication)

## Relationships
- Core Services Container -> Connection Pooler: Queries relational data synchronously via PostgreSQL wire protocol over TLS 1.3 (TCP)
- Core Services Container -> Read-Replica Instance: Routes analytical and reporting queries via PostgreSQL wire protocol over TLS 1.3 (TCP)
- Relational Storage Engine -> Read-Replica Instance: Streaming replication over TCP within EU availability zones
- Relational Storage Engine -> Audit Logging Extension: Internal hooks capturing DDL and DML operations

## Technology Stack
- PostgreSQL: Provides robust ACID guarantees for circulation management and relational data persistence
- PgBouncer: Manages client connections in transaction pooling mode to handle peak traffic without memory exhaustion
- `pg_audit`: Captures DDL and DML operations synchronously for GDPR compliance and audit reporting
- Patroni: Manages high availability, automated failover, and streaming replication across EU availability zones
- TLS 1.3 & mTLS: Enforces mandatory transport encryption for all incoming connections

## Rationale
This architecture guarantees strict EU-only data residency and GDPR compliance through localized encryption, dynamic secrets, row-level security, and `pg_audit`. Read-replicas and connection pooling ensure optimal performance to meet the sub-800ms response time requirement.