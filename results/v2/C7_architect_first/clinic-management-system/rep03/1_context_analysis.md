## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures high availability, 10-year data retention, and strict compliance with HIPAA and GDPR regulations.

## Key Elements
* **Users:** Doctors, Nurses, Receptionists, Billing Staff, Clinic Administrators, and Patients
* **Core System:** Clinic Management System (EMR, billing, scheduling engines)
* **External Systems:** Identity Provider (IdP), External Labs & Imaging Systems, Payment Gateway / Insurance Clearinghouse
* **Infrastructure:** On-Premises Kubernetes cluster (`on-prem-k8s`) and AWS Cloud (`eu-central-1`)

## Relationships
* Users -> Patient Portal / Web UI: HTTPS / TLS 1.3 with Multi-Factor Authentication (MFA)
* Clinic Management System -> Identity Provider: OpenID Connect (OIDC) over mTLS
* Clinic Management System -> External Labs: HL7 FHIR over HTTPS
* Clinic Management System -> Payment Gateway: REST over TLS 1.3
* Patient Portal (AWS) -> Core EMR (`on-prem-k8s`): Zero-trust API gateway with mTLS

## Technology Stack
* **Orchestration:** Kubernetes (`on-prem-k8s` for core EMR/billing data; AWS `eu-central-1` for stateless Patient Portal edge workloads)
* **Interoperability:** HL7 FHIR APIs for standardized lab and imaging data exchange
* **Security & Auth:** OpenID Connect (OIDC) with step-up MFA; AES-256 encryption at rest with Cloud HSM/KMS
* **Observability & Audit:** OpenTelemetry for distributed tracing; Immutable Write-Once-Read-Many (WORM) storage for audit trails

## Rationale
The hybrid architecture balances strict data residency and 10-year retention mandates for core EMRs on-premises with low-latency global delivery for patient portals in AWS. Pinning database writes and enforcing zero-trust mTLS eliminates split-brain risks while maintaining 99.99% availability and rigorous healthcare compliance.