## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict cross-border regional data isolation while maintaining compliance with GDPR, HIPAA, and EU MDR.]

## Key Elements
- Patients (EU/US): Utilize video care, e-prescriptions, and the AI symptom checker.
- Licensed Clinicians: Conduct secure cross-border video consultations.
- Local Pharmacies: Receive national-standard e-prescriptions.
- Compliance / Regulatory Officers & External Regulatory Auditors: Access audit logs for accountability.
- Cross-Border Telehealth Platform: GCP-hosted system (`europe-west3` and `us-central1`).
- Third-Party AI Model Provider: External service for symptom checking via HTTPS/REST.
- National E-Prescription Gateways / Pharmacy Networks: External systems using mTLS APIs.

## Relationships
- Patients & Clinicians to Platform: HTTPS / WebRTC (supporting degraded modes down to 300 kbit/s).
- Platform to Third-Party AI Model Provider: HTTPS/REST with payload pseudonymization.
- Platform to E-Prescription Gateways: mTLS APIs using HL7 FHIR and national standards.
- Inter-Region Link (EU to US): Zero-Trust link permitted only with cryptographically signed Patient Consent Tokens.
- Auditors to Platform: Secure, read-only HTTPS/SFTP export for audit logs.

## Technology Stack
- Cloud Provider: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data residency.
- Encryption: AES-256 with CMEK for data-at-rest; TLS 1.3 for data-in-transit.
- Authentication & Authorization: OAuth 2.0 / OIDC with MFA and RBAC at the API gateway.
- Interoperability: HL7 FHIR (US) and national e-prescription standards (EU).

## Rationale
[This architecture ensures stringent regional compliance by separating data storage between GCP regions while maintaining secure, consent-driven cross-border access. It guarantees high availability and traceability to satisfy international healthcare regulations.]