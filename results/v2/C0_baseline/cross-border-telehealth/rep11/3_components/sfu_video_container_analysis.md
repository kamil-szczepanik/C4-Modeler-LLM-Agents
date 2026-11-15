## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The SFU Video Container manages secure, real-time WebRTC video consultations with adaptive streaming for unstable connections.]

## Key Elements
- WebRTC Media Router (LiveKit Server / Go)
- Adaptive Bitrate Controller (LiveKit Egress/Ingress SDK / Go)
- Session Signaling Handler (WebSockets / gRPC)
- TURN/STUN Relay Service (Coturn)
- Patients and Licensed Clinicians

## Relationships
- Patients and Licensed Clinicians connect to WebRTC Media Router via WebRTC (UDP/TCP) using SRTP
- Session Signaling Handler communicates with Core Services Container via gRPC with mTLS
- Adaptive Bitrate Controller publishes degradation metrics to Google Cloud Pub/Sub over TLS

## Technology Stack
- LiveKit Server / Go for real-time SFU media routing
- Coturn for regional NAT/firewall traversal (TURN/STUN)
- Google Cloud Pub/Sub for asynchronous telemetry and event publishing
- Google Kubernetes Engine (GKE) on C2/C3 network-optimized nodes for deployment

## Rationale
[This architecture ensures low-latency video and compliance with GDPR/HIPAA by keeping media traffic and TURN/STUN relays strictly within regional GCP boundaries. Adaptive bitrate control and dedicated network nodes guarantee reliable consultations for rural patients on unstable connections.]