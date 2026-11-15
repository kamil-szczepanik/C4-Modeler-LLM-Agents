## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA), and high availability for rural users.]

## Key Elements
- Patient PWA & Clinician Dashboard Frontends (React 18+, TypeScript, Zustand)
- API Gateway (Cloud Armor, Cloud Load Balancing)
- Video Media Router (Mediasoup SFU)
- GCP Cloud Storage and Cloud CDN
- GCP Regions: `europe-west3` (EU) and `us-central1` (US)

## Relationships
- Patient PWA & Clinician Dashboard Frontends -> API Gateway: API requests and authentication via HTTPS
- Authentication & Consent Module -> API Gateway: OAuth2/OIDC token exchange via HTTPS
- Video Consultation View -> Video Media Router (SFU): WebRTC media streams with DTLS-SRTP
- AI Symptom Checker UI -> API Gateway: Submits symptom payloads via HTTPS
- Clinical Dashboard -> API Gateway: Fetches FHIR/e-prescription data via HTTPS

## Technology Stack
- React 18+ with TypeScript: Type-safe, component-based UI development
- Zustand: Lightweight state management for frontend modules
- Service Workers (Workbox): PWA offline caching and resilience for unstable connections
- GCP Cloud Storage & Cloud CDN: High-availability static asset hosting and edge delivery
- `HttpOnly`, `SameSite=Strict` Cookies: Secure session management via API Gateway to prevent XSS token theft
- DTLS-SRTP: Encrypted WebRTC media transport for video consultations

## Rationale
- The architecture enforces regional data residency and security via GCP multi-region isolation and secure cookie handling.
- PWA caching and WebRTC SFU routing ensure continuous telehealth availability for users with low-bandwidth connections.