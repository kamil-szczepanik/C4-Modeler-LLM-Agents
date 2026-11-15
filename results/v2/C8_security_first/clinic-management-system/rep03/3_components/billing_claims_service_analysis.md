## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinical environments. It provides high availability and strict compliance for medium-sized hospitals and clinics.

## Key Elements
- **Users**: Billing Officers, Receptionists, Clinicians, Patients
- **External Systems**: Third-Party Payment Gateway & Insurance Clearinghouses, External Lab & Imaging Systems, Identity Provider (IdP)
- **Containers**: API Gateway (Kong/Nginx), Patient-Facing UI (React/Next.js), Clinical Core Services (Spring Boot), Interoperability Service (Apache Camel/Node.js), Billing & Claims Service (Spring Boot)
- **Components (Billing & Claims Service)**: Claim Management Component, Clearinghouse Adapter Component, Inbound Notification Listener, Financial Ledger & Audit Component, Billing Exception & DLQ Handler Component

## Relationships
- **Patient-Facing UI -> API Gateway**: Secure access via HTTPS/REST [HTTPS, REST]
- **API Gateway -> Clinical Core Services & Billing & Claims Service**: Internal routing via gRPC over mTLS [gRPC, mTLS]
- **Billing & Claims Service -> Interoperability Service**: Internal communication via gRPC over mTLS [gRPC, mTLS]
- **Billing & Claims Service -> Third-Party Payment Gateway & Insurance Clearinghouses**: Asynchronous messaging with JWE payload encryption [Kafka/RabbitMQ, JWE]

## Technology Stack
- **Spring Boot / Java**: Core application framework for robust business logic execution.
- **PostgreSQL**: Primary data store utilizing table partitioning for 10-year data retention compliance.
- **Kafka / RabbitMQ**: Message brokers handling asynchronous clearinghouse communication using the Transactional Outbox pattern.
- **HashiCorp Vault**: Dynamic secrets management for API keys, webhooks, and database credentials rotated every 30 days.
- **Kubernetes (on-prem-k8s, eu-central-1) & ArgoCD**: Container orchestration and GitOps deployment supporting active-active high availability.

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict network isolation, role-based access control, and encrypted payload handling. The resilient distributed design leverages the Transactional Outbox pattern and circuit breakers to meet the 99.99% availability SLA and 10-year data retention requirements.