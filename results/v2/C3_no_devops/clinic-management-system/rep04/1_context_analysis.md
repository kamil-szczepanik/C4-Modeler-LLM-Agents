## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, appointment scheduling, and medical billing. It ensures high availability, strict HIPAA/GDPR compliance, and seamless integration with external healthcare and financial networks.

## Key Elements
* **People**: Patient, Clinic Staff/Receptionist, Clinician/Doctor, Billing Specialist, System Administrator.
* **Internal System**: Clinic Management System (CMS).
* **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Payment Gateway.
* **Infrastructure**: On-premise Kubernetes and AWS (`eu-central-1`).

## Relationships
* **Patient / Staff / Clinician / Admin** -> **CMS**: HTTPS / TLS 1.3 via Secure Web & Mobile Client Gateway.
* **CMS** -> **Lab & Imaging Systems**: HL7 FHIR over HTTPS (REST/JSON).
* **CMS** -> **Insurance Clearinghouses**: X12 EDI over HTTPS.
* **CMS** -> **Identity Provider (IdP)**: OAuth2 / OIDC with Multi-Factor Authentication (MFA).
* **CMS** -> **Payment Gateway**: HTTPS (REST/JSON) with tokenization and HMAC request signing.

## Technology Stack
* **Deployment**: Hybrid cloud using on-premise Kubernetes and AWS (`eu-central-1`) to meet high availability (99.99%) and active-active constraints.
* **Security & Compliance**: TLS 1.3 for data in transit, AES-256 with customer-managed keys (CMK) for data at rest, OAuth2/OIDC for IAM, and RBAC/ABAC authorization.
* **Interoperability**: HL7 FHIR APIs and X12 EDI protocols for external clinical and financial system integration.

## Rationale
This hybrid architecture uses active-active deployment across on-premise Kubernetes and AWS to guarantee 99.99% availability and meet strict 10-year data retention mandates. Comprehensive security controls, tokenization, and standardized FHIR APIs ensure full HIPAA and GDPR compliance without sacrificing the high performance required for clinical workflows.