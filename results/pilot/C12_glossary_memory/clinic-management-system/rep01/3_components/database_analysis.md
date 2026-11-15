## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability and strict regulatory compliance across on-premise Kubernetes and AWS eu-central-1.

## Key Elements
- Clinic Management System [system, context]
- Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators, Practice Managers [person, context]
- Laboratory Information Systems (LIS), PACS Imaging Archives, Insurance Payment Gateways [externalSystem, context]
- Web Frontend (React), API Gateway (Node.js), EMR Processing Service (Java Spring Boot), Billing Engine (Java Spring Boot), Interoperability Service (Python), Database (PostgreSQL) [container, container]

## Relationships
- Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators, Practice Managers -> API Gateway via HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA
- Web Frontend -> API Gateway via HTTPS (TLS 1.3)
- API Gateway -> EMR Processing Service, Billing Engine, Interoperability Service via Internal gRPC
- Interoperability Service -> Laboratory Information Systems (LIS), PACS Imaging Archives, Insurance Payment Gateways via HL7 FHIR APIs over secure mutual TLS (mTLS)

## Technology Stack
- React: Single Page Application framework for responsive user interfaces.
- Node.js: API Gateway runtime for high-throughput routing and authentication enforcement.
- Java Spring Boot: Robust enterprise framework for core clinical and billing microservices.
- Python: Flexible language runtime for handling complex HL7 FHIR interoperability payloads.
- PostgreSQL 16: Relational database with Patroni, PgBouncer, and `pgcrypto` providing ACID compliance, AES-256 encryption, and 99.99% availability.

## Rationale
The hybrid architecture distributes workloads securely across on-premise Kubernetes and AWS eu-central-1 to meet strict HIPAA and GDPR compliance requirements. Microservices and encrypted PostgreSQL clustering guarantee 99.99% uptime and high-performance EMR access.