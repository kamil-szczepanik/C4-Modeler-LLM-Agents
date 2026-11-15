## Overview
Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and low-bandwidth resilience.

## Key Elements
* Web & Mobile Client Apps (Flutter / React Native)
* API Gateway (Google Cloud API Gateway / Apigee)
* Core Telehealth Service (Spring Boot / Java)
* AI Symptom Checker Service (FastAPI / Python)
* Interoperability & E-Prescription Service (Node.js)
* WebRTC SFU Media Relay (LiveKit on GKE)
* Data & Security Layer (Cloud SQL PostgreSQL, Cloud Storage, GCP Cloud KMS, GCP Service Mesh Istio)
* Client Components: Adaptive Media Component, Consent & Routing State Manager, Symptom Checker UI & Audit Logger, Offline-First Storage Engine

## Relationships
* Web & Mobile Client Apps -> API Gateway: HTTPS, GraphQL over TLS 1.3
* Web & Mobile Client Apps -> WebRTC SFU Media Relay: WebRTC, SRTP, DTLS
* Adaptive Media Component -> WebRTC SFU Media Relay: WebRTC, SRTP, DTLS
* Consent & Routing State Manager, Symptom Checker UI, Offline Storage -> API Gateway: HTTPS, GraphQL over TLS 1.3

## Technology Stack
* Flutter / React Native: Unified cross-platform client codebase
* LiveKit on GKE: Scalable WebRTC media relay for video consultations
* SQLCipher, iOS Keychain, Android Keystore: Client-side encryption at rest and secure enclave storage
* GCP (europe-west3, us-central1): Regional cloud infrastructure enforcing data residency

## Rationale
The architecture uses multi-region GCP deployment combined with client-side consent routing to strictly separate EU and US health data for GDPR and HIPAA compliance. It incorporates adaptive media streaming and offline-first storage to ensure reliable telehealth access for rural patients with unstable internet connections.