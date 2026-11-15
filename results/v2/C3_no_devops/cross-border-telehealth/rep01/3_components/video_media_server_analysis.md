## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and low-bandwidth resilience for rural users.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Service (Go / Spring Boot)
- Video Media Server (LiveKit SFU container deployed in `europe-west3` and `us-central1`)
- SFU Core Router (Go / LiveKit component)
- Adaptive Bitrate (ABR) Controller component
- Room & Session Manager (Go component)
- Media Compliance Logger component
- Regional Databases (Cloud Spanner / Cloud SQL)

## Relationships
- Patients / Clinicians -> SFU Core Router: Stream audio/video [WebRTC / ICE over UDP/TCP]
- Patients / Clinicians -> SFU Core Router: Control-plane signaling [WSS / TLS 1.3]
- Room & Session Manager -> Core Telehealth Service: Validate session token [gRPC]
- ABR Controller -> SFU Core Router: Command layer subscription changes [Internal Go Channel]
- Media Compliance Logger -> Regional Databases: Write anonymized session metadata [SQL over TLS]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance (GDPR/HIPAA).
- LiveKit SFU / Go: Powers real-time media routing and low-latency handling.
- WebRTC with SRTP / DTLS-SRTP: Secures end-to-end media transport with zero unencrypted fallback.
- JWT: Enforces short-lived, cryptographically signed token-based access control.

## Rationale
This architecture guarantees strict regional data isolation to comply with GDPR and HIPAA while supporting low-bandwidth optimization for rural users. The containerized component design ensures zero-disk persistence and robust auditability for cross-border healthcare delivery.