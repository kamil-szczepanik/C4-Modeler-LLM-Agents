## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR performance.]

## Key Elements
- Patients, Receptionists, Clinical Staff, Billing Specialists
- API Gateway (Kong Enterprise)
- Patient Portal Service, Scheduling Service, EMR Service, Billing Service, HL7 FHIR Integration Service, Analytics Service
- PostgreSQL Database, Apache Kafka, External Vault/HSM
- Identity Provider

## Relationships
- Users -> API Gateway: Access workflows [HTTPS via OAuth2/OIDC, Multi-Factor Auth, TLS 1.3]
- API Gateway -> Microservices: Routes validated requests [gRPC over mTLS, HTTP/2]
- API Gateway -> Identity Provider: Validates user tokens [OIDC/OAuth2]
- Microservices -> PostgreSQL Database: Persists encrypted data [SQL via TLS, AES-256 at rest]
- Microservices -> Apache Kafka: Streams clinical and billing events [TCP]

## Technology Stack
- Kong Enterprise: Chosen as the API Gateway for active-active hybrid Kubernetes routing and security plugin extensibility.
- PostgreSQL: Provides reliable relational data storage with AES-256 encryption at rest for HIPAA compliance.
- Apache Kafka: Enables high-throughput asynchronous event streaming between clinical and billing microservices.
- gRPC over mTLS: Ensures ultra-low latency and secure eastward communication between the gateway and microservices.

## Rationale
[This hybrid architecture combines active-active Kubernetes clusters with encrypted relational storage to meet strict 99.99% availability and data retention mandates. It leverages gRPC and edge caching to satisfy sub-second EMR performance constraints while maintaining robust HIPAA and GDPR security controls.]