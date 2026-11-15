## Overview
- Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.
- Designed to ensure regional data residency, strict regulatory compliance (GDPR/HIPAA), and robust performance for unstable rural internet connections.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway & Consent Container (Envoy / Google Cloud Endpoints, Open Policy Agent)
- Core Telehealth Backend (Node.js / Go)
- Video Consultation Service Container:
  - Signaling Controller (Node.js / WebSockets)
  - Media Router / SFU Core (Janus Media Server / C++)
  - Adaptive Bitrate & Quality Manager (C++ plugin)
  - Room Access Control & Consent Verifier (Node.js)
  - Recording & Transcoding Worker (Python / GStreamer)
  - TURN/STUN Relay Manager (Coturn on GCE Compute Engine)
- AI Symptom Checker (Python / FastAPI)
- Interoperability Adapter (Java / Spring Boot)
- Asynchronous Event Broker (GCP Pub/Sub)
- Dedicated Audit & Logging Container (Fluentbit / OpenTelemetry)
- Regional Databases (Cloud SQL PostgreSQL, Cloud Storage, Cloud Firestore in `europe-west3` and `us-central1`)
- External Systems: National Pharmacies, National EHR Gateways, Stripe, Twilio/Firebase

## Relationships
- Patients and Clinicians connect to Media Router and TURN/STUN Relay Manager via WebRTC (DTLS-SRTP over UDP/TCP) and TURN.
- Signaling Controller communicates with API Gateway via gRPC for session authorization.
- Signaling Controller queries Room Access Control & Consent Verifier via internal gRPC to validate real-time consent and data residency.
- Recording & Transcoding Worker streams encrypted media chunks to Regional Cloud Storage via HTTPS (REST).
- Media Router emits session telemetry to Audit & Logging Container via OpenTelemetry (gRPC).

## Technology Stack
- Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict data residency.
- Janus Media Server and Coturn for real-time video streaming and NAT traversal.
- Node.js, Python, Java, and Go for backend microservices and components.
- PostgreSQL, Cloud Firestore, and Cloud Storage for regional persistent data storage.
- WebRTC, gRPC, WebSockets, and HTTPS (REST/TLS) for communication protocols.

## Rationale
- The multi-region GCP architecture guarantees that EU health data remains in `europe-west3` and US data in `us-central1` to satisfy GDPR and HIPAA.
- Janus SFU combined with a custom Adaptive Bitrate Manager and Coturn relay ensures seamless video consultations even on unstable rural connections below 300 kbit/s.