## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention policy via a hybrid cloud architecture.

## Key Elements
*   **Users:** Receptionist / Front Desk, Clinician / Doctor, Billing Specialist, Patient
*   **External Systems:** External Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP)
*   **API Gateway:** Kong / Envoy with TLS, mTLS, OIDC
*   **EMR & Scheduling Service:** Java / Spring Boot, Encrypted PostgreSQL
*   **Billing & Claims Service:** Node.js / TypeScript, Redis, RabbitMQ
*   **Interoperability Service:** .NET Core / Apache Camel
*   **Audit Logger Sidecar:** Lightweight container

## Relationships
*   API Gateway -> Billing & Claims Service: Route billing requests [HTTPS via mTLS]
*   Billing & Claims Service -> Insurance Clearinghouses: Submit automated claims and appeals [REST / HL7 FHIR over HTTPS with mTLS & OAuth 2.0]
*   RabbitMQ -> Payment Reconciliation Worker: Pushes payment status updates [AMQP]
*   Billing & Claims Service -> External Notification Service: Dispatches patient alerts [HTTPS]

## Technology Stack
*   **Node.js / TypeScript:** Core runtime for the Billing & Claims Service due to asynchronous I/O performance.
*   **PostgreSQL:** Primary database with column-level encryption and point-in-time recovery for HIPAA/GDPR data retention.
*   **Redis:** Master-replica cache for ephemeral transaction states and rate-limiting.
*   **RabbitMQ:** Message broker for asynchronous payment reconciliation with Dead-Letter Queues (DLQ).
*   **Kubernetes (K8s):** Active-active hybrid deployment across on-prem-k8s and `eu-central-1` with HPA scaling.

## Rationale
This architecture achieves 99.99% availability through active-active Kubernetes multi-region deployments and RabbitMQ decoupling. Strict security controls—including mTLS, AES-256, column-level encryption, and HashiCorp Vault secrets—guarantee HIPAA and GDPR compliance.