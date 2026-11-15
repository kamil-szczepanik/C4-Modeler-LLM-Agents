## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and AI symptom checking for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable rural connections.

## Key Elements
- Single-Patient / Mobile App (Flutter / TypeScript)
- SFU Room & Session Manager (Go / LiveKit Core)
- Media Forwarding Engine (Go / WebRTC)
- TURN / ICE Relay Service (Coturn / LiveKit Egress)
- Recording & Egress Service (LiveKit Egress / Go)
- Core Telehealth Service (Go / gRPC)
- Cloud Storage (GCP)

## Relationships
- Single-Patient / Mobile App -> Media Forwarding Engine: Streams audio/video via WebRTC over UDP/TCP
- SFU Room & Session Manager -> Core Telehealth Service: Validates room entry via gRPC
- Media Forwarding Engine -> Recording & Egress Service: Triggers media archiving via gRPC
- Recording & Egress Service -> Cloud Storage (GCP): Persists encrypted recordings via HTTPS/TLS

## Technology Stack
- LiveKit on Google Kubernetes Engine (GKE): Powers the SFU media architecture and room management
- Go: Used for high-throughput media and session components
- WebRTC with Simulcast and Dynamic ABR: Ensures video continuity below 300 kbit/s
- Coturn: Provides NAT traversal for restricted rural networks
- GCP Cloud Storage (europe-west3, us-central1): Enforces regional data residency

## Rationale
This component architecture uses WebRTC simulcast and dynamic ABR to maintain video quality for rural users. Regional deployment on GCP enforces strict EU and US data residency mandates.