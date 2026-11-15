## Overview
• Manages patient admissions, electronic medical records (EMR), scheduling, and billing for clinical IT environments.
• Built on a hybrid architecture ensuring HIPAA/GDPR compliance and 99.99% high availability.

## Key Elements
• **Users:** Patients, Receptionists, Clinicians, Billing Specialists, and Hospital Administrators.
• **External Systems:** Insurance Payers/Clearinghouses and External Labs/Imaging (HL7 FHIR).
• **Core Containers:** Perimeter API Gateway, EMR Service, Billing Service, and Authentication Service.
• **Infrastructure:** On-premise Kubernetes cluster and AWS (`eu-central-1`).

## Relationships
• Users access the Perimeter API Gateway via HTTPS using OAuth 2.0 / OIDC and MFA.
• Clinicians and Receptionists interact with the EMR and Scheduling containers using internal REST/gRPC protocols.
• External Labs and Imaging Systems integrate via HL7 FHIR APIs secured with Mutual TLS (mTLS).
• Insurance Payers connect via asynchronous queue-based buffering and Dead Letter Queues (DLQs).

## Technology Stack
• **Cloud & Containerization:** Hybrid deployment utilizing on-premise Kubernetes and AWS (`eu-central-1`) for active-active redundancy.
• **Security:** TLS 1.3 for data in transit, mTLS for external integrations, AES-256 with on-premise customer-managed keys (CMK) for data at rest.
• **Identity & Access:** OAuth 2.0, OpenID Connect (OIDC), multi-factor authentication (MFA), and Attribute-Based Access Control (ABAC).
• **Observability & Audit:** OpenTelemetry for distributed tracing and write-once-read-many (WORM) storage for audit trails.
• **Integration:** HL7 FHIR APIs and asynchronous message queues with envelope encryption.

## Rationale
• The hybrid active-active setup guarantees 99.99% availability and meets strict data residency mandates.
• Asynchronous queueing and rigorous cryptographic controls isolate external volatility while ensuring HIPAA and GDPR compliance.