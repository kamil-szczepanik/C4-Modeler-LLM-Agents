## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention policy using a hybrid cloud architecture.

## Key Elements
- PostgreSQL Database Container
- Relational Engine (PostgreSQL v15+)
- Connection Pooler (PgBouncer)
- Replication & HA Manager (Patroni / etcd)
- Encryption & Audit Extension (pgcrypto & pgaudit)
- Core Clinic Service (Java / Spring Boot)
- Billing Service (Node.js)

## Relationships
- Core Clinic Service, Billing Service -> Connection Pooler: Queries data [TCP / SQL over TLS 1.3]
- Connection Pooler -> Relational Engine: Forwards validated client queries [TCP / Local Socket]
- Relational Engine <-> Replication & HA Manager: Synchronizes transaction logs [TCP]
- Relational Engine -> Encryption & Audit Extension: Writes audit trails and applies AES-256 encryption [Internal SPI]

## Technology Stack
- PostgreSQL v15+: Core relational database engine for robust transactional data management.
- PgBouncer: Connection pooler to prevent connection exhaustion from multiple microservices.
- Patroni / etcd: Replication and high availability manager for automated failover and 99.99% uptime.
- pgcrypto & pgaudit: Database extensions for AES-256 encryption at rest and compliance audit logging.
- TLS 1.3: Secure transport layer protocol for database queries.

## Rationale
This component architecture ensures high availability through automated failover and connection management across hybrid environments. It strictly enforces HIPAA and GDPR requirements via robust encryption at rest and tamper-evident audit logging.