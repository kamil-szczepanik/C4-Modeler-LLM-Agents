## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Built on GCP while enforcing strict regional data residency and low-bandwidth resilience.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web App & Mobile App (Flutter / React)
- GCP API Gateway
- Core Telehealth Backend (Go / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Video Streaming Server (WebRTC / SFU Mediasoup with SFU Core, ABR Controller, Signaling Handler, TURN/STUN Relay Agent)
- EU E-Prescriptions Adapter (Java / Spring Boot)
- US Healthcare Interoperability Service (Node.js / FHIR SDK)
- GCP Cloud SQL & Cloud Storage (PostgreSQL, WORM buckets, Cloud KMS, GCP Secret Manager)

## Relationships
- Web App & Mobile App -> Signaling Handler: Session setup [WebSocket / JSON]
- Web App & Mobile App <-> SFU Core: Encrypted media streams [WebRTC / DTLS / SRTP]
- Web App & Mobile App -> TURN/STUN Relay Agent: Relayed media packets [TURN over UDP/TCP]
- Signaling Handler -> TURN/STUN Relay Agent: Provisions HMAC credentials [REST API]
- ABR Controller -> SFU Core: Bitrate throttling and downmixing [Internal API]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance (GDPR/HIPAA).
- WebRTC / Mediasoup (SFU): Enables low-latency adaptive video consultations.
- Coturn: Provides NAT traversal for rural patients with unstable connections.
- PostgreSQL & Cloud Storage: Persists transactional and audit data securely.

## Rationale
This architecture guarantees strict regional isolation of health data to comply with GDPR and HIPAA mandates. It incorporates adaptive bitrate control and relay mechanisms to maintain video consultations for rural users on unstable networks.