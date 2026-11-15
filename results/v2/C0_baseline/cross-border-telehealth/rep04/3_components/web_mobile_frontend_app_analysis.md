## Overview
[A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.]
[Ensures strict GDPR and HIPAA compliance with region-locked data residency and offline resilience for rural areas.]

## Key Elements
- Web/Mobile Frontend App (React / Flutter)
- Routing & Shell Component
- Consent & Privacy Manager Component
- AI Symptom Checker UI Component
- Video Streaming Interface Component
- API Client & Local Storage Adapter

## Relationships
- Routing & Shell Component -> Consent & Privacy Manager Component: Manages UI state [In-Memory]
- Consent & Privacy Manager Component -> API Client & Local Storage Adapter: Syncs consent states [HTTPS/REST]
- AI Symptom Checker UI Component -> API Client & Local Storage Adapter: Sends symptom payloads [HTTPS/gRPC]
- Video Streaming Interface Component -> Video Session Manager: Establishes media streams [WebRTC]
- API Client & Local Storage Adapter -> API Gateway / Core Backend: Sends API requests [HTTPS/gRPC]

## Technology Stack
- React / Flutter: Builds a responsive Progressive Web App and mobile interface supporting low-bandwidth conditions
- Firebase Hosting / Cloud Storage + Cloud CDN: Regional edge hosting enforcing data residency in europe-west3 and us-central1
- WebRTC SDKs: Enables video streaming with adaptive bitrate controls for connections under 300 kbit/s
- AES-GCM / Secure Hardware: Encrypts cached patient health data bound to device Keychain/Keystore

## Rationale
[This architecture ensures regional data segregation and strict compliance with EU GDPR and US HIPAA mandates.]
[Client-side caching and adaptive video streaming provide reliable healthcare delivery for rural users with unstable internet.]