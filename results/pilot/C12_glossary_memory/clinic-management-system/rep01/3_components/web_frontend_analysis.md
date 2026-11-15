## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized hospitals and clinics with high availability and strict regulatory compliance. It provides role-tailored access via a secure, high-performance web frontend backed by microservices and encrypted data storage.

## Key Elements
- Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators, Practice Managers
- Laboratory Information Systems (LIS), PACS Imaging Archives, Insurance Payment Gateways
- Web Frontend (React)
- API Gateway (Node.js)
- EMR Processing Service (Java Spring Boot)
- Billing Engine (Java Spring Boot)
- Interoperability Service (Python)
- Database (PostgreSQL)

## Relationships
- Front Desk Staff -> API Gateway (HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA)
- Clinicians -> API Gateway (HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA)
- Billing Specialists -> API Gateway (HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA)
- Patients -> API Gateway (HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA)
- Clinic Administrators -> API Gateway (HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA)
- Practice Managers -> API Gateway (HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA)
- Web Frontend -> API Gateway (HTTPS (TLS 1.3))
- API Gateway -> EMR Processing Service (Internal gRPC)
- API Gateway -> Billing Engine (Internal gRPC)
- API Gateway -> Interoperability Service (Internal gRPC)
- Interoperability Service -> Laboratory Information Systems (LIS) (HL7 FHIR APIs over secure mutual TLS (mTLS))
- Interoperability Service -> PACS Imaging Archives (HL7 FHIR APIs over secure mutual TLS (mTLS))
- Interoperability Service -> Insurance Payment Gateways (HL7 FHIR APIs over secure mutual TLS (mTLS))

## Technology Stack
- React: Powers the Single Page Application container with responsive UI and sub-second EMR rendering.
- Node.js: Implements the API Gateway for routing, OAuth/MFA enforcement, and security policies.
- Java Spring Boot: Drives the EMR Processing Service and Billing Engine for robust, isolated clinical and financial workflows.
- Python: Executes the Interoperability Service for parsing and translating HL7 FHIR payloads.
- PostgreSQL: Encrypted database cluster providing ACID compliance and AES-256 encryption at rest.

## Rationale
This architecture uses a hybrid cloud model (`on-prem-k8s` and `eu-central-1`) to achieve 99.99% high availability and satisfy strict HIPAA and GDPR data residency mandates. Containerized microservices communicate via internal gRPC and secure HL7 FHIR APIs, ensuring high performance, fault isolation, and strict data retention compliance for 10+ years.