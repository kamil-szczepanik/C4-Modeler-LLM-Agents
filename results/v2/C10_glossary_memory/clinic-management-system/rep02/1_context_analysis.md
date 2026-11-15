## Overview
The Clinic Management System is a hybrid healthcare IT platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, secure operations, and regulatory compliance for medium-sized hospitals and clinics.

## Key Elements
- **Users**: Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators, Patients.
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Patient Portal / Mobile App.
- **Core Containers**: Unified API Gateway, EMR Microservice, Scheduling Service, Billing Service, Distributed Cache (Redis Enterprise).
- **Infrastructure**: On-premises Kubernetes (`on-prem-k8s`), AWS (`eu-central-1`), IPsec VPN.

## Relationships
- **Patient Portal to API Gateway**: HTTPS / REST and WebSocket via OIDC/OAuth 2.0.
- **Clinic System to Lab & Imaging Systems**: HL7 FHIR over HTTPS (REST/JSON) with W3C trace contexts.
- **Clinic System to Insurance Clearinghouses**: Secure EDI / HTTPS APIs with circuit breakers.
- **Clinic System to Identity Provider**: OIDC/SAML 2.0 over HTTPS for multi-factor authentication (MFA).
- **Hybrid Boundary (`on-prem-k8s` to `eu-central-1`)**: Encrypted IPsec site-to-site VPN and mutual TLS (mTLS).

## Technology Stack
- **Compute & Orchestration**: Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`) for active-active hybrid architecture.
- **Security & Identity**: Keycloak or Azure AD for IdP; HashiCorp Vault or AWS Secrets Manager for centralized secret management.
- **Data & Caching**: AES-256 encryption at rest; Redis Enterprise for distributed session state and WebSockets; WORM storage tier for audit logs.
- **Networking & Integration**: API Gateway for rate-limiting and JWT validation; TLS 1.3 for transit encryption.

## Rationale
This architecture ensures 99.99% active-active availability across hybrid regions while enforcing HIPAA and GDPR compliance. It leverages isolated trust boundaries, distributed caching, and asynchronous auditing to meet stringent performance and 10-year data retention mandates.