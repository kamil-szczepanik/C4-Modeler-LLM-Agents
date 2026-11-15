## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized healthcare facilities. It features a hybrid cloud architecture designed for high availability, strict HIPAA/GDPR compliance, and long-term secure data retention.

## Key Elements
- Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors
- React SPA & React Native Mobile Client
- Envoy API Gateway / Edge Proxy
- EMR & Scheduling Service (Java / Node.js)
- Billing & Claims Service (Java / Spring Boot)
- FHIR Interoperability Service (HAPI FHIR)
- Region-local PostgreSQL databases
- Apache Kafka / RabbitMQ message brokers
- AWS S3 / on-prem MinIO WORM Object Storage
- HashiCorp Vault
- Centralized SIEM & Observability Platform

## Relationships
- Clients -> Envoy API Gateway: Client traffic routed via [HTTPS / REST / WSS]
- EMR & Billing Services -> AWS S3 / MinIO WORM Storage: Write immutable payloads via [HTTPS / S3 API] with AES-256 encryption
- Storage Tiering Scheduler -> Object Storage Engine: Enforces lifecycle transitions via [S3 Lifecycle API]
- Object Storage Engine -> Centralized SIEM: Streams audit logs via [Syslog / HTTPS]
- Services -> HashiCorp Vault: Manages encryption keys via [HTTPS / Vault API]

## Technology Stack
- React & React Native: Cross-platform client UI layer ensuring responsive clinician and patient workflows.
- Java / Spring Boot & Node.js: Robust backend microservices handling clinical business logic and high-throughput transactions.
- PostgreSQL: Region-local relational storage for transactional integrity and low-latency EMR access.
- Apache Kafka / RabbitMQ: Event brokers enabling reliable asynchronous messaging across services.
- AWS S3 (Object Lock Compliance Mode) & MinIO: Hybrid object storage enforcing 10-year immutable WORM retention.
- HashiCorp Vault: Centralized secret and encryption key management ensuring cryptographic compliance.

## Rationale
The hybrid architecture utilizes active-active geo-distribution (`eu-central-1` and on-premises Kubernetes) to guarantee 99.99% uptime and low-latency performance. Integrated AWS S3 Object Lock and MinIO WORM storage, paired with HashiCorp Vault, satisfy rigorous HIPAA/GDPR mandates and 10-year audit retention constraints.