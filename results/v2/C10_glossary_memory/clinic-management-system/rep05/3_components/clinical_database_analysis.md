## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for healthcare providers in a hybrid cloud environment, ensuring HIPAA and GDPR compliance. It leverages a secure, resilient microservices architecture backed by a distributed database tier to maintain high availability and sub-second response times.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists
- **External Systems**: Lab & Imaging Systems, Insurance Payment Gateway, Identity Provider, Patient Portal, Notification Gateway, Hybrid API Gateway
- **Containers**: API Gateway / BFF Container (Kong / Envoy), EMR Service Container (Java / Spring Boot), Scheduling Service Container (Node.js / TypeScript), Billing Service Container (Go), Integration Service Container (Apache Camel / FHIR Server), Clinical Database (PostgreSQL), Audit & Observability Sidecar (FluentBit / Prometheus)
- **Database Components**: PostgreSQL Primary Node, PostgreSQL Read Replicas, Connection Pooler (PgBouncer), Data Archival Worker, PostgreSQL RLS Enforcer

## Relationships
- **Patient Portal -> Clinic Management System**: HTTPS/REST
- **Lab & Imaging Systems -> Integration Service Container**: HL7 FHIR over HTTPS
- **Insurance Payment Gateway -> Billing Service Container**: TLS 1.3
- **Identity Provider -> API Gateway / BFF Container**: OIDC/SAML 2.0
- **API Gateway / BFF Container -> EMR Service Container**: gRPC over mTLS
- **EMR Service Container -> Connection Pooler**: Queries patient records [TCP over mTLS]
- **Connection Pooler -> PostgreSQL Primary Node**: Routes write transactions [TCP over mTLS]
- **Connection Pooler -> PostgreSQL Read Replicas**: Routes read queries [TCP over mTLS]
- **Data Archival Worker -> PostgreSQL Primary Node**: Archives historical records [TCP over mTLS]
- **Clinical Database -> Audit & Observability Sidecar**: Streams cryptographically signed WALs [Local IPC / File Tail]

## Technology Stack
- **PostgreSQL 15**: Provides robust transactional storage, read replicas, and row-level security for data isolation.
- **PgBouncer**: Manages high concurrency and connection pooling for database services.
- **Java / Spring Boot & Node.js**: Powers resilient business logic and scheduling containers.
- **Apache Camel / FHIR Server**: Ensures HL7 interoperability with external clinical systems.
- **FluentBit / Prometheus**: Delivers tamper-evident logging, metrics, and audit tracking.

## Rationale
This architecture uses an active-passive hybrid deployment model with connection pooling and row-level security to satisfy strict HIPAA/GDPR compliance and 99.99% availability constraints. Off-peak archival workers and read replicas ensure sub-second EMR performance without compromising long-term data retention mandates.