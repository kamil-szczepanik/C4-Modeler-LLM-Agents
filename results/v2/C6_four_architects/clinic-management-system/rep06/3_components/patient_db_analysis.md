## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to securely manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance, and seamless interoperability with external clinical systems.

## Key Elements
- Primary DB Instance (PostgreSQL 15)
- Read Replica (PostgreSQL 15 Standby)
- Connection Pooler (PgBouncer)
- Encryption Manager (PostgreSQL TDE / pgcrypto)
- Failover Coordinator (Patroni / etcd)
- Backup & Archiving Agent (Barman / pgBackRest)
- Row-Level Security (RLS) Policy Engine
- External Systems: Identity Provider (IdP), External Labs & Imaging Systems, Insurance Payment Gateway, Hospital Notification/SMS Gateway
- Containers: Frontend Web App (React SPA), API Gateway (Nginx / Kong), Identity & Access Proxy, Patient & Scheduling Service (Java / Spring Boot), EMR Service (Node.js / TypeScript), Billing & Claims Service (.NET Core), FHIR Integration Broker, Async Message Broker, Audit & Compliance Log Shipper, Patient DB (PostgreSQL), EMR DB (MongoDB), Distributed Cache (Redis), Audit Data Store (AWS S3 / MinIO WORM)

## Relationships
- Patient & Scheduling Service -> PgBouncer: Manages database connections [TCP / TLS]
- Patient & Scheduling Service -> Row-Level Security Policy Engine: Applies context-aware access policies per query [SQL / TLS session variables]
- Primary DB Instance <-> Read Replica: Streams transaction logs [TCP / Streaming Replication]
- Primary DB Instance -> Audit & Compliance Log Shipper: Streams structured audit logs [File tailing / Unix Domain Socket]
- Failover Coordinator <-> Primary DB Instance / Read Replica: Health checks and consensus state management [TCP / HTTP]
- Backup & Archiving Agent -> Primary DB Instance: Pulls database backups and WAL streams [TCP / SSH/TLS]
- Backup & Archiving Agent -> Audit Data Store: Writes encrypted, immutable backups [HTTPS / S3 API]

## Technology Stack
- PostgreSQL 15: Provides robust, relational data storage for structured scheduling and patient demographics.
- PgBouncer: Manages incoming database connections to prevent connection exhaustion under high concurrency.
- Patroni / etcd: Enables automated leader election and failover for high availability.
- Barman / pgBackRest: Handles continuous WAL archiving and point-in-time recovery for long-term retention.
- PostgreSQL TDE / pgcrypto & RLS: Enforces AES-256 encryption at rest and database-level multi-tenant security for HIPAA/GDPR compliance.

## Rationale
This architecture uses an active-active hybrid design and robust replication to guarantee 99.99% uptime. Integrated security controls, encryption, and immutable backups ensure strict HIPAA and GDPR compliance with a 10-year data retention mandate.