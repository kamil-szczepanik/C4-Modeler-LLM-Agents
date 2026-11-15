## Overview
- Manages patient admissions, EMRs, scheduling, and billing for medium-sized clinics.
- Operates in a hybrid cloud environment requiring HIPAA/GDPR compliance and 99.99% availability.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, and Hospital Administrators
- Clinic Management System (Core Software System)
- External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- Identity Provider (IdP)
- Edge API Gateway and Asynchronous Event Broker

## Relationships
- Human actors to Clinic Management System via HTTPS (TLS 1.3)
- Clinic Management System to External Lab Systems via HL7 FHIR REST APIs over mTLS
- Clinic Management System to Payment Gateway via HTTPS / TLS 1.3
- Clinic Management System to Identity Provider via OIDC / OAuth 2.0 with MFA
- Hybrid nodes connected via IPsec VPN tunnels with mTLS (TLS 1.3)

## Technology Stack
- Kubernetes (`on-prem-k8s` and `eu-central-1` regions) for container orchestration
- AES-256 with customer-managed keys (CMK) for data at rest and WORM storage
- TLS 1.3 and mTLS for secure data in transit
- OAuth 2.0 / OIDC and JWT for authentication and token validation
- Message Queue / Event Broker for asynchronous decoupling

## Rationale
- Active-passive hybrid architecture eliminates wide-area network latency to maintain <1s EMR load times.
- Strict perimeter security, WORM logging, and mTLS ensure complete HIPAA and GDPR compliance.