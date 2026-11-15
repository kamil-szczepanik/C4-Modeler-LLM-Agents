## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability (99.99%), strict regulatory compliance (HIPAA, GDPR, 10-year data retention), and sub-second EMR interactions.

## Key Elements
- **Users:** Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance Officer
- **External Systems:** Insurance / Payer System, Lab & Imaging Systems
- **Containers:** Web Frontend, Patient Portal / Mobile App, API Gateway (with OAuth2/OIDC & ABAC), EMR Service, Billing / Claims Service, OpenTelemetry sidecars, Audit Logging sidecars, Dynamic Secrets Manager (HashiCorp Vault)
- **Infrastructure:** `on-prem-k8s` cluster and AWS (`eu-central-1`) connected via hybrid networking

## Relationships
- **Patients & Staff to Web Frontend / Mobile App:** HTTPS/TLS via API Gateway using OAuth2/OIDC with Multi-Factor Authentication.
- **API Gateway to EMR & Billing Services:** Internal gRPC/REST over mutual TLS (mTLS) with SPIFFE/SPIRE workload identities.
- **EMR Service to Lab & Imaging Systems:** HL7 FHIR APIs for clinical interoperability.
- **Billing / Claims Service to Insurance / Payer System:** Secure HTTPS with persistent encrypted queues (DLQ).
- **Cross-Region Replication:** Encrypted hybrid synchronization between `on-prem-k8s` and `eu-central-1` managed by Anycast DNS and Traffic Managers.

## Technology Stack
- **Kubernetes (`on-prem-k8s`, `eu-central-1`):** Orchestration platform ensuring 99.99% active-active high availability.
- **HL7 FHIR:** Standardized protocol for lab and imaging system interoperability.
- **mTLS & SPIFFE/SPIRE:** Zero-trust inter-container security and workload identity across hybrid boundaries.
- **HashiCorp Vault:** Dynamic secret management with short-lived credentials.
- **AES-256 & Hardware Security Modules (HSM):** Data protection at rest and envelope encryption.
- **OpenTelemetry:** Distributed tracing sidecars for performance monitoring (P95 < 1s).

## Rationale
This hybrid architecture isolates critical clinical and billing workloads while enforcing zero-trust security and strict data residency. By combining active-active Kubernetes clusters, automated queuing, and rigorous encryption, the system achieves 99.99% availability and full HIPAA/GDPR compliance without compromising sub-second clinical performance.