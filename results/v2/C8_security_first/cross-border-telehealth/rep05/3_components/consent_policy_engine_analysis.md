## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while strictly enforcing regional data residency and compliance. The Consent & Policy Engine secures this architecture through context-aware policy evaluation, hardware-bound edge bundles, and regional isolation.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Compliance & Policy Administrator
- Frontend Client Apps (Flutter with Secure Storage/TPM/Secure Enclave)
- API Gateway / BFF (Envoy / gRPC-Web)
- Consent & Policy Engine Container (Go)
- Policy Evaluation Service (OPA Embedded)
- Consent Management API (Go / Gin)
- Bundle Signer & Publisher (Go)
- Regional Consent Store (Cloud SQL PostgreSQL)
- Regional GCP HTTP(S) Load Balancers (`europe-west3`, `us-central1`)

## Relationships
- Frontend Client Apps -> API Gateway / BFF: Requests video consultations and consent updates [gRPC-Web / HTTPS, mTLS]
- API Gateway / BFF -> Policy Evaluation Service: Requests policy validation [gRPC over mTLS]
- Policy Evaluation Service -> Regional Consent Store: Queries persistent consent states [PostgreSQL protocol, mTLS]
- Bundle Signer & Publisher -> Frontend Client Apps: Distributes signed OPA policy bundles [HTTPS]

## Technology Stack
- Go: Chosen for high-throughput, low-latency policy evaluation and API handling.
- Open Policy Agent (OPA) / Rego: Enables flexible, context-aware, and cryptographically signed policy enforcement.
- Cloud SQL PostgreSQL: Provides reliable regional data persistence with strict regional isolation.
- Flutter & Device Keystores: Supports cross-platform client apps with hardware-backed cryptographic bundle binding.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data storage and preventing cross-border leakage. Additionally, edge-cached OPA bundles and hardware binding support unstable rural internet connections while maintaining robust security and accountability.