## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability in rural areas with unstable internet connections.

## Key Elements
* Patient Mobile/Web App (Flutter / React)
* UI Presentation Layer
* State & Local Persistence Manager (SQLite / Secure Local Storage)
* API Client & Auth Module (Dio / Axios with OIDC/OAuth2)
* WebRTC Media Client (LiveKit SDK)
* Localization & Accessibility Engine (i18next / Flutter Localization)
* Post-Consultation & E-Prescription Viewer
* API Gateway (Envoy / Kong)
* LiveKit/WebRTC Media Relays (TURN / STEF)
* AI Orchestrator & Audit Service

## Relationships
* Patients (EU & US) -> Patient Mobile/Web App: Accesses telehealth services and AI symptom checker [HTTPS/WSS]
* Patient Mobile/Web App -> API Gateway: Sends API requests and streams media [HTTPS/WSS (OAuth2/OIDC, mTLS, PKCE)]
* Patient Mobile/Web App -> LiveKit/WebRTC Media Relays: Establishes video streams with dynamic bitrate scaling [SRTP/DTLS (TURN/STEF)]
* UI Presentation Layer -> Localization & Accessibility Engine: Renders localized, accessible UI components [In-memory]
* State & Local Persistence Manager -> Post-Consultation & E-Prescription Viewer: Supplies cached summaries and prescription metadata [In-memory]

## Technology Stack
* Flutter / React: Cross-platform client framework for mobile and web accessibility
* SQLite / Platform-native Secure Enclaves (Keychain/Keystore): Encrypted local data storage and offline queuing
* LiveKit SDK & WebRTC: Low-bandwidth video streaming with audio-only fallback modes
* OIDC/OAuth2 with PKCE: Secure token exchange and authentication flow
* Fastlane & GitHub Actions: Automated code-signing and multi-region deployment pipelines

## Rationale
This architecture ensures GDPR and HIPAA compliance by enforcing strict client-side encryption and secure multi-region data routing. It guarantees continuous availability for rural patients through robust local caching, degraded-mode handling, and adaptive WebRTC media streaming.