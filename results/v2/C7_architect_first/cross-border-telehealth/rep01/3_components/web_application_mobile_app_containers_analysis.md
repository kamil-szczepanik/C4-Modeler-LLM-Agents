## Overview
[A secure, cross-border telehealth platform delivering video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while enforcing strict regional data residency.]

## Key Elements
*   UI Layer (React / React Native)
*   AI Symptom Checker Client Module
*   Media Client Module (WebRTC)
*   Local State & Consent Manager
*   Offline Sync Queue
*   GCP API Gateway
*   Media Relay Containers (Coturn TURN/STUN, Mediasoup SFU)

## Relationships
*   UI Layer -> AI Symptom Checker Client Module [Internal Application Events]
*   UI Layer -> Media Client Module [Internal Application Events]
*   AI Symptom Checker Client Module -> GCP API Gateway [HTTPS/REST]
*   Media Client Module -> Media Relay Containers [WSS/WebRTC]
*   Local State & Consent Manager -> GCP API Gateway [HTTPS with Signed Consent Claims]

## Technology Stack
*   React / React Native: Client-facing web and mobile applications.
*   SQLCipher: Encrypted local storage for offline-first caching and PHI protection.
*   WebRTC / Mediasoup SFU: Real-time video streaming with adaptive bitrate scaling for low-bandwidth connections (<300 kbit/s).
*   OAuth 2.0 / OpenID Connect: Authentication utilizing short-lived JWTs and strict token binding.
*   Play Integrity / DeviceCheck: Mobile device attestation for rooted or jailbroken device detection.

## Rationale
[This architecture satisfies rigorous GDPR and HIPAA data residency mandates by enforcing strict client-side consent gating and token validation at the GCP API Gateway. Furthermore, the offline-first sync queue and adaptive WebRTC streaming ensure high availability and continuous care for rural patients with unstable internet connections.]