## Overview
The Clinic Management System is a hybrid cloud-based clinical IT platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- **PostgreSQL Container**: Primary relational data store.
- **PgBouncer**: Connection pooler for handling microservice traffic spikes.
- **Patroni & etcd**: Replication manager for automated failover and high availability.
- **Barman**: Backup manager for point-in-time recovery and long-term retention.
- **Security Modules**: `pgcrypto` for AES-256 encryption and `pgaudit` for audit trails.
- **Microservices**: Patient & Scheduling, EMR, Billing & Claims, and Interoperability services.

## Relationships
- Patient, EMR, & Billing Services -> PgBouncer: Connection requests via [TCP/JDBC]
- PgBouncer -> PostgreSQL Engine: Routed database queries via [TCP/SQL]
- Billing & Claims Service -> PostgreSQL Read Replica: Read-only queries via [JDBC/SQL]
- PostgreSQL Engine -> Patroni: Health checks and replication state via [TCP]
- PostgreSQL Engine -> Barman: Encrypted archival backups via [TCP/SSH]

## Technology Stack
- **PostgreSQL**: Primary SQL database chosen for robust ACID compliance and data integrity.
- **PgBouncer**: Connection pooler selected to sustain sub-second P95 EMR load performance.
- **Patroni**: High-availability orchestrator chosen to guarantee 99.99% uptime via automated failover.
- **Barman**: Backup tool selected to satisfy 10+ year data retention and recovery requirements.
- **pgcrypto & pgaudit**: Built-in extensions chosen to enforce AES-256 encryption at rest and HIPAA/GDPR audit logging.

## Rationale
This architecture ensures 99.99% high availability and strict HIPAA/GDPR compliance using robust replication and audit extensions. It maintains high performance through dedicated connection pooling and read-replica offloading.