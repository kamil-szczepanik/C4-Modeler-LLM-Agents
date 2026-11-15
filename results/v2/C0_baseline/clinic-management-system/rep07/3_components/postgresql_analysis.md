## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely handle patient admissions, scheduling, Electronic Medical Records (EMR), and billing. It ensures high availability, strict regulatory compliance, and rapid data access for clinical workflows.

## Key Elements
- **Users**: Patients, Clinicians/Doctors, Receptionists/Admins, Billing Specialists, Compliance/IT Auditors
- **External Systems**: Patient Portal App, Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- **Containers**: API Gateway, EMR Service, Appointment Service, Billing Container, Audit & Compliance Container, HL7 FHIR Interoperability Service, PostgreSQL (with Redis & pg_audit), Apache Kafka
- **PostgreSQL Components**: Relational Storage Engine (PostgreSQL 16), PgBouncer, `pg_audit` extension, Vault + `pgcrypto`, Redis 7 caching layer, Row-Level Security Policies Engine

## Relationships
- **API Gateway -> Services**: Routes HTTPS/REST/gRPC traffic with mTLS
- **EMR Service -> PgBouncer -> PostgreSQL**: Reads/writes patient records via TCP/PostgreSQL Wire Protocol (TLS 1.3)
- **Appointment Service -> PgBouncer -> PostgreSQL**: Manages scheduling data via TCP/PostgreSQL Wire Protocol (TLS 1.3)
- **PostgreSQL -> Apache Kafka**: Streams audit logs via secure sidecar for compliance retention

## Technology Stack
- **Database**: PostgreSQL 16 with table partitioning for core persistence and ACID compliance
- **Connection Pooling**: PgBouncer for managing high concurrency and preventing exhaustion
- **Caching**: Redis 7 for low-latency EMR retrieval (<1s P95)
- **Encryption**: Vault + PostgreSQL `pgcrypto` for AES-256 envelope encryption at rest
- **Compliance & Monitoring**: `pg_audit` for immutable audit logs; Prometheus for real-time metrics

## Rationale
This architecture uses PostgreSQL 16 with PgBouncer and Redis caching to meet strict performance targets (<1s EMR load) while supporting high concurrency. Furthermore, native Row-Level Security (RLS), `pg_audit`, and automated WAL archiving to S3 ensure rigorous HIPAA/GDPR compliance and reliable 10-year data retention.