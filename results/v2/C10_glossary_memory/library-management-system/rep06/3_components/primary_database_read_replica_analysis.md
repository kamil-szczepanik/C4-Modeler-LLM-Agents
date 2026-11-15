## Overview
- Manages transactional data for the Library Management System while enforcing strict EU-only data residency and high-performance requirements.
- Offloads heavy read traffic to ensure uninterrupted self-service borrowing and sub-800ms search responses for patrons.

## Key Elements
- Connection Pooler (PgBouncer)
- Primary Database Instance (PostgreSQL 15)
- Read Replica Instance (PostgreSQL 15)
- Failover & Consensus Manager (Patroni / etcd)

## Relationships
- Connection Pooler -> Primary Database Instance: Routes write transactions [PostgreSQL Protocol, TLS 1.3]
- Connection Pooler -> Read Replica Instance: Routes read queries [PostgreSQL Protocol, TLS 1.3]
- Primary Database Instance -> Read Replica Instance: Replicates data [Streaming Replication, TLS 1.3]
- Failover & Consensus Manager -> Primary Database Instance: Monitors health and manages failover [TCP/HTTP]
- Failover & Consensus Manager -> Read Replica Instance: Monitors health and manages promotion [TCP/HTTP]

## Technology Stack
- PostgreSQL 15: Core relational database engine for robust ACID compliance
- PgBouncer: Connection pooling to prevent resource exhaustion from microservices
- Patroni / etcd: Automated high-availability failover and consensus management
- AES-256 with CMK: Data encryption at rest in EU-sovereign storage
- mTLS & SCRAM-SHA-256: Strict transport security and authentication

## Rationale
- High availability and automated failover guarantee operational uptime for circulation workflows during peak academic periods.
- Read separation and connection pooling protect performance SLAs while meeting strict EU data residency constraints.