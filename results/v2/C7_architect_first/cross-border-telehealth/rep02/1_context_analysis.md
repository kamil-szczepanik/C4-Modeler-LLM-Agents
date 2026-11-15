## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and regulatory compliance via isolated GCP deployments.]

## Key Elements
- Patients and Licensed Clinicians
- Local Pharmacists and Compliance Auditors
- Platform Administrators
- EU Telehealth Platform (GCP europe-west3)
- US Telehealth Platform (GCP us-central1)
- National EU E-Prescription Gateways and US Pharmacy Systems
- WebRTC Video Infrastructure
- Regional GCP Artifact Registries and KMS

## Relationships
- Patients/Clinicians to Platforms via HTTPS and TLS 1.3
- Platforms to EU E-Prescription Gateways and US Pharmacy Systems via mTLS and regional APIs
- Platforms to WebRTC Video Infrastructure via regional endpoints supporting sub-300 kbit/s degraded modes
- Cross-region data access via token-exchange proxies using short-lived OAuth2 tokens based on patient consent

## Technology Stack
- Google Cloud Platform (GCP) for isolated regional infrastructure (`europe-west3`, `us-central1`)
- HL7 FHIR and national standards for US and EU interoperability
- Customer-Managed Encryption Keys (CMEK) via GCP KMS for region-specific at-rest encryption
- OAuth2/OIDC with FIDO2 hardware tokens for zero-trust IAM and PAM
- Cryptographically signed AI model weights stored in GCP Artifact Registries for EU MDR traceability

## Rationale
[Region-isolated architectures and token-exchange proxies ensure compliance with GDPR and HIPAA without data leakage. Localized synthetic monitoring and degraded-mode WebRTC fallbacks guarantee high availability for unstable rural connections.]