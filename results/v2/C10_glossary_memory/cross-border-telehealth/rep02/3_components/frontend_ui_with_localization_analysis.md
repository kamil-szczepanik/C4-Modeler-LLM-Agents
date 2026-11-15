## Overview
The Cross-Border Telehealth Platform is a secure telemedicine system providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR, HIPAA, and EU MDR compliance on GCP.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Pharmacists (EU/US)
- Compliance & Regulatory Auditors
- National e-Prescription Gateways (EU)
- Pharmacy Systems (US)
- Third-Party Video Infrastructure (WebRTC CPaaS)
- Regional Identity Providers (eIDAS/OIDC/OAuth 2.0)
- Regional API Gateways (GCP Cloud Endpoints/API Gateway)
- Frontend UI (with localization) (Flutter Web/Mobile)
- Video Streaming Service (WebRTC, UDP/TCP/TLS, TURN)
- AI Symptom Checker Service (AI / GCP, Cloud HSM)
- Consent & Data Management Service (CMEK, GCP)
- Immutable Logging Service (GCP Cloud Storage, Cloud Logging, Pub/Sub)

## Relationships
- Patients (EU & US) -> Frontend UI (with localization) [HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0]
- Licensed Clinicians -> Frontend UI (with localization) [HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0]
- Pharmacists (EU/US) -> Frontend UI (with localization) [HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0]
- Compliance & Regulatory Auditors -> Frontend UI (with localization) [HTTPS (TLS 1.3)]
- Frontend UI (with localization) -> Regional API Gateways [HTTPS (REST/GraphQL), TLS 1.3]
- Regional API Gateways -> Consent & Data Management Service [gRPC over mTLS]
- AI Symptom Checker Service -> Immutable Logging Service [GCP Pub/Sub (encrypted with regional CMEK)]
- Regional API Gateways -> Third-Party Video Infrastructure (WebRTC CPaaS) [WebRTC (UDP/TCP/TLS via TURN relays)]
- Regional API Gateways -> National e-Prescription Gateways (EU) [HTTPS/REST (national standards)]
- Regional API Gateways -> Pharmacy Systems (US) [HTTPS/REST (HL7 FHIR)]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider across `europe-west3` and `us-central1` regions for data residency enforcement.
- Flutter Web/Mobile: Cross-platform frontend framework supporting offline-first capabilities and dynamic localization.
- WebRTC & TURN: Real-time video streaming with adaptive bitrate codecs for low-bandwidth rural connections (<300 kbit/s).
- GCP Cloud HSM & CMEK: Cryptographic key management ensuring data encryption and signed AI outputs.
- gRPC over mTLS: Secure, high-performance inter-service communication.

## Rationale
The multi-region GCP architecture guarantees strict compliance with EU GDPR and US HIPAA by isolating data storage per region. Decoupled microservices and WebRTC ensure high availability and low-bandwidth resilience for rural users without compromising traceability or security.