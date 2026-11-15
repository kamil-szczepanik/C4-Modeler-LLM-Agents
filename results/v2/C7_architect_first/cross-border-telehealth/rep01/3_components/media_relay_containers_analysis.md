## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures regional data residency, strict regulatory compliance (GDPR/HIPAA), and reliable performance for users with unstable internet connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web Application & Mobile App Containers (React, React Native)
- Core Services GKE Clusters (Google Kubernetes Engine, Istio, gRPC)
- Media Relay Containers (Coturn TURN/STUN, Mediasoup SFU)
- Data Containers (Cloud SQL PostgreSQL, Cloud Storage with WORM policies)
- External Systems (National e-Prescription Gateways, Pharmacy Networks, AI Model Providers)

## Relationships
- Web App & Mobile App -> Signaling & Room Management Component: Real-time session negotiation via WebSockets (WSS)
- Web App & Mobile App -> SFU Media Router & TURN/STUN Relay: Media streaming via WebRTC over UDP/TCP with DTLS-SRTP
- Core Services -> Media Relay Containers: Connects consultation traffic via gRPC and internal telemetry streams
- Media Relay Containers -> GCP Cloud Monitoring: Exports connection metrics via Prometheus exporters

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for localized data residency and compliance
- Node.js & TypeScript: Powers signaling and room management components
- Mediasoup (C++ core with Node.js wrapper) & Coturn: Selective Forwarding Unit and TURN/STUN relay for real-time media
- WebRTC (DTLS-SRTP): End-to-end encrypted protocol for secure video and audio streaming
- GCP Network Load Balancer & GKE: Dedicated node pools with `hostNetwork: true` for low-latency packet routing

## Rationale
This architecture enforces strict regional data residency by isolating EU and US traffic within specific GCP regions. The Mediasoup SFU and Coturn implementation guarantees reliable, adaptive video and audio consultations for rural patients operating below 300 kbit/s.