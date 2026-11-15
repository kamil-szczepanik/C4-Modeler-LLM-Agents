## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures regional data residency and low-bandwidth resilience for rural users.

## Key Elements
- Web Application & Mobile Client Gateway (React / React Native)
- API Gateway (Node.js / Go)
- Signaling Controller (Node.js / WebSockets)
- Adaptive Bitrate Manager (Go)
- TURN/SFU Proxy Controller (C++ / Pion-based)
- Audit & Compliance Logger
- Google Kubernetes Engine (GKE) with Cilium CNI
- Google Cloud External HTTP(S) Load Balancer

## Relationships
- Client Gateway -> API Gateway via HTTPS/WSS (TLS 1.3)
- API Gateway -> Signaling Controller via gRPC over mTLS (Istio)
- Signaling Controller -> Adaptive Bitrate Manager via internal channels
- TURN/SFU Proxy Controller -> External WebRTC Infrastructure via UDP/DTLS (SRTP media relay)
- Signaling Controller -> API Gateway via asynchronous gRPC for audit logging

## Technology Stack
- GCP (europe-west3, us-central1): Ensures regional data residency compliance (GDPR/HIPAA).
- WebRTC with DTLS-SRTP: Secures real-time video/audio media streams with blind-relay enforcement.
- Go and Node.js: Powers high-performance signaling and bitrate management components.
- GKE with Cilium CNI and eBPF: Optimizes UDP packet throughput and enforces network policies.

## Rationale
This architecture isolates media processing in regional clusters to satisfy strict healthcare data residency laws. The component design prioritizes audio and implements automated reconnection to maintain clinical continuity for users with unstable internet connections.