## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict clinical interoperability, and comprehensive regulatory compliance across on-premises and AWS environments.

## Key Elements
- **Actors:** Patient (Patient Portal via HTTPS), Clinician/Doctor (HTTPS/MFA), Receptionist (HTTPS/MFA), Billing Staff (HTTPS/MFA)
- **Software System:** Clinic Management System (Hybrid Architecture spanning on-premises and AWS eu-central-1)
- **Containers:** Patient Portal (SPA/Mobile), On-Premises Clinical Service, AWS Billing & Claims Service, Identity Provider (IdP)
- **External Systems:** External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, On-Premises Hardware Security Module (HSM)

## Relationships
- Patient Portal to Clinic Management System via HTTPS/TLS 1.3
- Clinicians, Receptionists, and Billing Staff to Clinic Management System via HTTPS/MFA with fine-grained RBAC/ABAC
- Clinic Management System to External Lab & Imaging Systems via HL7 FHIR over REST/TLS 1.3
- Clinic Management System to Payment Gateway / Insurance Clearinghouse via REST/TLS 1.3
- Clinic Management System to Identity Provider via OIDC/SAML
- On-Premises Kubernetes Cluster to AWS eu-central-1 via redundant IPsec Site-to-Site VPN with mTLS

## Technology Stack
- **Compute & Orchestration:** Kubernetes (on-premises and cloud) for container management and active-active scaling
- **Interoperability:** HL7 FHIR for standardized clinical data exchange
- **Security & Encryption:** AES-256 for data at rest, TLS 1.3 and IPsec for data in transit, on-premises HSM for key management, OIDC/SAML for authentication
- **Telemetry:** OpenTelemetry and Prometheus for unified hybrid observability and immutable audit logging

## Rationale
This architecture guarantees strict HIPAA and GDPR compliance by maintaining Patient Health Information (PHI) on-premises under data sovereignty rules while leveraging AWS for scalable billing workloads. Redundant IPsec tunnels and autonomous edge caching ensure 99.99% availability and uninterrupted clinical operations during network partitions.