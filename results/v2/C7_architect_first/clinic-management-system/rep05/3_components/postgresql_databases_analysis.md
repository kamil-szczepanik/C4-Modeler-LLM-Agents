## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical workflows while adhering strictly to HIPAA and GDPR compliance mandates.

## Key Elements
- Patient Portal Service, Patient & Scheduling Service, EMR Service, Billing Service, Integration Service
- PostgreSQL 16 Databases (Patient & Portal DB, Scheduling DB, EMR DB, Billing DB) with Patroni and CloudNativePG operator
- HashiCorp Vault for dynamic secrets and credential rotation
- Apache Kafka Event Broker
- API Gateway (Kong, Nginx, Envoy sidecar)

## Relationships
- Patient Portal Service -> Patient & Portal DB: Reads/writes data [TCP / mTLS]
- Patient & Scheduling Service -> Scheduling DB: Reads/writes data [TCP / mTLS]
- EMR Service -> EMR DB: Reads/writes active and archival data [TCP / mTLS]
- Billing Service -> Billing DB: Reads/writes financial records [TCP / mTLS]
- Integration Service -> Patient, Scheduling, EMR, & Billing DBs: Interoperability data sync [TCP / mTLS]

## Technology Stack
- PostgreSQL 16: Core relational data persistence with active/archival partitioning for performance
- CloudNativePG Operator: Kubernetes-native management of high-availability Patroni clusters
- HashiCorp Vault: Dynamic credential injection and automated rotation
- pgaudit: Immutable database audit logging for HIPAA compliance
- S3/MinIO: Encrypted object storage for immutable backups

## Rationale
The microservices-aligned database-per-service architecture prevents domain coupling and enforces strict security boundaries. Active/archival partitioning and automated replication ensure <1s P95 EMR query performance while supporting the 10-year data retention mandate.