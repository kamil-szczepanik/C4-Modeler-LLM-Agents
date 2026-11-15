## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It guarantees strict regional data residency, regulatory compliance, and high availability for low-bandwidth users.

## Key Elements
- Web & Mobile Clients (React / React Native)
- Signaling & Room Manager (Node.js/TypeScript)
- SFU Core Router (Mediasoup C++ worker wrapper)
- Adaptive Bitrate & Quality Controller (Node.js)
- NAT Traversal Agents (GCP STUN/TURN integration)
- Media Region Router
- Media Session Logger
- Media Encryption Enforcer
- STUN/TURN Health & Metrics Exporter
- Consent & Audit Logging Service (Go)

## Relationships
- Web & Mobile Clients -> Signaling & Room Manager: WebSocket [WSS]
- Web & Mobile Clients -> SFU Core Router: WebRTC [ICE/DTLS/SRTP over UDP/TCP]
- SFU Core Router <-> Adaptive Bitrate & Quality Controller: Asynchronous Worker IPC
- Media Session Logger -> Consent & Audit Logging Service: Regional Telemetry [gRPC]
- STUN/TURN Health & Metrics Exporter -> Core Telehealth Service: Health Check [gRPC]

## Technology Stack
- GCP (europe-west3, us-central1): Cloud infrastructure ensuring strict data residency per region
- Node.js & Mediasoup: Real-time media streaming and Selective Forwarding Unit (SFU) capabilities
- DTLS-SRTP with AES-GCM: Native secure transport configuration for encrypted media streams
- WebSockets & WebRTC: Low-latency client-server signaling and peer-to-peer media transport

## Rationale
The component architecture isolates media handling into regional GCP nodes to satisfy strict GDPR and HIPAA data residency constraints. Using Mediasoup with an adaptive bitrate controller ensures uninterrupted video consultations for rural patients on unstable connections below 300 kbit/s.