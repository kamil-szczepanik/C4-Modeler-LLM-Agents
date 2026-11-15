## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring regulatory compliance (GDPR, HIPAA, and EU MDR) and low-bandwidth availability.

## Key Elements
* Patients (EU & US)
* Licensed Clinicians
* EU/US Regional Pharmacies
* Regulatory Authorities / Notified Bodies (EU/US)
* Cross-Border Telehealth Platform (Core System)
* EU Regional Instance (`europe-west3`)
* US Regional Instance (`us-central1`)
* Identity Providers (IDPs)
* Third-Party Video Infrastructure

## Relationships
* Patients and Clinicians to Cross-Border Telehealth Platform via HTTPS/TLS 1.3 and WebRTC
* Cross-Border Telehealth Platform to EU/US Regional Pharmacies via HTTPS/REST using national EU standards and US HL7 FHIR
* Cross-Border Telehealth Platform to IDPs via OAuth2/OIDC
* Regulatory Authorities to Regional Instances via HTTPS / TLS 1.3 with mTLS and signed JWT

## Technology Stack
* Cloud Provider: GCP (`europe-west3` and `us-central1`) for isolated regional deployment
* Authentication: OAuth2/OIDC with short-lived JWTs and cryptographically signed consent scopes
* Encryption: Cloud KMS with region-specific, customer-managed encryption keys (CMEK) and TLS 1.3
* Video Streaming: WebRTC-compliant SFU/MCU provider supporting adaptive bitrate streaming
* Storage/Auditing: GCP Cloud Audit Logs with Write-Once-Read-Many (WORM) storage policies

## Rationale
Isolating data into two distinct GCP regions with air-gapped control planes guarantees compliance with strict EU and US data residency mandates. Using adaptive WebRTC streaming, immutable audit logging, and cryptographic consent validation satisfies all clinical, regulatory, and degraded-connectivity requirements without compromising data security.