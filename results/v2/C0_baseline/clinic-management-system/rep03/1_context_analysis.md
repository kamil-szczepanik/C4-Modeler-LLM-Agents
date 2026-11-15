## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It operates as a hybrid architecture ensuring high availability and strict regulatory compliance.

## Key Elements
* Front Desk Staff, Clinicians, Billing Officers, Patients, and Regulatory Auditors
* Clinic Management System (internal hybrid software system)
* Identity Provider (OIDC/SAML)
* External Lab & Imaging Systems (HL7 FHIR)
* Third-Party Payment Gateway & Insurance Clearinghouse
* Centralized SIEM & Observability Platform
* Global Traffic Manager / Anycast DNS
* Distributed Network Interconnect / SD-WAN

## Relationships
* Users interact with the Clinic Management System via HTTPS and OIDC
* Clinic Management System integrates with Lab & Imaging Systems via HL7 FHIR over HTTPS
* Clinic Management System connects to Payment Gateway & Insurance Clearinghouse via REST over HTTPS
* Services communicate across the hybrid boundary using mTLS with SPIFFE/SPIRE identities
* Telemetry and audit logs stream to the SIEM Platform via secure syslog/OTLP with PHI masking

## Technology Stack
* Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`) for hybrid cloud deployment
* TLS 1.3 and mTLS for all network transport security
* AES-256 for data at rest, managed via on-prem Hardware Security Modules (HSMs) and AWS KMS
* OIDC/SAML for multi-factor authentication and identity federation
* DNSSEC and Anycast DNS for traffic routing and DDoS mitigation

## Rationale
This architecture satisfies high availability and sub-second performance SLAs through active-active hybrid redundancy and global traffic management. It enforces HIPAA and GDPR compliance via zero-trust boundaries, robust encryption, and centralized audit logging.