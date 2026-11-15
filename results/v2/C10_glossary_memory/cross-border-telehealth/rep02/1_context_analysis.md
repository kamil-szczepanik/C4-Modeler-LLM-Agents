## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency while ensuring HIPAA and EU MDR compliance.

## Key Elements
* **External Actors:** Patients (EU & US), Licensed Clinicians, Pharmacists (EU/US), Compliance & Regulatory Auditors.
* **External Systems:** National e-Prescription Gateways (EU), Pharmacy Systems (US), Third-Party Video Infrastructure (WebRTC CPaaS), Regional Identity Providers (eIDAS/OIDC/OAuth 2.0).
* **Cross-Border Telehealth Platform Containers:** Regional API Gateways, Frontend UI (with localization), Video Streaming Service, AI Symptom Checker Service, Consent & Data Management Service, Immutable Logging Service.
* **Infrastructure:** GCP Regions (`europe-west3` for EU, `us-central1` for US).

## Relationships
* Patients and Clinicians interact with the Platform via HTTPS (TLS 1.3) and secure WebSockets using OIDC/OAuth 2.0 authentication.
* Video Streaming Service connects via WebRTC (UDP/TCP/TLS fallback via TURN relays) for low-bandwidth consultations (<300 kbit/s).
* Platform integrates with EU National Gateways and US Pharmacy Systems via HTTPS/REST using national standards and HL7 FHIR.
* Regional Identity Providers validate authentication tokens using OpenID Connect.
* Immutable Logging Service records cryptographically signed AI outputs and audit trails locally per region.

## Technology Stack
* **Cloud Platform:** GCP (`europe-west3` and `us-central1`) for strict regional data isolation.
* **Infrastructure as Code:** Terraform and GitOps pipelines to prevent configuration drift.
* **Data Security:** Customer-Managed Encryption Keys (CMEK) at rest and TLS 1.3 in transit.
* **Interoperability:** HL7 FHIR (US) and national standards (EU) for e-prescriptions.
* **Video & Communications:** WebRTC-compatible CPaaS with adaptive bitrate codecs and TURN relays.

## Rationale
The regional GCP split and localized CMEK encryption enforce GDPR and HIPAA data residency constraints. Adaptive WebRTC streaming with TCP/TLS fallback ensures continuous availability for rural patients with unstable internet connections.