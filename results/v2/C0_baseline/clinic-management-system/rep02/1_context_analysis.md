## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and high-performance hybrid cloud operations.

## Key Elements
* **Users**: Patient, Clinician (Doctor/Nurse), Receptionist/Front Desk, Billing Specialist, Hospital Administrator.
* **System**: Clinic Management System (CMS).
* **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP).
* **Containers/Infrastructure**: Web Application Firewall (WAF), API Gateway, On-Premises & Cloud Kubernetes Clusters (`on-prem-k8s`, `eu-central-1`), WORM Object Storage.

## Relationships
* **Users to CMS**: Patients and staff access the CMS via HTTPS (Web/Mobile) through a WAF.
* **CMS Authentication**: CMS authenticates users against the IdP using OpenID Connect (OIDC) / SAML 2.0 with multi-factor authentication (MFA).
* **CMS to External Systems**: CMS integrates with External Lab Systems using HL7 FHIR APIs and Payment Gateways via REST, secured over TLS 1.3 and mTLS.
* **Internal Communication**: Inter-container communication within Kubernetes utilizes service mesh mTLS and OAuth2/JWT scopes.

## Technology Stack
* **Deployment**: Hybrid cloud (`on-prem-k8s` and `eu-central-1`) with Kubernetes edge resilience and local caching for offline operational modes.
* **Security**: AES-256 and field-level encryption for PHI/PII, customer-managed encryption keys (CMK) with FIPS 140-2 validation, WORM object storage for 10-year data retention, and OAuth2/JWT for access control.
* **Interoperability**: HL7 FHIR APIs, REST over TLS 1.3, and mTLS.
* **Observability**: Centralized OpenTelemetry injection for real-time tracking and telemetry.

## Rationale
This architecture eliminates data divergence risks in clinical records by avoiding eventual consistency while enforcing active-warm disaster recovery. Strict zero-trust boundaries, field-level encryption, and local Kubernetes caching satisfy stringent HIPAA/GDPR compliance and high-performance requirements.