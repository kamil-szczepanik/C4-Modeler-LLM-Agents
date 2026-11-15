## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It ensures strict cross-border health data residency and regulatory compliance.

## Key Elements
- Patients (Mobile and Web clients)
- Clinicians (Web clients)
- Cross-Border Telehealth Platform (GCP instances in `europe-west3` and `us-central1`)
- External Pharmacies (EU national e-prescription networks and US pharmacy networks)
- Identity Providers (OAuth2/OIDC)

## Relationships
- Patients & Clinicians to Platform: HTTPS, WebRTC, OIDC (authentication/video/data mgmt)
- Platform to External Pharmacies: mTLS, HL7 FHIR (US), national e-prescription standards (EU via REST/SOAP)
- Platform to Identity Providers: OAuth2/OIDC over HTTPS

## Technology Stack
- Cloud Provider: GCP (`europe-west3` for EU, `us-central1` for US) to enforce data residency
- Protocols: HTTPS, TLS 1.3, mTLS, WebRTC with global TURN/STUN relay servers
- Standards: HL7 FHIR (US), national e-prescription standards (EU)
- Security & Storage: AES-256 for data-at-rest, OAuth2/OIDC, append-only ledgers for AI audit logs

## Rationale
Regionally isolated GCP instances enforce strict GDPR and HIPAA compliance while maintaining localized data residency. Distributed WebRTC relays and cryptographic audit logging satisfy rural availability and EU MDR traceability constraints.