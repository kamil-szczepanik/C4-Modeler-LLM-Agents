## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA/MDR), and resilient performance over unstable rural networks.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Compliance Officers.
- **Client Apps Container**: Flutter/Web application running on patient and clinician devices.
- **Internal Components**: Offline Sync & Local Storage, Video Adaptation, API Client & Region Router, Consent & State Management, Local Telemetry & Audit Logger.
- **External Systems**: Google Cloud API Gateway, LiveKit WebRTC SFU, EU National E-Prescription Gateways, US Pharmacy Networks.

## Relationships
- Patients & Clinicians -> Client Apps: Accesses telehealth services and consultations via [HTTPS / WebSockets].
- Client Apps -> Video Media Server: Streams real-time video via [WebRTC (SRTP with DTLS-SRTP)].
- Client Apps -> API Gateway: Communicates securely via [HTTPS with SSL/Certificate Pinning and mTLS].
- Offline Sync Component -> SQLite with SQLCipher: Encrypts local data at rest using [AES-256 bound to Secure Enclave/Keystore].

## Technology Stack
- **Flutter / Web**: Cross-platform client framework for unified mobile and browser support.
- **SQLite with SQLCipher**: Encrypted local storage for offline caching on mobile devices.
- **LiveKit SDK**: WebRTC client library for dynamic bitrate scaling and degraded-mode audio fallback.
- **Bloc / Provider**: State management pattern for enforcing consent-gated local execution.

## Rationale
This architecture uses an offline-first, encrypted client design to maintain continuous care under unstable rural network conditions while strictly enforcing regional data residency and consent. Hardware-backed security controls and tamper-evident local logging ensure full compliance with GDPR, HIPAA, and EU MDR mandates.