## Overview
The Clinic Management System is a hybrid healthcare platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. It ensures HIPAA and GDPR compliance while maintaining high availability across distributed clinical environments.

## Key Elements
- **Users**: Patients, Clinical Staff (Doctors & Nurses), Administrative & Billing Staff, Hospital IT / Compliance Officers
- **Core System**: Clinic Management System (Distributed Hybrid Architecture)
- **Containers/Nodes**: Clinic Edge Nodes (On-Premises K8s) and Central Cloud Backbone (`eu-central-1` AWS)
- **External Systems**: Identity Provider (IdP), Third-Party Payment Gateway, External Lab & Imaging Systems

## Relationships
- Users to Clinic Management System via HTTPS / TLS 1.3 with mandatory MFA
- Clinic Edge Nodes to Central Cloud Backbone via IPsec VPN / AWS Direct Connect tunnels using asynchronous sync and CRDTs
- Clinic Management System to Identity Provider via OIDC / SAML
- Clinic Management System to Third-Party Payment Gateway via HTTPS / REST
- Clinic Management System to External Lab & Imaging Systems via HL7 FHIR APIs (HTTPS / REST over mTLS)

## Technology Stack
- **Compute & Orchestration**: Kubernetes (On-Premise K8s and AWS) managed via GitOps (ArgoCD/Flux) for fleet management
- **Security & Encryption**: TLS 1.3, end-to-end mTLS, AES-256 with customer-managed keys (CMK), and WORM storage for immutable audit logs
- **Data & Synchronization**: CRDTs (Conflict-free Replicated Data Types) and local caching for edge resilience
- **Observability**: OpenTelemetry for unified telemetry across hybrid nodes

## Rationale
The hybrid architecture guarantees 99.99% availability and local resilience through edge nodes that operate autonomously during WAN partitions. This setup strictly enforces HIPAA and GDPR compliance via localized data caching, cryptographic erasure, and secure cloud synchronization.