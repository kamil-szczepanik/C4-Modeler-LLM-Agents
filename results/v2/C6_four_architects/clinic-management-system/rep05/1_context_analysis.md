## Overview
The Clinic Management System is a distributed healthcare platform designed to manage patient admissions, electronic medical records, scheduling, and billing. It operates in a hybrid cloud environment to ensure high availability, strict regulatory compliance, and low-latency clinical operations.

## Key Elements
*   **Users:** Patient (Web/Mobile), Clinician/Staff (Desktop/Web), Billing Administrator (Web).
*   **Containers & Services:** Patient Portal App (React/TypeScript), Clinician Workspace (Electron/React), API Gateway/Load Balancer (NGINX/AWS ALB), Core EMR Service, Billing & Claims Service.
*   **Infrastructure & Data Stores:** PostgreSQL (AES-256 at rest), Managed AWS RDS, Apache Kafka/RabbitMQ message broker, On-Premise Kubernetes (`on-prem-k8s`), AWS (`eu-central-1`).
*   **External Systems:** Identity Provider (IdP), Insurance Gateway, External Lab & Imaging Systems, National Health Registry, External Archival Storage, SMS/Notification Gateway.

## Relationships
*   **Patients & Staff $\rightarrow$ API Gateway:** HTTPS (TLS 1.3) for portal access, registration, and scheduling.
*   **API Gateway $\rightarrow$ Microservices:** gRPC for internal service-to-service communication.
*   **CMS $\rightarrow$ IdP:** OIDC/SAML 2.0 for federated multi-factor authentication.
*   **CMS $\rightarrow$ Lab & Imaging Systems:** HL7 FHIR over HTTPS via `on-prem-k8s`.
*   **CMS $\rightarrow$ Insurance Gateway & Registry:** REST/JSON over HTTPS with mTLS.
*   **Services $\rightarrow$ Databases:** TLS 1.3 for encrypted connections to PostgreSQL and AWS RDS.

## Technology Stack
*   **Frontend:** React, TypeScript, Electron for client applications.
*   **Backend & Gateway:** Go or Java/Spring Boot for core microservices; NGINX and AWS ALB for routing and TLS termination.
*   **Messaging:** Apache Kafka or RabbitMQ for asynchronous event decoupling.
*   **Databases:** PostgreSQL with AES-256 encryption at rest and managed AWS RDS.
*   **Deployment:** Hybrid model utilizing on-premise Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`).

## Rationale
This hybrid architecture isolates sensitive clinical workloads on-premises for low-latency device integration and data sovereignty while leveraging AWS cloud scalability for patient portals and billing. The selected protocols and encryption standards satisfy HIPAA, GDPR, and 99.99% availability requirements.