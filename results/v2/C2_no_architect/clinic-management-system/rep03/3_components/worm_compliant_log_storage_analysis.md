## Overview
[The Clinic Management System provides patient registration, appointment scheduling, EMR, and billing for healthcare providers. It is architected for hybrid deployment with HIPAA/GDPR compliance and 99.99% availability.]

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Officers, Compliance Officers, Auditors, Patients
- **Systems**: Clinic Management System, Lab Systems, Imaging Systems
- **Containers**: Ingress Controller (Kubernetes Ingress / Istio), Patient Registration Container, Appointment Scheduling Container, EMR Container, Billing & Insurance Claim Container, HL7 FHIR Interoperability Engine, PostgreSQL/MySQL Hybrid Databases, WORM-Compliant Log Storage, Compliance Reporting Dashboard
- **Components**: Metadata Indexing Layer, Local-Buffering Proxy

## Relationships
- **EMR Container -> WORM-Compliant Log Storage**: Sends asynchronous audit logs [gRPC/TLS with mTLS]
- **Patient Registration Container -> WORM-Compliant Log Storage**: Sends asynchronous audit logs [gRPC/TLS with mTLS]
- **Clinic Management System -> Lab Systems / Imaging Systems**: Exchanges clinical data [HL7 FHIR REST APIs]
- **Compliance Officers / Auditors -> Compliance Reporting Dashboard**: Accesses audit reports [OAuth2/OIDC, MFA, RBAC]

## Technology Stack
- **Orchestration**: Kubernetes (on-prem-k8s and AWS eu-central-1) for hybrid active-active deployment meeting 99.99% availability.
- **Databases**: PostgreSQL/MySQL with AES-256 encryption at rest for core transactional data.
- **Storage & Immutability**: AWS S3 Object Lock and immutable on-prem appliances with AES-256 and HSM-backed CMEK to satisfy 10-year retention.
- **Security & Protocols**: gRPC over TLS 1.3 with mTLS, OAuth2/OIDC, and TPM/HSM-backed edge encryption for zero-trust logging.

## Rationale
[This hybrid architecture utilizes cloud-native immutability controls and local edge-buffering proxies to guarantee 99.99% uptime and tamper-proof 10-year data retention. Strict zero-trust security measures and HL7 FHIR interoperability ensure complete HIPAA and GDPR compliance.]