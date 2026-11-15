## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It provides a secure, highly available hybrid cloud platform ensuring strict HIPAA and GDPR compliance.

## Key Elements
* **Human Actors:** Patient, Receptionist / Administrative Staff, Clinician / Doctor, Billing Specialist
* **Internal Systems:** Clinic Management System (CMS) core application running across hybrid infrastructure
* **External Systems:** External Lab & Imaging Systems, Third-Party Payment Gateway & Insurance Clearinghouses, Identity Provider (IdP)
* **Containers & Infrastructure:** On-Premises Kubernetes Clusters, AWS (`eu-central-1`), Local Caching Layers, Hardware Accelerators (AWS Nitro / HSMs), WORM Object Storage

## Relationships
* **Actors to CMS:** HTTPS / TLS 1.3 for all user interface interactions and web client access
* **CMS to IdP:** OpenID Connect (OIDC) / SAML 2.0 for Multi-Factor Authentication (MFA) and session management
* **CMS to Lab & Imaging Systems:** HL7 FHIR over HTTPS (REST/JSON) for diagnostic results interoperability
* **CMS to Payment Gateway/Clearinghouses:** Secure HTTPS API for billing and claims processing
* **Hybrid Interconnect:** Zero-Trust mTLS and dedicated VPN backhauls between on-prem clinics and AWS

## Technology Stack
* **Cloud Infrastructure:** Hybrid deployment utilizing On-Premises Kubernetes and AWS (`eu-central-1`) for active-active high availability
* **Security & Encryption:** AES-256 for data at rest, hardware accelerators (AWS Nitro / HSMs) for cryptographic offloading, Attribute-Based Access Control (ABAC)
* **Identity & Access:** OIDC / SAML 2.0 via external Identity Provider for MFA
* **Interoperability:** HL7 FHIR REST/JSON APIs
* **Deployment & Operations:** GitOps (ArgoCD) for container deployments, OpenTelemetry for HIPAA-compliant observability, WORM object storage for 10-year archiving

## Rationale
The hybrid architecture balances strict 99.99% availability and 10-year data retention requirements through active-active replication and WORM storage. Hardware-accelerated encryption and local caching maintain sub-second EMR performance without compromising HIPAA and GDPR security mandates.