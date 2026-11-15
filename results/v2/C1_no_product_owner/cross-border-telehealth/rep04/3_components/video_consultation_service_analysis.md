## Overview
- The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US.
- The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and resilient media streaming for low-bandwidth rural connections.

## Key Elements
- Signaling Controller (Node.js / WebSockets)
- SFU Media Router (LiveKit Core / Go)
- Adaptive Quality Manager (Go)
- Session Audit Logger (Go / gRPC)
- Regional GKE Clusters (GCP `europe-west3`, `us-central1`)
- Google Cloud Memorystore for Redis
- Regional IAM Services

## Relationships
- Signaling Controller -> SFU Media Router: Controls media streams [gRPC]
- Adaptive Quality Manager -> SFU Media Router: Enforces bitrate limits [Internal API]
- Signaling Controller -> Regional IAM Services: Validates JWT tokens [gRPC/mTLS]
- Signaling Controller -> Session Audit Logger: Emits session lifecycle events [gRPC]
- Session Audit Logger -> Data Storage: Persists signed audit logs [SQL]

## Technology Stack
- LiveKit Core / Go: Powers the SFU media routing container for real-time video
- WebSockets / Node.js: Manages low-latency session signaling and SDP exchanges
- GCP Dataplane V2 (eBPF): Optimizes high-throughput UDP packet handling on GKE
- DTLS-SRTP: Encrypts real-time WebRTC media streams end-to-end
- Google Cloud Memorystore for Redis: Maintains decoupled, regional ephemeral room state

## Rationale
- The containerized microservice design with RAM-only processing satisfies strict HIPAA, GDPR, and EU MDR compliance without writing PHI to disk.
- KEDA autoscaling and the Adaptive Quality Manager ensure reliable video consultations under degraded rural bandwidth constraints (<300 kbit/s).