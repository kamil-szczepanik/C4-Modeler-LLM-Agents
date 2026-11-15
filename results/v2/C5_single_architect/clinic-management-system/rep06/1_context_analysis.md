## Overview
The Clinic Management System is a distributed clinical IT platform managing patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% uptime, and interoperability across hybrid cloud environments.

## Key Elements
- **Patient / User, Clinician / Staff, Hospital Administrator**: Internal actors accessing the system via HTTPS.
- **Clinic Management System (CMS)**: Core distributed software system handling clinical workflows.
- **External Lab & Imaging Systems**: External systems providing diagnostics.
- **Insurance Payment Gateways**: Third-party financial processors for claims.
- **Identity Provider (IdP)**: External system enforcing multi-factor authentication.
- **SMS / Notification Gateway**: External service for alerts and MFA.
- **Regulatory Compliance / Auditing Authority**: External entity for statutory reporting.

## Relationships
- **Patient, Clinician, Admin -> CMS**: HTTPS (TLS 1.3) for portal, EMR, and billing access.
- **CMS -> External Lab & Imaging Systems**: HL7 FHIR (REST/JSON over mTLS).
- **CMS -> Insurance Payment Gateways**: HTTPS/REST for claim submissions.
- **CMS -> Identity Provider (IdP)**: OIDC/SAML 2.0 for authentication.
- **CMS -> SMS / Notification Gateway**: SMPP / HTTPS REST for alerts.
- **CMS -> Regulatory Authority**: Secure batch export via SFTP/HTTPS.

## Technology Stack
- **Kubernetes (on-prem-k8s & eu-central-1)**: Hybrid cloud infrastructure to meet active-active 99.99% availability.
- **HL7 FHIR (REST/JSON)**: Interoperability standard for medical data exchange.
- **OIDC/SAML 2.0**: Authentication protocols for secure access and MFA enforcement.
- **AES-256**: Data encryption standard at rest for HIPAA/GDPR compliance.

## Rationale
This hybrid architecture isolates core clinical workflows behind standardized API boundaries while meeting strict regulatory and high-availability demands. Open protocols ensure seamless integration with external healthcare and payment ecosystems.