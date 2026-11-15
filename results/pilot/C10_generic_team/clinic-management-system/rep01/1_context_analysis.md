## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical operations while strictly enforcing HIPAA and GDPR compliance across distributed environments.

## Key Elements
*   **Users:** Clinical Staff, Administrative Staff, Patients, and External Labs/Imaging Systems.
*   **Systems:** Clinic Management System (Core), External Lab Systems, External Imaging Systems, and Third-Party Billing/Insurance Gateways.
*   **Containers:** API Gateway, EMR Service, Scheduling Service, Billing Service, Patient Registration Service, and Message Queue/Event Bus.
*   **Components:** Read Replicas, Caching Layer, FHIR Adapter, Immutable Audit Logger, and ABAC Security Engine.

## Relationships
*   **Users to API Gateway:** Clinical staff and patients access front-end applications via HTTPS (TLS 1.3) with Multi-Factor Authentication (MFA).
*   **API Gateway to Microservices:** Routes internal traffic to EMR, Scheduling, and Billing services using gRPC and REST over TLS.
*   **EMR Service to External Labs/Imaging:** Integrates using HL7 FHIR APIs over HTTPS.
*   **Services to Data Storage:** Utilizes PostgreSQL databases with AES-256 encryption at rest, protected by active-active replication across on-prem-k8s and AWS eu-central-1.

## Technology Stack
*   **Orchestration & Infrastructure:** Kubernetes (on-prem-k8s and AWS eu-central-1) for hybrid active-active container orchestration.
*   **API & Integration:** HL7 FHIR for clinical interoperability, gRPC for internal service-to-service communication, and REST.
*   **Database & Storage:** PostgreSQL with read replicas, CQRS, and automated cold-storage archiving for 10-year retention.
*   **Security & Compliance:** AES-256 encryption at rest, Attribute-Based Access Control (ABAC), and policy-as-code deployment validation.
*   **Resilience Patterns:** CQRS, Saga pattern, Bulkhead pattern, and Circuit Breakers for high availability and fault isolation.

## Rationale
This hybrid architecture uses active-active deployment across on-premises Kubernetes and AWS eu-central-1 to guarantee 99.99% uptime and low-latency EMR access. Domain-Driven Design, CQRS, and cryptographic audit logging ensure HIPAA/GDPR compliance, data residency, and the strict 10-year data retention mandate.