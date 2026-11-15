## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, appointments, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention mandate.

## Key Elements
- **Clinic Management System:** Central software system boundary.
- **Hospital Staff:** Doctors, nurses, and admins interacting via HTTPS/MFA.
- **Patient Portal:** External system/actor for patient self-service.
- **External Lab & Imaging Systems:** Third-party clinical systems.
- **Insurance Clearinghouses:** External systems for claim submissions.
- **Identity Provider (IdP):** Enterprise authentication system (Azure AD / Keycloak).
- **Regulatory Audit System:** External system for compliance log ingestion.

## Relationships
- **Hospital Staff & Patient Portal -> Clinic Management System:** HTTPS (TLS 1.3), OIDC/SAML 2.0, OAuth2.
- **Clinic Management System -> Lab & Imaging Systems:** HL7 FHIR REST APIs over mTLS.
- **Clinic Management System -> Insurance Clearinghouses:** SFTP / HIPAA-compliant EDI (X12).
- **Clinic Management System -> Identity Provider:** OIDC / SAML 2.0.
- **Clinic Management System -> Regulatory Audit System:** Cryptographically signed webhooks/syslog over TLS.

## Technology Stack
- **Hybrid Cloud (`on-prem-k8s` + AWS `eu-central-1`):** Ensures high availability (99.99%) and local operational resilience.
- **HL7 FHIR & EDI X12:** Protocols for secure healthcare interoperability and billing.
- **OpenTelemetry & Centralized SIEM:** For distributed tracing and audit logging.
- **AES-256 & Envelope Encryption:** Secures patient data at rest across hybrid boundaries.

## Rationale
This hybrid architecture uses on-premise Kubernetes and AWS regions to guarantee active-active high availability and fault tolerance during WAN disruptions. Strict zero-trust boundaries, mTLS, and encrypted audit logging ensure full HIPAA and GDPR compliance.