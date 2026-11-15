## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance, and seamless interoperability with external clinical and financial services.

## Key Elements
- Patients / Consumers
- Clinic Staff / Receptionists
- Healthcare Providers (Doctors/Nurses)
- Billing Specialists
- System Administrators / Compliance Officers
- Clinic Management System (Core Software System)
- Identity Provider (IdP)
- Lab & Imaging Systems
- Payment Gateway / Insurance Clearinghouse
- Public Health Authority / Regulatory Registry

## Relationships
- Users to Clinic Management System via HTTPS
- Clinic Management System to Identity Provider via OIDC/SAML
- Clinic Management System to Lab & Imaging Systems via HL7 FHIR over HTTPS
- Clinic Management System to Payment Gateway via HTTPS
- Clinic Management System to Public Health Authority via SFTP/HTTPS (encrypted batch exports)
- On-prem Kubernetes cluster to AWS eu-central-1 via mTLS hybrid link

## Technology Stack
- Kubernetes (on-premises and AWS eu-central-1): Enables high availability (99.99% active-active) across the hybrid cloud deployment.
- HL7 FHIR: Standardizes interoperability with external diagnostic and imaging systems.
- OIDC/SAML: Manages secure enterprise authentication and multi-factor authentication.
- AES-256: Secures data at rest across all persistent storage tiers.
- TLS 1.3 / mTLS / SSH-2: Secures data in transit internally and externally.

## Rationale
The hybrid architecture balances on-premise control with cloud scalability to meet strict HIPAA and GDPR compliance requirements. AES-256 encryption, OIDC/SAML authentication, and HL7 FHIR standards collectively ensure high availability, data security, and interoperability.