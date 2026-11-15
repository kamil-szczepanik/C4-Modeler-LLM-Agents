## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and low-bandwidth resilience for rural connectivity.

## Key Elements
- Patients and Licensed Clinicians (End Users)
- React / Flutter Web and Mobile Apps
- Google Cloud API Gateway / Region Router
- Go / Spring Boot Core Telehealth Backends
- LiveKit / WebRTC SFU Video Media Servers (LiveKit SFU Core, SFU Webhook Handler, Adaptive Bitrate Engine, SFU Telemetry Aggregator)
- Global TURN/STUN Edge Relays
- Google Cloud SQL & Cloud Storage with Cloud KMS

## Relationships
- Patients / Clinicians -> LiveKit SFU Core: Media and signaling streaming [WebRTC over UDP/TCP, WSS]
- Go / Spring Boot Core Telehealth Backends -> LiveKit SFU Core: Room provisioning and token generation [gRPC / HTTPS]
- LiveKit SFU Webhook Handler -> Core Telehealth Backend: Session lifecycle events and quality telemetry [HTTPS POST, HMAC-SHA256, mTLS]
- LiveKit SFU Core -> Global TURN/STUN Edge Relays: Media relay through edge nodes [STUN/TURN]

## Technology Stack
- LiveKit / WebRTC SFU: Powers real-time video sessions with Simulcast support for degraded-mode operations
- Google Kubernetes Engine (GKE): Hosts isolated regional SFU clusters in `europe-west3` and `us-central1`
- Go: Used for high-performance SFU core, webhook handlers, and telemetry components
- DTLS-SRTP & TLS 1.3: Secures all media and signaling transmission in transit
- HMAC-SHA256 & mTLS: Secures inter-container webhook communication

## Rationale
Isolated regional deployments in GCP ensure full compliance with GDPR and HIPAA data residency mandates. Simulcast and adaptive bitrate controls guarantee reliable consultations for rural patients on unstable connections below 300 kbit/s.