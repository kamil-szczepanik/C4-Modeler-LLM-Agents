## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The system ensures strict regional data residency, HIPAA/GDPR compliance, and EU MDR traceability.

## Key Elements
- Patients (EU & US) [person]
- Licensed Clinicians [person]
- Pharmacists (EU/US) [person]
- Compliance & Regulatory Auditors [person]
- Frontend UI (with localization & offline-first local storage) [container] (Flutter Web/Mobile)
- Regional API Gateways [container] (GCP Cloud Endpoints/API Gateway)
- Video Streaming Service [container] (WebRTC, UDP/TCP/TLS, TURN)
- AI Symptom Checker Service [container] (AI / GCP, Cloud HSM)
- Consent & Data Management Service [container] (CMEK, GCP)
- Immutable Logging Service [container] (GCP Cloud Storage, Cloud Logging, Pub/Sub)
- National e-Prescription Gateways (EU) [externalSystem]
- Pharmacy Systems (US) [externalSystem]
- Third-Party Video Infrastructure (WebRTC CPaaS) [externalSystem]
- Regional Identity Providers [externalSystem] (eIDAS/OIDC/OAuth 2.0)

## Relationships
- Patients & Licensed Clinicians -> Frontend UI: HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0
- Frontend UI -> Regional API Gateways: HTTPS (REST/GraphQL), TLS 1.3
- Regional API Gateways -> Consent & Data Management Service: gRPC over mTLS
- AI Symptom Checker Service -> Immutable Logging Service: GCP Pub/Sub (encrypted with regional CMEK)
- Cross-Border Telehealth Platform -> Third-Party Video Infrastructure: WebRTC (UDP/TCP/TLS via TURN relays)
- Cross-Border Telehealth Platform -> National e-Prescription Gateways (EU): HTTPS/REST (national standards)
- Cross-Border Telehealth Platform -> Pharmacy Systems (US): HTTPS/REST (HL7 FHIR)

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for strict regional data residency.
- Flutter (Web/Mobile): Cross-platform UI supporting localized compliance flows and offline-first encrypted storage (SQLCipher).
- gRPC & mTLS: High-performance, secure internal communication between regional containers.
- GCP Cloud KMS & Cloud HSM: Customer-Managed Encryption Keys and hardware-backed cryptographic signing for EU MDR traceability.
- GCP Pub/Sub: Asynchronous event streaming with Dead-Letter Queues for reliable logging.

## Rationale
The multi-region container architecture isolates data between GCP regions to strictly satisfy GDPR and HIPAA data residency constraints. Hardware-backed cryptographic signing and isolated immutable logging guarantee EU MDR traceability for the AI symptom checker.