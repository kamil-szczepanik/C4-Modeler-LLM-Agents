## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It utilizes GCP (`europe-west3` and `us-central1`) to enforce strict regional data residency and compliance.

## Key Elements
- React Web Application & React Native Mobile App
- GCP Cloud Endpoints / Envoy API Gateway
- Video Media Server (LiveKit / WebRTC SFU)
- SFU Router (LiveKit Core / Go)
- ABR Controller (Custom Go module)
- Media Signaling Handler (Node.js / LiveKit SDK)
- GCP Google Kubernetes Engine (GKE) & Google Cloud Storage (CMEK)

## Relationships
- React App / Mobile App -> Media Signaling Handler: Session negotiation [WSS / TLS 1.3]
- React App / Mobile App -> SFU Router: Media streaming [WebRTC / DTLS-SRTP]
- ABR Controller -> SFU Router: Quality adjustments [Internal gRPC]
- Media Signaling Handler -> SFU Router: Token validation & session tickets [In-memory]
- SFU Router -> GCP Cloud Storage: Encrypted recording streams [HTTPS / CMEK]

## Technology Stack
- **LiveKit Server (Go):** Core WebRTC SFU for real-time media routing.
- **Node.js / LiveKit SDK:** Handles signaling, authentication, and JWT validation.
- **GCP GKE & Cloud Storage:** Ephemeral container orchestration and region-locked storage.
- **DTLS-SRTP & TLS 1.3:** End-to-end transport security for media and signaling.

## Rationale
This architecture ensures strict regional data residency compliance (GDPR/HIPAA) through isolated GCP deployments. It supports reliable, low-bandwidth video consultations for rural users via adaptive bitrate control and secure WebRTC SFU routing.