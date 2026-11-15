## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It guarantees strict regional data residency and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Cross-Border Telehealth Platform (GCP regions: `europe-west3`, `us-central1`)
- National E-Prescription Networks (EU) & US Pharmacy Systems
- WebRTC SFU (Selective Forwarding Unit) Media Relay
- Break-Glass Identity Provider (IdP)

## Relationships
- Patients & Clinicians -> Cross-Border Telehealth Platform: HTTPS / WebRTC (TLS 1.3, adaptive below 300 kbit/s)
- Cross-Border Telehealth Platform (EU) -> National E-Prescription Networks: mTLS over REST/SOAP
- Cross-Border Telehealth Platform (US) -> US Pharmacy Systems: HL7 FHIR over HTTPS (OAuth 2.0)
- Platform -> Immutable Storage: GCP Bucket Lock for cryptographically signed AI audit logs

## Technology Stack
- Google Cloud Platform (GCP): Chosen for isolated regional deployments (`europe-west3` and `us-central1`) ensuring data residency.
- WebRTC SFU: Enables real-time video/audio consultations with automatic degradation for rural low-bandwidth connections.
- OAuth 2.0 / OpenID Connect with MFA: Secures clinician and patient access alongside resilient session token caching.
- HL7 FHIR & REST/SOAP: Standardizes interoperability with US and EU external pharmacy systems.

## Rationale
Independent regional deployments on GCP completely prevent cross-border data leakage to satisfy GDPR and HIPAA. Furthermore, WebRTC bandwidth adaptation and Break-Glass authorization ensure uninterrupted emergency and rural care without sacrificing security.