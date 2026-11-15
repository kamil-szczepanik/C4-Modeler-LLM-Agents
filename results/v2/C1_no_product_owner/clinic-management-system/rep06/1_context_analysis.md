## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and strict data retention over 10 years.

## Key Elements
* **Software System:** Clinic Management System (CMS) operating across hybrid infrastructure
* **People:** Doctor, Receptionist, Patient, Billing Administrator, System Administrator
* **External Systems:** External Lab / Imaging Systems, Payment Gateway, Insurance Payer APIs, Enterprise Identity Provider (IdP)

## Relationships
* **Users -> CMS:** HTTPS / WebSockets with mandatory multi-factor authentication (MFA)
* **CMS -> Enterprise IdP:** OIDC / SAML over HTTPS for centralized authentication
* **CMS -> External Lab / Imaging Systems:** HTTPS / REST using HL7 FHIR protocols
* **CMS -> Payment Gateway & Insurance Payers:** HTTPS / REST over TLS 1.3
* **On-Prem-K8s <-> EU-Central-1:** Mutual TLS (mTLS) via Istio service mesh with circuit breaking

## Technology Stack
* **Deployment:** Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) managed via GitOps (ArgoCD) for uniform deployments
* **Security & Encryption:** AES-256 at rest with FIPS 140-2/3 validated HSM envelope encryption and OAuth2/OIDC with FIDO2/WebAuthn MFA
* **Networking & Mesh:** Istio service mesh for mTLS and perimeter API gateways with fail-safe autonomy
* **Observability:** OpenTelemetry for distributed tracing and centralized log shipping with local PII masking

## Rationale
This hybrid architecture uses geo-distributed redundancy and strict mTLS perimeter controls to guarantee 99.99% availability and high-performance EMR loading. FIPS-validated envelope encryption and immutable audit trails satisfy rigorous HIPAA and GDPR compliance mandates.