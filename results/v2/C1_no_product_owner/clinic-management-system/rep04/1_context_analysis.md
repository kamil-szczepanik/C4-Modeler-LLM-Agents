## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external clinical systems.

## Key Elements
- **Users:** Patient/Client, Clinician/Medical Staff, Billing Admin
- **Core System:** Clinic Management System
- **Containers/Services:** On-premise Kubernetes clusters, AWS `eu-central-1` primary tier
- **External Systems:** External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- **Infrastructure Components:** Apache Kafka / AWS MSK event backbone, AWS S3 Object Lock (WORM storage), Cloud HSMs

## Relationships
- **Users to Core System:** Interact via HTTPS (Web/Mobile portal, EMR, billing interfaces).
- **Core System to Identity Provider:** Authenticates users via OIDC/SAML with short-lived JWTs and multi-factor authentication (MFA).
- **Core System to Lab & Imaging Systems:** Integrates via HL7 FHIR (REST/JSON over TLS).
- **Core System to Payment Gateway:** Submits claims via secure REST APIs.
- **Cross-Boundary & Inter-Service:** Secured via mutual TLS (mTLS), payload-level envelope encryption, and Zero Trust network policies.

## Technology Stack
- **Compute & Orchestration:** On-Premises Kubernetes and AWS (`eu-central-1`) for hybrid workload distribution.
- **Messaging & Integration:** Apache Kafka / AWS MSK with dead-letter queues for asynchronous, distributed event processing.
- **Security & Compliance:** Cloud HSMs for AES-256 key management at rest; AWS S3 Object Lock for 10-year WORM audit trails.
- **Deployment & Observability:** ArgoCD for GitOps continuous delivery; Fluentbit for centralized logging.

## Rationale
This hybrid architecture pairs local on-premise Kubernetes caching with AWS `eu-central-1` to achieve sub-second EMR performance and 99.99% availability without split-brain risks. Robust cryptographic controls, mTLS, and immutable WORM storage ensure strict compliance with HIPAA and GDPR data retention mandates.