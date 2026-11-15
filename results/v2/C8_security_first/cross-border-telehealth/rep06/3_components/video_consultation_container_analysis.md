## Overview
Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency while ensuring high availability for users with unstable internet connections.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway & BFF (Go, Envoy Proxy)
- Video Consultation Container (WebRTC SFU, MediaSoup)
- E-Prescription Integration Container (Node.js, Express)
- AI Symptom Checker Container (Python, FastAPI)
- Cloud SQL PostgreSQL and Google Cloud Storage
- Third-Party Video Relay / TURN Network
- National e-Prescription Gateways (EU) & US Pharmacy Networks (HL7 FHIR)

## Relationships
- Patients & Clinicians -> Video Consultation Container: Streams video via WebRTC [DTLS-SRTP]
- API Gateway & BFF -> Signaling Server: Authenticates requests [WSS / mTLS over gRPC/REST]
- Signaling Server -> SFU Media Router: Manages worker processes [Local IPC]
- SFU Media Router <-> Third-Party TURN Network: Relays media for NAT traversal [ICE/TURN over UDP/TCP]
- E-Prescription Integration Container -> EU Gateways / US Pharmacy Networks: Transmits prescriptions [HL7 FHIR / National Standards]

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for regional data residency compliance.
- Google Kubernetes Engine (GKE): Manages container orchestration with isolated node pools and NetworkPolicies.
- MediaSoup (C++): Powers the SFU media router for encrypted media handling (DTLS-SRTP).
- Node.js & WebSockets: Implements the Signaling Server and Adaptive Bitrate Controller.
- Prometheus & GKE HPA: Handles custom observability and autoscaling based on active rooms and network throughput.

## Rationale
This architecture guarantees strict regulatory compliance by enforcing data residency per region on GCP. Furthermore, the MediaSoup SFU with adaptive bitrate down to 150 kbit/s ensures reliable video consultations for rural patients with unstable connections.