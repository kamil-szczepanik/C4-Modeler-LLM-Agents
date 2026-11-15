## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The unified client architecture ensures strict regional data residency, low-bandwidth resilience, and regulatory compliance.]

## Key Elements
- Web / Mobile Client (React / React Native)
- UI Presentation Layer
- WebRTC Media Client
- Telemetry & Audit Logger
- Local State & Storage Manager
- API Gateway (Envoy / Cloud Endpoints)
- GCP Cloud CDN / Firebase Hosting

## Relationships
- Patients & Clinicians -> Web / Mobile Client: Access telehealth services, video consultations, and consent management [HTTPS (TLS 1.3) and WSS]
- UI Presentation Layer -> API Gateway: Sends synchronous application requests [HTTPS (TLS 1.3)]
- WebRTC Media Client -> API Gateway & SFU: Streams video consultations and handles adaptive bitrate fallback [WSS and WebRTC with Insertable Streams E2EE]
- Telemetry & Audit Logger -> API Gateway: Transmits scrubbed audit logs and regional usage telemetry [HTTPS (TLS 1.3)]

## Technology Stack
- React / React Native: Unified multi-platform client framework minimizing development overhead across regions
- WebRTC with Insertable Streams API: Real-time video streaming with end-to-end encryption to satisfy clinical privacy mandates
- Platform-Native Secure Enclaves & SQLite: Secure token storage and encrypted local state management for offline caching
- Firebase Hosting / Cloud CDN: Multi-region static asset delivery enforcing strict regional boundary isolation at the edge

## Rationale
[This client-side architecture enforces strict data privacy, local PHI-scrubbing, and cryptographic OTA integrity required for GDPR and HIPAA compliance. Furthermore, the modular component breakdown successfully addresses low-bandwidth stability and audit traceability for cross-border medical operations.]