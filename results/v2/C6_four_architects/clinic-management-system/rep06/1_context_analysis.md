## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability (99.99%) and strict HIPAA and GDPR compliance with a 10-year data retention policy.

## Key Elements
- **Users & Actors:** Doctor, Nurse, Receptionist, Billing Officer, Patient, and Regulatory/Audit Authority.
- **External Systems:** Identity Provider (IdP), External Labs & Imaging Systems, Insurance Payment Gateway, and Hospital Notification/SMS Gateway.
- **Containers (AWS eu-central-1):** API Gateway / Edge Proxy, Scheduling & Billing Services.
- **Containers (On-Premises Kubernetes):** EMR & Patient Records Service, FHIR Integration Broker, Audit Logging Service & Storage, EMR Secure Datastore (AES-256 encrypted relational database).
- **Shared Infrastructure:** Message Broker / Event Bus (Kafka/RabbitMQ), Transactional Datastore (Managed PostgreSQL/Aurora).

## Relationships
- **Users/Patients -> API Gateway / Edge Proxy:** HTTPS and OAuth2/OIDC with multi-factor authentication (MFA) via TLS 1.3.
- **API Gateway -> Microservices:** Internal gRPC over mTLS routing.
- **EMR Service -> EMR Secure Datastore:** PostgreSQL wire protocol over mTLS with AES-256 encryption at rest.
- **CMS -> External Labs & Imaging Systems:** HL7 FHIR over HTTPS.
- **CMS -> Insurance Payment Gateway:** REST over TLS 1.3.
- **CMS -> Notification Gateway:** REST over TLS 1.3.
- **EMR Service -> Audit Logging Service:** gRPC over mTLS.

## Technology Stack
- **Kubernetes (on-prem-k8s):** Hosts sensitive EMR containers and secure datastores to satisfy local data sovereignty and GDPR/HIPAA compliance.
- **AWS (`eu-central-1`):** Hosts stateless scalable services (API Gateway, Scheduling, Billing, Transactional Datastore) for high availability.
- **gRPC / mTLS:** Used for secure internal container-to-container communication.
- **HL7 FHIR & REST / TLS 1.3:** Ensures interoperability with external medical systems and secure external communications.
- **Apache Kafka / RabbitMQ:** Provides asynchronous messaging to decouple services and support 99.99% availability.

## Rationale
The hybrid architecture places sensitive electronic medical records and audit logging on-premises for strict HIPAA and GDPR compliance, while leveraging AWS cloud infrastructure for scalable scheduling, billing, and high availability (99.99%). Asynchronous messaging and encrypted storage guarantee system resilience and data protection across all operational workflows.