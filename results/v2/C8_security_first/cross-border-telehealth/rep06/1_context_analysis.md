## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict regional data residency, regulatory compliance, and resilience for unstable rural connections.]

## Key Elements
* Patients (EU/US)
* Licensed Clinicians
* Compliance / Quality Assurance Auditors
* External Pharmacy / Partner Network
* Cross-Border Telehealth Platform (Software System)
* National e-Prescription Gateways (EU) & US Pharmacy Networks (HL7 FHIR)
* Third-Party Video Relay / TURN Network
* External Identity Providers (OAuth2/OIDC)
* Localized AI Model Registries

## Relationships
* Patients & Clinicians -> Platform: HTTPS / WSS (TLS 1.3) via global Anycast Load Balancing
* Platform -> National e-Prescription Gateways (EU) & US Pharmacy Networks: HTTPS / REST with mTLS and signed JWTs (R-02, R-08)
* Platform -> Third-Party Video Relay / TURN Network: WebRTC / SRTP over DTLS with ephemeral tokens (R-06)
* Platform -> External Identity Providers: OAuth2 / OIDC over HTTPS
* Auditors -> Platform: IAM-restricted Read-Only APIs (R-04, R-07)

## Technology Stack
* Google Cloud Platform (GCP): Primary cloud provider hosting regions `europe-west3` and `us-central1`
* GCP VPC Service Controls: Hard-enforces regional data residency and trust boundaries (R-05)
* TLS 1.3 & mTLS: Secures all data in transit and inter-service communications
* SRTP over DTLS: Encrypts media streams for video consultations (R-06)
* OAuth2 / OIDC & PBAC: Manages clinician MFA and purpose-based access control (R-04)
* Cosign / Sigstore: Cryptographically signs AI model registry artifacts for EU MDR compliance (R-07)
* HL7 FHIR: Standard for US pharmacy interoperability (R-08)

## Rationale
[This architecture enforces strict regional isolation and compliance mandates (GDPR, HIPAA, EU MDR) while maintaining high availability for low-bandwidth rural users. Decentralized regional deployments protect patient privacy without compromising cross-border functionality.]