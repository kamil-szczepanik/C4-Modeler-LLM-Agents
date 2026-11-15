## Overview
The Video Session Manager coordinates real-time video consultations for a cross-border telehealth platform operating in the EU and US. It ensures reliable, secure, and compliant streaming for patients with unstable internet connections.

## Key Elements
- SFU Media Router (Mediasoup / C++ & Node.js)
- Session Signaling Controller (Go)
- Session Audit & Metadata Logger (Go)
- Session State Cache (Redis / GCP Memorystore)
- Web/Mobile Frontend App (React / Flutter)

## Relationships
- Web/Mobile Frontend App -> Session Signaling Controller: WebSocket signaling and authentication [WSS over TLS 1.3, JSON]
- Web/Mobile Frontend App -> SFU Media Router: Video/audio streaming and adaptive bitrate controls [WebRTC, UDP/SRTP, DTLS-SRTP]
- Session Signaling Controller -> Session State Cache: Ephemeral session and reconnection state management [TCP, Redis Protocol]
- SFU Media Router -> Session State Cache: Transport state verification for ICE restarts [TCP, Redis Protocol]
- Session Audit & Metadata Logger -> Regional GCP Databases: Telemetry and metadata persistence [TCP, SQL]

## Technology Stack
- Mediasoup & Node.js/C++: High-performance WebRTC packet forwarding with simulcast and adaptive bitrate support
- Go: Low-latency signaling control and audit logging
- GCP Memorystore (Redis): In-memory ephemeral session caching with automated 60-second TTL
- GCP Compute Engine: Dedicated media-plane instances with static public IPs for UDP port range 10000-20000

## Rationale
Decomposing the video manager into specialized components supports adaptive streaming and a 30-second reconnection window for rural users. Regional deployment in europe-west3 and us-central1 strictly enforces GDPR and HIPAA data residency requirements.