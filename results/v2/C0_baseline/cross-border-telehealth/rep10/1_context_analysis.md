## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability on unstable connections.

## Key Elements
- Patients (EU / US) and Licensed Clinicians
- Local Pharmacies and Compliance Auditors / Officers
- Cross-Border Telehealth Platform (GCP hosted in `europe-west3` and `us-central1`)
- Third-Party Video Infrastructure (WebRTC SFU / Twilio / Agora)
- National e-Prescription Gateways (EU) and US Pharmacy Networks (NCPDP / HL7 FHIR)
- Third-Party AI LLM/ML Provider / Vertex AI
- Federated Identity Provider and Patient Consent Dashboard

## Relationships
- Patients & Clinicians -> Telehealth Platform via HTTPS, WSS, and TLS 1.3
- Telehealth Platform -> Third-Party Video SFU via WebRTC and DTLS
- Telehealth Platform -> External Pharmacy Gateways via REST/FHIR and mTLS
- Telehealth Platform -> AI Symptom Checker via gRPC and HTTPS
- Cross-Region Replication -> Cryptographically tokenized or blocked per R-04 consent

## Technology Stack
- GCP (`europe-west3` and `us-central1`): Regional VPC isolation for data residency (R-05)
- OAuth2/OIDC with FIDO2/WebAuthn MFA: Federated identity and consent token management (R-04)
- WebRTC / SFU: Adaptive bitrate video supporting connections below 300 kbit/s (R-06)
- HL7 FHIR & REST: US interoperability and national EU APIs (R-08)
- Cloud Logging & Cloud Storage: Immutable audit pipelines with Object Retention for EU MDR traceability (R-07)
- Cloud KMS & Cloud HSM: AES-256 encryption-at-rest with regional customer-managed keys

## Rationale
The architecture enforces strict regional isolation and zero-trust cross-border controls to satisfy GDPR, HIPAA, and EU MDR mandates. Cloud-native GCP services combined with adaptive WebRTC streaming ensure high availability, regulatory compliance, and reliable care even in rural areas with unstable internet.