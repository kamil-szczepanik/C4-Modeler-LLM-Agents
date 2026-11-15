## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It delivers high-availability clinical operations while enforcing strict HIPAA and GDPR compliance.

## Key Elements
* Front-Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Hospital Administrator, and Compliance Officer
* Clinic Management System (Core Software System hosted on Hybrid Kubernetes)
* External Lab & Imaging Systems, Third-Party Payment & Insurance Gateway, and Identity Provider (IdP)
* API Gateway / Edge Proxy and Centralized KMS

## Relationships
* Users to API Gateway: HTTPS / TLS 1.3 with OAuth 2.0 / OpenID Connect MFA
* CMS to External Lab & Imaging Systems: HL7 FHIR REST APIs over HTTPS
* CMS to Payment & Insurance Gateway: Secure REST/SOAP APIs
* Hybrid Clusters (`on-prem-k8s` to AWS `eu-central-1`): mTLS with mutual authentication and global traffic management

## Technology Stack
* Kubernetes: Hybrid orchestration (`on-prem-k8s` + AWS `eu-central-1`) for active-active 99.99% availability
* API Gateway: Edge proxy for TLS termination, JWT validation, rate limiting, and edge caching to ensure <1s P95 EMR load times
* OAuth 2.0 / OpenID Connect: Multi-factor authentication and role-based access control (RBAC/ABAC)
* HL7 FHIR: Standardized interoperability protocol for external lab and imaging systems
* AES-256 / WORM Storage: Data encryption at rest and immutable 10-year audit log retention

## Rationale
This hybrid architecture uses geo-distributed Kubernetes and edge caching to meet the stringent <1s EMR load and 99.99% uptime requirements. Simultaneously, robust mTLS, WORM storage, and centralized KMS ensure seamless HIPAA and GDPR compliance.