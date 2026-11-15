## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across disparate regional networks.

## Key Elements
- Patients (EU & US) using Mobile/Web Clients
- Licensed Clinicians using the Clinician Portal
- Cross-Border Telehealth Platform deployed in GCP (`europe-west3` and `us-central1`)
- National E-Prescription Gateways (EU) & US Pharmacy Systems (HL7 FHIR)
- Identity Providers (EU eIDAS / US OAuth2)
- EU/US Regulatory & Auditing Bodies

## Relationships
- Patients & Clinicians -> Cross-Border Telehealth Platform via HTTPS / WebRTC (TLS 1.3) with regional Anycast edge routing
- Platform -> National E-Prescription Gateways & US Pharmacy Systems via REST / HL7 FHIR over mutual TLS (mTLS)
- Platform -> Identity Providers via OIDC over HTTPS
- Platform -> EU/US Regulatory Bodies via secure export API (HTTPS/SFTP) with regional data-residency filters

## Technology Stack
- GCP (`europe-west3` and `us-central1`): Regional deployment to enforce strict data residency (R-05)
- GCP Cloud Load Balancing: Regional edge routing pinned to specific data centers without shared global state
- WebRTC with TURN/STUN relay servers: Enables video consultations in low-bandwidth rural conditions (<300 kbit/s)
- GCP KMS (Customer-Managed Encryption Keys): Isolates encryption keys regionally to prevent cross-border key compromise
- GCP Cloud Storage with WORM bucket locks: Provides immutable storage for audit logs to satisfy AI traceability (R-07)
- HL7 FHIR and national EU standards: Ensures regional interoperability for e-prescriptions (R-08)

## Rationale
This architecture enforces strict regional isolation and cryptographic consent verification to comply with GDPR, HIPAA, and EU MDR mandates. Regional pinning, immutable audit logs, and low-bandwidth optimizations guarantee data privacy, system availability, and regulatory accountability across borders.