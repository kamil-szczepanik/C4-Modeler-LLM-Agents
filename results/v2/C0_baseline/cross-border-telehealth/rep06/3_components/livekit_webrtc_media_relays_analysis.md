## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency and low-bandwidth resilience.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- Patient Mobile/Web App & Clinician Portal
- API Gateway (Envoy / Kong)
- Core Telehealth Service & AI Orchestrator (GKE)
- LiveKit/WebRTC Media Relays (TURN/STUN Server, SFU Media Router, Telemetry & Stats Exporter)
- Regional Data Storage (Cloud SQL, Cloud Spanner, Cloud KMS)

## Relationships
- Patient App & Clinician Portal -> LiveKit/WebRTC Media Relays: Establishes media transport [ICE/STUN/TURN over UDP/TCP, DTLS-SRTP, TLS 1.3]
- SFU Media Router -> Telemetry & Stats Exporter: Emits network metrics [Internal IPC / Prometheus scrape]
- Core Telehealth Service -> Media Relays: Issues short-lived access tokens [JWT]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency per GDPR/HIPAA constraints.
- Google Kubernetes Engine (GKE): Hosts containerized services with custom HPA for media workloads.
- LiveKit (Go) & Coturn: Provides SFU routing and NAT traversal for adaptive sub-300 kbit/s video.
- DTLS-SRTP & TLS 1.3: Secures all media streams and control channels in transit.

## Rationale
Isolating regional deployments into distinct GCP regions prevents cross-border data leakage and satisfies strict medical regulations. Incorporating adaptive SFU routing and a 30-second session recovery grace period maintains reliable video consultations for rural patients with unstable connections.