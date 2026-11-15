## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability for rural users.

## Key Elements
- Patients (EU and US) and Licensed Clinicians (Users)
- Web App & Mobile App Container (React / Flutter)
- Consent & Routing Controller Component
- Resilient Video Client Component (WebRTC)
- Offline-First Symptom Module Component (SQLCipher/IndexedDB)
- API & SFU Client Component
- Localization & a11y Provider Component
- API Gateway and SFU Video Container

## Relationships
- Patients & Clinicians -> Web App & Mobile App: HTTPS/JSON and WebRTC (Video)
- Web App & Mobile App -> API Gateway: HTTPS/TLS 1.3 with regional routing headers, app version hashes, and encrypted payloads
- Resilient Video Client -> SFU Video Container: WebRTC signaling and media streaming with adaptive bitrate

## Technology Stack
- React (Web) and Flutter (Mobile): Cross-platform UI development
- SQLCipher / IndexedDB: Client-side encrypted local caching for offline-first symptom checking
- WebRTC & LiveKit/Janus: Real-time video consultations supporting degraded network modes (<300 kbit/s)
- Sentry / OpenTelemetry: Client-side RUM, error tracking, and performance monitoring
- OAuth 2.0 / OIDC: Secure session management and token handling

## Rationale
This architecture ensures strict regional data compliance and resilience for unstable rural internet connections. Client-side encryption, robust telemetry, and modular components support EU MDR traceability and HIPAA security standards.