## Overview
The Clinic Management System is a hybrid cloud-based healthcare platform that handles patient admissions, scheduling, electronic medical records (EMR), and billing. It provides secure, highly available clinical IT infrastructure for medium-sized hospitals and clinics.

## Key Elements
* **Connection Pooler** [PgBouncer]: Manages incoming TCP/IP connections from microservices.
* **Primary Database Instance** [PostgreSQL 15+]: Handles read/write transactions for EMR and patient records.
* **High Availability Replica** [Patroni / PostgreSQL Streaming Replication]: Active standby instance for automated failover.
* **Read-Only Replica** [PostgreSQL Streaming Replication]: Offloads read traffic to improve performance.
* **Audit Logging Engine** [pgaudit]: Captures DDL/DML statements for HIPAA-compliant auditing.
* **Backup & Archival Agent** [Barman / pgBackRest]: Manages point-in-time recovery and long-term data retention.

## Relationships
* **Patient & Scheduling Service, EMR Service, Billing & Claims Service -> Connection Pooler**: Routes database queries via TCP/IP [TLS 1.3].
* **Connection Pooler -> Primary Database Instance**: Forwards write operations and dynamic queries.
* **Primary Database Instance -> High Availability Replica**: Synchronizes data in real-time via Streaming Replication [TCP/IP, TLS 1.3].
* **Primary Database Instance -> Read-Only Replica**: Feeds read-only data for scaling.
* **Backup & Archival Agent -> Primary Database Instance**: Performs backups via Encrypted File System / API.

## Technology Stack
* **PostgreSQL 15+**: Relational database core ensuring robust ACID compliance for medical records.
* **PgBouncer**: Efficient connection pooling to prevent database exhaustion.
* **Patroni**: High availability manager providing automated failover for 99.99% uptime.
* **pgaudit**: Regulatory compliance auditing for strict HIPAA and GDPR mandates.
* **Barman / pgBackRest**: Reliable backup orchestration meeting the 10-year data retention constraint.

## Rationale
This architecture utilizes enterprise-grade open-source PostgreSQL components deployed across hybrid infrastructure to guarantee strict HIPAA/GDPR compliance, AES-256 encryption, and 99.99% high availability. The decoupled replication and pooling strategy ensures high-performance EMR retrieval under strict performance thresholds.