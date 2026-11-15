## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely handle patient admissions, electronic medical records (EMR), scheduling, and billing. It enforces strict HIPAA and GDPR compliance while maintaining 99.99% high availability and high-performance clinical workflows.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, and Hospital Administrators (Primary Users)
- WAF Container (Web Application Firewall at perimeter)
- API Gateway (Kubernetes Ingress / Gateway API)
- Patient Portal, EMR, Scheduling, Billing, Notification, and Analytics & Reporting Containers
- PostgreSQL Databases (with Patroni/etcd), Apache Kafka / RabbitMQ Event Broker, HashiCorp Vault (AES-256)
- External Systems: Insurance Clearinghouses, External Labs/Imaging Vendors

## Relationships
- Users -> WAF Container: Accesses system securely via HTTPS [HTTPS (TLS 1.3), OAuth2/OIDC, MFA]
- WAF Container -> API Gateway: Forwards filtered traffic securely [mTLS]
- EMR Container -> HL7 FHIR APIs: Exchanges lab and imaging data with external systems [HL7 FHIR REST/JSON]
- Containers -> PostgreSQL Databases / HashiCorp Vault: Persists records and fetches encrypted secrets [TLS, AES-256]

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid cloud orchestration ensuring active-active 99.99% uptime.
- PostgreSQL with Patroni/etcd: High-availability relational storage for strict data integrity and 10-year retention.
- Apache Kafka / RabbitMQ: Event broker for asynchronous messaging across microservices.
- HashiCorp Vault: Secrets management enforcing AES-256 encryption at rest.
- OWASP Core Rule Set & In-Memory Redaction: Perimeter security protecting against OWASP threats while masking PHI.

## Rationale
This architecture uses a hybrid Kubernetes deployment with an mTLS-secured WAF and API Gateway perimeter to guarantee 99.99% availability and strict HIPAA/GDPR compliance. Decoupled microservices backed by encrypted PostgreSQL and Kafka ensure high-performance EMR rendering under 1 second while safely managing sensitive healthcare workloads.