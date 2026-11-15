## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures regional data residency, strict regulatory compliance (GDPR/HIPAA), and resilient media streaming for unstable rural network connections.

## Key Elements
- Web Frontend (PWA): Next.js/React application for patients and clinicians.
- Media Relaying Service: LiveKit-based SFU/MCU container providing video consultations.
- SFU Media Router: Go-based LiveKit server node handling real-time WebRTC media forwarding and adaptive bitrate scaling.
- Room & Session Manager: Node.js/Go component managing virtual rooms, authentication, and region-locked policies.
- Telemetry & Audit Collector: Go-based component capturing WebRTC stats and compliance metadata.
- TURN/STUN Relay Gateway: Coturn/LiveKit Egress handling NAT traversal and TCP fallback.
- Target Cloud: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions.

## Relationships
- Web Frontend (PWA) -> Room & Session Manager: Authenticates and requests connection tokens [gRPC / HTTPS]
- Web Frontend (PWA) <-> SFU Media Router: Relays encrypted audio/video streams [WebRTC over UDP/TCP]
- Web Frontend (PWA) <-> TURN/STUN Relay Gateway: Relays encrypted media via TCP fallback [WebRTC over TLS/TCP]
- SFU Media Router -> Telemetry & Audit Collector: Streams session quality metrics [Internal gRPC]
- Telemetry & Audit Collector -> Core Backend services: Exports aggregated session logs [gRPC]

## Technology Stack
- LiveKit (SFU/MCU): Selected for real-time video and adaptive bitrate streaming to support low-bandwidth resilience.
- Go & Node.js: Used for backend components and media router services to ensure high concurrency and performance.
- GCP Managed Instance Groups (MIGs) / GKE: Deployed in isolated regional clusters to enforce strict data residency.
- Coturn: Implemented for TURN/STUN NAT traversal and TCP/443 fallback in restricted rural networks.

## Rationale
This architecture uses regional GCP deployments to strictly enforce EU and US health data residency constraints. LiveKit and Coturn integrations guarantee stable video consultations for patients in rural areas with unstable internet connections.