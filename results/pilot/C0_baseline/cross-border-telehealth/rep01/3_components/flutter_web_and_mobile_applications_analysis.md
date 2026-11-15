## Overview
This architecture summary defines the component-level design for the Flutter Web and Mobile Applications container within the Cross-Border Telehealth Platform. It enables secure, resilient video consultations, AI symptom checking, and localized consent management for patients and clinicians in the EU and US.

## Key Elements
* Presentation Layer (UI): Adaptive screens for patient onboarding, telehealth consultations, and clinician workflows.
* State Management Engine: Riverpod-based coordinator for asynchronous data synchronization and offline-first resilience.
* Local Secure Storage Service: SQLCipher with platform-secure hardware keys (Keychain/EncryptedSharedPreferences).
* Network & WebRTC Client: Manages HTTPS/TLS 1.3, WebSockets, and adaptive bitrate streaming via mediasoup SFU.
* AI Symptom Checker Wrapper: Validates input payloads and captures traceability metadata.

## Relationships
* Patients & Clinicians -> Presentation Layer: Uses for UI interactions and telehealth consultations [HTTPS/TLS 1.3, WebRTC]
* Network & WebRTC Client -> GCP Cloud Armor & Envoy API Gateway: Sends API requests and video streams [HTTPS/TLS 1.3, WebRTC over UDP/TCP]
* Network & WebRTC Client -> mediasoup SFU: Streams adaptive video consultations [WebRTC]
* State Management Engine -> Local Secure Storage Service: Reads/writes encrypted consent profiles and draft data [SQLCipher API]
* AI Symptom Checker Wrapper -> GCP Cloud Armor & Envoy API Gateway: Dispatches validated symptom payloads [HTTPS/TLS 1.3]

## Technology Stack
* Flutter / Dart: Core multiplatform framework for web and mobile clients ensuring unified UI codebase.
* Riverpod: State management for reactive, asynchronous data synchronization and offline caching.
* SQLCipher: Encrypted local database ensuring data privacy at rest on client devices.
* WebRTC / mediasoup: Real-time communication protocols and SFU for low-bandwidth video consultations.
* OAuth 2.0 with PKCE & JWT: Secure client authentication using volatile memory storage.

## Rationale
The component architecture prioritizes high availability in unstable rural environments through adaptive WebRTC streaming and offline-first local storage. Strict encryption and token management mechanisms ensure full compliance with GDPR and HIPAA mandates.