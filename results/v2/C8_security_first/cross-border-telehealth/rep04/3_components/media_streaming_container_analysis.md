## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and high availability for rural users.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (Envoy and Google Cloud Load Balancing)
- Media Streaming Container (Janus WebRTC SFU on GKE)
- Signaling & Session Manager Component
- Adaptive Bitrate (ABR) Controller Component
- Media Relay & Encryption Engine Component
- Coturn Cluster (NAT/firewall traversal)
- Regional GCP Cloud Storage (CMEK)

## Relationships
- Patient/Clinician -> API Gateway: Media signaling and streaming [WSS / WebRTC]
- API Gateway -> Signaling & Session Manager: Authenticated room commands [WSS]
- ABR Controller -> DevOps Monitoring Stack: Real-time RTT, packet loss, and bitrate metrics [Prometheus / HTTP]
- Media Relay & Encryption Engine -> GKE UDP NodePorts: ICE/STUN/TURN media transport [DTLS-SRTP / AES-256]
- Media Relay & Encryption Engine -> Regional GCP Cloud Storage: Optional clinical audit recordings [HTTPS / CMEK]

## Technology Stack
- Google Kubernetes Engine (GKE) Autopilot: Container orchestration with regional deployment in `europe-west3` and `us-central1` for data residency.
- Janus WebRTC SFU (C++): Powers adaptive video streaming and audio-first fallback for unstable connections below 300 kbit/s.
- BoringSSL / libsrtp: Enforces mandatory DTLS-SRTP encryption with AES-256 ciphers.
- Coturn: Provides dedicated NAT/firewall traversal for rural users.
- Prometheus / Cloud Monitoring: Scrapes real-time streaming telemetry and enforces alerting thresholds.

## Rationale
Decomposing the Janus SFU into specialized signaling, ABR, and encryption components ensures strict security isolation and compliance with GDPR/HIPAA. Regional GKE deployments and dedicated Coturn clusters guarantee low-latency, resilient video consultations for users in unstable rural environments.