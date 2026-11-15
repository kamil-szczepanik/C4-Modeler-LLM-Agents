## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
* **Actors**: Patient, Clinic Staff/Receptionist, Clinician/Doctor, Billing Specialist, Hospital Administrator
* **Systems & Containers**: Clinic Management System (Core Software System), API Gateway / Edge Proxy
* **External Services**: Identity Provider (IdP), External Lab & Imaging Systems, External Payment Gateway & Insurance Clearinghouse

## Relationships
* **Actors to API Gateway**: HTTPS / TLS 1.3 (Web/Mobile) with OIDC / SAML 2.0 authentication and MFA
* **Clinic Management System to Lab & Imaging Systems**: HL7 FHIR over HTTPS with Mutual TLS (mTLS)
* **Clinic Management System to Payment/Insurance**: REST over TLS 1.3 with mTLS
* **Hybrid Interconnect (`on-prem-k8s` to `eu-central-1`)**: Encrypted VPN/Direct Connect with mTLS and AES-256 data encryption

## Technology Stack
* **Cloud & Orchestration**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for hybrid active-active deployment and 99.99% availability
* **Security & Auth**: OIDC, SAML 2.0, MFA, AES-256, and Mutual TLS (mTLS) to enforce HIPAA/GDPR compliance
* **Interoperability**: HL7 FHIR over HTTPS for standardized clinical data exchange
* **Observability & Edge**: OpenTelemetry and API Gateway / Edge Proxy for sub-second P95 performance and audit tracking

## Rationale
This hybrid architecture uses an API Gateway and containerized microservices to balance strict security and regulatory compliance with sub-second performance. The combination of active-active Kubernetes deployment and encrypted interconnects guarantees high availability and data protection across environments.