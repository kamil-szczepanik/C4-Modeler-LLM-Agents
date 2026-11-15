## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. Containerized Selective Forwarding Units (SFUs) ensure real-time, low-bandwidth video communication while strictly enforcing regional data residency.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Google Kubernetes Engine (GKE) cluster spanning `europe-west3` and `us-central1`
- Containerized SFUs container (`mediasoup`)
- Signaling & Room Manager (Node.js/TypeScript)
- Media Router Worker & Bandwidth Adaptation Engine (C++)
- Core Telehealth Service (Go)

## Relationships
- Client Applications -> Containerized SFUs: WebRTC (ICE/DTLS/SRTP) for media streams and WebSockets (WSS) for signaling
- Signaling & Room Manager -> Core Telehealth Service: gRPC over Istio mTLS mesh for peer authorization, audit logging, and room state
- Signaling & Room Manager -> Media Router Worker: Local Unix sockets for inter-process communication (IPC)

## Technology Stack
- mediasoup / C++: High-performance WebRTC media routing and simulcast/SVC stream adaptation for bandwidth resilience (<300 kbit/s)
- Node.js/TypeScript: Signaling, room management, and worker lifecycle control
- GCP (GKE): Container orchestration with regional node affinity to enforce data residency
- Istio mTLS / gRPC: Secure service-to-service communication and control plane encryption
- tmpfs (RAM-backed emptyDir): Ephemeral memory isolation to prevent local disk persistence of media buffers

## Rationale
GKE regional node affinity guarantees that EU and US health data remain in their respective jurisdictions to satisfy GDPR and HIPAA. Containerized mediasoup SFUs with built-in simulcast and tmpfs isolation deliver low-bandwidth video resilience and zero-retention PHI security.