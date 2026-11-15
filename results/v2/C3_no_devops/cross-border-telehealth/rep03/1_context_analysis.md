## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US while ensuring strict medical and privacy compliance. It maintains regional data isolation and resilience for users with low-bandwidth connections.]

## Key Elements
- Patients and Licensed Clinicians (primary users)
- Pharmacies and National/State Health Authorities (external partners)
- Regulatory Authorities (EU MDR / US HHS)
- Cross-Border Telehealth Platform (core software system hosted on GCP)
- Regional Payment Gateways (Stripe/Adyen regional instances)
- EU National E-Prescription Gateways and US Pharmacy Networks
- EU/US Identity Providers and AI Inference Provider

## Relationships
- Patients & Clinicians to Cross-Border Telehealth Platform via HTTPS and WebSockets (low-bandwidth optimized)
- Cross-Border Telehealth Platform to EU National Gateways / US Pharmacy Networks via HTTPS / REST with mTLS
- Cross-Border Telehealth Platform to Regional Payment Gateways via HTTPS / REST
- Platform containers communicating via internal mTLS managed by Anthos Service Mesh

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for regional data residency enforcement
- GCP KMS: Customer-managed encryption keys (CMEK) for localized data-at-rest encryption
- Anthos Service Mesh: Manages internal mTLS and zero-trust micro-segmentation across containers
- OAuth 2.0 / OpenID Connect (OIDC): Federated authentication with multi-factor authentication support
- HL7 FHIR (US) and National Standards (EU): Used for e-prescription interoperability

## Rationale
[This architecture enforces strict regional isolation and cryptographic logging in GCP to meet GDPR, HIPAA, and EU MDR compliance requirements. Container sandboxing and low-bandwidth optimizations ensure secure, reliable care for all users.]