## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It operates on a hybrid cloud architecture to satisfy strict regulatory compliance, high availability, and performance requirements.

## Key Elements
- **Users:** `Patient` (Web/Mobile), `Clinician/Staff` (Secure Workstation)
- **Core System:** `Clinic Management System (CMS)` distributed across `on-prem-k8s` and AWS `eu-central-1`
- **External Systems:** `External Lab & Imaging Systems`, `Payment Gateway / Insurance Clearinghouse`
- **Infrastructure & Security Components:** FIPS 140-2 Level 3 HSM / AWS KMS, Enterprise Secrets Manager (HashiCorp Vault), Prometheus, OpenTelemetry

## Relationships
- `Patient` & `Clinician/Staff` interact with `CMS` via HTTPS (TLS 1.3, OIDC, MFA)
- `CMS` integrates with `External Lab & Imaging Systems` using HL7 FHIR RESTful APIs over mTLS
- `CMS` connects to `Payment Gateway / Insurance Clearinghouse` via HTTPS REST/SOAP APIs
- Hybrid inter-service communication secured via mutual TLS (mTLS) with short-lived certificates

## Technology Stack
- **Orchestration:** Kubernetes (`on-prem-k8s` and cloud) for container management and Horizontal Pod Autoscalers (HPA)
- **Security & Compliance:** AES-256 at rest, FIPS 140-2 Level 3 HSM / AWS KMS, HashiCorp Vault for secrets management, Cosign for image signing
- **Observability & Reliability:** OpenTelemetry for distributed tracing, Prometheus for metrics, eBPF-based runtime threat detection
- **Interoperability:** HL7 FHIR over HTTPS/mTLS for clinical system integration

## Rationale
This hybrid architecture balances strict data sovereignty and 10-year retention mandates (retaining sensitive EMR data on-premises) with scalable cloud services for public portals. Zero-trust networking, mTLS, and HSM-backed encryption ensure robust HIPAA and GDPR compliance while meeting 99.99% availability and sub-second performance goals.