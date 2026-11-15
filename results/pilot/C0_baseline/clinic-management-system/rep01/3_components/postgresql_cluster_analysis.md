## Overview
The PostgreSQL Cluster is the primary transactional data store for the Clinic Management System, ensuring high availability, regulatory compliance, and sub-second performance. It securely manages patient demographics, electronic medical records (EMR), and billing data across a hybrid cloud infrastructure.

## Key Elements
- Primary Database Node: Manages write operations and DDL execution.
- Synchronous Standby Nodes: Maintains zero-data-loss high availability via Patroni.
- Asynchronous Read Replicas: Scales query loads for EMR and billing operations.
- PgBouncer: Manages connection pooling and routes incoming application queries.
- Audit Logging Sidecar: Collects `pgaudit` security logs for immutable tracking.

## Relationships
- Core API Service -> PgBouncer: Persists transactional data via PostgreSQL wire protocol over TCP with mTLS.
- EMR Engine -> PgBouncer: Queries patient records via PostgreSQL wire protocol over TCP with mTLS.
- Primary Database Node -> Synchronous Standby Nodes: Replicates transactions via streaming replication protocol over TLS 1.3.
- PostgreSQL Cluster -> WORM Object Storage: Exports automated pg_backrest archives for long-term retention.

## Technology Stack
- PostgreSQL: Core relational database engine chosen for robust ACID compliance.
- Patroni with etcd: Orchestrates automated failover and consensus across Kubernetes environments to guarantee 99.99% uptime.
- PgBouncer: Connection pooler optimized for handling concurrent clinical traffic spikes.
- AES-256 and LUKS: Provides storage-level and transparent data encryption to satisfy HIPAA and GDPR mandates.
- SCRAM-SHA-256 with mTLS: Secures authentication and transport over TCP across the hybrid infrastructure.

## Rationale
This architecture guarantees strict HIPAA and GDPR compliance through encryption, row-level security, and immutable audit logs. The active-active high availability setup and connection pooling ensure sub-second EMR screen loads and continuous uptime for critical hospital workflows.