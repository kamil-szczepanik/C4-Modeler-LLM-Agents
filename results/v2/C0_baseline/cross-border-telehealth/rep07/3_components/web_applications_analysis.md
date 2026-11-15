## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces regional data residency on GCP while ensuring secure, low-bandwidth resilient access.]

## Key Elements
* Patients (EU / US), Licensed Clinicians, Platform Administrators
* Global External HTTP(S) Load Balancer with GCP Cloud CDN
* Web Applications (Flutter Web / HTML5 / CSS)
* Regional API Gateways (Kong / GCP API Gateway)
* Media Relay / SFU Container (LiveKit / Mediasoup)
* GKE Regional Clusters with SPIFFE/SPIRE mTLS

## Relationships
* Web Applications -> Global External HTTP(S) Load Balancers: HTTPS (TLS 1.3) with strict CSP and SRI headers
* Web Applications -> Regional API Gateways: REST/GraphQL over HTTPS (TLS 1.3)
* Web Applications -> Media Relay / SFU Container: WebRTC (UDP/TCP with DTLS/SRTP)

## Technology Stack
* Flutter Web / HTML5 / CSS: Cross-platform web UI supporting responsive layouts and WCAG 2.1 AA accessibility
* Web Crypto API (AES-GCM): Encrypts local state and consent tokens in IndexedDB for shared rural devices
* WebRTC APIs: Enables low-latency video consultations down to <300 kbit/s with adaptive bitrate streaming
* GCP Cloud CDN: Manages multi-region edge caching and cache-busting for static WASM/JS bundles

## Rationale
[Decoupled regional deployment on GCP ensures strict adherence to GDPR and HIPAA data residency mandates. Edge caching, encrypted local storage, and WebRTC optimizations guarantee high availability and privacy for unstable rural connections.]