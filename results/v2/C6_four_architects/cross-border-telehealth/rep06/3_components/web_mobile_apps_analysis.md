## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and resilience for unstable rural connections.

## Key Elements
- Patients and Clinicians (Users)
- Web & Mobile Apps Container (React / React Native)
- UI Presentation Layer (Component)
- Video/Audio Session Controller (Component)
- Offline Data Synchronizer (Component)
- Regional Configuration & Telemetry Manager (Component)
- Local Consent & State Manager (Component)
- Google Cloud API Gateway with Open Policy Agent (OPA)
- Video Streaming Service (mediasoup SFU on GCP Compute Engine)

## Relationships
- UI Presentation Layer -> Regional Configuration & Telemetry Manager [Local JS Calls]
- UI Presentation Layer -> Local Consent & State Manager [Local JS Calls]
- UI Presentation Layer -> Offline Data Synchronizer [Local JS Calls]
- Video/Audio Session Controller -> Video Streaming Service [WebRTC/UDP, failing over to TCP/TURN relay via API Gateway]
- Regional Configuration & Telemetry Manager & UI Presentation Layer -> Google Cloud API Gateway with OPA [mTLS / HTTPS / WSS with regional headers]
- Local Consent & State Manager -> Offline Data Synchronizer [Local JS Calls]

## Technology Stack
- React / React Native: Cross-platform UI development for web and mobile devices.
- IndexedDB and SQLite: Local storage for offline data caching and consent persistence.
- WebRTC, STUN/TURN, and mediasoup SFU: Real-time video/audio streaming with adaptive bitrate and fallback support.
- Google Cloud API Gateway with OPA: Secured API routing and policy enforcement across regions (`europe-west3` and `us-central1`).

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by pinning client requests and data processing to regional GCP datacenters. Additionally, client-side consent management, offline synchronization, and adaptive WebRTC fallbacks guarantee reliable, compliant telehealth services even over unstable rural internet connections.