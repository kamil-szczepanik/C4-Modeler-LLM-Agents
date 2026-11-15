## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, HIPAA, and EU MDR compliance within GCP.

## Key Elements
* Cross-Border Telehealth Platform [system, context]
* Patients (EU & US) [person, container]
* Licensed Clinicians [person, container]
* Pharmacists (EU/US) [person, container]
* Compliance & Regulatory Auditors [person, container]
* National e-Prescription Gateways (EU) [externalSystem, container]
* Pharmacy Systems (US) [externalSystem, container]
* Third-Party Video Infrastructure (WebRTC CPaaS) [externalSystem, container]
* Regional Identity Providers (eIDAS/OIDC/OAuth 2.0) [externalSystem, container]
* Regional API Gateways (GCP Cloud Endpoints/API Gateway) [container]
* Frontend UI (with localization) (Flutter Web/Mobile) [container]
* Video Streaming Service (WebRTC, UDP/TCP/TLS, TURN) [container]
  - Signaling & Session Manager Component (Node.js/Go, gRPC/WebSockets)
  - Adaptive Quality & Fallback Controller Component (C++/WebRTC, DTLS/SCTP)
  - TURN Relay Coordinator Component (Coturn-based, UDP/TCP/TLS)
* AI Symptom Checker Service (AI / GCP, Cloud HSM) [container]
* Consent & Data Management Service (CMEK, GCP) [container]
* Immutable Logging Service (GCP Cloud Storage, Cloud Logging, Pub/Sub) [container]

## Relationships
* Patients (EU & US) -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
* Licensed Clinicians -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
* Pharmacists (EU/US) -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
* Compliance & Regulatory Auditors -> Frontend UI (with localization) (HTTPS (TLS 1.3))
* Frontend UI (with localization) -> Regional API Gateways (HTTPS (REST/GraphQL), TLS 1.3)
* Regional API Gateways -> Consent & Data Management Service (gRPC over mTLS)
* AI Symptom Checker Service -> Immutable Logging Service (GCP Pub/Sub, encrypted with regional CMEK)
* Regional API Gateways -> Third-Party Video Infrastructure (WebRTC CPaaS) (WebRTC via TURN relays)
* Regional API Gateways -> National e-Prescription Gateways (EU) (HTTPS/REST)
* Regional API Gateways -> Pharmacy Systems (US) (HTTPS/REST (HL7 FHIR))

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud environment ensuring regional data isolation.
* Flutter Web/Mobile: Cross-platform localized user interface supporting offline-first storage.
* WebRTC, DTLS/SCTP, SRTP: Low-bandwidth video consultations with encrypted media streams.
* GCP Cloud HSM & CMEK: Cryptographic key management for data encryption and signed AI outputs.
* Node.js/Go & C++: High-performance backend services and memory-safe media processing.

## Rationale
The architecture uses multi-region GCP deployment to strictly enforce data residency boundaries for EU and US health data. Modular containerization with WebRTC and adaptive streaming guarantees service availability under unstable rural internet connections.