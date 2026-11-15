## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring strict HIPAA and GDPR compliance. It leverages a hybrid cloud architecture to deliver high availability, secure data retention, and low-latency clinical operations.

## Key Elements
- API Gateway (NGINX/Kong)
- Identity Service (Keycloak)
- Patient & EMR Service (Spring Boot)
- Appointment Service (Spring Boot)
- Billing Service (Spring Boot)
- HL7 FHIR Integration Engine (Apache Camel)
- Event Broker (Apache Kafka)
- Primary Database & Tiered Storage (Patroni PostgreSQL Cluster, MinIO S3-compatible WORM storage, Data Proxy Component, Data Lifecycle Service)
- Audit Logging Service (Java / Spring Boot)

## Relationships
- Patient & EMR Service -> Primary Database & Tiered Storage: Reads/writes clinical data via PostgreSQL / S3 [TLS 1.3, mTLS]
- Billing Service -> Primary Database & Tiered Storage: Reads/writes billing data [TLS 1.3]
- HL7 FHIR Integration Engine -> External Labs & Imaging Systems: Exchanges health data [HTTPS / HL7 FHIR]
- API Gateway -> Microservices: Routes client requests [gRPC / HTTPS]

## Technology Stack
- Patroni PostgreSQL Cluster: Manages hot transactional data with synchronous replication for 99.99% uptime.
- MinIO S3-Compatible Storage: Provides Write-Once-Read-Many (WORM) object locking for 10-year compliance retention.
- PgBouncer: Handles dynamic connection pooling to maintain sub-second P95 performance.
- AES-256 & HSM: Secures data at rest via customer-managed keys and envelope encryption.
- Apache Kafka: Enables decoupled, event-driven messaging across services.

## Rationale
This hybrid architecture guarantees high availability (99.99%) through active-active synchronization across on-premise Kubernetes and AWS (`eu-central-1`). Tiered storage combined with row-level security and strict encryption fulfills strict HIPAA/GDPR compliance mandates without compromising sub-second EMR performance.