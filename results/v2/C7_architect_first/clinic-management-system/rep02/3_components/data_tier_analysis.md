## Overview
The Clinic Management System is a clinical IT platform for medium-sized hospitals and clinics that manages patient admissions, EMRs, scheduling, and billing. It uses a secure hybrid cloud architecture to ensure 99.99% availability and strict HIPAA and GDPR compliance.

## Key Elements
- **Primary DB Instance**: PostgreSQL 16 handling transactional writes and critical reads.
- **Replica DB Instances**: PostgreSQL 16 managed by Patroni for read-only EMR and reporting queries.
- **Audit Ledger Component**: WORM-enabled append-only database table partition using Row-Level Security.
- **Connection Pooler**: PgBouncer routing traffic and preventing connection starvation.
- **External KMS**: HashiCorp Vault managing per-record Data Encryption Keys (DEKs).

## Relationships
- **Core Services -> Primary DB Instance**: Executes transactional writes and critical reads via SQL over mTLS (`sslmode=verify-full`).
- **Core Services -> Replica DB Instances**: Executes high-volume EMR and reporting reads via SQL over mTLS.
- **Primary DB Instance -> Replica DB Instances**: Synchronous/asynchronous data replication via Patroni.
- **Data Tier -> WORM Object Storage**: Continuous WAL archiving via encrypted streams.

## Technology Stack
- **PostgreSQL 16**: Chosen for robust relational integrity, extensions, and proven healthcare ecosystem compatibility.
- **Patroni**: Selected for automated high-availability management, ensuring RTO < 60s and RPO < 5s.
- **HashiCorp Vault**: Implemented for envelope encryption and cryptographic erasure to satisfy GDPR compliance.
- **PgBouncer**: Deployed for intelligent connection pooling and read-query routing to protect P95 load times.

## Rationale
This architecture balances strict regulatory compliance (HIPAA/GDPR) with high-availability demands (99.99% uptime) through a resilient primary-replica database pattern. Isolating read workloads and utilizing envelope encryption protects system performance (P95 < 1s) while ensuring data privacy and ten-year retention mandates.