## Overview
[The Video Streaming Service container provides low-latency WebRTC video consultations for the Cross-Border Telehealth Platform across EU and US regions. It ensures robust communication for rural patients with unstable internet connections while maintaining strict regional data residency.]

## Key Elements
- Signaling Server (Node.js / WebSockets)
- SFU Router Core (mediasoup / C++ / Node.js)
- Adaptive Bitrate & Quality Manager (Go)
- TURN/STUN Relay Manager (Coturn on GCP Compute Engine)
- Media Session Audit Logger (Go)
- Geo-Distributed TURN Coordinator (Go)

## Relationships
- Web & Mobile Apps -> Signaling Server: Session control [WSS]
- Web & Mobile Apps <-> SFU Router Core: Media streaming [WebRTC/UDP/DTLS]
- Adaptive Bitrate & Quality Manager -> SFU Router Core: Adjusts simulcast layers [Internal IPC]
- SFU Router Core -> Media Session Audit Logger: Emits session telemetry [gRPC]
- Web & Mobile Apps -> Geo-Distributed TURN Coordinator: Relay allocation [HTTPS]
- Geo-Distributed TURN Coordinator -> TURN/STUN Relay Manager: Provisions endpoints [gRPC]

## Technology Stack
- mediasoup SFU: Minimizes CPU and bandwidth overhead for video routing
- Coturn on GCP Compute Engine: Handles NAT traversal for unstable rural connections
- Node.js & Go: Delivers high-concurrency connection management and telemetry processing

## Rationale
[This architecture enforces regional data residency by isolating session metadata locally within europe-west3 and us-central1. It guarantees degraded-mode operation below 300 kbit/s via dynamic bitrate management.]