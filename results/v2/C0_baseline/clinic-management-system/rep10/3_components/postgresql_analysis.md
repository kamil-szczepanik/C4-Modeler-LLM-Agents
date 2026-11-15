## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides high availability, secure multi-tenant data isolation, and strict compliance with HIPAA and GDPR regulations.

## Key Elements
- Patients, Clinicians/Doctors, Administrative Staff, Billing Officers, Compliance Officers/Auditors
- Web Application (React / TypeScript), API Gateway (NGINX / Envoy)
- EMR Service (Node.js / Go), Billing & Claims Service (Java / Spring Boot), Scheduling Service (Node.js / Go), Notification Service (Python / FastAPI), Integration Service (Java / Spring Boot)
- PostgreSQL (PostgreSQL 15+ with Patroni, PgBouncer, `pgaudit`, `pg_crypto`, `pg_partman`)
- Redis (Redis), RabbitMQ (RabbitMQ Message Broker), HashiCorp Vault (HashiCorp Vault)
- External Insurance/Clearinghouse System, External Laboratory & Imaging System (`HL7 FHIR`)

## Relationships
- Web Application -> API Gateway: Routes client requests [HTTPS / REST / WebSocket]
- API Gateway -> EMR Service: Forwards clinical requests [gRPC / mTLS]
- API Gateway -> Billing & Claims Service: Forwards financial requests [gRPC / mTLS]
- API Gateway -> Scheduling Service: Forwards appointment requests [gRPC / mTLS]
- EMR Service -> PostgreSQL Engine: Reads/writes current partition tables via PgBouncer [SQL / mTLS]
- EMR Service -> PostgreSQL Archive: Reads historical data via read-only foreign tables (FDW) [SQL / mTLS]
- Billing & Claims Service -> PostgreSQL Engine: Reads and writes billing data via PgBouncer [SQL / mTLS]
- Scheduling Service -> PostgreSQL Engine: Reads and writes scheduling data via PgBouncer [SQL / mTLS]
- Integration Service -> External Laboratory & Imaging System: Exchanges health records [HL7 FHIR / HTTPS]

## Technology Stack
- PostgreSQL 15+: Core relational database chosen for robust ACID compliance and advanced partitioning capabilities.
- Patroni: Automated high-availability manager for PostgreSQL to achieve 99.99% uptime via hot-standby failover.
- PgBouncer: Connection pooler to manage high-concurrency container connection spikes safely.
- CloudNativePG: Kubernetes operator for managing automated backups, PITR, and PostgreSQL lifecycle.
- HashiCorp Vault: Centralized secret management for certificate-based authentication and AES-256 key rotation.
- pgaudit & pgcrypto: Native extensions ensuring immutable audit trails and column-level encryption for HIPAA/GDPR.

## Rationale
This architecture guarantees 99.99% availability and meets the 10-year data retention mandate through Active-Standby PostgreSQL replication, automated PITR, and declarative table partitioning. Strict mTLS, Row-Level Security, and FDW isolation ensure comprehensive HIPAA and GDPR compliance without sacrificing sub-second EMR performance.