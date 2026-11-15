## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% uptime, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- **Patients**: End-users accessing the Web/Mobile Portal for registration and appointments.
- **Medical Staff**: Doctors, nurses, and receptionists managing EMRs, scheduling, and billing.
- **Clinic Management System (CMS)**: Core software system handling clinical and billing workflows across hybrid infrastructure.
- **External IdP**: Azure AD / Okta handling Multi-Factor Authentication via OIDC/SAML 2.0.
- **Payment Gateway**: External service processing patient billing and credit cards.
- **Lab & Imaging Systems**: Third-party medical systems communicating via HL7 FHIR APIs.
- **Notification Service**: Twilio/SendGrid gateway for SMS/Email reminders.

## Relationships
- **Patients / Medical Staff** interact with **CMS** via HTTPS/REST (Web/Mobile UI).
- **CMS** authenticates users against **External IdP** via OIDC/SAML 2.0.
- **CMS** processes payments with **Payment Gateway** via HTTPS/REST.
- **CMS** exchanges clinical data with **Lab & Imaging Systems** via HL7 FHIR REST APIs.
- **CMS** dispatches alerts via **Notification Service** using HTTPS/REST.

## Technology Stack
- **Hybrid Kubernetes (`on-prem-k8s` + `eu-central-1`)**: Satisfies data residency, local caching, and active-active 99.99% availability requirements.
- **TLS 1.3**: Secures all data in transit across external and internal boundaries.
- **AES-256**: Mandated for database and storage encryption at rest to meet security constraints.
- **HL7 FHIR**: Standardized protocol ensuring interoperability with external clinical systems.

## Rationale
This hybrid architecture combines on-premise Kubernetes clusters with cloud deployment to strictly satisfy HIPAA, GDPR, and data residency mandates. Active-active replication and OIDC/MFA integration securely deliver the required 99.99% availability and strict access controls.