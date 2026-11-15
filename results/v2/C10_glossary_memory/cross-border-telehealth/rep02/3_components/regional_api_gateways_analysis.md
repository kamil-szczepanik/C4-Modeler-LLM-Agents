## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, HIPAA, and GDPR compliance using GCP cloud regions.

## Key Elements
- Patients (EU & US), Licensed Clinicians, Pharmacists (EU/US), Compliance & Regulatory Auditors
- Regional API Gateways (GCP Cloud Endpoints/API Gateway with Envoy proxy components: Edge Routing & Residency Enforcer, JWT & Consent Validator, Rate Limiting & Degradation Handler, Localized Error & Fallback Responder)
- Frontend UI (Flutter Web/Mobile)
- Video Streaming Service (WebRTC CPaaS)
- AI Symptom Checker Service (AI / GCP, Cloud HSM)
- Consent & Data Management Service (CMEK, GCP)
- Immutable Logging Service (GCP Cloud Storage, Cloud Logging, Pub/Sub)
- National e-Prescription Gateways (EU) and Pharmacy Systems (US)

## Relationships
- Patients/Clinicians -> Frontend UI via HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0
- Frontend UI -> Regional API Gateways via HTTPS (REST/GraphQL), TLS 1.3
- Regional API Gateways -> Consent & Data Management Service via gRPC over mTLS
- Regional API Gateways -> Third-Party Video Infrastructure via WebRTC (UDP/TCP/TLS via TURN relays)
- Regional API Gateways -> National e-Prescription Gateways (EU) via HTTPS/REST
- Regional API Gateways -> Pharmacy Systems (US) via HTTPS/REST (HL7 FHIR)
- AI Symptom Checker Service -> Immutable Logging Service via GCP Pub/Sub (encrypted with regional CMEK)

## Technology Stack
- Google Cloud Platform (GCP): Chosen for robust regional isolation (`europe-west3` and `us-central1`).
- Google Cloud API Gateway / Envoy proxy: Powers edge routing, token validation, and traffic control.
- Flutter Web/Mobile: Enables localized, offline-first cross-platform user interfaces.
- WebRTC CPaaS with TURN relays: Supports low-bandwidth video streaming for rural connections.
- Cloud HSM and CMEK: Ensures cryptographic signing and regional data encryption.
- Terraform: Enforces infrastructure-as-code separation between regions.

## Rationale
The architecture strictly separates EU and US data processing within dedicated GCP regions to satisfy GDPR and HIPAA mandates. Envoy-based edge gateways, mTLS, and regional token validation ensure secure, consent-driven cross-border operations while supporting graceful degradation for rural users.