## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient records, scheduling, and billing for clinical environments. It serves as a secure, high-availability source of truth for healthcare data while ensuring strict regulatory compliance.

## Key Elements
*   **Database Cluster:** PostgreSQL (Primary-Replica configuration)
*   **Connection Management:** pgBouncer
*   **Orchestration/Failover:** Patroni with a quorum-based witness node
*   **Security Infrastructure:** HashiCorp Vault, Bastion host
*   **Audit/Compliance:** pgaudit, AWS S3 (WORM storage)
*   **Automation:** pg_partman, pg_exporter

## Relationships
*   **EMR/Billing Services -> pgBouncer:** Connection pooling via TCP
*   **Application Services -> PostgreSQL:** mTLS-encrypted connections using SCRAM-SHA-256
*   **PostgreSQL Primary -> Replicas:** Synchronous replication for RPO=0
*   **PostgreSQL -> S3:** Continuous WAL archiving and logical decoding for audit logs
*   **Reporting/Billing Services -> Read-Only Replica:** Data access via Foreign Data Wrapper (FDW)

## Technology Stack
*   **PostgreSQL:** Relational database engine for ACID compliance.
*   **Patroni:** Manages high-availability cluster state and failover.
*   **pg_partman:** Automates time-based table partitioning for performance and archival.
*   **pgaudit:** Provides detailed session/object auditing for HIPAA compliance.
*   **HashiCorp Vault:** Manages dynamic, short-lived database credentials.
*   **pgcrypto:** Enables field-level encryption for PHI/PII.

## Rationale
The architecture utilizes synchronous replication and Patroni to guarantee 99.99% availability and zero data loss (RPO=0). Table partitioning and read-only replicas ensure the system maintains sub-second P95 performance for clinical staff while offloading intensive billing and regulatory reporting tasks.