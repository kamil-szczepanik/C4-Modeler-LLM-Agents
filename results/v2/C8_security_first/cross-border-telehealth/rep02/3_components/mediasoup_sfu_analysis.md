## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability for users with unstable internet connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Istio Service Mesh & API Gateway (Istio)
- Backend-for-Frontend (BFF) (Node.js, GraphQL)
- Mediasoup SFU (Mediasoup WebRTC)
- Worker Pool (C++ / Node.js)
- Room & Signaling Manager (Node.js)
- Simulcast & Adaptation Controller (C++)
- Telemetry & Stats Exporter
- STUN/TURN Relay Agent (coturn)
- AI Triage Service, Consent Manager, E-Prescription Adapter, Regional WORM Storage (GCP Storage)

## Relationships
- Istio Service Mesh & API Gateway -> Mediasoup SFU: Routes video and audio streams [DTLS-SRTP]
- Room & Signaling Manager -> Worker Pool: Controls transport and producer/consumer creation [IPC]
- Mediasoup SFU -> BFF: Reports QoE telemetry and connection state changes [gRPC / WebSocket]
- Simulcast & Adaptation Controller -> Telemetry & Stats Exporter: Feeds bitrate and packet loss metrics [Internal IPC]
- Mediasoup SFU (Worker Pool) <-> STUN/TURN Relay: Relays media packets for NAT traversal [UDP/TURN]

## Technology Stack
- Google Cloud Platform (GCP): Targeted cloud provider across `europe-west3` and `us-central1` for data residency.
- Mediasoup WebRTC & Node.js/C++: Handles real-time video/audio SFU capabilities and low-bandwidth adaptation.
- Kubernetes with KEDA: Manages custom Prometheus metric-driven autoscaling for media workloads.
- Istio: Enforces mTLS, TLS termination, and API routing security.
- coturn: Provides NAT traversal for rural patients with restrictive firewalls.

## Rationale
This architecture isolates stateless media processing in regional GCP zones to satisfy GDPR and HIPAA data residency mandates. Custom KEDA scaling, simulcast adaptation, and STUN/TURN relays ensure resilient video consultations for rural patients under 300 kbit/s.