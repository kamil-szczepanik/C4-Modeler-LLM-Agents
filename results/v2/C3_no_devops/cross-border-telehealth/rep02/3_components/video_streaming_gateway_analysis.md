## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance (GDPR/HIPAA), and robust video streaming for low-bandwidth connections.

## Key Elements
- Patients & Licensed Clinicians
- Web & Mobile Client Containers
- Video Streaming Gateway Container
- SFU Media Router Component (MediaSoup C++/Node.js)
- Adaptive Bitrate & Transcoding Controller Component
- Signaling & Session Manager Component (Node.js/Go)
- Media Telemetry Exporter Component
- Core Telehealth Backend Container

## Relationships
- Web & Mobile Client -> Signaling & Session Manager: WSS (JSON-RPC over WebSockets) for real-time room orchestration using short-lived JWTs
- Web & Mobile Client <-> SFU Media Router: WebRTC (SRTP/DTLS) for media transport with DTLS 1.3 encryption
- Adaptive Bitrate & Transcoding Controller -> SFU Media Router: Internal IPC / gRPC for dynamic media layer adjustments
- Media Telemetry Exporter -> Core Telehealth Backend: HTTP (Prometheus scrape protocol) for session quality metrics

## Technology Stack
- MediaSoup (C++ / Node.js worker): Core SFU media routing for high-performance packet forwarding
- WebRTC (SRTP/DTLS 1.3): Encrypted, real-time audio and video transport
- JSON-RPC over WebSockets (WSS): Signaling and session establishment protocol
- gRPC / IPC: Low-latency internal communication between controllers and media workers
- Prometheus: Real-time telemetry and session quality metrics collection
- GCP GKE / GCE (`europe-west3`, `us-central1`): Regional container orchestration with strict data residency pinning

## Rationale
Decomposing the Video Streaming Gateway into specialized components enables adaptive bitrate handling to maintain consultations in degraded network conditions below 300 kbit/s. Hard-pinned regional deployments on GCP ensure full compliance with regional GDPR and HIPAA data residency mandates.