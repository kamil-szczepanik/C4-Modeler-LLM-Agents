## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while strictly enforcing regional data residency and compliance. The system utilizes GCP regions (europe-west3, us-central1) to maintain separated data per jurisdiction.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Pharmacists (EU/US)
- Compliance & Regulatory Auditors
- Frontend UI (with localization) (Flutter Web/Mobile)
- Regional API Gateways (GCP Cloud Endpoints/API Gateway)
- Video Streaming Service (WebRTC, UDP/TCP/TLS, TURN)
- AI Symptom Checker Service (AI / GCP, Cloud HSM)
- Consent & Data Management Service (CMEK, GCP)
- Immutable Logging Service (GCP Cloud Storage, Cloud Logging, Pub/Sub)
  - Log Ingestion Component (Go, gRPC/PubSub subscriber)
  - Cryptographic Verifier Component (Go, Tink/Cloud HSM)
  - WORM Storage Manager Component (Java/Go, GCP Cloud Storage Object Lock)
- National e-Prescription Gateways (EU)
- Pharmacy Systems (US)
- Third-Party Video Infrastructure (WebRTC CPaaS)
- Regional Identity Providers (eIDAS/OIDC/OAuth 2.0)

## Relationships
- Patients (EU & US) -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Licensed Clinicians -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Pharmacists (EU/US) -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Compliance & Regulatory Auditors -> Frontend UI (with localization) (HTTPS (TLS 1.3))
- Frontend UI (with localization) -> Regional API Gateways (HTTPS (REST/GraphQL), TLS 1.3)
- Regional API Gateways -> Consent & Data Management Service (gRPC over mTLS)
- AI Symptom Checker Service -> Immutable Logging Service (GCP Pub/Sub (encrypted with regional CMEK))
- Immutable Logging Service -> Regional Cloud Storage (GCP Cloud Storage Object Lock API over HTTPS)
- Regional API Gateways -> Third-Party Video Infrastructure (WebRTC CPaaS) (WebRTC (UDP/TCP/TLS via TURN relays))
- Regional API Gateways -> National e-Prescription Gateways (EU) (HTTPS/REST (national standards))
- Regional API Gateways -> Pharmacy Systems (US) (HTTPS/REST (HL7 FHIR))

## Technology Stack
- Flutter Web/Mobile: Localized client interface with offline-first capabilities.
- GCP Cloud Endpoints/API Gateway: Regional API traffic routing and management.
- WebRTC, UDP/TCP/TLS, TURN: Low-bandwidth adaptive video streaming.
- GCP Cloud HSM & Tink: Cryptographic signing, verification, and key management.
- GCP Pub/Sub: Asynchronous messaging and buffer for immutable logging.
- GCP Cloud Storage Object Lock: WORM (Write Once, Read Many) tamper-proof storage.
- Go & Java: High-performance services and log ingestion components.

## Rationale
This architecture ensures strict regional data isolation between the EU and US to comply with GDPR and HIPAA mandates. Furthermore, immutable logging with cryptographic verification guarantees traceability for AI medical recommendations under the EU MDR.