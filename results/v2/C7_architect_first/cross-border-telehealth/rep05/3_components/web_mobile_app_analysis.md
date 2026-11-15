## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures strict data residency, regulatory compliance, and high availability in rural, low-bandwidth environments.

## Key Elements
- Patients, Clinicians, Regional Pharmacists
- Web & Mobile App Container (Flutter / TypeScript)
- API Gateway (Google Cloud API Gateway)
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI)
- Integration Service Container (Node.js / TypeScript)
- Video Media Server (LiveKit / WebRTC)
- Cloud SQL (PostgreSQL), Cloud Storage, Cloud Pub/Sub
- UI Layer, State & Offline Manager, Video Client Wrapper, API & WebSocket Client, Consent & Policy Interceptor

## Relationships
- Patients/Clinicians/Pharmacists -> Web & Mobile App: Accesses platform interfaces via HTTPS/WebSockets
- Web & Mobile App -> API Gateway: Sends API requests and WebSocket messages via HTTPS/WebSockets
- Web & Mobile App -> Video Media Server: Connects for video consultations via WebRTC
- State & Offline Manager -> Consent & Policy Interceptor -> API Gateway: Routes region-locked, consented sync payloads via HTTPS

## Technology Stack
- Flutter & React/TypeScript: Cross-platform mobile and web presentation layers
- SQLCipher & IndexedDB: Local encrypted storage for offline caching (R-06)
- LiveKit Web/Mobile SDK: Real-time WebRTC video consultation delivery
- Android Keystore & iOS Keychain: Hardware-backed cryptographic key storage
- Firebase Remote Config / Unleash: Regional feature flag management for runtime control

## Rationale
The architecture combines offline-first client resilience with strict region-locked interception to ensure data residency compliance under GDPR and HIPAA. This approach guarantees service continuity in unstable rural environments while protecting sensitive health data across borders.