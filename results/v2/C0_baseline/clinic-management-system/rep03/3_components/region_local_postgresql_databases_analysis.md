## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It utilizes a hybrid cloud architecture to ensure high availability, low-latency data access, and strict regulatory compliance.

## Key Elements
- React Single-Page Application / React Native Mobile Client
- Envoy API Gateway / Edge Proxy
- EMR & Scheduling Service (Node.js / Java)
- Billing & Claims Service (Java / Spring Boot)
- FHIR Interoperability Service (HAPI FHIR, Java)
- Region-local PostgreSQL databases (PostgreSQL, CNPG operator, Amazon RDS)
- PgBouncer Connection Pooler
- Localized Apache Kafka / RabbitMQ message brokers
- AWS S3 / on-prem WORM Object Storage
- HashiCorp Vault

## Relationships
- EMR & Scheduling Service -> Region-local PostgreSQL databases: Reads and writes operational data [Encrypted TCP, mTLS]
- Billing & Claims Service -> Region-local PostgreSQL databases: Reads and writes billing data [Encrypted TCP, mTLS]
- Region-local PostgreSQL databases -> AWS S3 / on-prem WORM Object Storage: Streams WAL and daily backups [Encrypted HTTPS / S3 API]
- Microservices -> HashiCorp Vault: Dynamically retrieves short-lived database credentials [Encrypted HTTPS]
- Region-local PostgreSQL databases -> Centralized SIEM: Forwards audit logs (`pgaudit`) [Encrypted TCP / Syslog]

## Technology Stack
- PostgreSQL / CNPG / Amazon RDS: Provides regional data storage with automated failover and Row-Level Security (RLS) to meet uptime and isolation mandates.
- PgBouncer: Manages high connection concurrency from microservices.
- HashiCorp Vault: Secures credentials via mTLS and dynamic secrets generation.
- AES-256 and TLS 1.3: Enforces data-at-rest and in-transit encryption for HIPAA/GDPR compliance.
- WORM Object Storage: Guarantees secure, immutable 10-year data retention.

## Rationale
This architecture uses regional PostgreSQL databases combined with connection pooling and automated failover to achieve sub-second EMR performance and 99.99% uptime. Strict encryption, audit logging, and role-based access mechanisms ensure full HIPAA and GDPR compliance across hybrid environments.