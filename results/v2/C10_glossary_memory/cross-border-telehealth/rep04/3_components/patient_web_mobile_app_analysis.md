## Overview
The Cross-Border Telehealth Platform delivers secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients using GCP. The Patient Web/Mobile App provides an offline-first, compliant interface to ensure accessibility and continuous care for rural users.

## Key Elements
- Patients (Person)
- Patient Web/Mobile App (Container, Flutter / React Native)
- Local Secure Storage Component (Component, SQLite / Encrypted Shared Preferences)
- Consent Management UI Component (Component)
- Symptom Checker Client Component (Component)
- Video Consultation Client Component (Component)
- API Gateway & Routing Service (Container, Envoy Proxy / Istio)

## Relationships
- Patients -> Patient Web/Mobile App [HTTPS / WebSockets (adaptive codec)]
- Patient Web/Mobile App -> API Gateway & Routing Service [HTTPS / WebSockets]
- Local Secure Storage Component -> API Gateway & Routing Service [HTTPS (REST) / mTLS]
- Consent Management UI Component -> Local Secure Storage Component [Local Encrypted Write / Read]
- Video Consultation Client Component -> API Gateway & Routing Service [WebSockets / HTTPS]

## Technology Stack
- Flutter / React Native: Cross-platform mobile development for unified patient experience
- SQLite / Encrypted Shared Preferences: Local secure storage for offline-first resilience
- WebRTC with adaptive codecs: Video streaming optimized for low-bandwidth connections (<300 kbit/s)
- OpenTelemetry: Client-side telemetry with strict PII/PHI redaction
- Android Keystore / iOS Keychain: Hardware-backed key derivation for client encryption

## Rationale
This architecture ensures GDPR and HIPAA compliance while supporting offline triage and encrypted local caching for unstable rural connections. Strict hardware-backed security and regional data routing guarantee patient trust and regulatory adherence.