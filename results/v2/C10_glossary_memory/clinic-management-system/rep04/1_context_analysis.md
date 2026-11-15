## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA and GDPR compliance while maintaining high availability and sub-second performance.

## Key Elements
- **Actors:** Patient, Clinician (Doctors/Nurses), Billing/Admin Staff, Compliance Officer
- **Internal Systems:** Clinic Management System spanning `on-prem-k8s` and `eu-central-1`
- **External Systems:** Lab & Imaging Systems, Insurance Clearinghouse / External Billing Provider
- **Containers/Infrastructure:** Microservices mesh, active-active databases, secure secrets manager with HSM, CI/CD pipeline with runtime scanning

## Relationships
- **Actors to Clinic Management System:** HTTPS (TLS 1.3, OAuth2/OIDC, MFA)
- **Clinic Management System to Lab & Imaging Systems:** HL7 FHIR over REST/JSON (TLS 1.3)
- **Clinic Management System to Insurance Clearinghouse:** HTTPS / EDI X12
- **Internal Hybrid Interconnect (`on-prem-k8s` to `eu-central-1`):** mTLS and IPsec VPN tunnels

## Technology Stack
- **Infrastructure:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for active-active multi-region deployment and scalability
- **Security & Cryptography:** AES-256 for data-at-rest with customer-managed keys (CMK) via Hardware Security Modules (HSM); TLS 1.3 and mTLS for data-in-transit
- **Authentication & Authorization:** OAuth2/OIDC with multi-factor authentication (MFA) and Attribute-Based Access Control (ABAC)
- **Interoperability Standards:** HL7 FHIR (REST/JSON) and EDI X12 for external integrations

## Rationale
This architecture guarantees 99.99% active-active availability and sub-second EMR performance by combining edge-proximate on-premises Kubernetes with AWS cloud resources. Strict zero-trust microsegmentation, mTLS, and AES-256 encryption fulfill stringent HIPAA, GDPR, and 10-year audit retention mandates without compromising clinical workflows.