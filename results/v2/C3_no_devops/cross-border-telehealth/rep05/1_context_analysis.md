## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures strict regional data residency and regulatory compliance while maintaining reliable access for low-bandwidth users.

## Key Elements
* Patients (Web/Mobile Clients)
* Licensed Clinicians and Compliance Officers
* Cross-Border Telehealth Platform (GCP `europe-west3` and `us-central1`)
* EU National E-Prescription Gateways
* US Pharmacy Networks (HL7 FHIR APIs)
* Third-Party Video Relay/TURN Infrastructure

## Relationships
* Patients and Clinicians interact with the Platform via HTTPS/TLS 1.3
* Video media streams use WebRTC with DTLS-SRTP over UDP/TCP
* Platform connects to EU National Gateways via SOAP/REST with mTLS
* Platform connects to US Pharmacy Networks via HL7 FHIR REST APIs with mTLS
* Cross-region replication enforced via cryptographic consent tokens

## Technology Stack
* Cloud Provider: GCP (`europe-west3` for EU, `us-central1` for US) for regional data isolation
* Authentication: OAuth 2.0, OIDC, and MFA for identity federation and role-based access
* Consent Management: UMA (User-Managed Access) scopes for granular data sharing
* Encryption: TLS 1.3 in transit, AES-256 at rest with CMEK, and DTLS-SRTP for media
* Audit Logging: GCP Cloud Audit Logs for immutable, append-only AI model traceability

## Rationale
This architecture guarantees strict GDPR and HIPAA compliance by isolating regional data within designated GCP boundaries. Furthermore, WebRTC with DTLS-SRTP and degraded-mode support ensures reliable, secure telehealth services for patients with unstable internet connections.