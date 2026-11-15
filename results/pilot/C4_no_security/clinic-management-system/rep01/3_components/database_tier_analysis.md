## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical workflows while strictly enforcing HIPAA and GDPR compliance across a hybrid infrastructure.

## Key Elements
- Patients, Clinical Staff, Hospital Administrators
- Global Anycast Load Balancer and API Gateways (Kong)
- Patient Portal (Node.js, React)
- EMR & Scheduling Service (Java Spring Boot)
- Billing & Insurance Claim Service (Python FastAPI)
- HL7 FHIR Interoperability Engine (Apache Camel)
- Database Tier (PostgreSQL with Patroni, PgBouncer, AES-256)
- Messaging & Audit Layer (Apache Kafka, FluentBit, S3)
- Infrastructure & Mesh (Kubernetes, AWS eu-central-1, on-prem-k8s, Envoy sidecar)

## Relationships
- Patients, Clinical Staff, Hospital Administrators -> Global Anycast Load Balancer: Accesses application via HTTPS [TLS 1.3]
- Patient Portal -> EMR & Scheduling Service: Routes API requests [gRPC / REST]
- EMR & Scheduling Service -> Database Tier: Persists and queries clinical state [Encrypted TCP, TLS 1.3]
- Billing & Insurance Claim Service -> Database Tier: Persists financial data [Encrypted TCP, TLS 1.3]
- HL7 FHIR Interoperability Engine -> Database Tier: Persists lab and imaging payloads [Encrypted TCP, TLS 1.3]
- Database Tier -> Messaging & Audit Layer: Streams audit logs and backups [FluentBit, AWS S3 Object Lock]

## Technology Stack
- PostgreSQL with Patroni & PgBouncer: Provides active-active high availability and connection pooling
- HashiCorp Vault: Manages AES-256 encryption keys for Transparent Data Encryption (TDE)
- Apache Camel: Powers the HL7 FHIR interoperability engine for lab and imaging integration
- Kubernetes (on-prem-k8s and AWS eu-central-1): Orchestrates the hybrid cloud deployment
- pg_backrest with AWS S3 Object Lock: Enforces immutable 10-year data retention and archiving

## Rationale
This architecture utilizes a distributed PostgreSQL cluster with asynchronous cross-site replication to achieve 99.99% uptime across hybrid cloud environments. Robust encryption, Row-Level Security, and automated auditing ensure strict compliance with HIPAA and GDPR mandates.