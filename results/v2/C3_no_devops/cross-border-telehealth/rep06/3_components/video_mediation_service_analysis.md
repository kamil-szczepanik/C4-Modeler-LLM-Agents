## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency on GCP while ensuring reliable real-time communication under unstable network conditions.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Regional API Gateways (Google Cloud API Gateway in `europe-west3` and `us-central1`)
- Video Mediation Service (Twilio / WebRTC integration)
- Session Signaling Controller (Go / WebSockets)
- Bandwidth Adaptation Engine (Go)
- Telemetry & Audit Collector (Go)
- Media Quality Policy Enforcer (Go)
- Google Cloud Pub/Sub
- Memorystore for Redis (Regional)
- Third-Party Video Provider

## Relationships
- Patients/Clinicians -> Regional API Gateways: Access platform features [HTTPS / WSS]
- Regional API Gateways -> Session Signaling Controller: Initiates call setup and routes cryptographically signed JWTs [gRPC over HTTP/2 with mTLS]
- Session Signaling Controller -> Memorystore for Redis: Persists ephemeral signaling state and session tokens [Redis Protocol]
- Bandwidth Adaptation Engine & Media Quality Policy Enforcer -> Third-Party Video Provider: Dynamically adjusts streams and prioritizes audio [WebRTC / SRTP / DTLS]
- Telemetry & Audit Collector -> Google Cloud Pub/Sub: Streams scrubbed session quality metrics and compliance logs [gRPC]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider across `europe-west3` (EU) and `us-central1` (US) for regional isolation.
- Go: Chosen for internal microservices due to low memory footprint and high concurrency handling.
- WebSockets & gRPC (HTTP/2): Used for low-latency real-time signaling and internal component communication.
- WebRTC, SRTP, & DTLS: Used for encrypted peer-to-peer and media stream transmission.
- Memorystore for Redis: Regional caching for ephemeral session tokens and state management.
- Google Cloud Pub/Sub: Asynchronous telemetry and audit log streaming.

## Rationale
This architecture complies with GDPR and HIPAA mandates by strictly isolating regional health data and session states within GCP. Furthermore, the Go-based media adaptation components guarantee continuous care for rural patients by prioritizing audio and scaling bandwidth under 300 kbit/s.