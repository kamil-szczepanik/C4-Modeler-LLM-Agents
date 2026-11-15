## Overview
The Clinic Management System is a hybrid healthcare platform designed to manage patient records, appointments, and billing with strict regulatory compliance. Its data layer architecture provides secure, highly available, and high-performance data storage across on-premise Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Primary Relational Store**: PostgreSQL (Multi-Master / Citus or Cloud Managed RDS) for structured EMR, billing, and scheduling data.
- **Audit Logging Store**: Append-only PostgreSQL schema with row-level security for tamper-proof audit trails.
- **Blob Object Store**: MinIO (on-premise) and AWS S3 (cloud) for large medical imaging and lab binary files.
- **Data Access Proxy**: PgBouncer for connection pooling and load distribution.
- **Encryption & Key Management Module**: HashiCorp Vault or AWS KMS providing FIPS 140-2 Level 3 HSM encryption.
- **Replication & Sync Manager**: Debezium and Kafka Connect for hybrid cross-site synchronization.
- **Database Migration & Schema Manager**: Flyway or Liquibase for zero-downtime version-controlled schema upgrades.

## Relationships
- Core Services & EMR Service -> **Data Access Proxy**: TLS (TCP/JDBC) for connection pooling.
- **Data Access Proxy** -> **Primary Relational Store**: TCP/JDBC.
- **EMR Service** -> **Blob Object Store**: HTTPS (S3 API) with pre-signed URLs for binary transfers.
- **Primary Relational Store** -> **Audit Logging Store**: Internal synchronous logical replication.
- **Primary Relational Store** & **Blob Object Store** <-> **Encryption & Key Management Module**: gRPC/HTTPS for envelope encryption and key rotation.
- **Replication & Sync Manager** -> **Primary Relational Store**: TLS (Logical Replication Stream) between `on-prem-k8s` and `eu-central-1`.

## Technology Stack
- **PostgreSQL**: Chosen for robust relational data handling and ACID compliance.
- **MinIO / AWS S3**: Selected for scalable binary object storage supporting long-term retention.
- **PgBouncer**: Implemented to prevent database exhaustion under high hybrid concurrency.
- **Debezium / Kafka Connect**: Utilized for reliable hybrid active-active replication.
- **HashiCorp Vault / AWS KMS**: Deployed to enforce AES-256 encryption at rest and FIPS compliance.
- **Flyway / Liquibase**: Used for atomic, zero-downtime schema evolution.

## Rationale
This 7-component data layer architecture ensures 99.99% availability and sub-second EMR performance via connection pooling and direct object transfers. It strictly enforces HIPAA and GDPR compliance through isolated audit logging, FIPS-compliant AES-256 encryption, and robust multi-master hybrid replication.