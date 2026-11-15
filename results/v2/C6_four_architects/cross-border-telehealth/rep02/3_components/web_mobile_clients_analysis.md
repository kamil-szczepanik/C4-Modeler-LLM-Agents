## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients using GCP regions `europe-west3` and `us-central1`. It ensures strict data residency, HIPAA/GDPR compliance, and uninterrupted availability for rural users.

## Key Elements
- Patients and Clinicians (Users)
- Web & Mobile Clients Container (React, React Native, TypeScript)
- 11 Client Components: Patient Portal App, Clinician Workspace App, WebRTC Media Client Module, Local State & Storage Manager, AI Symptom Checker UI Module, E-Prescription & FHIR Viewer, Consent & Privacy Manager, Telemetry & Audit Logger, Adaptive Bitrate Controller, Regional Endpoint Router, Secure Token & Session Manager
- API Gateway & Routing Container (Kong / GCP API Gateway)
- Core Telehealth Service Container (Java / Spring Boot)
- WebRTC Media Broker Container (Node.js / Mediasoup)
- AI Symptom Checker Service Container (Python / FastAPI)
- FHIR & E-Prescription Integration Service Container (Python / Java)
- Consent & Audit Logging Service Container (Go)
- Messaging and Databases (Cloud Pub/Sub, Cloud SQL PostgreSQL, Cloud Storage)

## Relationships
- Patients & Clinicians -> Web & Mobile Clients: Accesses telehealth features [HTTPS, WSS]
- Web & Mobile Clients -> Regional Endpoint Router: Pins geographic context [In-memory routing]
- Regional Endpoint Router -> API Gateway & Routing: Transmits regional requests [TLS 1.3 over HTTPS]
- WebRTC Media Client Module -> WebRTC Media Broker: Streams video [UDP/DTLS via ICE/STUN/TURN]
- Consent & Privacy Manager, Telemetry & Audit Logger -> API Gateway: Transmits consent and audit payloads [TLS 1.3 over HTTPS]
- API Gateway & Routing -> Core Telehealth, AI Symptom Checker, and Integration Services: Routes authenticated traffic [gRPC / HTTPS]

## Technology Stack
- React & React Native: Maximizes code sharing across web, iOS, and Android clients.
- IndexedDB & SQLite: Provides local offline caching to handle unstable rural connections (R-06).
- WebRTC & Mediasoup: Enables peer-to-peer and SFU video consultations.
- TypeScript: Ensures type safety across client modules and the Regional Endpoint Router.
- OAuth 2.0 / OIDC: Secures session management and token refreshes.

## Rationale
This architecture uses client-side regional routing and offline storage to satisfy GDPR/HIPAA data residency and rural availability constraints. Decoupling WebRTC media streaming and local state management ensures low-bandwidth resilience and high-quality video consultations.