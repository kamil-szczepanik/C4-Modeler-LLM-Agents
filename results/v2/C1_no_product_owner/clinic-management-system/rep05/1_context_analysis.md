## Overview
The Clinic Management System (CMS) orchestrates patient admissions, electronic medical records, scheduling, and billing for healthcare facilities. It operates within a hybrid cloud environment to satisfy high availability and strict medical compliance requirements.

## Key Elements
- Patients, Doctors, Nurses, and Administrative Staff (Users)
- Clinic Management System (Core Software System)
- External Laboratory & Imaging Systems
- Payment Gateway and Insurance Clearinghouse
- Identity Provider (IdP) with OIDC/SAML
- SIEM & Audit Platform and Enterprise KMS
- Global Traffic Manager / WAF with GSLB

## Relationships
- Users to CMS via HTTPS / Web / Mobile / Desktop Apps
- CMS to External Laboratory & Imaging Systems via HL7 FHIR over HTTPS
- CMS to Payment Gateway via secure API over HTTPS
- CMS to IdP via OIDC/SAML for Multi-Factor Authentication
- CMS to SIEM & Audit Platform via encrypted Syslog / HTTPS
- CMS to Enterprise KMS via PKCS#11 / Cloud KMS API over TLS 1.3
- On-prem Kubernetes cluster and AWS (`eu-central-1`) connected via Istio/Linkerd mTLS (TLS 1.3)

## Technology Stack
- Hybrid Cloud (On-prem Kubernetes and AWS `eu-central-1`) for high availability and regional failover
- HL7 FHIR APIs for medical interoperability with external clinical systems
- AES-256 with Hardware Security Module (HSM) backed Key Management Services for data at rest
- Istio or Linkerd service mesh for cryptographic service isolation and mTLS
- Global Traffic Manager / WAF for active-active edge routing and DDoS protection

## Rationale
This hybrid architecture isolates high-frequency clinical workloads while leveraging cloud scalability to achieve 99.99% availability. Strict zero-trust networking, mTLS, and dedicated KMS integration ensure full compliance with HIPAA, GDPR, and 10-year data retention mandates.