## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability (99.99%), strict regulatory compliance (HIPAA/GDPR), and ten-year data retention.

## Key Elements
- **Users:** Patients, Clinicians/Doctors, Administrative Staff, Billing Officers, and Compliance Officers/Auditors.
- **Core System:** Clinic Management System bounded context.
- **External Systems:** External Insurance/Clearinghouse System, and External Laboratory & Imaging System.
- **Containers/Components:** On-premise Kubernetes clusters, AWS `eu-central-1` cloud environment, sidecar log collectors (FluentBit), WORM object storage tier, and Enterprise Identity Provider (IdP).

## Relationships
- **Users to Clinic Management System:** HTTPS/TLS 1.3 with OAuth 2.0/OIDC step-up Multi-Factor Authentication (MFA) and Role-Based/Attribute-Based Access Control (RBAC/ABAC).
- **Clinic Management System to External Insurance System:** HTTPS / REST (HL7 FHIR) for real-time claim adjudication.
- **Clinic Management System to Lab & Imaging Systems:** HL7 FHIR over mutual TLS (mTLS).
- **Hybrid Infrastructure:** Encrypted VPN/Direct Connect tunnels with BGP failover between on-premise clusters and AWS `eu-central-1`.

## Technology Stack
- **Kubernetes:** On-premise and AWS `eu-central-1` deployment targets for active-active hybrid orchestration.
- **APIs & Protocols:** HL7 FHIR over mTLS and REST over TLS 1.3 for interoperability and secure communication.
- **Security & Cryptography:** AES-256 encryption at rest with envelope encryption using Cloud KMS/HSM and customer-managed keys (CMK).
- **Observability:** FluentBit sidecar collectors for asynchronous, immutable WORM log shipping.
- **Identity:** Enterprise Identity Provider supporting OIDC/SAML 2.0 and MFA.

## Rationale
The hybrid architecture balances strict compliance and data sovereignty (local on-premise control with AWS `eu-central-1`) with high availability (99.99% active-active). Asynchronous log shipping and tiered WORM storage isolate heavy audit and retention workloads to protect sub-second EMR performance.