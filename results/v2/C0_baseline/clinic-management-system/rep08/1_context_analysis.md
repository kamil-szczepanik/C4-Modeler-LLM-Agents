## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical workflows while strictly enforcing healthcare data security and regulatory compliance.

## Key Elements
*   **Users:** Patient, Clinician, Administrative Staff, Compliance Officer / Auditor
*   **Core System:** Clinic Management System (Hybrid on-premise Kubernetes & AWS `eu-central-1`)
*   **External Systems:** Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, SIEM & Immutable Cold Storage
*   **Infrastructure:** mTLS & IPsec VPN, OpenTelemetry Distributed Tracing, Cloud HSMs

## Relationships
*   Patients & Staff to Clinic Management System via HTTPS/TLS 1.3 (Multi-Factor Authentication via OIDC/SAML 2.0)
*   Clinic Management System to Identity Provider via OIDC/SAML 2.0 for authentication and RBAC/ABAC enforcement
*   Clinic Management System to Lab & Imaging Systems via HL7 FHIR (REST/JSON) for diagnostic data exchange
*   Clinic Management System to Payment Gateway / Insurance Clearinghouse via HTTPS/REST for claims submission
*   Clinic Management System to SIEM & Immutable Cold Storage via Syslog/TLS and cloud-native object storage APIs for HIPAA/GDPR audit trails

## Technology Stack
*   **Compute:** On-premise Kubernetes and AWS (`eu-central-1`) utilizing blue/green deployments for active-active 99.99% uptime
*   **Security & Encryption:** TLS 1.3 for data in transit, AES-256 with localized hardware-backed Cloud HSMs for data at rest
*   **Integration Protocols:** HL7 FHIR over REST/JSON, OIDC/SAML 2.0, HTTPS/REST
*   **Observability:** OpenTelemetry with strict PHI/PII payload masking for distributed tracing and SIEM log aggregation

## Rationale
This hybrid architecture combines on-premise infrastructure control with cloud scalability to meet stringent data residency and HIPAA/GDPR compliance mandates. Active-active deployments with dedicated cryptographic key management ensure high availability and uncompromised patient data protection.