## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency while ensuring high availability for rural users.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Video Session Manager (GKE container)
- Signaling Server Component (Node.js / WebSockets)
- Media Gateway Controller (C++ / WebRTC SFU / Mediasoup)
- Session Audit Logger Component (Node.js)
- Session State Coordinator (Memorystore for Redis)
- Regional Data Storage & Audit Layer (Cloud SQL, BigQuery)

## Relationships
- Signaling Server -> Media Gateway Controller: Coordinates stream routing [In-Process / IPC]
- Signaling Server -> API Gateway: Receives session control commands [gRPC]
- Session Audit Logger -> Regional Data Storage & Audit Layer: Persists session metrics [gRPC over VPC]
- Signaling Server -> Session State Coordinator: Manages room states and tokens [Redis Protocol / VPC]
- Media Gateway Controller -> Session State Coordinator: Updates media states [Redis Protocol / VPC]

## Technology Stack
- Google Kubernetes Engine (GKE): Deploys regional node pools to maintain persistent UDP connections and strict data residency.
- Node.js & WebSockets: Powers real-time session signaling and audit logging.
- C++ & Mediasoup/LiveKit: Implements WebRTC SFU for adaptive bitrate control down to 300 kbit/s.
- Memorystore for Redis: Provides regional state caching for the 60-second reconnection grace window.
- DTLS-SRTP & WSS (TLS 1.3): Secures media streams and signaling with mTLS.

## Rationale
GKE combined with regional Redis caching guarantees real-time WebRTC stability and data residency compliance (GDPR/HIPAA). Adaptive bitrate control and a 60-second reconnection window ensure reliable healthcare delivery for rural users with unstable internet connections.