## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics. It operates as a hybrid cloud architecture designed for high availability, strict data residency, and healthcare compliance.

## Key Elements
- Patients
- Doctors, Nurses, and Clinic Staff
- Hospital Administrators
- Billing Specialists / Revenue Cycle Managers
- Clinic Management System (Hybrid Software System)
- Payment Gateway
- Insurance Verification Service
- External Lab & Imaging Systems
- Public Health Registries

## Relationships
- Patients interact with the system via HTTPS for self-service scheduling and lab results.
- Clinical and administrative staff access the system via HTTPS with Multi-Factor Authentication (MFA).
- The system connects to the Payment Gateway using REST over TLS 1.3 for billing transactions.
- The system integrates with Insurance Verification and Public Health Registries via REST and OAuth2 over HTTPS.
- External Lab and Imaging Systems communicate with the platform via HL7 FHIR over HTTPS/TLS.
- Internal hybrid components communicate across boundaries using mutual TLS (mTLS) with TLS 1.3.

## Technology Stack
- **Compute:** Kubernetes (`on-prem-k8s` and cloud-based clusters in `eu-central-1`) for active-active container orchestration and high availability.
- **Security:** AES-256 for data at rest, envelope encryption with local Key Management Service (KMS) / Hardware Security Module (HSM), and OIDC/OAuth2 for MFA and RBAC/ABAC enforcement.
- **Interoperability:** HL7 FHIR APIs for standardized clinical data exchange.
- **Observability:** OpenTelemetry for unified distributed tracing, metrics, and log aggregation across hybrid environments.
- **Storage:** Local-first read-replicas with bounded staleness and immutable append-only logs for audit trails.

## Rationale
This hybrid architecture uses local-first on-premise Kubernetes clusters to guarantee continuous autonomous clinical workflows and zero downtime during network partitions. Simultaneously, cloud resources in `eu-central-1` handle heavy analytics, billing, and long-term 10-year cold storage while enforcing strict HIPAA and GDPR compliance.