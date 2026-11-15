## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and low-bandwidth resilience.

## Key Elements
- Patients & Clinicians (Users)
- API Gateway / BFF (Go, gRPC/REST)
- Video Consultation Service (Golang / WebRTC SFU (LiveKit)):
  - Signaling Controller (Golang, WebSockets)
  - SFU Media Router (Golang / LiveKit SDK)
  - Bandwidth Adaptation Engine (Golang)
  - NAT Traversal Manager (Golang, Pion TURN)
  - Audit & Compliance Logger (Golang)
- Regional Data Storage (Cloud SQL PostgreSQL, Cloud Storage)
- External Systems: EU/US Pharmacy Networks, AI Model Provider

## Relationships
- API Gateway / BFF -> Signaling Controller: Initiates consultation room joining [gRPC over mTLS via Istio]
- Signaling Controller <-> SFU Media Router: Coordinates peer sessions [In-memory Go channels]
- SFU Media Router <-> NAT Traversal Manager: Allocates UDP relay ports [ICE/TURN protocol]
- Bandwidth Adaptation Engine -> SFU Media Router: Dynamically adjusts bitrates [In-memory Go function calls]
- Regional Audit & Compliance Logger -> Regional Data Storage: Persists localized session telemetry [PostgreSQL / SQL via gRPC]

## Technology Stack
- Golang: Chosen for high concurrency and performance in real-time media routing.
- WebRTC SFU (LiveKit) & Pion TURN: Enables scalable peer-to-peer media handling and NAT traversal for unstable rural connections.
- GCP (europe-west3, us-central1): Enforces regional data residency for GDPR and HIPAA compliance.
- Cloud SQL (PostgreSQL): Secures structured audit logs and patient metadata per region.

## Rationale
This architecture ensures strict geographic data isolation to comply with GDPR and HIPAA mandates while offering robust real-time communication. The modular Golang-based components deliver resilient, low-bandwidth video streaming for rural users.