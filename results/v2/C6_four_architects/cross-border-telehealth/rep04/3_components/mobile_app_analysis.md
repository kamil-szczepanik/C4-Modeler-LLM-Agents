## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and regulatory compliance on Google Cloud Platform.

## Key Elements
- **UI Layer (Flutter Widgets):** Presentation layer for consultations, e-prescriptions, and symptom checker.
- **State Management & Local Cache (Hive / SQLite):** Manages regional data isolation and offline-first capabilities.
- **API Client (Dio / gRPC):** Communicates with the Ingress Layer via HTTPS/WSS.
- **Video Module (LiveKit Flutter SDK):** Handles adaptive bitrate streaming for low-bandwidth connections.
- **Consent Module:** Manages local consent states.
- **AI Symptom Checker Client:** Handles local input validation and securely transmits payloads.
- **Secure Storage Manager (Flutter Secure Storage):** Encrypts auth tokens and regional routing preferences.
- **Localization & Regional Routing Manager:** Stamps payloads with jurisdictional context (`europe-west3` vs `us-central1`).

## Relationships
- **Mobile App -> Ingress Layer:** Sends client requests via HTTPS/WSS with region-specific routing headers.

## Technology Stack
- **Flutter:** Single codebase cross-platform development with native WebRTC performance.
- **Hive / SQLite:** Local storage ensuring offline-first resilience and regional data residency enforcement.
- **LiveKit Flutter SDK:** Video streaming optimized for unstable rural connections below 300 kbit/s.
- **Flutter Secure Storage:** Platform-native secure enclaves for HIPAA and GDPR compliance.

## Rationale
This architecture ensures offline-first resilience for rural users and strictly enforces regional data residency on Google Cloud. Client-side boundary controls guarantee compliance with GDPR, HIPAA, and EU MDR auditability requirements.