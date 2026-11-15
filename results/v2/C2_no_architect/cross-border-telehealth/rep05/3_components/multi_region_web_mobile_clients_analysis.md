## Overview
[The Multi-region Web/Mobile Clients serve as the primary user interface for patients, clinicians, and support staff across the EU and US. It delivers secure video consultations, e-prescriptions, and AI symptom checking while enforcing strict regional data residency.]

## Key Elements
- Patients
- Licensed Clinicians
- Support Staff
- Compliance/Legal Officers
- Multi-region Web/Mobile Clients (Web and Mobile applications)
- Edge Routing & WebRTC SFU Containers
- AI Symptom Checker Container
- Consent Management Service

## Relationships
- Patients -> Multi-region Web/Mobile Clients: Accesses platform for video consultations and symptom checking via HTTPS / WebRTC
- Licensed Clinicians -> Multi-region Web/Mobile Clients: Conducts consultations and issues e-prescriptions via HTTPS
- Multi-region Web/Mobile Clients -> Edge Routing & WebRTC SFU Containers: Streams video and consultations using WebRTC with TLS 1.3
- AI Symptom Checker Container -> Multi-region Web/Mobile Clients: Returns urgency recommendations via mTLS

## Technology Stack
- OAuth 2.0 with PKCE: Secures user authentication and authorization flows
- Android Keystore / iOS Secure Enclave: Provides hardware-backed encrypted local storage for offline caching
- WebAuthn / Mobile Biometrics: Enforces local biometric re-authentication upon app foregrounding
- TLS 1.3 with Certificate Pinning: Secures network transport and mitigates MitM attacks in untrusted environments
- GCP Cloud Monitoring / Crashlytics: Handles client telemetry with PII/PHI stripped at the edge

## Rationale
[This architecture ensures GDPR and HIPAA compliance by strictly partitioning regional client builds and telemetry to prevent data leakage. Additionally, adaptive bitrate streaming and secure local caching guarantee high availability and data protection for rural patients with unstable connections.]