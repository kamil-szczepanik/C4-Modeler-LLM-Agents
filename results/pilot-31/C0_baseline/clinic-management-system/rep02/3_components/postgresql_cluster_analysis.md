## Overview
The Clinic Management System is a hybrid-cloud clinical platform designed to manage patient EMRs, scheduling, and billing. It ensures high availability and strict regulatory compliance (HIPAA/GDPR) for long-term health data management.

## Key Elements
*   **Database Cluster:** PostgreSQL managed by Patroni.
*   **Consensus Store:** etcd for cluster leader election.
*   **Connection Pooler:** PgBouncer for high-concurrency management.
*   **Backup/Archival:** pgBackRest with WORM storage integration.
*   **Security:** HashiCorp Vault for dynamic credential management.
*   **Audit Layer:** Audit Logging Sidecar via logical decoding.

## Relationships
*   **App Services -> PostgreSQL:** mTLS-encrypted SQL connections via PgBouncer.
*   **Primary -> Standby:** Synchronous replication (local) and Asynchronous replication (cross-region).
*   **PostgreSQL -> WORM Storage:** Continuous WAL archiving via pgBackRest.
*   **Logical Decoding -> Audit Sidecar:** Real-time DML/DDL event streaming.
*   **API Gateway -> PostgreSQL:** Session-based RLS context propagation.

## Technology Stack
*   **PostgreSQL/Patroni:** High-availability database engine with automated failover.
*   **Time-Range Partitioning:** Used for EMR/Audit tables to optimize retention and GDPR compliance.
*   **Row-Level Security (RLS):** Cryptographically enforced data segmentation per user identity.
*   **pgBackRest:** Continuous backup and point-in-time recovery for 10-year retention.
*   **HashiCorp Vault:** Dynamic, short-lived credential rotation for application services.

## Rationale
This architecture utilizes Patroni and synchronous replication to meet the 99.99% uptime requirement while ensuring data consistency for billing. Time-range partitioning and logical decoding enable efficient long-term data lifecycle management and immutable auditing required for HIPAA/GDPR compliance.