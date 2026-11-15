## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Ensures compliance with GDPR, HIPAA, and EU MDR via region-locked GCP deployment.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- Web & Mobile Client Containers (Flutter / React Native)
- UI Presentation & Routing Module
- Offline-First State & Caching Manager
- API & Sync Client
- WebRTC Media Client
- API Gateway & Video Streaming Gateway

## Relationships
- Patients & Clinicians -> Web & Mobile Client Containers [HTTPS, WebRTC]
- Web & Mobile Client Containers -> API Gateway [HTTPS/gRPC via mTLS]
- Web & Mobile Client Containers -> Video Streaming Gateway [WebRTC media streams with SRTP/DTLS]

## Technology Stack
- Flutter / React Native: Cross-platform consistency and robust offline database integrations.
- SQLCipher & Secure Enclaves: Local at-rest encryption for cached PHI/PII on mobile devices.
- gRPC over mTLS: Bandwidth-efficient offline queue synchronization.
- WebRTC / MediaHub SFU: Low-latency video streaming for degraded connections under 300 kbit/s.

## Rationale
The architecture ensures high availability in unstable rural environments through offline-first caching while strictly maintaining regional data residency and security compliance for healthcare data.