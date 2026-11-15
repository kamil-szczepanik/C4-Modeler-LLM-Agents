## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US.]
[The web application container acts as the primary patient and clinician client interface, ensuring offline resilience and strict regulatory compliance.]

## Key Elements
* Patient Portal UI & Clinician Dashboard (React, TypeScript)
* Video Client Wrapper (WebRTC / LiveKit SDK)
* State & Consent Manager (Redux Toolkit / LocalStorage)
* Local Audit & Telemetry Interceptor (TypeScript)
* Offline Cache & Sync Manager (IndexedDB / Service Worker)
* Routing & Localization Engine (React Router / i18next)
* Client Auth & Session Handler (OpenID Connect / OAuth2 SDK)

## Relationships
* Patient Portal UI -> API Gateway: Communicates via HTTPS/REST for business logic, e-prescriptions, and symptom checking
* Video Client Wrapper -> Video Consultation Service (LiveKit): Connects via WSS/WebRTC for real-time video consultations
* Patient Portal UI -> Local Audit & Interceptor: Passes UI events and consent decisions via In-Memory Function Calls
* Local Audit & Interceptor -> API Gateway: Forwards batched telemetry, consent, and audit payloads via HTTPS/REST
* Patient Portal UI -> Offline Cache & Sync Manager: Reads/writes cached state via IndexedDB API
* Offline Cache & Sync Manager -> API Gateway: Synchronizes queued requests via HTTPS/REST upon reconnection
* Patient Portal UI -> Routing & Localization Engine: Delegates route resolution and locale assets via In-Memory Function Calls
* Patient Portal UI -> Client Auth & Session Handler: Verifies active session tokens via In-Memory Function Calls
* Client Auth & Session Handler -> API Gateway: Authenticates requests via HTTPS with Bearer Tokens

## Technology Stack
* React & TypeScript: Powers the Single Page Application UI and clinician dashboard
* WebRTC & LiveKit SDK: Manages real-time audio/video streams with dynamic bitrate adaptation for unstable connections
* IndexedDB & Service Worker: Implements PWA caching strategies for offline resilience on rural connections
* Redux Toolkit: Manages local session state and granular data-sharing consent checks
* OpenID Connect / OAuth2 SDK: Handles secure in-memory token management for HIPAA and GDPR compliance
* React Router & i18next: Handles client-side navigation and dynamic jurisdictional localization

## Rationale
[This component architecture isolates real-time video handling and enforces client-side telemetry to satisfy strict traceability and offline availability requirements.]
[Storing session tokens exclusively in memory and capturing consent locally ensures robust compliance with GDPR and HIPAA across regional deployments.]